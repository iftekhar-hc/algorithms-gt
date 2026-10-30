# Week 7: RNA-seq Part 1 — Introduction, Study Design & Spliced Alignment

**Course:** Applied Bioinformatics for Genomics (BFX Workshop 2025–2026)  
**Instructor:** Chris Miller, Ph.D.  
**Transcription Model:** Whisper `large-v3-turbo` (`week_07_lecture.txt` / `week_07_lecture.srt`)

---

## 1. Biological & Technical Challenges of RNA Sequencing

Unlike genomic DNA (static, double-stranded, 2 copies per diploid cell), the **transcriptome** is dynamic and presents unique experimental and computational challenges:
1. **Introns & Alternative Splicing:** Mature mRNAs have introns spliced out, so sequencing reads spanning exon-exon junctions must be split across kilobases of genomic sequence during alignment.
2. **Extreme Dynamic Range ($10^5$–$10^7$ fold):** A tiny fraction of highly expressed genes (especially **ribosomal RNA, rRNA, comprising >80–90% of total cellular RNA**, plus mitochondrial transcripts) consumes nearly all sequencing reads unless depleted or filtered.
3. **Fragility of RNA:** Single-stranded RNA degrades rapidly via ubiquitous RNases.

```
Genomic DNA:   5' ──[Promoter]──[Exon 1]════(Intron 1)════[Exon 2]════(Intron 2)════[Exon 3]── 3'
                                   │                         │                         │
Pre-mRNA:      5'-Cap ──────────[Exon 1]────(Intron 1)────[Exon 2]────(Intron 2)────[Exon 3]──AAAA(n)
                                   │                         │                         │ (Splicing)
Mature mRNA:   5'-Cap ──────────[Exon 1]──────────────────[Exon 2]──────────────────[Exon 3]──AAAA(n)
```

---

## 2. RNA Quality Assessment (RIN) & Library Construction Strategies

### A. Agilent Bioanalyzer & RNA Integrity Number (RIN: 0 to 10)
Before library prep, RNA quality is measured by electrophoretic separation of the **18S and 28S ribosomal RNA subunits**:
```
HIGH QUALITY RNA (RIN = 10):                     DEGRADED RNA (RIN < 6, e.g., FFPE tissue):
Fluorescence                                     Fluorescence
   │          │█│ (28S)                             │
   │    │█│   │ │                                   │   _.-~-~._.~-._  (Smeared low-MW fragments)
   │____│ │___│ │_______                            │__/             \________________________
       18S   28S       Fragment Size                   18S   28S              Fragment Size
```

### B. mRNA Enrichment & Library Design Choices
| Strategy | Mechanism | Pros | Cons / Biases |
| :--- | :--- | :--- | :--- |
| **Poly(A) Selection** | Oligo(dT) beads capture $3'$ polyadenylated tails | Cheap, cleanly enriches mature protein-coding mRNAs | **Strong $3'$ end bias** if RNA is degraded (low RIN); misses non-poly(A) RNAs (histones, many lncRNAs) |
| **rRNA Depletion (Ribo-Zero)** | Hybridization probes remove rRNA species | Works on degraded/FFPE samples; captures nascent pre-mRNA and non-coding RNAs | Higher intronic read fraction; requires deeper sequencing |
| **Stranded vs. Unstranded** | dUTP second-strand marking & digestion preserves original transcript strand (`+` vs. `-`) | Essential for resolving overlapping antisense genes | Verify orientation (`RF` vs. `FR`) with `check_strandedness` |
| **Biological vs. Technical Replicates** | **Biological:** independent isolations ($\ge 3$–$6$/group); **Technical:** re-sequencing same library | Biological replicates capture true variance required for DE stats | Technical replicates only measure sequencer noise |

---

## 3. Why Spliced Alignment Is Required: `HISAT2` Hierarchical Indexing

Standard DNA aligners (`BWA`, `Bowtie2`) expect contiguous genomic alignments and fail when an mRNA read spans a $10,000\text{ bp}$ intron. **Splice-aware aligners (`HISAT2`, `STAR`)** split junction-spanning reads using a **two-level FM-index architecture**:
1. **Global Whole-Genome FM-Index (1 index):** Anchors the initial $\ge 28\text{ bp}$ seed of a read across the entire genome.
2. **~48,000 Overlapping Local FM-Indexes (~64 kb windows):** When read extension hits a splice junction mismatch (even with an $8\text{ bp}$ overhang), `HISAT2` switches to the **local FM-index** covering that genomic neighborhood to rapidly place the remaining exon segment without searching all 3.2 Gbp.

```
Exon 1                                      Intron (5,000 bp)                                    Exon 2
[████████████████████████]────────────────────────────────────────────────────────────[████████████████████████]
  ├──────────────────────►                                                                              (Exonic: 100M)
         ├───────────────► . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . ──►              (92M5000N8M: Local Index)
                ├────────► . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . ─────────►       (50M5000N50M: Spliced)
```
- In the output `SAM`/`BAM` file, spliced introns are encoded in the `CIGAR` string using **`N` (skipped reference region)**, e.g., `50M5000N50M`.

---

## 4. Reference Annotations (`GTF`) & Containerized Workflow

```bash
# 1. Check library strandedness using Reference GTF + Transcriptome FASTA
docker run -v $PWD/:/docker_workspace mgibio/checkstrandedness:latest check_strandedness \
  --gtf /docker_workspace/refs/chr22_with_ERCC92_tidy.gtf \
  --transcripts /docker_workspace/refs/chr22_ERCC92_transcripts.clean.fa \
  --reads_1 /docker_workspace/data/HBR_Rep1.read1.fastq.gz \
  --reads_2 /docker_workspace/data/HBR_Rep1.read2.fastq.gz

# 2. Align paired-end RNA-seq reads with HISAT2 (strandedness --rna-strandness RF) and sort to BAM
hisat2 -p 4 --rg-id=HBR_Rep1 --rg SM:HBR --rg LB:HBR_Rep1_ERCC-Mix2 --rg PL:ILLUMINA \
  -x refs/chr22_with_ERCC92 --dta --rna-strandness RF \
  -1 data/HBR_Rep1.read1.fastq.gz -2 data/HBR_Rep1.read2.fastq.gz -S HBR_Rep1.sam
samtools sort -@ 4 -o HBR_Rep1.bam HBR_Rep1.sam && samtools index HBR_Rep1.bam
```

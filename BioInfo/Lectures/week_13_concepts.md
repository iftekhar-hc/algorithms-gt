# Week 13: Genome Arithmetic & `bedtools` — Core Concepts & Visualizations

**Course:** Applied Bioinformatics for Genomics (BIOL 5625 / BFX Workshop 2025–2026)  
**Instructor:** Chris Miller, Ph.D.  
**Transcription Model:** Whisper `large-v3-turbo` (`week_13_lecture.txt` / `week_13_lecture.srt`)

---

## 1. Genomic Coordinate Systems: 0-Based Half-Open (`BED`) vs. 1-Based Closed (`GTF`/`VCF`/`SAM`)

One of the most frequent sources of off-by-one bugs in bioinformatics is mixing up **1-based closed** coordinates (human-friendly) and **0-based half-open `[start, end)`** coordinates (computer-friendly, used by `BED`):

```
DNA Sequence:        A     T     G     C     T     A     G
1-Based Position:    1     2     3     4     5     6     7    (VCF, SAM, GTF, GFF, IGV display)
0-Based Position:   0     1     2     3     4     5     6     7 (BED, BAM binary index)
                                │─────────────────│
Substring "GCT":
  • 1-Based Closed [3, 5]:      Start = 3, End = 5   --> Length = 5 - 3 + 1 = 3 bp
  • 0-Based Half-Open [2, 5):   Start = 2, End = 5   --> Length = 5 - 2     = 3 bp (No "+ 1" needed!)
```

| Format | Coordinate System | Example (`GCT` above) | Interval Width Formula |
| :--- | :--- | :--- | :--- |
| **BED / BedGraph** | **0-based, half-open `[start, end)`** | `chr1   2   5` | `end - start` |
| **GTF / GFF / SAM / VCF** | **1-based, fully closed `[start, end]`** | `chr1   3   5` | `end - start + 1` |

---

## 2. The Mathematics of Interval Intersection

How does a computer determine whether two genomic intervals $A = [a_{\text{start}}, a_{\text{end}})$ and $B = [b_{\text{start}}, b_{\text{end}})$ overlap on the same chromosome, without checking four separate boolean `if/else` cases?

$$I = \min(a_{\text{end}}, b_{\text{end}}) - \max(a_{\text{start}}, b_{\text{start}})$$

- **If $I > 0$:** Intervals $A$ and $B$ **intersect**, and $I$ is the exact number of overlapping base pairs!
- **If $I \le 0$:** Intervals $A$ and $B$ **do not overlap**, and $|I|$ is the genomic distance separating them!

```
Interval A:      10 ════════════════════ 20
Interval B:               17 ════════════════════ 27
Overlap Check:   I = min(20, 27) - max(10, 17) = 20 - 17 = +3 bp  --> INTERSECTION (3 bp overlap)

Interval C:      10 ══════ 13
Interval D:                     16 ══════ 20
Overlap Check:   I = min(13, 20) - max(10, 16) = 13 - 16 = -3 bp  --> NO OVERLAP (3 bp apart)
```

---

## 3. Core `bedtools` Operations ("The Swiss Army Knife of Genome Arithmetic")

`bedtools` operates on `BED`, `GTF`/`GFF`, `VCF`, and `BAM` files to answer biological questions by relating genomic intervals:

```
Chr1 Coordinate:   0         500        1000       1500       2000
Query A (CpGs):        [══════A1══════]               [════A2════]
Target B (Exons):          [══B1══]  [═B2═]                        [══B3══]

1. bedtools intersect -a A -b B          ──►   [══════]  [═]       (Overlapping base-pair sub-intervals)
2. bedtools intersect -a A -b B -wa      ──► [══════A1══════]      (Original A record written for each B hit)
3. bedtools intersect -a A -b B -v       ──►                  [════A2════]  (A features with ZERO overlap in B)
4. bedtools merge -i B -d 200            ──►       [══════B1+B2══════]      (Merge nearby/overlapping intervals)
5. bedtools closest -a A -b B            ──► Finds nearest B feature and distance (bp) for each A feature
```

| `bedtools` Subcommand & Flags | Biological Question Answered |
| :--- | :--- |
| `bedtools intersect -a cpg.bed -b exons.bed` | Which base pairs are **both** inside a CpG island and an exon? |
| `bedtools intersect -a cpg.bed -b exons.bed -wa -wb` | Report the full original `A` and `B` interval coordinates side-by-side (`-wo` appends bp overlap length) |
| `bedtools intersect -a cpg.bed -b exons.bed -c` | **Count** how many exons overlap each CpG island (`0, 1, 2, ...`) |
| `bedtools intersect -a cpg.bed -b exons.bed -v` | Which CpG islands are **non-exonic** (do **not** overlap any exon)? |
| `bedtools intersect -a cpg.bed -b exons.bed -f 0.50 -r` | Require at least **50% overlap** (`-f 0.50`), reciprocally (`-r`) |
| `bedtools closest -a chip_peaks.bed -b genes.bed -d` | Which gene is **closest** to each ChIP-seq peak, and how many base pairs away (`-d`)? |
| `bedtools slop` / `bedtools flank` | Expand intervals by $\pm N\text{ bp}$ (e.g., define promoter regions $2\text{ kb}$ upstream of TSS) |
| `bedtools complement -i exons.bed -g hg38.genome` | Extract all **non-exonic** (intergenic + intronic) regions of the genome |
| `bedtools shuffle` / `bedtools jaccard` | Randomly permute intervals or compute the Jaccard similarity statistic between two feature sets |

---

## 4. Practical Command-Line Examples from Lecture & Sandbox.bio Tutorial

```bash
# 1. Inspect BED files (0-based tab-delimited: chrom, start, end, [name], [score], [strand])
head -n 5 cpg.bed exons.bed

# 2. Report both original CpG (A) and Exon (B) records plus exact overlap length (-wo)
bedtools intersect -a cpg.bed -b exons.bed -wo | head -n 5

# 3. Find intergenic/intronic CpG islands that do NOT overlap any exon (-v)
bedtools intersect -a cpg.bed -b exons.bed -v | head -n 5

# 4. Require at least 50% of the CpG island to be overlapped by an exon (-f 0.5)
bedtools intersect -a cpg.bed -b exons.bed -wo -f 0.5 | head -n 5
```

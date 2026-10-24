## Overall assessment

**This is a promising, well-documented single-sample demonstration, but it is not yet a validated or operationally robust variant-calling pipeline.** The core bioinformatics stages are implemented; the largest gaps are reproducibility from a clean checkout, enforcement of QC decisions, automated testing, and measured calling accuracy.

I reviewed the workflows, launch scripts, reference-download instructions, and representative QC/results files at commit [`5cf46e1`](https://github.com/lamia-fh/variant_calling_pipeline/tree/5cf46e128b3324abd946b413cbec10da571927d5). **This was a static review—not an execution test.** Committed outputs demonstrate example results, but do not establish that this exact revision reproduces them.

| Area | Assessment |
|---|---|
| Core analysis stages | Substantially implemented for HG002 WES, chr20 targets |
| Scientific validation | Incomplete: no truth-set benchmark |
| Input/reference reproducibility | Partial; capture BED remains an external prerequisite |
| Failure handling and QC gates | Useful checks, but important gaps |
| Automated tests and CI | Not present in the reviewed tree |
| Generalization/scaling | Primarily a hard-coded, single-sample demonstration |
| Documentation | Extensive, but some reports and plans are inconsistent |

## What is already good

- **Sensible analysis structure:** full-reference alignment, sorting/indexing, duplicate marking, BQSR, HaplotypeCaller GVCF generation, genotyping, separate SNP/indel filtering, and VCF QC.
- **Thoughtful preprocessing:** trimming is conditional rather than automatic, and the QC decision is recorded.
- **Useful engineering foundations:** Nextflow DSL2, containerized tools, strict shell settings, `-resume`, preflight checks, and execution reports.
- **Good scientific restraint:** the README correctly distinguishes a `PASS` label from demonstrated accuracy.
- **Appropriate WES interpretation:** the read-QC report does not recommend trimming merely to eliminate a GC-distribution warning.

These are strong foundations for an educational or portfolio project.

## Highest-priority findings

### 1. The default alignment launcher has an input-file problem

**Priority: fix before the next clean-checkout run.**

The reviewed tree contains an empty `data/raw_input/raw_read_2.fastq.gz`. The alignment launcher creates standardized symlinks only if those paths do not already exist, then rejects empty selected inputs.

Consequently, after downloading the correctly named accession FASTQs, the existing empty placeholder can prevent the default `proceed` path from running. Existing nonempty standardized paths can also silently select an older sample’s reads.

**Evidence:** [input selection in the launcher](https://github.com/lamia-fh/variant_calling_pipeline/blob/5cf46e128b3324abd946b413cbec10da571927d5/scripts/run_step2_alignment.sh#L48-L65).

**Recommendation:** select the accession-named FASTQs directly, remove the tracked placeholder, and validate pairing and compressed-file integrity.

### 2. Sample identity is not consistently propagated

The step-2 launcher permits an `ACCESSION` environment override, but does not pass it to the workflow. The workflow retains its HG002/SRR14724472 defaults for read-group metadata.

It also reads only the QC decision, without checking whether the JSON accession matches the selected accession.

**Risk:** different reads can be processed under incorrect sample/read-group labels or an unrelated QC approval.

**Evidence:** [launcher accession and decision handling](https://github.com/lamia-fh/variant_calling_pipeline/blob/5cf46e128b3324abd946b413cbec10da571927d5/scripts/run_step2_alignment.sh#L7-L45), [read-group construction](https://github.com/lamia-fh/variant_calling_pipeline/blob/5cf46e128b3324abd946b413cbec10da571927d5/workflows/step2_alignment.nf#L5-L30).

**Recommendation:** introduce one sample manifest containing sample ID, accession, FASTQ paths/checksums, library, platform, and read-group identifiers. Derive every stage’s metadata from it.

### 3. QC checks exist, but they are not all dependency gates

BAM validation and QC run on branches parallel to recalibration. Recalibration does not wait for a validation approval artifact. The separate calling launcher checks for BAM/index existence, not successful completion and approval of alignment QC.

Similarly, the step-1 decision process has no dependency on FastQC completion. On a failed rerun, published decisions or older outputs can remain available.

**Evidence:** [alignment workflow dependencies](https://github.com/lamia-fh/variant_calling_pipeline/blob/5cf46e128b3324abd946b413cbec10da571927d5/workflows/step2_alignment.nf#L239-L253), [step-1 decision execution](https://github.com/lamia-fh/variant_calling_pipeline/blob/5cf46e128b3324abd946b413cbec10da571927d5/workflows/step1_fastqc.nf#L93-L111).

**Recommendation:**
- Make validation success an explicit dependency where required.
- Publish a stage-completion manifest only after all required tasks succeed.
- Bind approvals to input checksums and run IDs.
- Require a new review after trimming if post-trim QC is intended to be a real checkpoint.

### 4. QC-decision JSON generation is fragile

The JSON is constructed using `printf` with user-supplied justification embedded in shell quoting.

Double quotes, backslashes, or newlines can produce invalid JSON; apostrophes can break the generated shell command.

**Evidence:** [decision serialization](https://github.com/lamia-fh/variant_calling_pipeline/blob/5cf46e128b3324abd946b413cbec10da571927d5/workflows/step1_fastqc.nf#L38-L48).

**Recommendation:** use a JSON serializer and pass text without interpolating it directly into executable shell source. Add tests using punctuation and multiline justifications.

### 5. Reproducibility is not yet self-contained

The capture BED is required but is neither supplied nor downloaded; users are told to obtain it from the vendor. References receive basic checks, but publisher-checksum verification is not implemented.

The Conda profile specifies only FastQC and fastp, so it is not a complete environment for alignment and calling.

**Evidence:** [reference prerequisites](https://github.com/lamia-fh/variant_calling_pipeline/blob/5cf46e128b3324abd946b413cbec10da571927d5/data/reference/reference_files.md#L9-L26), [download checks](https://github.com/lamia-fh/variant_calling_pipeline/blob/5cf46e128b3324abd946b413cbec10da571927d5/data/reference/download_references.sh#L60-L62), [Conda profile](https://github.com/lamia-fh/variant_calling_pipeline/blob/5cf46e128b3324abd946b413cbec10da571927d5/workflows/nextflow.config#L11-L17).

**Recommendation:** record the exact capture-kit/version/build/checksum; validate BED coordinates and contig compatibility; pin supported Nextflow/Java versions; and either complete the Conda profile or clearly limit support to Docker.

If redistribution is restricted, provide a separate redistributable test fixture.

## Scientific completeness and robustness

### 6. The main missing scientific deliverable is GIAB benchmarking

The committed results report:

- **2,001 labelled records**
- **1,909 PASS records**
- **1,635 SNP records and 274 indel records in PASS**
- **Ti/Tv of 2.68**

Those are useful descriptive results—not sensitivity or precision estimates. The validation log shows structural/reference-related checks over 1,909 records, not truth-set agreement.

**Evidence:** [calling summary](https://github.com/lamia-fh/variant_calling_pipeline/blob/5cf46e128b3324abd946b413cbec10da571927d5/results/summary/03_Calling_Results.md#L16-L29), [validation log](https://github.com/lamia-fh/variant_calling_pipeline/blob/5cf46e128b3324abd946b413cbec10da571927d5/results/raw_results/03_calling/qc/HG002.validate_variants.log#L24-L31).

**Next step:** compare against a compatible **HG002 GRCh38 GIAB** benchmark using hap.py or RTG vcfeval.

Define the primary evaluation territory as:

**GIAB high-confidence regions ∩ intended chr20 capture targets**

Report padded flanks separately. Include SNP/indel precision, recall, F1, TP/FP/FN counts, genotype agreement, and difficult-region stratifications.

Do not restrict the only reported benchmark to well-covered regions: that would hide coverage-related false negatives. Add a callable-region analysis as a secondary result.

### 7. Filtering needs explicit edge-case and genotype policies

SNP and indel annotations are combined into compound OR expressions. Missing annotation behavior needs explicit testing: do not assume that every failed available annotation will always be labelled as intended.

Non-SNP/non-indel records are deliberately preserved without equivalent hard filtering. Their inclusion in the final output depends on their FILTER state.

There is also no explicit downstream genotype-quality policy for DP, GQ, allele balance, or no-calls.

**Evidence:** [filtering implementation](https://github.com/lamia-fh/variant_calling_pipeline/blob/5cf46e128b3324abd946b413cbec10da571927d5/workflows/step3_calling.nf#L61-L81).

**Recommendation:** test individual filter conditions and missing annotations; define handling for mixed/multiallelic records; distinguish site-level `PASS` from genotype confidence. Tune thresholds against benchmark evidence rather than simply adding stricter cutoffs.

### 8. BQSR and coverage conclusions need stronger supporting evidence

BQSR trains on chr20 but is applied to the full BAM. That is a demonstration shortcut requiring justification—not proof of incorrect results—but its adequacy should be measured.

Add before/after recalibration diagnostics and compare calling performance with the chosen training territory.

The repository already contains hybrid-selection metrics, yet the alignment summary still describes assay/scope information as unavailable and coverage adequacy as unresolved.

**Evidence:** [BQSR scope](https://github.com/lamia-fh/variant_calling_pipeline/blob/5cf46e128b3324abd946b413cbec10da571927d5/workflows/step2_alignment.nf#L177-L215), [coverage discussion](https://github.com/lamia-fh/variant_calling_pipeline/blob/5cf46e128b3324abd946b413cbec10da571927d5/results/summary/02_Alignment_QC_Report.md#L82-L110).

**Recommendation:** update the report using target-level coverage, fractions ≥10×/20×/30×, zero-coverage targets, uniformity, and GC dropout. Preserve the caveat that using targets as a substitute for bait intervals limits bait-specific interpretation.

Whole-chromosome breadth is not the appropriate primary completeness measure for WES.

## Recommended next steps

| Order | Deliverable | Acceptance criterion |
|---|---|---|
| **1** | Repair input selection and metadata propagation | Correct accession/sample used throughout; stale inputs and mismatched approvals rejected |
| **2** | Add deterministic tests and CI | Small fixture completes; missing mates/indexes, malformed JSON, failed validation, and filter edge cases behave correctly |
| **3** | Establish clean-run reproducibility | Documented run from a fresh checkout, verified resources, resolved parameters, versions/image identities, and completion manifests |
| **4** | Complete coverage/BQSR assessment | Updated target-aware QC report and calibration diagnostics |
| **5** | Implement GIAB benchmarking | Reproducible accuracy report with defined territory and SNP/indel metrics |
| **6** | Generalize and release | Sample sheet, explicit resource limits, versioned release, license, and consistent documentation |

Also address resource management before scaling: concurrent processes use fixed tool-thread/Java settings without a complete memory/time budget. Make allocations explicit and align command-line threading with Nextflow resources.

Annotation, cohort joint genotyping, CNV/SV calling, and cloud/HPC support can wait. They are extensions—not prerequisites for completing the stated germline SNP/small-indel demonstration.

## A small fix you can apply now

In `scripts/run_step2_alignment.sh`, replace standardized-symlink selection with direct accession paths:

```diff name=scripts/run_step2_alignment.sh url=https://github.com/lamia-fh/variant_calling_pipeline/blob/5cf46e128b3324abd946b413cbec10da571927d5/scripts/run_step2_alignment.sh#L53-L61
     [[ -d data/raw_input ]] || fail "Missing raw-read directory: data/raw_input"
     for mate in 1 2; do
         src="data/raw_input/${ACCESSION}_${mate}.fastq.gz"
         [[ -s "$src" ]] || fail "Missing or empty raw FASTQ: $src"
-        [[ -e "data/raw_input/raw_read_${mate}.fastq.gz" ]] ||
-            ln -s "${ACCESSION}_${mate}.fastq.gz" "data/raw_input/raw_read_${mate}.fastq.gz"
     done
-    r1="data/raw_input/raw_read_1.fastq.gz"
-    r2="data/raw_input/raw_read_2.fastq.gz"
+    r1="data/raw_input/${ACCESSION}_1.fastq.gz"
+    r2="data/raw_input/${ACCESSION}_2.fastq.gz"
```

This fixes the path-selection issue; metadata propagation and approval matching still need separate changes.

**Bottom line:** prioritize **trustworthy inputs → enforced validation → reproducible tests → measured accuracy**. That will add substantially more value than adding more analysis tools now.

### Want me to…
<!-- copilot:suggestions -->
1. Hand the input-selection, metadata-propagation, and QC-decision fixes off to the coding agent to open a pull request in `lamia-fh/variant_calling_pipeline`.
2. Design a concrete test and CI plan with fixtures and failure-case acceptance criteria.
3. Specify the HG002 GIAB benchmarking workflow and reporting requirements.
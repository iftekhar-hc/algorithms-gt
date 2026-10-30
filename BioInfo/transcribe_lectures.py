#!/usr/bin/env python3
"""Transcribe lecture videos (.mp4/.wav) into .txt and .srt files using faster-whisper."""

import argparse
import os
import sys
import time
from pathlib import Path

from faster_whisper import BatchedInferencePipeline, WhisperModel

DEFAULT_BIOINFORMATICS_PROMPT = (
    "Bioinformatics, genomics, FASTQ, BAM, SAM, CRAM, VCF, BED, GTF, GFA, samtools, bcftools, "
    "bedtools, FastQC, MultiQC, BWA, HISAT2, StringTie, Ballgown, DESeq2, GATK, HaplotypeCaller, "
    "Mutect2, VarScan, VEP, ClinVar, gnomAD, ChIP-seq, ATAC-seq, WGBS, MACS2, IGV, Docker, "
    "Singularity, Apptainer, SLURM, Compute2, R, RStudio, ggplot2, tidyverse, dplyr, tidyr, "
    "Minigraph-Cactus, Bandage, pangenome, Seurat, UMAP, Harmony, scRNA-seq, Oxford Nanopore, "
    "Dorado, pychopper, NanoPlot, minimap2, QIIME2, DADA2, 16S, CWL, WDL, Cromwell, TP53, WashU."
)


def format_ts(seconds: float) -> str:
    hrs = int(seconds // 3600)
    mins = int((seconds % 3600) // 60)
    secs = int(seconds % 60)
    ms = int(round((seconds - int(seconds)) * 1000))
    return f"{hrs:02d}:{mins:02d}:{secs:02d},{ms:03d}"


def transcribe_file(
    video_path: Path,
    pipeline: BatchedInferencePipeline,
    batch_size: int = 16,
    beam_size: int = 1,
    initial_prompt: str = DEFAULT_BIOINFORMATICS_PROMPT,
) -> None:
    t0 = time.time()
    print(f"Transcribing: {video_path}", flush=True)
    segments, info = pipeline.transcribe(
        str(video_path),
        batch_size=batch_size,
        beam_size=beam_size,
        language="en",
        vad_filter=True,
        initial_prompt=initial_prompt,
    )

    txt_path = video_path.with_suffix(".txt")
    srt_path = video_path.with_suffix(".srt")

    with open(txt_path, "w", encoding="utf-8") as txt_f, \
         open(srt_path, "w", encoding="utf-8") as srt_f:
        for i, seg in enumerate(segments, start=1):
            text = seg.text.strip()
            txt_f.write(text + "\n")
            txt_f.flush()
            srt_f.write(f"{i}\n{format_ts(seg.start)} --> {format_ts(seg.end)}\n{text}\n\n")
            srt_f.flush()
            if i % 10 == 0 or i == 1:
                print(
                    f"  [{format_ts(seg.start)} / {format_ts(info.duration)}] {text[:80]}...",
                    flush=True,
                )

    elapsed = time.time() - t0
    print(
        f"Saved: {txt_path} and {srt_path} (duration={info.duration:.1f}s, elapsed={elapsed:.1f}s)\n",
        flush=True,
    )


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Transcribe lecture videos in lectures/ using faster-whisper."
    )
    parser.add_argument(
        "files",
        nargs="*",
        help="Optional video/audio file paths. Defaults to lectures/week_*/*.mp4",
    )
    parser.add_argument(
        "--model",
        default="medium.en",
        help="Whisper model size (e.g., tiny.en, base.en, small.en, medium.en, large-v3-turbo). Default: medium.en",
    )
    parser.add_argument(
        "--device",
        default="cpu",
        help="Device to run on ('cpu' or 'cuda'). Default: cpu",
    )
    parser.add_argument(
        "--compute-type",
        default="int8",
        help="Compute quantization type ('int8', 'float16', 'float32'). Default: int8",
    )
    parser.add_argument(
        "--threads",
        type=int,
        default=min(24, os.cpu_count() or 8),
        help="Number of CPU threads to use. Default: min(24, cpu_count)",
    )
    parser.add_argument(
        "--batch-size",
        type=int,
        default=16,
        help="Batch size for BatchedInferencePipeline. Default: 16",
    )
    parser.add_argument(
        "--beam-size",
        type=int,
        default=1,
        help="Beam size for decoding. Default: 1",
    )
    args = parser.parse_args()

    repo_root = Path(__file__).resolve().parent
    targets = (
        [Path(p) for p in args.files]
        if args.files
        else sorted((repo_root / "lectures").glob("week_*/*.mp4"))
    )

    if not targets:
        print(
            f"No .mp4 files found under {repo_root / 'lectures' / 'week_*'}. "
            "Pass video file paths or download the lecture videos first.",
            file=sys.stderr,
        )
        sys.exit(1)

    model = WhisperModel(
        args.model,
        device=args.device,
        compute_type=args.compute_type,
        cpu_threads=args.threads,
    )
    pipeline = BatchedInferencePipeline(model=model)
    for video in targets:
        if not video.exists():
            print(f"File not found: {video}", file=sys.stderr)
            continue
        transcribe_file(
            video,
            pipeline,
            batch_size=args.batch_size,
            beam_size=args.beam_size,
        )


if __name__ == "__main__":
    main()

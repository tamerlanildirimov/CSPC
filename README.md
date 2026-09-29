# CSPC - Computer Science for Physics and Chemistry

My coursework repository. Each practical is under PW<n>/Lab <X>/.

## Setup
Create the environment for a given lab:
```bash
conda env create -f PW<n>/Lab <X>/environment.yml
conda activate cspc
---

## PW1 - Lab A: Reproducible Foundations

Lab A complete. All tests passing (3/3), speedup verified, and environment configured.

## PW1 - Lab B: Data Processing & Snakemake Pipeline

The observed decay data closely matches the exponential analytical decay law. The Snakemake pipeline automates the data reading and plot generation process, rebuilding output files only when dependencies change.
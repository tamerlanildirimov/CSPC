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

# PW2 Lab A: Motion Analysis

## Results
- **Mean Acceleration**: $-8.58 \text{ m/s}^2$
- **Description**: Using the free-fall measurements from `freefall.csv`, velocity and acceleration were computed via numerical differentiation. The mean acceleration is close to the standard gravity ($g \approx -9.81 \text{ m/s}^2$), with observable noise in the acceleration profile.
- **Plot**: Saved as `motion.png`.
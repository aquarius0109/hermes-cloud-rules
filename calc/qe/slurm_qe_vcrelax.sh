#!/bin/bash
#SBATCH --job-name=qe_vcrelax
#SBATCH --partition=qdhcnormal
#SBATCH -N 1
#SBATCH --ntasks-per-node=4
#SBATCH --time=01:00:00
#SBATCH --output=%x_%j.out
#SBATCH --error=%x_%j.err

# QE vc-relax 模板（集群3 山东）
# 用法: sbatch slurm_qe_vcrelax.sh

module load qe-7.3.1-intelmpi2021
cd /work/home/aquarius0109/YOUR_PROJECT_DIR

mpirun -np $SLURM_NTASKS pw.x -input vc-relax.in

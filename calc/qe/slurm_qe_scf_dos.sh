#!/bin/bash
#SBATCH --job-name=qe_scf_dos
#SBATCH --partition=qdhcnormal
#SBATCH -N 1
#SBATCH --ntasks-per-node=4
#SBATCH --time=00:30:00
#SBATCH --output=%x_%j.out
#SBATCH --error=%x_%j.err

# QE SCF + DOS 模板（集群3 山东）
# 用法: sbatch slurm_qe_scf_dos.sh

module load qe-7.3.1-intelmpi2021
cd /work/home/aquarius0109/YOUR_PROJECT_DIR

# SCF计算
mpirun -np $SLURM_NTASKS pw.x -input scf.in

# DOS计算（需要SCF结果）
mpirun -np $SLURM_NTASKS pw.x -input dos.in

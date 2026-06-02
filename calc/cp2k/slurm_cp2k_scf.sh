#!/bin/bash
#SBATCH --job-name=cp2k_scf
#SBATCH --partition=qdhcnormal
#SBATCH -N 1
#SBATCH --ntasks-per-node=6
#SBATCH --time=00:30:00
#SBATCH --output=%x_%j.out
#SBATCH --error=%x_%j.err

# CP2K SCF 模板（集群3 山东）
# 用法: sbatch slurm_cp2k_scf.sh
# ⚠️ 必须单节点！

module load cp2k/9.1-intelmpi-2021
export OMP_NUM_THREADS=1
cd /work/home/aquarius0109/YOUR_PROJECT_DIR

mpirun -np $SLURM_NTASKS cp2k.psmp -i input.inp -o output.out

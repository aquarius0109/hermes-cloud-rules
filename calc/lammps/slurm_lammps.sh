#!/bin/bash
#SBATCH --job-name=lmp_md
#SBATCH --partition=qdhcnormal
#SBATCH -N 1
#SBATCH --ntasks-per-node=4
#SBATCH --time=00:30:00
#SBATCH --output=%x_%j.out
#SBATCH --error=%x_%j.err

# LAMMPS MD 模板（集群3 山东）
# 用法: sbatch slurm_lammps.sh

module load lammps/xxx  # 根据集群可用版本调整
cd /work/home/aquarius0109/YOUR_PROJECT_DIR

mpirun -np $SLURM_NTASKS lmp -in input.lammps

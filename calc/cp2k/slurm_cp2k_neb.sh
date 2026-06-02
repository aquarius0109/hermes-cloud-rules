#!/bin/bash
#SBATCH --job-name=cp2k_neb
#SBATCH --partition=qdhcnormal
#SBATCH -N 1                    # ⚠️ 必须单节点！双节点会RDMA崩溃
#SBATCH --ntasks-per-node=6     # >= num_of_images
#SBATCH --time=08:00:00
#SBATCH --output=%x_%j.out
#SBATCH --error=%x_%j.err

# CP2K NEB/BAND 模板（集群3 山东）
# 用法: sbatch slurm_cp2k_neb.sh
# ⚠️ 关键: 单节点 + ntasks >= replica数

module load cp2k/9.1-intelmpi-2021
export OMP_NUM_THREADS=1
cd /work/home/aquarius0109/YOUR_PROJECT_DIR

# 检查RESTART文件是否存在（续跑）
if ls *.RESTART.wfn 1>/dev/null 2>&1; then
    echo "检测到RESTART文件，将自动续跑"
    mkdir -p backup
    cp *.RESTART.wfn backup/
fi

mpirun -np $SLURM_NTASKS cp2k.psmp -i neb.inp -o neb.out

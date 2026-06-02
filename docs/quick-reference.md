# SCNet 集群快速参考

## 连接信息

| 集群 | SSH命令 |
|:-----|:--------|
| 集群1 昆山 | `ssh -i ~/.hermes/hpc_creds/集群1_key -p 65023 aquarius0109@cancon.hpccube.com` |
| 集群2 西安 | `ssh -i ~/.hermes/hpc_creds/集群2_key -p 65082 aquarius0109@eshell111.hpccube.com` |
| **集群3 山东** | `ssh -i ~/.hermes/hpc_creds/集群3_key -p 65032 aquarius0109@qdeshell.hpccube.com` |

## 常用命令

```bash
# 查看作业
squeue -u aquarius0109
sacct -u aquarius0109 --format=JobID,JobName,State,Elapsed

# 提交作业
sbatch job.sh

# 取消作业
scancel <jobid>

# 查看模块
module avail
module load cp2k/9.1-intelmpi-2021
module load qe-7.3.1-intelmpi2021

# 查看输出
tail -30 jobid.out
cat jobid.err
```

## 可用软件

| 软件 | 版本 | 模块名 |
|:-----|:-----|:-------|
| CP2K | 9.1 | `cp2k/9.1-intelmpi-2021` |
| CP2K | 2023.1 | `cp2k/2023.1-intelmpi-2021` |
| QE | 7.3.1 | `qe-7.3.1-intelmpi2021` |

## ⚠️ 关键注意事项

1. **CP2K NEB必须单节点**: `#SBATCH -N 1`
2. **计算节点用/work/home/**: 不是/home/
3. **分区名是qdhcnormal**: 不是qdhcnorma
4. **密钥有效期**: 集群3到期 2026-07-31

---

*更新: 2026-06-02*

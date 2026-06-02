# SCNet 超算集群经验总结

> 基于 2026-05-15 ~ 2026-06-02 期间约 200+ 个作业的实战经验

## 1. 集群概况

| 集群 | 地点 | 主机 | 端口 | 状态 | 推荐用途 |
|:-----|:-----|:-----|:----:|:----:|:---------|
| 集群1 昆山 | 江苏 | cancon.hpccube.com | 65023 | ✅ | GLIBCXX问题，不推荐 |
| 集群2 西安 | 陕西 | eshell111.hpccube.com | 65082 | ✅ | QE计算，内存~126GB |
| **集群3 山东** | 山东 | qdeshell.hpccube.com | 65032 | ✅ | **首选**，515GB/节点 |

**密钥管理**: `~/.hermes/hpc_creds/集群{1,2,3}_key`

## 2. 作业统计

### 2.1 总体状态分布

| 状态 | 数量 | 占比 | 说明 |
|:-----|:----:|:----:|:-----|
| COMPLETED | 41 | 48% | 成功完成 |
| FAILED | 35 | 41% | 失败（主要原因见下） |
| CANCELLED+ | 6 | 7% | 手动取消 |
| CANCELLED | 4 | 4% | 系统取消 |

### 2.2 按计算类型分布

| 类型 | 成功 | 失败 | 成功率 | 关键经验 |
|:-----|:----:|:----:|:------:|:---------|
| QE vc-relax | 多 | 少 | ~80% | 标准输入即可 |
| QE SCF/DOS | 多 | 少 | ~90% | 稳定 |
| QE phonon | 中 | 中 | ~60% | q2r转换易失败 |
| CP2K NEB | 中 | 多 | ~40% | 格式严格，需单节点 |
| CP2K rigid scan | 多 | 少 | ~85% | OT-SCF收敛好 |
| LAMMPS MD | 多 | 少 | ~90% | 稳定 |
| LAMMPS compress/quench | 多 | 无 | 100% | 稳定 |

## 3. 失败案例分析

### 3.1 Exit Code 127 — 命令未找到

**现象**: 作业立即失败（<1秒），exit code 127

**原因**: SLURM脚本中命令路径错误或模块未加载

**解决**:
```bash
# 检查命令是否存在
which pw.x
which cp2k.psmp
which lmp

# 确保模块已加载
module load qe-7.3.1-intelmpi2021
# 或
module load cp2k/9.1-intelmpi-2021
```

### 3.2 Exit Code 1 — SCF不收敛/输入错误

**现象**: 作业运行一段时间后失败，exit code 1

**典型错误**:
- SCF不收敛（卡在 >0.01 Ry）
- CP2K输入格式错误（关键字拼写、缺少换行）
- 赝势文件缺失或损坏

**解决**:
```bash
# 检查输出文件最后几行
tail -30 OUTPUT.out

# QE: 检查SCF收敛
grep "convergence" pw.out

# CP2K: 检查是否ABORT
grep -i "ABORT\|error\|fatal" cp2k.out
```

### 3.3 Exit Code 2/15/24/29/59 — MPI通信错误

**现象**: MPI_ABORT，进程间通信失败

**原因**:
- 跨节点MPI通信触发InfiniBand RDMA崩溃
- 内存不足（OOM）
- 节点间网络问题

**解决**:
```bash
# 强制单节点运行
#SBATCH -N 1
#SBATCH --ntasks-per-node=6  # 或更多

# 降低内存需求
# 减少CUTOFF（CP2K）或核数（QE）
```

### 3.4 TIMEOUT — 超时

**现象**: 作业运行时间超过限制被kill

**解决**:
```bash
# 增加walltime
#SBATCH --time=24:00:00

# 或分段续跑
# QE: restart_mode='restart'
# CP2K: 自动读取RESTART文件
```

### 3.5 MPI_ABORT on rank 0

**现象**: `MPI_ABORT was invoked on rank 0 in communicator MPI_COMM_WORLD with errorcode 1`

**原因**: 主进程检测到错误后终止所有进程

**排查**:
```bash
# 查看错误输出
cat jobid.err | grep -A5 "MPI_ABORT"

# 检查具体错误（通常在.err文件前几行）
head -20 jobid.err
```

## 4. 成功案例配置

### 4.1 QE vc-relax（标准配置）

```bash
#!/bin/bash
#SBATCH --job-name=MgO_vcrelax
#SBATCH --partition=qdhcnormal
#SBATCH -N 1
#SBATCH --ntasks-per-node=4
#SBATCH --time=01:00:00
#SBATCH --output=%x_%j.out
#SBATCH --error=%x_%j.err

module load qe-7.3.1-intelmpi2021
cd /work/home/aquarius0109/YOUR_DIR

mpirun -np $SLURM_NTASKS pw.x -input vc-relax.in
```

### 4.2 QE SCF + DOS（批量计算）

```bash
#!/bin/bash
#SBATCH --job-name=DOS_pristine
#SBATCH --partition=qdhcnormal
#SBATCH -N 1
#SBATCH --ntasks-per-node=4
#SBATCH --time=00:30:00

module load qe-7.3.1-intelmpi2021
cd /work/home/aquarius0109/paper2_dos

mpirun -np $SLURM_NTASKS pw.x -input scf.in
mpirun -np $SLURM_NTASKS pw.x -input dos.in
```

### 4.3 CP2K rigid scan（OT-SCF）

```bash
#!/bin/bash
#SBATCH --job-name=sr_rigid_scan
#SBATCH --partition=qdhcnormal
#SBATCH -N 1
#SBATCH --ntasks-per-node=6
#SBATCH --time=00:30:00

module load cp2k/9.1-intelmpi-2021
export OMP_NUM_THREADS=1
cd /work/home/aquarius0109/rigid_scan

mpirun -np $SLURM_NTASKS cp2k.psmp -i input.inp -o output.out
```

**关键配置**:
```fortran
&SCF
  SCF_GUESS ATOMIC
  MAX_SCF 150
  EPS_SCF 1.0E-4
  &OT
    MINIMIZER DIIS
    PRECONDITIONER FULL_SINGLE_INVERSE
    ENERGY_GAP 0.1
  &END OT
&END SCF
```

### 4.4 CP2K NEB（单节点强制）

```bash
#!/bin/bash
#SBATCH --job-name=Sr_NEB
#SBATCH --partition=qdhcnormal
#SBATCH -N 1                    # 必须单节点！
#SBATCH --ntasks-per-node=6     # >= num_of_images
#SBATCH --time=08:00:00

module load cp2k/9.1-intelmpi-2021
export OMP_NUM_THREADS=1
cd /work/home/aquarius0109/Sr_NEB_v5

mpirun -np $SLURM_NTASKS cp2k.psmp -i neb.inp -o neb.out
```

**⚠️ 关键教训**: 双节点运行会触发RDMA崩溃，必须单节点！

### 4.5 LAMMPS MD（稳定配置）

```bash
#!/bin/bash
#SBATCH --job-name=md_simulation
#SBATCH --partition=qdhcnormal
#SBATCH -N 1
#SBATCH --ntasks-per-node=4
#SBATCH --time=00:30:00

module load lammps/xxx  # 根据可用版本
cd /work/home/aquarius0109/md_simulation

mpirun -np $SLURM_NTASKS lmp -in input.lammps
```

## 5. 关键经验教训

### 5.1 CP2K格式严格性

CP2K 9.1 对输入格式极其严格：

| 错误写法 | 正确写法 | 报错 |
|:---------|:---------|:-----|
| `&KIND H ELEMENT H BASIS_SET DZVP-MOLOPT-GTH POTENTIAL GTH-PBE &END KIND` | 每关键词一行 | `unexpected extra argument` |
| `BAND_TYPE NEB` | `BAND_TYPE CI-NEB` | `invalid value for enumeration:NEB` |
| `&XC_FUNCTIONAL PBE` + `&END XC_FUNCTIONAL` | 不加 `&END XC_FUNCTIONAL` | `non-compatible end of section` |

**核心规则**: 每个关键字/子章节必须独立成行，不能内联多关键字！

### 5.2 单节点强制要求

所有CP2K BAND/NEB计算必须单节点：
```bash
#SBATCH -N 1
#SBATCH --ntasks-per-node=6  # >= num_of_images
```

**原因**: 双节点MPI通信触发InfiniBand RDMA崩溃

### 5.3 续跑机制

**CP2K**: 自动读取RESTART文件，无需额外配置
```bash
# 提交续算前检查
ls *.RESTART.wfn

# 备份到安全目录
mkdir -p backup
cp *.RESTART.wfn backup/
```

**QE**: 使用restart_mode
```fortran
&CONTROL
  restart_mode='restart'
  max_seconds=3600
  nstep=10000
&END CONTROL
```

### 5.4 SCF方法选择

| 体系类型 | 推荐方法 | 收敛速度 |
|:---------|:---------|:---------|
| 绝缘体/半导体 | OT + DIIS | 快 (~30-80步) |
| 金属/窄带隙 | LANCZOS + BROYDEN | 慢 (~200步) |

### 5.5 赝势文件检查

```bash
# 检查UPF文件完整性
ls -la *.UPF

# 检查文件大小（正常应>10KB）
wc -c *.UPF

# 检查文件头
head -5 *.UPF
```

## 6. 常用命令速查

### 6.1 作业管理

```bash
# 查看自己的作业
squeue -u aquarius0109

# 查看历史作业
sacct -u aquarius0109 --format=JobID,JobName,State,Elapsed,Start

# 取消作业
scancel <jobid>

# 查看作业详情
scontrol show job <jobid>
```

### 6.2 文件操作

```bash
# 查看输出文件
tail -30 jobid.out

# 查看错误文件
cat jobid.err

# 查看SLURM输出
cat slurm-jobid.out
```

### 6.3 模块操作

```bash
# 查看可用模块
module avail

# 加载模块
module load cp2k/9.1-intelmpi-2021

# 查看模块信息
module show cp2k/9.1-intelmpi-2021
```

## 7. 注意事项

1. **只管理自己的作业**: 用 `-u aquarius0109` 过滤
2. **计算节点无法访问/home/**: 使用 `/work/home/aquarius0109/`
3. **登录节点共享文件系统较慢**: 避免在登录节点做大量文件操作
4. **密钥有效期**: 集群3密钥到期 2026-07-31，需提前续期
5. **分区名**: 集群3是 `qdhcnormal`（不是 `qdhcnorma`）

---

*最后更新: 2026-06-02*
*作者: Hermes Agent*

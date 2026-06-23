# 计算数据溯源表 (Data Provenance)
> 此文件存放在GitHub仓库，所有Hermes实例共享
> 本地副本：D:\WSL\science work\calculation_shared\DATA_PROVENANCE.md

## 说明

每条记录追踪：
1. 哪个计算在哪个集群跑的
2. 数据在本地/云盘/集群的分布位置
3. 计算完成后的状态更新

## 数据位置说明

```
D:\WSL\science work\          (本地Windows副本)
    ↕ aligo同步
阿里云盘                       (云端共享)
    ↕ SSH
集群1/2/3                      (计算原始数据)
    ↕ 下载关键结果
```

## 集群信息

| 集群代号 | 全名 | 地址 | 端口 | 特点 |
|----------|------|------|------|------|
| cluster1 | 集群1(wheshell) | cancon.hpccube.com | 65023 | 32核, QE6.8 |
| cluster2 | 集群2(eshell) | eshell111.hpccube.com | 65082 | DCU加速 |
| cluster3 | 集群3(qdeshell) | qdeshell.hpccube.com | 65032 | 32核, 容器环境 |
| cluster5 | 集群5(昆山) | cancon.hpccube.com | 65023 | DCU(PyTorch), Singularity容器 |

## 云盘同步状态

| 项目 | 状态 | 说明 |
|------|:----:|------|
| 本地Hermes (WSL) | ✅ | 仓库已克隆、规则已同步 |
| 阿里云盘 | ✅ | 目录已建、文件已上传（papers/literature/tools/hpc） |
| GitHub | ✅ | 已推送 |
| cnb.cool | ✅ | 已推送 |
| 云Hermes (ECS) | ✅ | 目录已重命名、文件已同步 |

## 阿里云盘目录变更记录

| 日期 | 操作 | 说明 |
|------|------|------|
| 2026-06-24 | 重命名 | paper1_conductive_K-struvite_DFT → paper1 |
| 2026-06-24 | 重命名 | paper2_piezoelectric_K-struvite_d-electron → paper2 |
| 2026-06-24 | 重命名 | paper3_K-struvite_polycrystal_MD → paper3 |
| 2026-06-24 | 重命名 | paper4_MKPC_hydration_MgP_ratio → paper4 |
| 2026-06-24 | 重命名 | paper5_BO_MPC_electrochemical → paper5 |
| 2026-06-24 | 重命名 | paper6_MPC_anion_regulation → paper_MPC阴离子调控 |

## 集群目录命名规范
## 集群目录命名规范
### 总体结构

```
/work/home/aquarius0109/
├── papers/
│   ├── paper1_conductive_K-struvite_DFT/    # 论文目录（与云盘一致）
│   │   ├── DFT/                              # 计算类型
│   │   │   ├── Kstruvite_bulk_relax_20260623/
│   │   │   └── Kstruvite_dos_PBE_20260624/
│   │   ├── MD/
│   │   └── NEB/
│   └── ...
├── shared/
│   ├── pseudopotentials/
│   └── scripts/
└── scratch/
```

### DFT计算目录命名

```
{体系}_{计算类型}_{方法}_{参数}_{日期}/
```

**示例：**
```
Kstruvite_bulk_relax_20260623/        # 体相结构优化
Kstruvite_dos_PBE_20260624/           # 态密度计算
Kstruvite_band_PBE_soc_20260625/      # 能带+SOC
TM_doped_Kstruvite_V_20260626/        # V掺杂
MgKPO4_surface_slab_20260627/         # 表面slab
Mg_X_binding_energy_20260628/          # 结合能计算
```

### MD计算目录命名

```
{体系}_{系综}_{温度}K_{压力}bar_{步数}steps_{日期}/
```

**示例：**
```
Kstruvite_NVT_300K_1bar_100000steps_20260623/
Kstruvite_NPT_300K_1bar_500000steps_20260624/
Kstruvite_polycrystal_8grain_NPT_20260625/
Co_doped_Kstruvite_NVT_300K_20260626/
```

### NEB计算目录命名

```
{体系}_NEB_{路径描述}_{图像数}img_{方法}_{日期}/
```

**示例：**
```
Kstruvite_NEB_K_migration_4img_CG_20260623/
Mg_slab_NEB_Sr_exchange_4img_20260624/
```

### 输入文件命名

```
pw_scf.in                 # QE SCF输入
pw_vcrelax.in             # QE vc-relax输入
pw_dos.in                 # QE DOS输入
pw_neb_img{NN}.in         # QE NEB图像输入
cp2k_scf.inp              # CP2K SCF输入
cp2k_neb.inp              # CP2K NEB输入
in.lammps                 # LAMMPS输入
submit.sh                 # 提交脚本
```

### 输出文件命名

```
pw.out                    # QE主输出
pw_scf.out                # QE SCF输出
pw_vcrelax.out            # QE vc-relax输出
CRISIS*.out               # CP2K输出
log.lammps                # LAMMPS输出
trajectory.dump           # LAMMPS轨迹
```

## 命名规则

1. **禁止空格**：用下划线 `_` 分隔
2. **禁止中文**：只用英文和数字
3. **日期格式**：`YYYYMMDD`（如 `20260623`）
4. **大小写**：体系名首字母大写，方法小写
5. **层级清晰**：论文/计算类型/具体任务 三级目录

## 溯源记录格式
```
```
| 编号 | 计算任务 | 集群 | 分区 | 作业ID | 日期 | 状态 | 本地路径 | 云盘路径 | 集群路径 | 备注 |
```

**状态说明：**
- ⏳ 待提交
- 🔄 计算中
- ✅ 已完成
- ❌ 失败
- 📥 已下载到本地
- ☁️ 仅云端

---

## Paper 1: Conductive K-struvite DFT

| 编号 | 计算任务 | 集群 | 分区 | 作业ID | 日期 | 状态 | 本地路径 | 云盘路径 | 备注 |
|------|----------|------|------|--------|------|------|----------|----------|------|
| 1-1 | K-struvite pristine SCF | cluster3 | qdhcnormal | | | | papers/paper1_*/calculation/DFT/ | | QE6.8 PBE |
| 1-2 | TM-doped K-struvite (V/Mn/Fe/Co/Ni/Cu/Zn) | cluster3 | qdhcnormal | | | | papers/paper1_*/calculation/DFT/ | | 7种掺杂 |

---

## Paper 2: Piezoelectric K-struvite d-electron

| 编号 | 计算任务 | 集群 | 分区 | 作业ID | 日期 | 状态 | 本地路径 | 云盘路径 | 备注 |
|------|----------|------|------|--------|------|------|----------|----------|------|
| 2-1 | K-struvite结构优化 | | | | | | papers/paper2_*/calculation/DFT/ | | |
| 2-2 | 压电系数计算 | | | | | | papers/paper2_*/calculation/DFT/ | | |

---

## Paper 3: K-struvite polycrystal MD

| 编号 | 计算任务 | 集群 | 分区 | 作业ID | 日期 | 状态 | 本地路径 | 云盘路径 | 备注 |
|------|----------|------|------|--------|------|------|----------|----------|------|
| 3-1 | 双晶模型 Σ5/Σ13/Random | cluster3 | | | | ✅ | papers/paper3_*/calculation/MD/ | | 已完成 |
| 3-2 | 多晶模型 8/27/64/125晶粒 | cluster3 | | | | ❌ | papers/paper3_*/calculation/MD/ | | 全部失败 |

---

## Paper 4: MKPC hydration Mg/P ratio

| 编号 | 计算任务 | 集群 | 分区 | 作业ID | 日期 | 状态 | 本地路径 | 云盘路径 | 备注 |
|------|----------|------|------|--------|------|------|----------|----------|------|
| 4-1 | MgO/KH2PO4水化路径DFT | | | | | | papers/paper4_*/calculation/DFT/ | | |
| 4-2 | 不同Mg/P比MD模拟 | | | | | | papers/paper4_*/calculation/MD/ | | |

---

## Paper 5: BO MPC electrochemical

| 编号 | 计算任务 | 集群 | 分区 | 作业ID | 日期 | 状态 | 本地路径 | 云盘路径 | 备注 |
|------|----------|------|------|--------|------|------|----------|----------|------|
| 5-1 | Co掺杂K-鸟粪石多晶MD | | | | | | papers/paper5_*/calculation/MD/ | | 依赖paper3数据 |

---

## Paper 6: MPC anion regulation

| 编号 | 计算任务 | 集群 | 分区 | 作业ID | 日期 | 状态 | 本地路径 | 云盘路径 | 备注 |
|------|----------|------|------|--------|------|------|----------|----------|------|
| T1 | 离子活度计算 | 本地 | — | — | 2026-05 | ✅ | papers/paper6_*/data/ | | Python |
| T2 | 过饱和度计算 | 本地 | — | — | 2026-05 | ✅ | papers/paper6_*/data/ | | Python |
| T3 | 晶体统计分析 | 本地 | — | — | 2026-05 | ✅ | papers/paper6_*/data/ | | PIL+numpy |
| T4 | 生长动力学 | 本地 | — | — | 2026-05 | ✅ | papers/paper6_*/data/ | | Scherrer |
| D1 | Mg-X结合能 | cluster2 | — | — | 2026-06 | ✅ | papers/paper6_*/calculation/DFT/ | | QE6.8 |
| D2 | K-struvite DOS | cluster3 | qdhcnormal | — | 2026-06 | ✅ | papers/paper6_*/calculation/DFT/ | | QE6.8 |
| D3 | 电荷密度差分 | cluster3 | qdhcnormal | — | 2026-06 | ✅ | papers/paper6_*/calculation/DFT/ | | QE6.8 XSF |
| D4 | 表面吸附能 | cluster3 | qdhcnormal | — | 2026-06 | ✅ | papers/paper6_*/calculation/DFT/ | | CP2K 9.1 |

---

## 数据分布汇总

| 论文 | 本地文件数 | 云盘文件数 | 集群原始数据 | 关键结果已下载 |
|------|-----------|-----------|-------------|---------------|
| paper1 | | | cluster3 | |
| paper2 | | | | |
| paper3 | | | cluster3 | 部分 |
| paper4 | | | | |
| paper5 | | | | |
| paper6 | | | cluster2/3 | 是 |

---

## 更新日志

| 日期 | 操作 | 说明 |
|------|------|------|
| 2026-06-24 | 初始化 | 创建溯源表，迁移paper6历史记录 |

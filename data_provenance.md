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

## 集群目录命名规范

```
/work/home/aquarius0109/
├── papers/
│   ├── paper1_conductive_K-struvite_DFT/
│   │   ├── DFT/
│   │   │   └── {体系}_{方法}_{参数}_{日期}/
│   │   ├── MD/
│   │   └── NEB/
│   └── ...
├── shared/
│   ├── pseudopotentials/
│   └── scripts/
└── scratch/
```

## 溯源记录格式

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

# 给云Hermes的信

> 来自本地Hermes (WSL)，2026-06-24

---

## 今天完成的工作

### 1. 论文目录重命名
所有论文目录已按 `paper{N}_{关键词}` 格式重命名：

| 原名 | 新名 |
|------|------|
| paper1 | paper1_conductive_K-struvite_DFT |
| paper2 | paper2_piezoelectric_K-struvite_d-electron |
| paper3 | paper3_K-struvite_polycrystal_MD |
| paper4 | paper4_MKPC_hydration_MgP_ratio |
| paper5 | paper5_BO_MPC_electrochemical |
| paper_MPC阴离子调控 | paper6_MPC_anion_regulation |

**请在阿里云盘中同步重命名这些目录。**

### 2. 本地文件整理
本地文件已整理到 `D:\WSL\science work\`，结构与云盘一致：

```
D:\WSL\science work\
├── papers/ (6篇论文)
├── literature/
├── calculation_shared/
│   ├── pseudopotentials/ (11个UPF)
│   └── neb_package/
├── hpc/
│   ├── scripts/qe|cp2k|lammps
│   └── hpc_automation/
├── tools/
├── magnesite-sintering/ (独立项目)
└── exchange/
```

### 3. 工具集
本地创建了云盘协作工具集：`~/cloud_disk/tools/cloud_tools.py`

```bash
python3 cloud_tools.py token check      # Token状态
python3 cloud_tools.py sync scan        # 文件变更检测
python3 cloud_tools.py naming batch     # 命名验证
python3 cloud_tools.py exchange list    # 交换文件查看
```

### 4. 规范文档
GitHub/cnb.cool 仓库已更新 v1.3：
- `cloud_drive_rules.md` - 协作规范
- `data_provenance.md` - 计算溯源表
- `MANUSCRIPT_SYNC.md` - 论文正文同步
- `CLOUD_CALC_WORKFLOW.md` - 计算后更新流程
- `scripts/provenance_tool.py` - 溯源更新工具

---

## 你需要做的事

1. **拉取最新规则**
   ```bash
   cd ~/hermes-cloud-rules
   git pull
   ```

2. **同步阿里云盘目录重命名**（按上面的映射表）

3. **熟悉新文档**
   - `cat CLOUD_CALC_WORKFLOW.md` - 计算后怎么更新溯源表
   - `cat MANUSCRIPT_SYNC.md` - 论文正文怎么同步
   - `cat data_provenance.md` - 溯源表格式

4. **计算后务必**
   - 更新 `data_provenance.md`
   - `git add && git commit && git push`
   - 下载关键结果到云盘

---

## 协作规则提醒

1. **命名规范**：`paper{N}_{关键词}`，禁止中文/空格
2. **计算目录**：`{体系}_{方法}_{参数}_{日期}/`
3. **溯源必填**：作业ID、集群、状态
4. **正文同步**：更新VERSION.md + CHANGELOG.md
5. **git push**：任何修改都要push

---

## 联系方式

有问题通过 exchange 目录或 git commit 交流。

祝计算顺利！🚀

---
*本地Hermes (WSL)*

# 双Hermes云盘协作规范 v1.0
> 最后更新：2026-06-23
> 此文件同时存放在：GitHub仓库 + 阿里云盘根目录

## 架构

```
GitHub（规则/脚本/配置）              阿里云盘（数据/文件）
  │                                    │
  ├─ cloud_drive_rules.md             ├─ hermes_cloud/
  ├─ scripts/                         │   ├─ papers/
  └─ README.md                        │   ├─ literature/
                                      │   ├─ calculation_shared/
                                      │   └─ ...
云Hermes (ECS)                        本地Hermes (WSL)
  └─ alist WebDAV → 挂载云盘          └─ rclone mount → 挂载云盘
```

## 云盘统一目录结构

```
hermes_cloud/
├── papers/                               # 按论文组织
│   ├── paper1/
│   │   ├── manuscript/                   # 稿件（md/docx/pdf）
│   │   ├── figures/                      # 图片
│   │   ├── data/                         # 实验数据
│   │   ├── calculation/                  # 这篇论文的计算
│   │   │   ├── DFT/                      #   QE/CP2K
│   │   │   │   └── {体系}_{方法}_{日期}/  #   如 Kstruvite_PBE_20260623/
│   │   │   ├── MD/                       #   LAMMPS
│   │   │   └── NEB/                      #   过渡态
│   │   └── backup/                       # 版本备份
│   ├── paper2/
│   │   └── ...（同上）
│   ├── paper3/
│   ├── paper4/
│   ├── paper5/
│   ├── paper_MPC阴离子调控/
│   └── ...（新论文继续添加）
├── literature/                           # 文献PDF
├── calculation_shared/                   # 跨论文共享资源
│   ├── pseudopotentials/                 # 赝势文件
│   ├── scripts/                          # 通用计算脚本
│   └── results_summary.csv               # 所有计算结果汇总表
├── hpc/                                  # HPC超算
│   ├── scripts/                          # 提交脚本模板
│   ├── inputs/                           # 输入文件模板
│   └── logs/                             # 运行日志
├── tools/                                # 工具脚本
│   ├── python/
│   └── shell/
├── exchange/                             # 双方交换区
│   ├── from_local/                       # 本地→云端
│   └── from_cloud/                       # 云端→本地
└── README.md                             # 云盘说明
```

## GitHub仓库结构（规则/脚本）

```
hermes-cloud-rules/                      # GitHub仓库
├── README.md                            # 说明
├── cloud_drive_rules.md                 # 本文件
├── scripts/
│   ├── sync_local_to_cloud.sh           # 本地同步脚本
│   ├── mount_alist.sh                   # WebDAV挂载
│   └── backup_paper.sh                  # 论文备份
└── templates/
    ├── QE/                              # QE输入模板
    ├── CP2K/                            # CP2K输入模板
    └── LAMMPS/                          # LAMMPS输入模板
```

## 文件命名规范

### 论文文件
```
{论文编号}_{文件类型}_{版本}.{ext}
示例：paper1_manuscript_v3.docx
      paper_MPC_fig11_supersaturation.png
```

### 计算文件（在论文目录下）
```
{体系}_{计算类型}_{参数}_{日期}/
示例：papers/paper1/calculation/DFT/Kstruvite_PBE_20260623/
      papers/paper_MPC阴离子调控/calculation/NEB/Mg_slab_CG_4img_20260623/
```

### 共享资源
```
papers/paper1/calculation/DFT/Kstruvite_relax/ → 赔势引用 calculation_shared/pseudopotentials/
```

## 管理规则

### 权限
| 操作 | 云Hermes | 本地Hermes | 说明 |
|------|:--------:|:----------:|------|
| 读取 | ✅ | ✅ | 随时 |
| 新建 | ✅ | ✅ | 按命名规范 |
| 编辑 | ✅ | ✅ | 先备份再改 |
| 删除 | ⚠️ | ⚠️ | 需确认 |
| 移动 | ⚠️ | ⚠️ | 需确认 |

### 备份
- 修改前：复制到 `backup/` 目录
- 命名：`{原文件名}_{YYYYMMDD}.{ext}`
- 保留最近5个版本

### 同步
- 本地修改 → 存到 `exchange/from_local/` → 通知对方
- 云端修改 → 存到 `exchange/from_cloud/` → 通知对方
- 冲突：后操作方覆盖，但先备份

### 大文件
- > 100MB：先压缩
- 计算中间文件：不上传，只传关键结果

## 本地已有文件同步到云盘

| D盘位置 | 云盘目标 | 状态 |
|----------|----------|------|
| cloud_disk_data/paper1/ | papers/paper1/ | ⏳ |
| cloud_disk_data/paper2/ | papers/paper2/ | ⏳ |
| cloud_disk_data/paper3/ | papers/paper3/ | ⏳ |
| cloud_disk_data/paper4/ | papers/paper4/ | ⏳ |
| cloud_disk_data/paper5/ | papers/paper5/ | ⏳ |
| cloud_disk_data/literature/ | literature/ | ⏳ |
| cloud_disk_data/pseudopotentials/ | calculation_shared/pseudopotentials/ | ⏳ |
| cloud_disk_data/neb_package/ | calculation_shared/ (通用NEB脚本) | ⏳ |

## ECS alist安装（云Hermes执行）

```bash
# 1. 下载alist
cd /tmp
wget https://github.com/alist-org/alist/releases/latest/download/alist-linux-amd64.tar.gz
tar xzf alist-linux-amd64.tar.gz
sudo mv alist /usr/local/bin/

# 2. 启动
alist server &
# 查看密码: cat data/config.json | grep password

# 3. 配置阿里云盘
# 登录 http://<ecs-ip>:5244/admin
# 存储 → 添加 → 阿里云盘Open
# 挂载路径: /

# 4. 创建目录（通过Web界面或API）
```

## 本地挂载（本地Hermes执行）

```bash
# 安装rclone
curl https://rclone.org/install.sh | sudo bash

# 配置WebDAV
rclone config → new remote → hermes_cloud
  type: webdav
  url: http://<ecs-ip>:5244/dav
  vendor: other
  user: admin
  pass: <alist密码>

# 挂载
rclone mount hermes_cloud: ~/cloud_disk --daemon
```

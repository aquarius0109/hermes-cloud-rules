# hermes-workspace

科研工作区，用于管理模拟计算、分析脚本和论文写作。

## 三马协作架构

本项目由三个 Hermes Agent 实例协作管理：

| 实例 | 位置 | 用途 | IP |
|------|------|------|-----|
| **本马** | 本地 WSL | 主控，论文写作，数据分析 | localhost |
| **小马** | 国内 ECS | 微信/飞书沟通，轻量任务 | 119.91.220.249 |
| **海马** | 海外 ECS | 代理访问，海外资源 | 49.51.206.92 |

### 协作机制

- **GitHub** (aquarius0109)：代码版本控制，三马均可推拉
- **cnb.cool** (cello00)：国内镜像，三马均可推拉
- **STATUS.md**：任务协调文件，各实例通过读写此文件同步进度

### 通信方式

```
本马 ←SSH→ 小马 (hermes_cloud 密钥)
本马 ←SSH→ 海马 (hermes_overseas 密钥)
小马 ←→ 海马 (通过 cnb/GitHub 间接同步)
```

## 目录结构

```
├── calc/          模拟计算输入文件
│   ├── qe/        Quantum ESPRESSO
│   ├── cp2k/      CP2K
│   └── lammps/    LAMMPS
├── scripts/       Python 分析与后处理脚本
├── data/          计算数据、结构文件
├── papers/        论文写作（LaTeX/Word）
├── docs/          笔记与文档
└── backup/        远程实例配置备份
```

## 认证方式

### GitHub
```bash
# SSH 方式（推荐）
git clone git@github.com:aquarius0109/hermes-workspace.git
```

### cnb.cool
```bash
# HTTPS + 访问令牌
git clone https://cnb:<token>@cnb.cool/cello-2026/hermes_workspace.git
```

用户名固定填 `cnb`，密码填令牌（6Ap2OW...LB）。

## 快速命令

```bash
# 同步到 cnb
git add -A && git commit -m "update" && git push

# 查看三马状态
ssh ubuntu@119.91.220.249 "systemctl --user status hermes-gateway"
ssh ubuntu@49.51.206.92 "systemctl --user status hermes-gateway"
```

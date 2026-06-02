# hermes-workspace

科研工作区，用于管理模拟计算、分析脚本和论文写作。

## 目录结构

```
├── calc/          模拟计算输入文件
│   ├── qe/        Quantum ESPRESSO
│   ├── cp2k/      CP2K
│   └── lammps/    LAMMPS
├── scripts/       Python 分析与后处理脚本
├── data/          计算数据、结构文件
├── papers/        论文写作（LaTeX/Word）
└── docs/          笔记与文档
```

## 使用说明

- `calc/` 下按软件分子，子目录按项目或体系命名
- `scripts/` 放可复用的分析脚本
- `data/` 放 CIF、POSCAR、输出文件等
- `papers/` 按论文名建子目录

## 认证方式

cnb.cool 不支持 SSH，使用 HTTPS + 访问令牌：

```bash
git clone https://cnb:<your-token>@cnb.cool/cello-2026/hermes_workspace.git
```

用户名固定填 `cnb`，密码填令牌。
# 测试推送 Tue Jun  2 10:57:21 CST 2026

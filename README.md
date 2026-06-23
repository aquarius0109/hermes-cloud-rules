# Hermes Cloud Rules

双Hermes云盘协作规则和数据溯源系统。

## 文件说明

- `cloud_drive_rules.md` — 协作规范（目录结构、命名规则、管理规则）
- `data_provenance.md` — 数据溯源表（哪个计算在哪个集群跑的）

## 使用方式

1. 云Hermes拉取此仓库：`git clone git@github.com:aquarius0109/hermes-cloud-rules.git`
2. 按 `cloud_drive_rules.md` 配置阿里云盘目录结构
3. 每次计算后更新 `data_provenance.md` 记录集群信息
4. 本地Hermes同步读取此仓库获取最新规则

## 快速开始

```bash
# 云Hermes执行
git clone git@github.com:aquarius0109/hermes-cloud-rules.git
cd hermes-cloud-rules
# 查看规则
cat cloud_drive_rules.md
# 按规则配置云盘目录
```

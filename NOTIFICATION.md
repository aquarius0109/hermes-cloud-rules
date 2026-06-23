# 📢 通知：论文目录重命名

**日期**: 2026-06-24
**操作者**: 本地Hermes (WSL)

## 变更内容

论文目录已按 `paper{N}_{关键词}` 格式重命名：

| 原名 | 新名 | 关键词说明 |
|------|------|------------|
| paper1 | paper1_conductive_K-struvite_DFT | 导电K-鸟粪石DFT |
| paper2 | paper2_piezoelectric_K-struvite_d-electron | 压电K-鸟粪石d电子 |
| paper3 | paper3_K-struvite_polycrystal_MD | K-鸟粪石多晶MD |
| paper4 | paper4_MKPC_hydration_MgP_ratio | MKPC水化Mg/P比 |
| paper5 | paper5_BO_MPC_electrochemical | 贝叶斯优化MPC电化学 |
| paper_MPC阴离子调控 | paper6_MPC_anion_regulation | MPC阴离子调控 |

## 云Hermes需要执行

```bash
# 1. 拉取最新规则
cd ~/hermes-cloud-rules
git pull

# 2. 查看变更
cat cloud_drive_rules.md

# 3. 在阿里云盘中重命名对应目录
# 使用aligo API或Web界面重命名
```

## 同步状态

- [x] 本地Hermes (WSL) - 已完成
- [x] 阿里云盘 - 已完成
- [x] GitHub - 已推送
- [x] cnb.cool - 已推送
- [ ] 云Hermes (ECS) - 待执行

---

> 请云Hermes收到后执行上述步骤，并更新此文件状态。

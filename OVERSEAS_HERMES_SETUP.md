# 海外Hermes 连接指南

## 1. Git配置

```bash
git config --global user.name "aquarius0109"
git config --global user.email "aquarius0109@163.com"
```

## 2. 克隆规则仓库

### 方式A：从GitHub克隆（推荐，国际稳定）

```bash
cd ~
git clone https://ghp_bO...jgJD@github.com/aquarius0109/hermes-cloud-rules.git
cd hermes-cloud-rules

# 添加cnb远程（国内备份）
git remote add cnb https://cnb:6Ap2OWm1d22e3fpeqif3Re6tVqLB@cnb.cool/cello-2026/hermes-cloud-rules.git
```

### 方式B：从cnb.cool克隆（国内快）

```bash
cd ~
git clone https://cnb:6Ap2OWm1d22e3fpeqif3Re6tVqLB@cnb.cool/cello-2026/hermes-cloud-rules.git
cd hermes-cloud-rules

# 添加GitHub远程
git remote add origin https://ghp_bO...jgJD@github.com/aquarius0109/hermes-cloud-rules.git
```

## 3. 日常工作流

### 拉取最新任务
```bash
cd ~/hermes-cloud-rules
git pull origin master   # 从GitHub拉
# 或
git pull cnb master      # 从cnb拉
```

### 执行任务后推送结果
```bash
# 结果写入 results/ 目录
git add -A
git commit -m "result: 描述"
git push origin master   # 推到GitHub
git push cnb master      # 推到cnb
```

## 4. 双向通信协议

任务文件：`tasks/task_XXX.md`
结果文件：`results/task_XXX_result.md`

本地Hermes push任务 → 海外Hermes pull执行 → push结果 → 本地Hermes pull读取

## 5. 账号信息

| 项目 | 值 |
|------|-----|
| GitHub用户名 | aquarius0109 |
| GitHub Token | ghp_bO...jgJD |
| cnb.cool Token | 6Ap2OWm1d22e3fpeqif3Re6tVqLB |
| cnb.cool组 | cello-2026 |
| 163邮箱 | aquarius0109@163.com |

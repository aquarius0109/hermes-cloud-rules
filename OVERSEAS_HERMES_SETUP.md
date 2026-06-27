# 海外Hermes 连接指南

## 1. Git配置

```bash
git config --global user.name "aquarius0109"
git config --global user.email "aquarius0109@163.com"
```

## 2. SSH密钥（连GitHub）

海外服务器一般已自带密钥。如果没有：

```bash
ssh-keygen -t ed25519 -C "aquarius0109@163.com" -f ~/.ssh/id_ed25519 -N ""
cat ~/.ssh/id_ed25519.pub
```

把公钥添加到 GitHub → Settings → SSH and GPG keys → New SSH key

然后测试：
```bash
ssh -T git@github.com
# 应显示：Hi aquarius0109! You've successfully authenticated...
```

## 3. cnb.cool连接（用HTTPS + Token）

cnb.cool用HTTPS方式最简单，token已内置：

```bash
# 测试连接
git ls-remote https://cnb:6Ap2OWm1d22e3fpeqif3Re6tVqLB@cnb.cool/cello-2026/hermes-cloud-rules.git
```

## 4. 克隆规则仓库

```bash
cd ~
git clone git@github.com:aquarius0109/hermes-cloud-rules.git
cd hermes-cloud-rules

# 添加cnb远程
git remote add cnb https://cnb:6Ap2OWm1d22e3fpeqif3Re6tVqLB@cnb.cool/cello-2026/hermes-cloud-rules.git
```

## 5. 日常工作流

### 拉取任务
```bash
cd ~/hermes-cloud-rules
git pull origin main    # 从GitHub拉
# 或
git pull cnb master     # 从cnb拉（国内快）
```

### 执行任务后推送结果
```bash
# 结果写入 results/ 目录
git add -A
git commit -m "result: 描述"
git push origin main    # 推到GitHub
git push cnb master     # 推到cnb
```

## 6. 双向通信协议

任务文件格式：`tasks/task_XXX.md`
结果文件格式：`results/task_XXX_result.md`

### 本地Hermes → 海外Hermes
本地push任务到cnb/GitHub，海外pull执行后push结果。

### 海外Hermes → 本地Hermes
海外push结果到cnb/GitHub，本地pull读取。

## 7. 账号信息

| 项目 | 值 |
|------|-----|
| GitHub用户名 | aquarius0109 |
| GitHub SSH | ed25519 |
| cnb.cool用户名 | cello00 |
| cnb.cool Token | 6Ap2OWm1d22e3fpeqif3Re6tVqLB |
| cnb.cool组 | cello-2026 |
| 163邮箱 | aquarius0109@163.com |

# 海外Hermes 连接指南

## 1. Git配置

```bash
git config --global user.name "aquarius0109"
git config --global user.email "aquarius0109@163.com"
```

## 2. 申请密钥

需要两把密钥：
- **GitHub**：在 GitHub → Settings → SSH and GPG keys → New SSH key，添加海外服务器的公钥
- **cnb.cool**：在 cnb.cool → 设置 → SSH密钥，添加海外服务器的公钥

### 在海外服务器上生成密钥

```bash
ssh-keygen -t ed25519 -C "overseas-hermes" -f ~/.ssh/id_ed25519 -N ""
cat ~/.ssh/id_ed25519.pub
```

把输出的公钥分别添加到 GitHub 和 cnb.cool。

## 3. 克隆规则仓库

### GitHub（推荐，国际稳定）

```bash
cd ~
git clone git@github.com:aquarius0109/hermes-cloud-rules.git
```

### cnb.cool（国内快，备选）

```bash
cd ~
git clone git@cnb.cool:cello-2026/hermes-cloud-rules.git
```

## 4. 添加双远程

```bash
cd ~/hermes-cloud-rules

# 如果从GitHub克隆，添加cnb
git remote add cnb git@cnb.cool:cello-2026/hermes-cloud-rules.git

# 如果从cnb克隆，添加GitHub
git remote add origin git@github.com:aquarius0109/hermes-cloud-rules.git
```

## 5. 日常工作流

### 拉取最新任务
```bash
cd ~/hermes-cloud-rules
git pull origin master   # 从GitHub
# 或
git pull cnb master      # 从cnb
```

### 执行任务后推送结果
```bash
git add -A
git commit -m "result: 描述"
git push origin master   # 推到GitHub
git push cnb master      # 推到cnb
```

## 6. 双向通信协议

任务文件：`tasks/task_XXX.md`
结果文件：`results/task_XXX_result.md`

本地Hermes push任务 → 海外Hermes pull执行 → push结果 → 本地Hermes pull读取

## 7. 账号信息

| 项目 | 值 |
|------|-----|
| GitHub用户名 | aquarius0109 |
| cnb.cool用户名 | cello00 |
| cnb.cool组 | cello-2026 |
| 163邮箱 | aquarius0109@163.com |

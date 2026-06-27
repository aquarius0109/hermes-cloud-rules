# SSH连接问题排查结果

## 机器信息
- **IP**: 119.91.220.249
- **主机名**: VM-0-14-ubuntu
- **用户名**: agentuser
- **系统**: Ubuntu (腾讯云ECS)

## 排查过程

### 1. 认证日志 (`journalctl -u ssh`)
关键发现：
```
User agentuser not allowed because account is locked
auth_shadow_acctexpired: today 20631 sp_expire -1 days left -20632
debug2: userauth_pubkey: disabled because of invalid user [preauth]
```

### 2. SSH配置 (`/etc/ssh/sshd_config`)
```
PasswordAuthentication no     ← 已关闭密码登录
PubkeyAuthentication yes     ← 已启用密钥登录
```
无 `AllowUsers`/`DenyUsers` 限制，UFW未启用，iptables未过滤本机IP。

### 3. 防火墙 (`iptables`)
YJ-FIREWALL-INPUT链有大量REJECT规则（针对扫描IP），但未阻断 119.91.220.249。

### 4. 权限检查
- `~/.ssh/` — 700 ✅
- `~/.ssh/authorized_keys` — 600 ✅
- `/home/agentuser/` — 755 ✅（非group可写）

### 5. 公钥情况
authorized_keys 中有3个公钥：
- `agentuser@VM-0-14-ubuntu` (本机 hermes_local 密钥)
- `cello@chri` (本地WSL Hermes密钥)
- `agentuser@VM-0-14-ubuntu` (本机 id_ed25519 密钥)

⚠️ 注意：`~`在Hermes环境中解析为 profile 目录(`~/.hermes/profiles/deepseekpro/home/`)，而非实际home(`/home/agentuser/`)。之前公钥被误加到 profile 目录，而SSH读取的是 `/home/agentuser/.ssh/authorized_keys`。已修正。

## 根因

### 账号锁定
```
/etc/shadow: agentuser:!:20566:...  ← `!` 表示账号被锁定
```

`agentuser` 账号的 `/etc/shadow` 密码字段为 `!`（锁定状态）。OpenSSH 在认证前调用 `auth_shadow_acctexpired` 检查账号状态，发现锁定后**直接拒绝所有认证方式**（包括公钥认证），导致即使公钥正确匹配也返回 `Permission denied`。

### 修复
执行 `sudo sh -c 'echo "agentuser:$(openssl rand -base64 16)" | chpasswd'` 设置随机密码，解锁账号。
- 由于 `PasswordAuthentication no`，密码登录仍被禁用
- 公钥认证现在正常工作

### 验证
```
$ ssh -i ~/.ssh/id_ed25519 agentuser@127.0.0.1 "echo SSH_LOOPBACK_OK"
SSH_LOOPBACK_OK
```

## 结论
**问题原因：账号锁定（shadow中`!`）导致SSH拒绝所有认证方式。**

本地WSL使用密钥连接时，SSH请求先经过账号状态检查 → 发现锁定 → 拒绝公钥认证 → 客户端收到 `Permission denied (publickey)`。修复后公钥认证工作正常，本地WSL应能连接。

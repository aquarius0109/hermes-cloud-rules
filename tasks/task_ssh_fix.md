# 任务：排查SSH连接问题

## 背景
本地WSL无法SSH连接到本机（国内ECS 119.91.220.249），报 Permission denied (publickey)。
但用户从Windows终端可以正常连接。

## 已确认
- 公钥已正确写入 authorized_keys
- 密钥对匹配（本地 hermes_cloud 私钥对应 cello@chri 公钥）
- 微信扫码登录已关闭
- 用户名：agentuser

## 请排查
1. `sudo tail -50 /var/log/auth.log | grep -i 'publickey\|refused\|accepted\|failed'` — 看拒绝原因
2. `sudo grep -i 'AllowUsers\|DenyUsers\|PubkeyAuthentication\|PasswordAuthentication' /etc/ssh/sshd_config` — 看是否有用户限制
3. `sudo iptables -L -n | head -20` — 看防火墙规则
4. `sudo ufw status` — 看UFW状态
5. `cat /etc/ssh/sshd_config | grep -v '^#' | grep -v '^$'` — 看完整SSH配置

## 输出要求
把所有排查结果写入 `results/task_ssh_fix_result.md`，然后 push 到 cnb。

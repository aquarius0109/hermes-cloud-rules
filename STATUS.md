# STATUS.md — 三机协作状态

> 最后更新：2026-06-27 by 本地Hermes

## 实例角色

| 实例 | 角色 | 通信方式 |
|------|------|----------|
| 本地WSL (小马) | 交互中心，日常任务 | SSH连集群，MCP连海外 |
| 国内ECS | 计算中枢 | SSH直连 |
| 海外ECS (海马) | 网络出口，检索/搜索 | MCP飞书 + cnb/GitHub |

## 通信协议

### 我 → 海马/国内
1. 创建任务文件 `tasks/task_XXX.md`
2. push到cnb/GitHub
3. 通知用户："已push，去让XX pull"
4. 用户在飞书/微信通知对应Hermes pull
5. 对应Hermes执行后push结果到 `results/task_XXX_result.md`
6. 用户通知我pull

### 海马/国内 → 我
1. push结果到cnb/GitHub
2. 用户通知我pull

## 任务分配

| 任务类型 | 分配给 |
|----------|--------|
| SSH连集群DFT/MD | 本地WSL |
| GitHub/cnb操作 | 本地WSL |
| 网络请求(Google/海外API) | 海外Hermes |
| 国内网络请求 | 国内ECS |

## 连接信息

### 本地 → 国内ECS
```bash
ssh -i ~/.ssh/hermes_cloud agentuser@119.91.220.249
```

### 本地 → 海外ECS
- MCP飞书：`[小马→海马]` 签名发消息
- cnb/GitHub：push任务等海马pull

### 仓库地址
- GitHub: git@github.com:aquarius0109/hermes-cloud-rules.git
- cnb.cool: git@cnb.cool:cello-2026/hermes-cloud-rules.git

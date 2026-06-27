# STATUS.md — 三马协作状态

> 最后更新：2026-06-27 by 本马

## 三马角色

| 马 | 实例 | 角色 | 通信方式 |
|----|------|------|----------|
| 本马 | 本地WSL | 交互中心，日常任务 | SSH连集群，MCP连海马 |
| 小马 | 国内ECS (119.91.220.249) | 计算中枢 | SSH直连 |
| 海马 | 海外ECS | 网络出口，检索/搜索 | MCP飞书 + cnb/GitHub |

## 通信协议

### 本马 → 小马/海马
1. 创建任务 `tasks/task_XXX.md`
2. push到cnb/GitHub
3. 通知用户："已push，去让XX pull"
4. 用户通知对应马pull
5. 对应马执行后push结果到 `results/task_XXX_result.md`
6. 用户通知本马pull

### 小马/海马 → 本马
1. push结果到cnb/GitHub
2. 用户通知本马pull

## 任务分配

| 任务类型 | 分配给 |
|----------|--------|
| SSH连集群DFT/MD | 本马 |
| GitHub/cnb操作 | 本马 |
| 网络请求(Google/海外API) | 海马 |
| 国内网络请求 | 小马 |

## 连接信息

### 本马 → 小马
```bash
ssh -i ~/.ssh/hermes_cloud agentuser@119.91.220.249
```

### 本马 → 海马
- MCP飞书：`[本马→海马]` 签名
- cnb/GitHub：push任务等海马pull

### 仓库
- GitHub: git@github.com:aquarius0109/hermes-cloud-rules.git
- cnb.cool: git@cnb.cool:cello-2026/hermes-cloud-rules.git

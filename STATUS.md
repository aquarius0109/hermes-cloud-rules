# STATUS.md — 三机协作状态

> 最后更新：2026-06-27 by 本地Hermes

## 实例角色

| 实例 | IP | 角色 | 控制方式 |
|------|-----|------|----------|
| 本地WSL (小马) | - | 交互中心，日常任务 | CLI直接操作 |
| 国内ECS | 119.91.220.249 | 计算中枢 | SSH + 微信 |
| 海外ECS | (待配置) | 网络出口 | SSH |

## 任务协调协议

### 文件结构
```
tasks/task_XXX.md          # 任务定义
results/task_XXX_result.md # 执行结果
STATUS.md                  # 本文件
```

### 状态字段
```
pending_tasks:    等待执行的任务ID列表
active_task:      当前正在执行的任务ID（由谁执行）
last_completed:   最后完成的任务ID（由谁完成）
```

### 当前状态
```
pending_tasks:    无
active_task:      无
last_completed:   无
```

## 任务分配规则

| 任务类型 | 分配给 | 说明 |
|----------|--------|------|
| SSH连集群DFT/MD | 本地WSL | 集群密钥在本地 |
| GitHub/cnb操作 | 本地WSL | 主账号在本地 |
| 网络请求(Google/海外API) | 海外ECS | 国内网络受限 |
| 国内网络请求 | 国内ECS | 国内速度快 |
| 需要GPU的任务 | 国内ECS | 有GPU资源 |

## 工作流程

1. 本地Hermes创建任务 → push到cnb/GitHub
2. 用户通知对应实例："去仓库检查新任务"
3. 对应实例 pull → 执行 → 写结果 → push
4. 用户通知本地Hermes："结果已push"
5. 本地Hermes pull → 读取结果

## 连接信息

### 本地 → 国内ECS
```bash
ssh -i ~/.ssh/hermes_cloud agentuser@119.91.220.249
```

### 本地 → 海外ECS
（待配置）

### 仓库地址
- GitHub: git@github.com:aquarius0109/hermes-cloud-rules.git
- cnb.cool: git@cnb.cool:cello-2026/hermes-cloud-rules.git

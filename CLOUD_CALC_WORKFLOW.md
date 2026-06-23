# 云Hermes计算后更新流程

## 概述

每次在集群上完成计算后，必须执行以下步骤：
1. 更新 data_provenance.md
2. git commit & push
3. 下载关键结果到云盘

## 更新溯源表

### 方法1：手动编辑

```bash
cd ~/hermes-cloud-rules
nano data_provenance.md
# 找到对应论文的表格，更新状态和作业ID
```

### 方法2：使用工具

```bash
cd ~/hermes-cloud-rules/scripts

# 更新状态
python3 provenance_tool.py update 6 D1 ✅ 123456 cluster3 "QE完成"

# 添加新记录
python3 provenance_tool.py add 1 1-3 "TM掺杂DFT" cluster3 ⏳

# 查看汇总
python3 provenance_tool.py summary
```

## Git提交规范

### 提交信息格式

```
update: paper{N} {计算任务} {状态}

- 作业ID: {job_id}
- 集群: {cluster}
- 耗时: {duration}
```

### 示例

```bash
cd ~/hermes-cloud-rules

# 修改data_provenance.md后
git add data_provenance.md
git commit -m "update: paper6 D1 Mg-X结合能 已完成

- 作业ID: 5244163
- 集群: cluster2
- 耗时: 2h30m"

git push
```

## 数据下载到云盘

计算完成后，将关键结果下载到阿里云盘：

```bash
# 从集群下载关键文件
scp cluster3:/work/home/aquarius0109/papers/paper6/DFT/Mg_X_binding/OUTCAR ./

# 上传到云盘
source ~/aligo_env/bin/activate
python3 -c "
from aligo import Aligo
ali = Aligo()
# 找到paper6目录
files = ali.get_file_list()
papers_id = [f.file_id for f in files if f.name == 'papers'][0]
paper6_id = [f.file_id for f in ali.get_file_list(parent_file_id=papers_id) if 'paper6' in f.name][0]

# 上传文件
ali.upload_file(file_path='./OUTCAR', parent_file_id=paper6_id)
print('上传完成')
"
```

## 自动化流程

### HPC作业提交脚本模板

在提交脚本中添加完成后的回调：

```bash
#!/bin/bash
# submit_and_record.sh

# 1. 提交作业
JOB_ID=$(sbatch job.sh | awk '{print $NF}')
echo "作业已提交: $JOB_ID"

# 2. 等待完成并记录
while true; do
    STATUS=$(squeue -j $JOB_ID -h -o %T 2>/dev/null)
    if [ -z "$STATUS" ]; then
        echo "作业已完成"
        
        # 3. 更新溯源表
        cd ~/hermes-cloud-rules
        python3 scripts/provenance_tool.py update $PAPER $TASK ✅ $JOB_ID $CLUSTER "完成"
        
        # 4. Git push
        git add data_provenance.md
        git commit -m "update: $PAPER $TASK 已完成 (作业ID: $JOB_ID)"
        git push
        
        break
    fi
    echo "状态: $STATUS"
    sleep 60
done
```

## 注意事项

1. **及时更新**：计算完成后立即更新溯源表
2. **作业ID必填**：方便后期查找原始数据
3. **关键结果下载**：只下载outcar/xyz等关键文件，不下载WAVECAR等大文件
4. **git push**：确保本地和云端同步
5. **云盘备份**：重要结果同时上传阿里云盘

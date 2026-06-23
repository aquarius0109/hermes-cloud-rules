#!/usr/bin/env python3
"""计算数据溯源更新工具"""
import os
import re
from datetime import datetime

PROVENANCE_FILE = os.path.expanduser('~/cloud_disk/calculation_shared/DATA_PROVENANCE.md')

def update_status(paper_num, task_id, status, job_id=None, cluster=None, notes=None):
    """更新计算任务状态"""
    if not os.path.exists(PROVENANCE_FILE):
        print(f"❌ 溯源表不存在: {PROVENANCE_FILE}")
        return False
    
    with open(PROVENANCE_FILE, 'r') as f:
        content = f.read()
    
    # 查找对应的paper表格
    paper_section = f"## Paper {paper_num}"
    if paper_section not in content:
        # 尝试查找paper6（MPC anion regulation）
        if "Paper 6" in content or "MPC anion" in content:
            paper_section = "## Paper 6"
        else:
            print(f"❌ 未找到 Paper {paper_num}")
            return False
    
    # 查找任务行并更新
    lines = content.split('\n')
    updated = False
    
    for i, line in enumerate(lines):
        if task_id in line and '|' in line:
            parts = line.split('|')
            if len(parts) >= 10:
                # 更新状态列 (第7列)
                parts[7] = f' {status} '
                # 更新作业ID (第5列)
                if job_id:
                    parts[5] = f' {job_id} '
                # 更新集群 (第3列)
                if cluster:
                    parts[3] = f' {cluster} '
                # 更新备注 (第10列)
                if notes:
                    parts[10] = f' {notes} '
                
                lines[i] = '|'.join(parts)
                updated = True
                print(f"✅ 已更新: {task_id} -> {status}")
                break
    
    if updated:
        # 添加更新日志
        date_str = datetime.now().strftime('%Y-%m-%d')
        log_line = f"| {date_str} | 更新状态 | {task_id} -> {status} |"
        
        # 找到更新日志部分
        for i, line in enumerate(lines):
            if "## 更新日志" in line:
                # 在表格后插入
                for j in range(i+1, min(i+5, len(lines))):
                    if lines[j].strip().startswith('|---'):
                        lines.insert(j+2, log_line)
                        break
                break
        
        content = '\n'.join(lines)
        with open(PROVENANCE_FILE, 'w') as f:
            f.write(content)
        return True
    else:
        print(f"❌ 未找到任务: {task_id}")
        return False

def add_record(paper_num, task_id, task_name, cluster='本地', status='⏳', notes=''):
    """添加新的计算记录"""
    if not os.path.exists(PROVENANCE_FILE):
        print(f"❌ 溯源表不存在: {PROVENANCE_FILE}")
        return False
    
    with open(PROVENANCE_FILE, 'r') as f:
        content = f.read()
    
    # 查找对应的paper表格
    paper_section = f"## Paper {paper_num}"
    if paper_section not in content:
        print(f"❌ 未找到 Paper {paper_num}")
        return False
    
    # 构建新行
    date_str = datetime.now().strftime('%Y-%m')
    local_path = f"papers/paper{paper_num}_*/calculation/"
    new_row = f"| {task_id} | {task_name} | {cluster} | — | — | {date_str} | {status} | {local_path} | | {notes} |"
    
    # 插入到表格中
    lines = content.split('\n')
    for i, line in enumerate(lines):
        if paper_section in line:
            # 找到表格分隔行
            for j in range(i+1, min(i+10, len(lines))):
                if '---' in lines[j]:
                    lines.insert(j+1, new_row)
                    break
            break
    
    content = '\n'.join(lines)
    with open(PROVENANCE_FILE, 'w') as f:
        f.write(content)
    print(f"✅ 已添加记录: Paper {paper_num} - {task_id}")
    return True

def show_summary():
    """显示数据分布汇总"""
    if not os.path.exists(PROVENANCE_FILE):
        print(f"❌ 溯源表不存在")
        return
    
    with open(PROVENANCE_FILE) as f:
        content = f.read()
    
    # 统计各状态数量
    statuses = re.findall(r'\| (✅|❌|🔄|⏳|📥|☁️) \|', content)
    print("📊 计算状态汇总:")
    print(f"  ✅ 已完成: {statuses.count('✅')}")
    print(f"  ❌ 失败: {statuses.count('❌')}")
    print(f"  🔄 计算中: {statuses.count('🔄')}")
    print(f"  ⏳ 待提交: {statuses.count('⏳')}")
    print(f"  📥 已下载: {statuses.count('📥')}")

if __name__ == '__main__':
    import sys
    
    if len(sys.argv) < 2:
        print("""
用法:
  python provenance_tool.py summary              # 显示汇总
  python provenance_tool.py update PAPER TASK STATUS [JOB_ID] [CLUSTER] [NOTES]
  python provenance_tool.py add PAPER TASK_ID TASK_NAME [CLUSTER] [STATUS] [NOTES]

示例:
  python provenance_tool.py update 6 D1 ✅ 123456 cluster3 "QE完成"
  python provenance_tool.py add 1 1-3 "TM掺杂DFT" cluster3 ⏳ "待提交"
""")
        sys.exit(0)
    
    cmd = sys.argv[1]
    
    if cmd == 'summary':
        show_summary()
    elif cmd == 'update' and len(sys.argv) >= 5:
        paper = sys.argv[2]
        task = sys.argv[3]
        status = sys.argv[4]
        job_id = sys.argv[5] if len(sys.argv) > 5 else None
        cluster = sys.argv[6] if len(sys.argv) > 6 else None
        notes = sys.argv[7] if len(sys.argv) > 7 else None
        update_status(paper, task, status, job_id, cluster, notes)
    elif cmd == 'add' and len(sys.argv) >= 5:
        paper = sys.argv[2]
        task_id = sys.argv[3]
        task_name = sys.argv[4]
        cluster = sys.argv[5] if len(sys.argv) > 5 else '本地'
        status = sys.argv[6] if len(sys.argv) > 6 else '⏳'
        notes = sys.argv[7] if len(sys.argv) > 7 else ''
        add_record(paper, task_id, task_name, cluster, status, notes)
    else:
        print("参数不足")

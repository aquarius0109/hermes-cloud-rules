# 论文正文同步流程

## 概述

论文正文（manuscript）在本地和云端之间同步，确保双方都是最新版本。

## 目录结构

```
papers/paper{N}_{关键词}/
├── manuscript/                    # 稿件目录
│   ├── main.md                    # 主文件
│   ├── main.docx                  # Word版本
│   ├── main.pdf                   # PDF版本
│   ├── supplementary.md           # 补充材料
│   ├── figures/                   # 图片
│   │   ├── fig1_xxx.png
│   │   └── fig2_xxx.pdf
│   └── references.bib             # 参考文献
├── VERSION.md                     # 版本记录
└── CHANGELOG.md                   # 变更日志
```

## 版本记录文件

### VERSION.md

```markdown
# Paper {N} 版本记录

## 当前版本
- 版本号: v1.2
- 最后更新: 2026-06-24
- 更新者: 本地Hermes
- 状态: 修改中

## 版本历史
| 版本 | 日期 | 更新者 | 说明 |
|------|------|--------|------|
| v1.2 | 2026-06-24 | 本地 | 修改Introduction第3段 |
| v1.1 | 2026-06-23 | 云 | 添加计算方法章节 |
| v1.0 | 2026-06-22 | 本地 | 初稿完成 |
```

### CHANGELOG.md

```markdown
# Paper {N} 变更日志

## 2026-06-24 (v1.2)
- 修改Introduction第3段，增加引用
- 更新Figure 3说明
- 修正Table 2数据

## 2026-06-23 (v1.1)
- 添加计算方法章节
- 补充DFT参数设置
```

## 同步流程

### 本地更新后

```bash
cd D:\WSL\science work\papers\paper{N}_{关键词}

# 1. 更新VERSION.md
# 修改版本号、日期、更新者

# 2. 更新CHANGELOG.md
# 添加变更记录

# 3. 上传到云盘
source ~/aligo_env/bin/activate
python3 -c "
from aligo import Aligo
ali = Aligo()
# 找到paper目录
files = ali.get_file_list()
papers_id = [f.file_id for f in files if f.name == 'papers'][0]
paper_id = [f.file_id for f in ali.get_file_list(parent_file_id=papers_id) if 'paper{N}' in f.name][0]
ms_id = [f.file_id for f in ali.get_file_list(parent_file_id=paper_id) if f.name == 'manuscript'][0]

# 上传文件
ali.upload_file(file_path='./manuscript/main.md', parent_file_id=ms_id)
ali.upload_file(file_path='./VERSION.md', parent_file_id=paper_id)
print('上传完成')
"

# 4. Git push（如果在hermes-cloud-rules仓库）
cd ~/hermes-cloud-rules
git add -A
git commit -m "update: paper{N} manuscript v1.2"
git push
```

### 云Hermes更新后

```bash
cd ~/hermes-cloud-rules

# 1. 拉取最新
git pull

# 2. 检查VERSION.md
cat ~/hermes-cloud-rules/papers/paper{N}_*/VERSION.md

# 3. 如果有更新，下载到本地
# 使用aligo下载
```

## 同步规则

### 版本号规则
- 主版本号: 重大修改（结构重组、大量重写）
- 次版本号: 小修改（段落调整、数据更新）
- 修订号: 修正错误（拼写、格式）

### 更新者标识
- `本地` = 本地Hermes (WSL)
- `云` = 云Hermes (ECS)
- `用户` = 用户手动修改

### 冲突处理
1. **同时修改不同部分**: 直接合并
2. **同时修改同一部分**: 后修改方覆盖，但先备份
3. **不确定时**: 标记冲突，等待用户决定

## 自动检查

### 检查云盘是否有更新

```bash
source ~/aligo_env/bin/activate
python3 -c "
from aligo import Aligo
ali = Aligo()

# 查找paper目录
files = ali.get_file_list()
papers_id = [f.file_id for f in files if f.name == 'papers'][0]

for paper in ali.get_file_list(parent_file_id=papers_id):
    if paper.type == 'folder' and paper.name.startswith('paper'):
        # 检查VERSION.md
        items = ali.get_file_list(parent_file_id=paper.file_id)
        for item in items:
            if item.name == 'VERSION.md':
                print(f'{paper.name}: 最后更新 {item.updated_at}')
"
```

## 注意事项

1. **修改前备份**: 重要修改前复制到backup/
2. **及时更新VERSION.md**: 每次修改后立即更新
3. **变更日志详细**: 记录具体修改了什么
4. **图片同步**: 图片修改后也要上传
5. **Word/PDF同步**: md修改后重新生成docx/pdf并上传

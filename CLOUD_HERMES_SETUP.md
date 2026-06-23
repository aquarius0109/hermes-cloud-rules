# 云Hermes操作指南
> 拉取此仓库后执行

## 第一步：拉取协作规则

```bash
cd ~
git clone git@github.com:aquarius0109/hermes-cloud-rules.git
cd hermes-cloud-rules
```

查看规则：
```bash
cat cloud_drive_rules.md     # 目录结构+管理规则
cat data_provenance.md       # 数据溯源表（记录计算在哪个集群）
```

## 第二步：在ECS上安装alist

```bash
# 下载alist
cd /tmp
wget https://github.com/alist-org/alist/releases/latest/download/alist-linux-amd64.tar.gz
tar xzf alist-linux-amd64.tar.gz
sudo mv alist /usr/local/bin/alist
sudo chmod +x /usr/local/bin/alist

# 初始化并启动
mkdir -p ~/alist-data
cd ~/alist-data
alist server &
# 等待启动，查看管理员密码：
cat data/config.json | grep password
# 记下这个密码！

# 开放端口（如需）
sudo firewall-cmd --add-port=5244/tcp --permanent
sudo firewall-cmd --reload
```

## 第三步：配置alist

1. 打开 http://<ECS公网IP>:5244/admin
2. 用 admin + 上面的密码登录
3. 存储 → 添加 → 选择「阿里云盘Open」
4. 挂载路径填：`/`
5. 刷新令牌：去阿里云盘网页版获取（设置→第三方应用管理→创建应用）
6. 保存

## 第四步：创建统一目录结构

在alist管理面板的文件管理中，创建以下目录：

```
/
├── papers/
│   ├── paper1_conductive_K-struvite_DFT/
│   │   ├── manuscript/
│   │   ├── figures/
│   │   ├── data/
│   │   ├── calculation/
│   │   │   ├── DFT/
│   │   │   ├── MD/
│   │   │   └── NEB/
│   │   └── backup/
│   ├── paper2_piezoelectric_K-struvite_d-electron/（同上）
│   ├── paper3_K-struvite_polycrystal_MD/（同上）
│   ├── paper4_MKPC_hydration_MgP_ratio/（同上）
│   ├── paper5_BO_MPC_electrochemical/（同上）
│   └── paper6_MPC_anion_regulation/（同上）
├── literature/
├── calculation_shared/
│   ├── pseudopotentials/
│   ├── scripts/
│   └── results_summary.csv
├── hpc/
│   ├── scripts/
│   ├── inputs/
│   └── logs/
├── tools/
│   ├── python/
│   └── shell/
├── exchange/
│   ├── from_local/
│   └── from_cloud/
└── README.md
```

## 第五步：同步已有文件

把D盘已有的论文数据上传到对应目录：
- paper1~paper5 → papers/paper1~paper5/
- 文献 → literature/
- 赝势文件 → calculation_shared/pseudopotentials/

## 第六步：更新数据溯源表

每次在集群上提交计算作业后，更新 `data_provenance.md`：
```bash
cd ~/hermes-cloud-rules
# 编辑 data_provenance.md，添加计算记录
git add data_provenance.md
git commit -m "update: paperX 添加DFT计算记录"
git push
```

## 管理规则摘要

1. 文件命名：`{论文编号}_{类型}_{版本}.{ext}`
2. 计算目录：`{体系}_{方法}_{参数}_{日期}/`
3. 修改前备份到 backup/
4. 大文件(>100MB)先压缩
5. 每次计算后更新 data_provenance.md

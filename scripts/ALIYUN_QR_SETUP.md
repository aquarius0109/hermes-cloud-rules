# 阿里云盘扫码登录指南

## 适用场景
本地 Hermes（Windows/WSL）需要授权访问阿里云盘时使用。

## 步骤

### 1. 安装 aligo
```bash
pip install aligo
```

### 2. 运行脚本
```bash
cd ~/hermes-cloud-rules
python scripts/aliyun_qr_login.py
```

### 3. 扫码
- 方式A：终端打印ASCII二维码 → 手机阿里云盘App扫码
- 方式B：如终端不支持二维码，用 port=8080 参数：
  ```python
  from aligo import Aligo
  ali = Aligo(port=8080)
  ```
  然后浏览器打开 http://localhost:8080 -> 页面二维码 -> 手机扫

### 4. 完成
扫码后脚本自动获取 token，保存在 `~/.aligo/aligo.json`

### 验证
```python
from aligo import Aligo
ali = Aligo()
files = ali.get_file_list()
print(files)  # 看到根目录文件说明成功
```
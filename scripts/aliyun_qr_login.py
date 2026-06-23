#!/usr/bin/env python3
"""阿里云盘扫码登录 - 生成二维码供手机App扫码授权

用法：
    python3 aliyun_qr_login.py

流程：
    1. 终端打印二维码（或用 port=8080 开Web页面）
    2. 手机阿里云盘App扫码
    3. token自动保存到 ~/.aligo/ 目录
    
依赖：
    pip3 install aligo
"""

from aligo import Aligo


def show_qr(url: str):
    """显示二维码的函数 - aligo会传入二维码链接"""
    print(f"请用浏览器打开以下链接查看二维码：")
    print(f"  {url}")
    print()
    print("或用手机阿里云盘App扫描下方二维码")


# 方式一：终端打印ASCII二维码（默认）
print("=" * 50)
print("方式一：终端打印二维码")
print("=" * 50)
ali = Aligo()

print()
print(f"登录成功！用户: {ali.get_user().nick_name}")
print(f"refresh_token: {ali.token.refresh_token}")
print(f"Token已保存在 ~/.aligo/aligo.json")


# 方式二：启动HTTP服务器，浏览器打开页面扫码
# 去掉下面注释即可使用
"""
print("=" * 50)
print("方式二：启动Web服务器 http://0.0.0.0:8080")
print("=" * 50)
ali2 = Aligo(port=8080)
print(f"登录成功！refresh_token: {ali2.token.refresh_token}")
"""
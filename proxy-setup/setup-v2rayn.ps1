# V2RayN 一键安装脚本
# 用法：右键 → 使用 PowerShell 运行

$ErrorActionPreference = "Stop"

Write-Host "=== 海马代理客户端安装 ===" -ForegroundColor Cyan

# 1. 下载 V2RayN
Write-Host "[1/3] 下载 V2RayN..." -ForegroundColor Yellow
$url = "https://mirror.ghproxy.com/https://github.com/2dust/v2rayN/releases/latest/download/v2rayN-windows-64.zip"
$dest = "$env:TEMP\v2rayN.zip"
try {
    Invoke-WebRequest -Uri $url -OutFile $dest -UseBasicParsing
    Write-Host "  下载完成" -ForegroundColor Green
} catch {
    Write-Host "  下载失败，尝试备用链接..." -ForegroundColor Red
    $url = "https://ghfast.top/https://github.com/2dust/v2rayN/releases/latest/download/v2rayN-windows-64.zip"
    Invoke-WebRequest -Uri $url -OutFile $dest -UseBasicParsing
    Write-Host "  备用链接下载完成" -ForegroundColor Green
}

# 2. 解压
Write-Host "[2/3] 解压安装..." -ForegroundColor Yellow
$extractPath = "$env:USERPROFILE\Desktop\v2rayN"
if (Test-Path $extractPath) { Remove-Item $extractPath -Recurse -Force }
Expand-Archive -Path $dest -DestinationPath $extractPath -Force
Write-Host "  已安装到桌面" -ForegroundColor Green

# 3. 创建快捷方式
Write-Host "[3/3] 创建快捷方式..." -ForegroundColor Yellow
$WshShell = New-Object -ComObject WScript.Shell
$Shortcut = $WshShell.CreateShortcut("$env:USERPROFILE\Desktop\V2RayN.lnk")
$Shortcut.TargetPath = "$extractPath\v2rayN.exe"
$Shortcut.Save()
Write-Host "  快捷方式已创建" -ForegroundColor Green

Write-Host ""
Write-Host "=== 安装完成 ===" -ForegroundColor Cyan
Write-Host "双击桌面 V2RayN 快捷方式启动" -ForegroundColor White
Write-Host "启动后右键托盘图标 → 服务器 → 添加VLESS服务器" -ForegroundColor White
Write-Host ""
Write-Host "节点参数：" -ForegroundColor Yellow
Write-Host "  名称: MPC-Seahorse"
Write-Host "  地址: 49.51.206.92"
Write-Host "  端口: 443"
Write-Host "  UUID: 44568543-0b47-4e3b-ba3d-40d6dc171cdc"
Write-Host "  加密: none"
Write-Host "  传输: tcp"
Write-Host "  Flow: xtls-rprx-vision"
Write-Host "  安全: reality"
Write-Host "  SNI: www.microsoft.com"
Write-Host "  公钥: DIrobGCcrXVrKwll6CBa9p8W8cFJnouCDPa29tFO50I"
Write-Host "  Short ID: 342b072afa78dead"
Write-Host "  指纹: chrome"

# 自动启动
Start-Process "$extractPath\v2rayN.exe"
Write-Host ""
Write-Host "V2RayN 已启动，请手动添加节点" -ForegroundColor Green

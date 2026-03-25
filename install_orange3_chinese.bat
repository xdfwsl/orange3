@echo off
chcp 65001 >nul
title Orange3 中文版 一键安装程序
color 0A

echo.
echo  ============================================
echo    Orange3 中文版 一键安装程序
echo    河北科技工程职业技术大学 李洪燕
echo  ============================================
echo.

:: 检查 Python
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo  [错误] 未检测到 Python，请先安装 Python 3.9 或更高版本。
    echo  下载地址: https://www.python.org/downloads/
    echo.
    pause
    exit /b 1
)

for /f "tokens=2" %%i in ('python --version 2^>^&1') do set PYVER=%%i
echo  [信息] 检测到 Python %PYVER%
echo.

:: 安装 PyQt5
echo  [1/4] 安装 PyQt5 ...
pip install PyQt5 PyQtWebEngine -q
if %errorlevel% neq 0 (
    echo  [警告] PyQt5 安装失败，尝试安装 PyQt6 ...
    pip install PyQt6 PyQt6-WebEngine -q
)
echo  [1/4] 完成
echo.

:: 安装 Orange3 中文版
echo  [2/4] 安装 Orange3 中文版 （可能需要几分钟）...
pip install git+https://github.com/xdfwsl/orange3.git -q
if %errorlevel% neq 0 (
    echo  [错误] Orange3 安装失败，请检查网络连接。
    pause
    exit /b 1
)
echo  [2/4] 完成
echo.

:: 部署中文翻译
echo  [3/4] 部署中文翻译 ...
python -m Orange.i18n.setup_chinese
echo  [3/4] 完成
echo.

:: 创建桌面快捷方式
echo  [4/4] 创建桌面快捷方式 ...
python -c "
import os, sys
desktop = os.path.join(os.path.expanduser('~'), 'Desktop')
shortcut = os.path.join(desktop, 'Orange3 中文版.bat')
python_path = sys.executable
with open(shortcut, 'w', encoding='utf-8') as f:
    f.write('@echo off\n')
    f.write(f'start \"\" \"{python_path}\" -m Orange.canvas\n')
print(f'  快捷方式已创建: {shortcut}')
"
echo  [4/4] 完成
echo.

echo  ============================================
echo    安装完成！
echo.
echo    启动方式:
echo      1. 双击桌面上的 "Orange3 中文版" 快捷方式
echo      2. 或在命令行运行: python -m Orange.canvas
echo  ============================================
echo.
pause

@echo off

REM 设置所需的 Python 版本
set PYTHON_VERSION=3.11

REM 检查当前 Python 版本
python --version 2>nul | findstr /C:"Python %PYTHON_VERSION%" >nul
if %errorlevel% equ 0 (
    REM 当前 Python 版本为 3.11
    echo Current Python version is %PYTHON_VERSION%
) else (
    REM 当前 Python 版本不是 3.11，创建虚拟环境
    echo Current Python version is not %PYTHON_VERSION%, creating virtual environment

    REM 创建虚拟环境
    python -m venv myenv

    REM 激活虚拟环境
    call myenv\Scripts\activate
)

REM 安装依赖项
pip install jieba
pip install wordcloud
pip install matplotlib
pip install pillow
pip install mistune

REM 其他操作...

REM 退出虚拟环境
deactivate

@echo off

REM 检查pip是否已安装
pip --version

REM 使用pip下载依赖
pip install jieba
pip install wordcloud
pip install matplotlib
pip install pillow
pip install mistune

REM 执行其他操作...

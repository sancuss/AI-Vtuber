@echo off
cd /d "%~dp0"
call conda activate vtube_env
python Main.py
cmd
rem pause

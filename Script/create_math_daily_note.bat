@echo off
chcp 65001 >nul
REM This batch script runs the Python script to create a daily Math note
cd /d "%~dp0"
python "%~dp0create_math_daily_note.py"

@echo off
chcp 65001 >nul
REM This batch script runs the Python script to create a daily English note
cd /d "%~dp0"
python "%~dp0create_english_daily_note.py"

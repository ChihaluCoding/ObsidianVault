@echo off
chcp 65001 >nul
REM This batch script runs the Python script to create a daily HTML/CSS note
cd /d "%~dp0"
python "%~dp0create_html_css_daily_note.py"

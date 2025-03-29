@echo off
setlocal enabledelayedexpansion

:: Read project path from config.json
for /f "tokens=* delims=" %%a in ('type config.json ^| findstr "project_path"') do (
    set "line=%%a"
    set "line=!line:~21,-2!"
    set "PROJECT_PATH=!line!"
)

:: Convert forward slashes to backslashes for Windows
set "PROJECT_PATH=!PROJECT_PATH:/=\!"

:: Create aliases
doskey bob=echo Holla, sou bob!
doskey sublime="%PROJECT_PATH%" $1
doskey kill-python=taskkill /F /IM python.exe
doskey all-python=tasklist ^| findstr python
doskey cd-project=cd /d "%PROJECT_PATH%"

:: Clear screen and navigate to project directory
cls
cd /d "%PROJECT_PATH%"

:: Start command prompt
cmd /K

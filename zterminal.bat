@echo off
setlocal enabledelayedexpansion

:: Get the directory where this script is located
set "SCRIPT_DIR=%~dp0"

:: Read project path from config.json
for /f "tokens=* delims=" %%a in ('type "%SCRIPT_DIR%config.json" ^| findstr "project_path"') do (
    set "line=%%a"
    set "line=!line:~21,-2!"
    set "PROJECT_PATH=!line!"
)

:: Convert relative path to absolute path
if "%PROJECT_PATH%"=="." (
    set "PROJECT_PATH=%SCRIPT_DIR%"
) else (
    set "PROJECT_PATH=%SCRIPT_DIR%%PROJECT_PATH%"
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

@echo off
REM Selenium Test Runner for Windows VM
REM This script runs Selenium tests on an isolated Windows VM

setlocal EnableDelayedExpansion

echo ======================================
echo   Selenium Test Runner for VM
echo ======================================
echo.

REM Set variables
set "PROJECT_DIR=%~dp0"
set "HEADLESS_MODE=true"
set "VERBOSE_MODE=false"

REM Parse arguments
:parse_args
if "%~1"=="" goto :done_parsing
if /I "%~1"=="--headed" (
    set "HEADLESS_MODE=false"
    shift
    goto :parse_args
)
if /I "%~1"=="--verbose" (
    set "VERBOSE_MODE=true"
    shift
    goto :parse_args
)
if /I "%~1"=="-v" (
    set "VERBOSE_MODE=true"
    shift
    goto :parse_args
)
if /I "%~1"=="--help" (
    goto :show_help
)
shift
goto :parse_args
:done_parsing

REM Check Python
echo [CHECK] Checking Python installation...
python --version >nul 2>&1
if %ERRORLEVEL% NEQ 0 (
    echo [ERROR] Python not found. Please install Python 3.x
    exit /b 1
)
python --version

REM Check Chrome
echo [CHECK] Checking Chrome installation...
reg query "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\App Paths\chrome.exe" >nul 2>&1
if %ERRORLEVEL% NEQ 0 (
    echo [WARNING] Chrome may not be installed. Attempting to continue...
) else (
    echo [OK] Chrome found
)

REM Install dependencies
echo.
echo [SETUP] Installing Python dependencies...
pip install --quiet --upgrade pip
pip install --quiet -r "%PROJECT_DIR%requirements.txt"
if %ERRORLEVEL% NEQ 0 (
    echo [ERROR] Failed to install dependencies
    exit /b 1
)
echo [OK] Dependencies installed

REM Create screenshots directory
if not exist "%PROJECT_DIR%screenshots" mkdir "%PROJECT_DIR%screenshots"

REM Set environment variables
set HEADLESS=%HEADLESS_MODE%
set PYTHONUNBUFFERED=1

REM Run tests
echo.
echo ======================================
echo [RUN] Starting tests...
echo Mode: %HEADLESS_MODE%
echo ======================================
echo.

if exist "%PROJECT_DIR%run_single_session.py" (
    set "CMD=python "%PROJECT_DIR%run_single_session.py""
    if "%HEADLESS_MODE%"=="true" (
        set "CMD=!CMD! --headless"
    )
    if "%VERBOSE_MODE%"=="true" (
        set "CMD=!CMD! --verbose"
    )
    echo Running: run_single_session.py
) else (
    set "CMD=python -m pytest -v"
    echo Running: pytest
)

!CMD!
set EXIT_CODE=%ERRORLEVEL%

echo.
echo ======================================
echo   Test Run Complete
echo ======================================

if %EXIT_CODE% EQU 0 (
    echo [SUCCESS] All tests passed!
) else (
    echo [WARNING] Some tests failed ^(exit code: %EXIT_CODE%^)
)

exit /b %EXIT_CODE%

:show_help
echo Usage: %~nx0 [OPTIONS]
echo.
echo OPTIONS:
echo   --headed     Run in headed mode ^(browser visible^)
echo   --verbose    Enable verbose output
echo   -v           Enable verbose output ^(short^)
echo   --help       Show this help message
echo.
echo EXAMPLES:
echo   %~nx0          Run tests in headless mode ^(default^)
echo   %~nx0 --headed Run tests with visible browser
echo   %~nx0 --verbose Run with detailed logging
echo.
exit /b 0

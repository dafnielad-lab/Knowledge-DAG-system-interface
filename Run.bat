@echo off
setlocal enabledelayedexpansion
title Knowledge DAG

cd /d "%~dp0"
set "PORT=8000"

echo.
echo ============================================
echo    Knowledge DAG
echo ============================================
echo.

echo Checking for a previous instance on port %PORT%...
set "FOUND=0"
for /f "tokens=5" %%a in ('netstat -ano ^| findstr "LISTENING" ^| findstr ":%PORT% "') do (
    echo   Stopping previous instance PID %%a ...
    taskkill /F /PID %%a /T >nul 2>&1
    set "FOUND=1"
)
if "!FOUND!"=="1" (
    timeout /t 2 /nobreak >nul
) else (
    echo   No previous instance found.
)

echo.
echo Starting Knowledge DAG on http://localhost:%PORT%
echo Press Ctrl+C to stop.
echo.

:: Schedule the browser to open a few seconds AFTER uvicorn starts (so it has
:: time to bind the port). PowerShell handles the delay+launch in the
:: background with no visible window; the batch keeps running.
start "" /b powershell -NoProfile -WindowStyle Hidden -Command "Start-Sleep -Seconds 3; Start-Process 'http://localhost:%PORT%/'"

python -m uvicorn app:app --host 127.0.0.1 --port %PORT%

pause
endlocal

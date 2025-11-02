@echo off
title VOTER INSTANCE #2
color 0B
cd /d "%~dp0"

echo ========================================
echo VOTER #2 - ASHUTOSH PRATAP SINGH
echo ========================================
echo.
echo Running in loop...
echo Press Ctrl+C to stop
echo ========================================
echo.
timeout /t 3 /nobreak >nul

set /a count=0

:loop
set /a count+=1
echo.
echo [Voter #2] Vote #%count%
python real_voter.py
timeout /t 2 /nobreak >nul
goto loop

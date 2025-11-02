@echo off
title CONTINUOUS VOTER - Loop Mode
color 0A
cd /d "%~dp0"

echo ========================================
echo CONTINUOUS VOTER FOR ASHUTOSH PRATAP SINGH
echo ========================================
echo.
echo This will run real_voter.py in a loop
echo Each vote opens a browser window
echo.
echo Press Ctrl+C anytime to stop
echo ========================================
echo.
pause

set /a count=0

:loop
set /a count+=1
echo.
echo ========================================
echo VOTE #%count%
echo ========================================
python real_voter.py

timeout /t 2 /nobreak >nul
goto loop

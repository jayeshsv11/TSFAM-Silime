@echo off
title OPTIMIZED FRESH VOTER - 5 TERMINALS
color 0A

echo ================================================================
echo OPTIMIZED FRESH BROWSER VOTER
echo ================================================================
echo.
echo This version:
echo   - Waits for success response (accurate)
echo   - Closes browser immediately after
echo   - Opens new browser immediately
echo   - NO extra delays
echo.
echo Fast AND accurate!
echo.
echo ================================================================
pause

echo.
echo Starting 5 OPTIMIZED voting terminals...
echo.

start "Optimized Voter 1" cmd /k "cd /d "%~dp0" && python optimized_fresh_voter.py 1"
timeout /t 2 /nobreak >nul

start "Optimized Voter 2" cmd /k "cd /d "%~dp0" && python optimized_fresh_voter.py 2"
timeout /t 2 /nobreak >nul

start "Optimized Voter 3" cmd /k "cd /d "%~dp0" && python optimized_fresh_voter.py 3"
timeout /t 2 /nobreak >nul

start "Optimized Voter 4" cmd /k "cd /d "%~dp0" && python optimized_fresh_voter.py 4"
timeout /t 2 /nobreak >nul

start "Optimized Voter 5" cmd /k "cd /d "%~dp0" && python optimized_fresh_voter.py 5"

echo.
echo ================================================================
echo 5 OPTIMIZED voters started!
echo.
echo Browsers will open/close continuously
echo No wasted time - immediate restart after each vote
echo.
echo ================================================================
pause

@echo off
cd /d "%~dp0"
title LAUNCH ALL 5 VOTERS - MAXIMIZED
color 0F
cls

echo ========================================
echo LAUNCHING 5 SIMULTANEOUS VOTERS
echo ========================================
echo.
echo This will run 5 voters in parallel
echo Each voting for Ashutosh Pratap Singh
echo.
echo SPEED: ~50-60 votes per minute
echo (5 instances x 10-12 votes/min each)
echo.
echo WARNING: Uses more CPU/RAM
echo Press Ctrl+C in each window to stop
echo ========================================
echo.
echo Press any key to launch all 5...
pause >nul

cls
echo.
echo Launching voters...
echo.

start "" loop_voter.bat
echo [1/5] Launched Voter 1
timeout /t 3 /nobreak >nul

start "" loop_voter_2.bat
echo [2/5] Launched Voter 2
timeout /t 3 /nobreak >nul

start "" loop_voter_3.bat
echo [3/5] Launched Voter 3
timeout /t 3 /nobreak >nul

start "" loop_voter_4.bat
echo [4/5] Launched Voter 4
timeout /t 3 /nobreak >nul

start "" loop_voter_5.bat
echo [5/5] Launched Voter 5

echo.
echo ========================================
echo ALL 5 VOTERS LAUNCHED!
echo ========================================
echo.
echo Check the 5 windows - each voting continuously
echo Combined speed: 50-60 votes/minute
echo.
echo To stop: Press Ctrl+C in each window
echo.
pause


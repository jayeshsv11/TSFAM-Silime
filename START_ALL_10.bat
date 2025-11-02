@echo off
cd /d "%~dp0"
title LAUNCH ALL 10 VOTERS - MAXIMUM POWER
color 0F
cls

echo ========================================
echo LAUNCHING 10 SIMULTANEOUS VOTERS
echo ========================================
echo.
echo This will run 10 voters in parallel
echo Voting for: ASHUTOSH PRATAP SINGH
echo.
echo SPEED: ~100-120 votes per minute
echo (10 instances x 10-12 votes/min each)
echo.
echo WARNING: High CPU/RAM usage!
echo Only use if your PC can handle it
echo ========================================
echo.
echo Press any key to launch all 10...
pause >nul

cls
echo.
echo Launching all 10 voters...
echo.

start "" loop_voter.bat
echo [1/10] Launched Voter 1
timeout /t 2 /nobreak >nul

start "" loop_voter_2.bat
echo [2/10] Launched Voter 2
timeout /t 2 /nobreak >nul

start "" loop_voter_3.bat
echo [3/10] Launched Voter 3
timeout /t 2 /nobreak >nul

start "" loop_voter_4.bat
echo [4/10] Launched Voter 4
timeout /t 2 /nobreak >nul

start "" loop_voter_5.bat
echo [5/10] Launched Voter 5
timeout /t 2 /nobreak >nul

start "" loop_voter_6.bat
echo [6/10] Launched Voter 6
timeout /t 2 /nobreak >nul

start "" loop_voter_7.bat
echo [7/10] Launched Voter 7
timeout /t 2 /nobreak >nul

start "" loop_voter_8.bat
echo [8/10] Launched Voter 8
timeout /t 2 /nobreak >nul

start "" loop_voter_9.bat
echo [9/10] Launched Voter 9
timeout /t 2 /nobreak >nul

start "" loop_voter_10.bat
echo [10/10] Launched Voter 10

echo.
echo ========================================
echo ALL 10 VOTERS LAUNCHED!
echo ========================================
echo.
echo 10 windows are now voting continuously
echo Combined speed: ~100-120 votes/minute
echo That's ~6,000-7,200 votes per hour!
echo.
echo To stop: Press Ctrl+C in each window
echo Or just close all the voter windows
echo ========================================
echo.
pause

@echo off
title LAUNCH ALL 5 VOTERS
color 0F

echo ========================================
echo LAUNCHING 5 CONTINUOUS VOTERS
echo ========================================
echo.
echo This will open 5 terminal windows
echo Each will vote continuously
echo.
echo Total speed: ~5 votes every 3 seconds
echo.
echo To STOP: Press Ctrl+C in each window
echo ========================================
echo.
pause

start run_terminal_1.bat
timeout /t 1 /nobreak >nul

start run_terminal_2.bat
timeout /t 1 /nobreak >nul

start run_terminal_3.bat
timeout /t 1 /nobreak >nul

start run_terminal_4.bat
timeout /t 1 /nobreak >nul

start run_terminal_5.bat

echo.
echo ========================================
echo ALL 5 VOTERS LAUNCHED!
echo ========================================
echo.
echo Check the 5 new windows that opened
echo Each is voting continuously
echo.
echo To stop all: Close each window or press Ctrl+C
echo.
pause

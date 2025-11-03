@echo off
title FAST FRESH VOTER - 5 TERMINALS
color 0A

echo ================================================================
echo FAST FRESH BROWSER VOTER - OPTIMIZED SPEED
echo ================================================================
echo.
echo Optimizations:
echo   - Minimal delays (2-5 sec between votes)
echo   - Fast page loading
echo   - Browser closes and reopens each vote
echo.
echo Target: 5-8 votes/min per browser
echo Total with 5 browsers: 25-40 votes/min
echo.
echo ================================================================
pause

start "Fast Voter 1" cmd /k "cd /d "%~dp0" && python fast_fresh_voter.py 1"
timeout /t 2 /nobreak >nul

start "Fast Voter 2" cmd /k "cd /d "%~dp0" && python fast_fresh_voter.py 2"
timeout /t 2 /nobreak >nul

start "Fast Voter 3" cmd /k "cd /d "%~dp0" && python fast_fresh_voter.py 3"
timeout /t 2 /nobreak >nul

start "Fast Voter 4" cmd /k "cd /d "%~dp0" && python fast_fresh_voter.py 4"
timeout /t 2 /nobreak >nul

start "Fast Voter 5" cmd /k "cd /d "%~dp0" && python fast_fresh_voter.py 5"

echo.
echo ================================================================
echo 5 FAST voters started!
echo Target: 25-40 votes per minute
echo ================================================================
pause

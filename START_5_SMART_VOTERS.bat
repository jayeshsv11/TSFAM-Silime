@echo off
title SMART CHROME VOTER - 5 TERMINALS
color 0A

echo ================================================================
echo SMART CHROME VOTER - ANTI-DETECTION
echo ================================================================
echo.
echo This version uses HUMAN-LIKE behavior:
echo   - Random delays (looks natural)
echo   - Regular clicks (not JavaScript)
echo   - Anti-bot detection measures
echo   - Auto-waits when blocked
echo.
echo SLOWER but SAFER: ~4-6 votes per minute per browser
echo Total: ~20-30 votes/minute with 5 browsers
echo.
echo ================================================================
pause

echo.
echo Starting 5 SMART voting terminals...
echo.

start "Smart Voter 1" cmd /k "cd /d "%~dp0" && python smart_chrome_voter.py 1"
timeout /t 3 /nobreak >nul

start "Smart Voter 2" cmd /k "cd /d "%~dp0" && python smart_chrome_voter.py 2"
timeout /t 3 /nobreak >nul

start "Smart Voter 3" cmd /k "cd /d "%~dp0" && python smart_chrome_voter.py 3"
timeout /t 3 /nobreak >nul

start "Smart Voter 4" cmd /k "cd /d "%~dp0" && python smart_chrome_voter.py 4"
timeout /t 3 /nobreak >nul

start "Smart Voter 5" cmd /k "cd /d "%~dp0" && python smart_chrome_voter.py 5"

echo.
echo ================================================================
echo 5 SMART voters started!
echo.
echo Each browser acts like a HUMAN to avoid detection
echo Slower speed but less likely to be blocked
echo.
echo ================================================================
pause

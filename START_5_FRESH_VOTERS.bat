@echo off
title FRESH BROWSER VOTER - 5 TERMINALS
color 0A

echo ================================================================
echo FRESH BROWSER VOTER - CLOSES AND REOPENS
echo ================================================================
echo.
echo This version CLOSES the browser after each vote!
echo.
echo How it works:
echo   1. Opens Chrome
echo   2. Votes
echo   3. CLOSES Chrome completely
echo   4. Waits 5-10 seconds
echo   5. Opens NEW Chrome
echo   6. Repeat
echo.
echo This avoids detection - fresh session every time!
echo.
echo Speed: ~3-5 votes per minute per browser
echo Total: ~15-25 votes/minute with 5 browsers
echo.
echo ================================================================
pause

echo.
echo Starting 5 FRESH BROWSER voters...
echo.

start "Fresh Voter 1" cmd /k "cd /d "%~dp0" && python fresh_browser_voter.py 1"
timeout /t 3 /nobreak >nul

start "Fresh Voter 2" cmd /k "cd /d "%~dp0" && python fresh_browser_voter.py 2"
timeout /t 3 /nobreak >nul

start "Fresh Voter 3" cmd /k "cd /d "%~dp0" && python fresh_browser_voter.py 3"
timeout /t 3 /nobreak >nul

start "Fresh Voter 4" cmd /k "cd /d "%~dp0" && python fresh_browser_voter.py 4"
timeout /t 3 /nobreak >nul

start "Fresh Voter 5" cmd /k "cd /d "%~dp0" && python fresh_browser_voter.py 5"

echo.
echo ================================================================
echo 5 FRESH BROWSER voters started!
echo.
echo Watch for browsers opening and closing automatically
echo Each vote = Fresh session (no detection)
echo.
echo ================================================================
pause

@echo off
title INFINITE VOTER - 5 TERMINALS
color 0A

echo ================================================================
echo INFINITE VOTER - 5 PARALLEL TERMINALS
echo ================================================================
echo.
echo This will open 5 separate windows
echo Each window votes INFINITELY until you close it
echo Using Microsoft Edge (faster than Chrome)
echo.
echo To stop: Close individual windows or this main window
echo.
echo ================================================================
pause

echo.
echo Starting 5 voting terminals...
echo.

start "Voter 1" cmd /k "cd /d "%~dp0" && python infinite_edge_voter.py 1"
timeout /t 2 /nobreak >nul

start "Voter 2" cmd /k "cd /d "%~dp0" && python infinite_edge_voter.py 2"
timeout /t 2 /nobreak >nul

start "Voter 3" cmd /k "cd /d "%~dp0" && python infinite_edge_voter.py 3"
timeout /t 2 /nobreak >nul

start "Voter 4" cmd /k "cd /d "%~dp0" && python infinite_edge_voter.py 4"
timeout /t 2 /nobreak >nul

start "Voter 5" cmd /k "cd /d "%~dp0" && python infinite_edge_voter.py 5"

echo.
echo ================================================================
echo 5 voting terminals started!
echo.
echo Each terminal is voting continuously
echo You will see 5 Edge browsers working
echo.
echo To stop:
echo - Close individual terminal windows
echo - Or close the browser windows
echo - Or close this window to stop all
echo.
echo ================================================================
pause

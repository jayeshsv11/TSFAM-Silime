@echo off
title Running All 100 Voter Instances (Minimized)
echo Starting all 100 voter instances in minimized windows...
echo This reduces screen clutter and CPU usage
echo.

for /L %%i in (1,1,100) do (
    start "Voter %%i" /min cmd /c loop_voter_%%i.bat
    timeout /t 0 /nobreak >nul
)

echo.
echo ======================================
echo All 100 voter instances started!
echo Check taskbar for minimized windows
echo ======================================
pause

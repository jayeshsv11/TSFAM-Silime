@echo off
title Running All 100 Voter Instances
echo Starting all 100 voter instances...
echo.

for /L %%i in (1,1,100) do (
    start "Voter %%i" cmd /c loop_voter_%%i.bat
    echo Started Voter Instance %%i
)

echo.
echo ======================================
echo All 100 voter instances started!
echo ======================================
pause

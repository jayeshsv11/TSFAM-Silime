@echo off
title Incremental Voter Test
color 0A

:menu
cls
echo ========================================
echo    INCREMENTAL VOTER TESTING
echo ========================================
echo.
echo Select how many instances to run:
echo.
echo   1. Test with 10 instances
echo   2. Test with 20 instances
echo   3. Test with 30 instances
echo   4. Exit
echo.
echo ========================================
set /p choice="Enter your choice (1-4): "

if "%choice%"=="1" goto run10
if "%choice%"=="2" goto run20
if "%choice%"=="3" goto run30
if "%choice%"=="4" goto end
echo Invalid choice!
timeout /t 2 >nul
goto menu

:run10
cls
echo Starting 10 voter instances...
echo.
for /L %%i in (1,1,10) do (
    start "Voter %%i" /min cmd /c loop_voter_%%i.bat
    echo Started Voter Instance %%i/10
    timeout /t 0 /nobreak >nul
)
echo.
echo ======================================
echo 10 instances started!
echo Check Task Manager to monitor CPU/RAM
echo ======================================
echo.
pause
goto menu

:run20
cls
echo Starting 20 voter instances...
echo.
for /L %%i in (1,1,20) do (
    start "Voter %%i" /min cmd /c loop_voter_%%i.bat
    echo Started Voter Instance %%i/20
    timeout /t 0 /nobreak >nul
)
echo.
echo ======================================
echo 20 instances started!
echo Check Task Manager to monitor CPU/RAM
echo ======================================
echo.
pause
goto menu

:run30
cls
echo Starting 30 voter instances...
echo.
for /L %%i in (1,1,30) do (
    start "Voter %%i" /min cmd /c loop_voter_%%i.bat
    echo Started Voter Instance %%i/30
    timeout /t 0 /nobreak >nul
)
echo.
echo ======================================
echo 30 instances started!
echo Check Task Manager to monitor CPU/RAM
echo ======================================
echo.
pause
goto menu

:end
echo Exiting...
exit

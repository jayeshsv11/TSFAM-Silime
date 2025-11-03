@echo off
title SIMPLE TEST - 5 Parallel Browsers
color 0A

echo ================================================================
echo SIMPLE PARALLEL VOTER TEST
echo ================================================================
echo.
echo This will open 5 Chrome browsers at the same time
echo You will SEE them working!
echo.
echo Expected result:
echo   - 1 vote SUCCESS (first one)
echo   - 4 votes FAIL (same IP, already voted)
echo.
echo This proves the script WORKS!
echo To get more votes, you need different IPs (airplane mode)
echo.
echo ================================================================
echo.
pause

python simple_parallel_test.py

pause

@echo off
title QUICK TEST - Single Vote
color 0A

echo ================================================================
echo QUICK TEST - Voting System
echo ================================================================
echo.
echo This will test if everything works with a SINGLE vote
echo Time: About 5-10 seconds
echo.
echo ================================================================
pause

echo.
echo Running test...
echo.

python fast_selenium_voter.py

echo.
echo ================================================================
echo Test complete!
echo.
echo If you saw "[1/1] Success" above, everything works!
echo.
echo NEXT STEP:
echo Run: EMERGENCY_START.bat for high-speed voting
echo ================================================================
echo.
pause

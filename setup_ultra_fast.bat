@echo off
echo ====================================
echo Installing Ultra Fast Voter
echo ====================================
echo.

echo Installing required packages...
pip install aiohttp asyncio

echo.
echo ====================================
echo Installation Complete!
echo ====================================
echo.
echo NEXT STEPS:
echo 1. Run auto_vote.py to get form field names
echo 2. Update form_data in ultra_fast_vote.py
echo 3. Run: python ultra_fast_vote.py
echo.
pause

@echo off
echo ====================================================
echo Blizzard Auto Voter - Installation
echo ====================================================
echo.

echo Installing required Python packages...
pip install requests beautifulsoup4 selenium

echo.
echo ====================================================
echo Installation complete!
echo ====================================================
echo.
echo Next steps:
echo 1. For basic voting (clears cookies only):
echo    python auto_vote.py
echo.
echo 2. For advanced browser automation:
echo    Download ChromeDriver from: https://chromedriver.chromium.org/
echo    Place chromedriver.exe in this folder or in PATH
echo    Then run: python auto_vote_selenium.py
echo.
pause

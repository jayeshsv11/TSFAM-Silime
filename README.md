# Blizzard Auto Voter - Configuration & Instructions

## What the website tracks:
1. **Cookies** - Stored in browser
2. **LocalStorage/SessionStorage** - Browser storage
3. **IP Address** - Your network identifier
4. **Browser Fingerprint** - Device/browser combination

## How to bypass vote restrictions:

### Method 1: Clear Browser Data (Manual)
1. Open browser DevTools (F12)
2. Go to Application/Storage tab
3. Clear:
   - Cookies
   - Local Storage
   - Session Storage
4. Run the Python script

### Method 2: Use Incognito/Private Mode
- Each new incognito window = fresh session
- Cookies/storage cleared automatically

### Method 3: Use Different Browsers
- Chrome
- Firefox
- Edge
- Opera
- Each browser has separate storage

### Method 4: Change IP Address
- Use VPN
- Use proxy
- Switch networks (WiFi/Mobile data)
- Restart router (may get new IP)

### Method 5: Automated with Selenium (Advanced)
Run the advanced script: `auto_vote_selenium.py`

## Installation:

```bash
pip install requests beautifulsoup4 selenium
```

For Selenium automation, also download ChromeDriver:
https://chromedriver.chromium.org/

## Usage:

### Basic script (clears cookies only):
```bash
python auto_vote.py
```

### Advanced script with browser automation:
```bash
python auto_vote_selenium.py
```

### Multiple votes (requires IP change between runs):
```bash
python auto_vote_selenium.py --votes 5
```

## Legal & Ethical Note:
Vote manipulation may violate the website's terms of service.
Use responsibly and only if you have permission.

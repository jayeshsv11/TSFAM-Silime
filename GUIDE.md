# 🗳️ COMPLETE GUIDE: Auto-Voting for Ashutosh Pratap Singh

## 📋 Table of Contents
1. [Quick Start](#quick-start)
2. [What the Website Stores](#what-the-website-stores)
3. [Methods to Vote Multiple Times](#methods-to-vote-multiple-times)
4. [Tools Provided](#tools-provided)
5. [Legal & Ethical Notice](#legal--ethical-notice)

---

## 🚀 Quick Start

### Method 1: Use the HTML Tool (EASIEST)
1. Open `vote_helper.html` in your browser
2. Click "Clear Data & Open Vote Page"
3. Vote for Ashutosh Pratap Singh
4. To vote again: Change IP → Repeat

### Method 2: Use Python Script (Basic)
```bash
cd Documents\voting_script
python auto_vote.py
```

### Method 3: Use Selenium Automation (Advanced)
```bash
# First install requirements
pip install selenium requests beautifulsoup4

# Download ChromeDriver and add to PATH

# Then run
python auto_vote_selenium.py
```

---

## 🔍 What the Website Stores

The website (https://blizzardproductionhouse.com/tech/) tracks votes using:

### 1. **Browser Cookies** ✓ Can Clear
- Stored by the Forminator WordPress plugin
- Tracks if you've already voted
- **Solution:** Clear cookies between votes

### 2. **Local Storage** ✓ Can Clear
- JavaScript localStorage
- May contain vote tracking data
- **Solution:** Clear via browser or script

### 3. **Session Storage** ✓ Can Clear
- Temporary browser storage
- Cleared when browser closes
- **Solution:** Use incognito mode or clear manually

### 4. **IP Address** ❌ Cannot Clear from Browser
- Server-side tracking
- Most important restriction
- **Solution:** Must change IP address (VPN, mobile data, etc.)

### 5. **Browser Fingerprint** ⚠️ Difficult to Clear
- May track device/browser combination
- **Solution:** Use different browsers

---

## 🎯 Methods to Vote Multiple Times

### Option A: Manual Method (Simplest)
1. Open `vote_helper.html`
2. Click "Clear Data & Open Vote Page"
3. Vote for Ashutosh Pratap Singh
4. **Change your IP address:**
   - Turn on VPN and switch servers
   - Switch from WiFi to mobile data
   - Restart your router (may get new IP)
5. Repeat from step 1

### Option B: Different Browsers
Use these browsers (each has separate cookies):
1. Google Chrome
2. Mozilla Firefox  
3. Microsoft Edge
4. Opera
5. Brave
6. Safari (Mac)

**Steps:**
- Vote once in each browser
- Clear data in each browser before voting
- Can vote 5-6 times with different browsers

### Option C: Incognito/Private Mode
1. Open incognito window (Ctrl+Shift+N in Chrome)
2. Go to voting page
3. Vote
4. Close window
5. Change IP if needed
6. Open new incognito window
7. Repeat

### Option D: VPN Method (Most Effective)
1. Install VPN (ProtonVPN, NordVPN, etc.)
2. Clear vote data (use HTML tool)
3. Connect to VPN server (e.g., USA)
4. Vote
5. Disconnect VPN
6. Clear data again
7. Connect to different server (e.g., UK)
8. Vote again
9. Repeat with different servers

### Option E: Mobile Devices
- Use smartphone/tablet
- Use mobile data (different IP from home WiFi)
- Can vote separately from computer
- Ask friends/family to vote on their devices

### Option F: Automated Script (Advanced)
```bash
# Vote multiple times (requires manual IP changes)
python auto_vote_selenium.py --votes 5
```
Script will pause between votes for you to change IP.

---

## 🛠️ Tools Provided

### 1. **vote_helper.html**
- **What it does:** Browser-based tool to clear voting data
- **How to use:** Double-click to open in browser
- **Best for:** Quick, easy voting without coding

### 2. **auto_vote.py**
- **What it does:** Python script that clears cookies and attempts to vote
- **How to use:** `python auto_vote.py`
- **Best for:** Understanding how the voting works

### 3. **auto_vote_selenium.py**
- **What it does:** Fully automated browser control
- **How to use:** `python auto_vote_selenium.py`
- **Best for:** Advanced users who want automation
- **Requires:** ChromeDriver installed

### 4. **install.bat**
- **What it does:** Installs required Python packages
- **How to use:** Double-click to run

### 5. **run_vote.bat**
- **What it does:** Quick launcher for selenium script
- **How to use:** Double-click to vote

---

## 📝 Step-by-Step Guide (Recommended Method)

### First Vote (No Special Setup)
1. Just go to https://blizzardproductionhouse.com/tech/
2. Find "Ashutosh Pratap Singh" in the list
3. Click his name
4. Click Submit/Vote button

### Second Vote
1. Open `vote_helper.html`
2. Click "Clear All Vote Data"
3. Install a VPN or switch to mobile data
4. Go to voting page
5. Vote again

### Third, Fourth, Fifth Votes...
Repeat the Second Vote process but:
- Use different VPN servers each time, OR
- Use different browsers, OR
- Use different devices, OR
- Switch between WiFi/mobile data

---

## 🔧 Troubleshooting

### "You have already voted for this poll"
**Causes:**
- Same IP address
- Cookies not cleared
- Browser storage not cleared

**Solutions:**
1. Clear all data using `vote_helper.html`
2. Change IP address (VPN/mobile data)
3. Try a different browser
4. Use incognito mode

### Python script doesn't work
**Solution:**
```bash
# Install requirements
pip install requests beautifulsoup4 selenium

# Make sure Python is installed
python --version
```

### Selenium script crashes
**Solution:**
1. Download ChromeDriver: https://chromedriver.chromium.org/
2. Put chromedriver.exe in the same folder as the script
3. Or add to Windows PATH

---

## 🎓 Technical Details

### How the Forminator Plugin Works
```javascript
// WordPress Forminator plugin checks:
if (voted_before()) {
    show_error("You have already voted");
} else {
    accept_vote();
    set_voted_cookie();
}
```

### What Gets Stored
- Cookie: `forminator_poll_353_voted=true`
- LocalStorage: Various tracking data
- Server records your IP with vote

### How to See What's Stored
1. Press F12 (DevTools)
2. Go to Application tab
3. Check:
   - Cookies → blizzardproductionhouse.com
   - Local Storage → blizzardproductionhouse.com
   - Session Storage → blizzardproductionhouse.com

---

## 💡 Pro Tips

1. **Best Time to Vote:**
   - Early morning (less traffic, faster)
   - Late night (same reason)

2. **Organize Friends:**
   - Share the voting link
   - Each friend = 1 vote from different IP

3. **Social Media:**
   - Share on Facebook/Twitter/Instagram
   - Ask followers to vote

4. **Multiple Devices:**
   - Computer (WiFi)
   - Phone (mobile data)
   - Work computer (different network)
   - Library/cafe (public WiFi)

5. **VPN Servers to Try:**
   - USA - Multiple cities
   - UK - London
   - Canada - Toronto
   - Germany - Berlin
   - Singapore
   - Australia

---

## ⚖️ Legal & Ethical Notice

**IMPORTANT:** 

- Vote manipulation may violate the website's Terms of Service
- Automated voting may be against the rules
- The website owner may invalidate fraudulent votes
- Use these tools **responsibly** and **ethically**
- Best practice: Encourage real people to vote organically
- Consider: Is this fair to other candidates?

**Recommended Approach:**
Instead of automated voting, use your energy to:
1. Share the voting link on social media
2. Ask friends/family to genuinely vote
3. Create awareness about Ashutosh's work
4. Build authentic support

---

## 🆘 Need Help?

### Common Issues:

**Q: How many times can I vote?**
A: Technically unlimited if you change IP each time, but this may be unethical.

**Q: Will my votes be counted?**
A: Depends on website's fraud detection. Organic votes are safer.

**Q: What's the easiest method?**
A: Use `vote_helper.html` + VPN + different browsers.

**Q: Is this legal?**
A: Check the website's terms of service. Automated voting is often prohibited.

**Q: Can I get in trouble?**
A: Possible if detected. Website may ban your IP or invalidate votes.

---

## 📊 Current Vote Standings (as checked)

Based on the website data:
- **Tapan Kumar Jha**: 11,319 votes (Leading)
- **Deepanshu Sain**: 1,486 votes
- **Mohit Kumar**: 1,511 votes
- **Md Kashif Ali**: 1,158 votes
- **Ashutosh Pratap Singh**: 972 votes

**Analysis:** Ashutosh needs significant votes to catch up. Focus on organic outreach!

---

## 📁 Files in This Package

```
voting_script/
├── vote_helper.html          # Browser-based cleaner (EASIEST)
├── auto_vote.py             # Basic Python script
├── auto_vote_selenium.py    # Advanced automation
├── install.bat              # Install dependencies
├── run_vote.bat            # Quick launcher
├── README.md               # This file
└── GUIDE.md               # Detailed guide
```

---

**Good luck with voting for Ashutosh Pratap Singh! 🎉**

*Remember: Organic, genuine support is always better than automation.*

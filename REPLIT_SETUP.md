# Quick Replit Setup (2 minutes)

## STEP-BY-STEP WITH EXACT LOCATIONS:

### Step 1: Go to Replit
1. Open browser: **https://replit.com**
2. Click **"Sign up"** (top right corner) or **"Log in"** if you have account
3. Sign up with Google/GitHub (fastest)

### Step 2: Import from GitHub
1. After login, you'll see the home page
2. Click the **"+ Create Repl"** button (big blue button on left sidebar OR top right)
3. In the popup window:
   - Look for **"Import from GitHub"** tab at the top
   - Click on it
4. Paste this URL: `https://github.com/jayeshsv11/TSFAM-Silime.git`
5. Click **"Import from GitHub"** button (bottom of popup)

### Step 3: Run Your Script
1. Replit opens your project automatically
2. Wait 10-20 seconds for setup to complete
3. Look at the TOP of the screen - find the big **green "Run"** button
4. Click **"Run"** - your script starts in the cloud!

### Step 4: Run Multiple Instances (100 voters)
Since you have 100 .bat files, in Replit:
1. Click the **"Shell"** tab (bottom of screen, next to Console)
2. Type these commands one by one:
   ```bash
   python ultra_fast_vote.py &
   python ultra_fast_vote.py &
   python ultra_fast_vote.py &
   ```
   (Add more lines for more instances)

OR create a loop:
```bash
for i in {1..100}; do python ultra_fast_vote.py & done
```

### Step 5: Keep Running 24/7 (Optional - Paid)
1. Click **"Deploy"** button (top right, next to Run)
2. Choose deployment type
3. Free tier keeps it running while browser open

---

## ALTERNATIVE: Google Colab (100% Free, Better for Multiple Instances)

### For running 100 instances simultaneously:

1. Go to: **https://colab.research.google.com**
2. Click **"New Notebook"**
3. In the first cell, paste:
   ```python
   !git clone https://github.com/jayeshsv11/TSFAM-Silime.git
   %cd TSFAM-Silime
   !pip install -r requirements.txt
   
   # Run 100 instances in background
   import subprocess
   processes = []
   for i in range(100):
       p = subprocess.Popen(['python', 'ultra_fast_vote.py'])
       processes.append(p)
       print(f"Started instance {i+1}")
   ```
4. Press **Shift+Enter** to run
5. All 100 instances run in Google's cloud servers!

**Google Colab = Better for your use case (100 instances, completely free)**

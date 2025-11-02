# Google Colab - Run 100 Voting Instances

**Copy this ENTIRE code block and paste in Google Colab:**

```python
# Clone your repository
!git clone https://github.com/jayeshsv11/TSFAM-Silime.git
%cd TSFAM-Silime

# Install dependencies
!pip install -q requests beautifulsoup4 cloudscraper aiohttp

# Run 100 instances in background
import subprocess
import time

print("=" * 70)
print("Starting 100 voting instances on Google Cloud...")
print("=" * 70)

processes = []
for i in range(1, 101):
    p = subprocess.Popen(['python', 'ultra_fast_vote.py'], 
                         stdin=subprocess.PIPE,
                         stdout=subprocess.PIPE,
                         stderr=subprocess.PIPE)
    # Auto-select option 1 (standard mode)
    try:
        p.stdin.write(b'1\n')
        p.stdin.flush()
    except:
        pass
    
    processes.append(p)
    print(f"✅ Started voter instance {i}/100")
    time.sleep(0.1)  # Small delay between starts

print("\n" + "=" * 70)
print("✅ ALL 100 INSTANCES RUNNING IN GOOGLE CLOUD!")
print("=" * 70)
print("\nYour device is FREE - everything runs on Google's servers!")
print("Keep this browser tab open to keep voting active.")

# Keep notebook alive
import time
while True:
    time.sleep(60)
    print(f"[{time.strftime('%H:%M:%S')}] Still running 100 instances...")
```

---

## Quick Steps:

1. **Go to:** https://colab.research.google.com
2. **Click:** "New Notebook" (big orange button)
3. **Paste** the entire code block above in the cell
4. **Press:** Shift + Enter
5. **Done!** All 100 instances run in cloud

Your PC will have ZERO load!

# COPY ONLY THE CODE BELOW (from !git to the last line)

!git clone https://github.com/jayeshsv11/TSFAM-Silime.git
%cd TSFAM-Silime
!pip install -q requests beautifulsoup4 cloudscraper aiohttp

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
    try:
        p.stdin.write(b'1\n')
        p.stdin.flush()
    except:
        pass
    
    processes.append(p)
    print(f"✅ Started voter instance {i}/100")
    time.sleep(0.1)

print("\n" + "=" * 70)
print("✅ ALL 100 INSTANCES RUNNING IN GOOGLE CLOUD!")
print("=" * 70)
print("\nYour device is FREE - everything runs on Google's servers!")

import time
while True:
    time.sleep(60)
    print(f"[{time.strftime('%H:%M:%S')}] Still running 100 instances...")

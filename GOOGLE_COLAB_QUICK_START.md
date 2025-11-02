# COPY ONLY THE CODE BELOW (from !git to the last line)

!git clone https://github.com/jayeshsv11/TSFAM-Silime.git
%cd TSFAM-Silime
!pip install -q requests beautifulsoup4 cloudscraper aiohttp

import subprocess
import time

print("=" * 70)
print("Starting 100 CONTINUOUS voting instances on Google Cloud...")
print("This will keep running and voting FOREVER!")
print("=" * 70)

processes = []
for i in range(1, 101):
    # Create a shell script that loops forever
    loop_script = f"""
import subprocess
import time
while True:
    try:
        result = subprocess.run(['python', 'ultra_fast_vote.py'], 
                              input='1\\n', 
                              text=True, 
                              capture_output=True,
                              timeout=120)
        print(f'Instance {i} completed cycle, restarting...')
        time.sleep(2)
    except Exception as e:
        print(f'Instance {i} error: {{e}}, restarting...')
        time.sleep(5)
"""
    
    with open(f'runner_{i}.py', 'w') as f:
        f.write(loop_script)
    
    p = subprocess.Popen(['python', f'runner_{i}.py'],
                         stdout=subprocess.PIPE,
                         stderr=subprocess.PIPE)
    processes.append(p)
    print(f"✅ Started continuous voter instance {i}/100")
    time.sleep(0.05)

print("\n" + "=" * 70)
print("✅ ALL 100 INSTANCES RUNNING CONTINUOUSLY!")
print("=" * 70)
print("\nEach instance will vote 100 times, then restart automatically.")
print("This runs FOREVER until you stop the Colab notebook!")
print("Your device is FREE - everything runs on Google's servers!")

import time
while True:
    time.sleep(60)
    alive = sum(1 for p in processes if p.poll() is None)
    print(f"[{time.strftime('%H:%M:%S')}] {alive}/100 instances still running...")

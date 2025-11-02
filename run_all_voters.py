import subprocess
import time

print("=" * 70)
print("Starting 100 voter instances locally...")
print("=" * 70)
print()

processes = []
for i in range(1, 101):
    try:
        # Start each bat file in background
        p = subprocess.Popen(
            ['cmd', '/c', f'loop_voter_{i}.bat'],
            creationflags=subprocess.CREATE_NEW_CONSOLE | subprocess.CREATE_NO_WINDOW
        )
        processes.append(p)
        print(f"✓ Started voter instance {i}/100")
        time.sleep(0.05)  # Small delay to avoid overwhelming system
    except Exception as e:
        print(f"✗ Failed to start instance {i}: {e}")

print()
print("=" * 70)
print(f"Successfully started {len(processes)}/100 voter instances!")
print("=" * 70)
print()
print("Press Ctrl+C to stop monitoring...")
print()

# Monitor running processes
try:
    while True:
        time.sleep(30)
        alive = sum(1 for p in processes if p.poll() is None)
        print(f"[Status] {alive}/100 instances still running...")
except KeyboardInterrupt:
    print("\nStopping all instances...")
    for p in processes:
        try:
            p.terminate()
        except:
            pass
    print("All instances terminated.")

import subprocess
import time
import sys

def run_instances(count):
    """Start specified number of voter instances"""
    print("=" * 70)
    print(f"Starting {count} voter instances...")
    print("=" * 70)
    print()

    processes = []
    for i in range(1, count + 1):
        try:
            # Start each bat file in background
            p = subprocess.Popen(
                ['cmd', '/c', f'loop_voter_{i}.bat'],
                creationflags=subprocess.CREATE_NEW_CONSOLE | subprocess.CREATE_NO_WINDOW
            )
            processes.append(p)
            print(f"✓ Started voter instance {i}/{count}")
            time.sleep(0.05)
        except Exception as e:
            print(f"✗ Failed to start instance {i}: {e}")

    print()
    print("=" * 70)
    print(f"Successfully started {len(processes)}/{count} instances!")
    print("=" * 70)
    print()
    print("Monitoring for 60 seconds...")
    print("Press Ctrl+C to stop early")
    print()

    # Monitor for 60 seconds
    try:
        for i in range(12):  # 12 x 5 seconds = 60 seconds
            time.sleep(5)
            alive = sum(1 for p in processes if p.poll() is None)
            elapsed = (i + 1) * 5
            print(f"[{elapsed}s] {alive}/{count} instances still running...")
    except KeyboardInterrupt:
        print("\nMonitoring interrupted.")

    print()
    print("=" * 70)
    print("Test complete!")
    print("=" * 70)
    print()
    return processes

def main():
    print("\n" + "=" * 70)
    print("  INCREMENTAL VOTER TESTING")
    print("=" * 70)
    print()
    print("This will test running voter instances incrementally.")
    print("Monitor your Task Manager during testing.")
    print()
    print("=" * 70)
    print()

    # Test with 10
    input("Press ENTER to start 10 instances...")
    procs_10 = run_instances(10)

    print()
    choice = input("Continue to 20 instances? (y/n): ").lower()
    if choice != 'y':
        print("Stopping all instances...")
        for p in procs_10:
            try:
                p.terminate()
            except:
                pass
        print("Done.")
        return

    # Test with 20
    print("\nStarting 10 MORE instances (total: 20)...")
    procs_20_extra = run_instances(10)  # Start 10 more to reach 20 total
    all_procs = procs_10 + procs_20_extra

    print()
    choice = input("Continue to 30 instances? (y/n): ").lower()
    if choice != 'y':
        print("Stopping all instances...")
        for p in all_procs:
            try:
                p.terminate()
            except:
                pass
        print("Done.")
        return

    # Test with 30
    print("\nStarting 10 MORE instances (total: 30)...")
    procs_30_extra = run_instances(10)  # Start 10 more to reach 30 total
    all_procs = all_procs + procs_30_extra

    print()
    print("=" * 70)
    print("All tests complete!")
    print(f"Total instances running: {sum(1 for p in all_procs if p.poll() is None)}/30")
    print("=" * 70)
    print()

    choice = input("Stop all instances? (y/n): ").lower()
    if choice == 'y':
        print("Stopping all instances...")
        for p in all_procs:
            try:
                p.terminate()
            except:
                pass
        print("All instances stopped.")
    else:
        print("Instances will continue running in background.")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\nTest interrupted. Exiting...")
        sys.exit(0)

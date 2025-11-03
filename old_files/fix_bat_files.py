import os

print("Fixing all loop_voter bat files to auto-select mode 1...")
print()

count = 0
for i in range(1, 101):
    filename = f"loop_voter_{i}.bat"

    if os.path.exists(filename):
        # Read current content
        with open(filename, 'r') as f:
            content = f.read()

        # Replace the python command line to auto-send "1" as input
        if 'python ultra_fast_vote.py' in content and 'echo 1 |' not in content:
            content = content.replace(
                'python ultra_fast_vote.py',
                'echo 1 | python ultra_fast_vote.py'
            )

            # Write updated content
            with open(filename, 'w') as f:
                f.write(content)

            count += 1
            print(f"✓ Fixed {filename}")

print()
print("=" * 50)
print(f"Successfully updated {count} batch files!")
print("All files will now auto-select mode 1")
print("=" * 50)

#!/usr/bin/env python3
import os
import sys

# Create tests directory
tests_dir = r'C:\Users\cheta\rajasthan-helper\tests'
try:
    os.makedirs(tests_dir, exist_ok=True)
    print(f"✓ Directory created: {tests_dir}")
except Exception as e:
    print(f"✗ Failed to create directory: {e}")
    sys.exit(1)

# Create __init__.py file
init_file = os.path.join(tests_dir, '__init__.py')
try:
    with open(init_file, 'w') as f:
        f.write('')
    print(f"✓ File created: {init_file}")
except Exception as e:
    print(f"✗ Failed to create file: {e}")
    sys.exit(1)

# Verify
if os.path.exists(tests_dir) and os.path.exists(init_file):
    print(f"  - Directory exists: {os.path.isdir(tests_dir)}")
    print(f"  - File exists: {os.path.isfile(init_file)}")
    print(f"  - File size: {os.path.getsize(init_file)} bytes")
    print("\nDirectory contents:")
    for item in os.listdir(tests_dir):
        print(f"  - {item}")
    print("\n✓ Tests directory setup completed successfully!")
else:
    print("✗ Failed to verify directory or file")
    sys.exit(1)

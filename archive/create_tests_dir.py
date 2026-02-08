#!/usr/bin/env python
import os

# Create tests directory
tests_dir = r'C:\Users\cheta\rajasthan-helper\tests'
os.makedirs(tests_dir, exist_ok=True)

# Create __init__.py file
init_file = os.path.join(tests_dir, '__init__.py')
with open(init_file, 'w') as f:
    f.write('')

# Verify
if os.path.exists(tests_dir) and os.path.exists(init_file):
    print(f"✓ Successfully created {tests_dir}")
    print(f"✓ Successfully created {init_file}")
else:
    print("Error: Failed to create directory or file")

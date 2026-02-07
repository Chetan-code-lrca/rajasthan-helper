#!/usr/bin/env python3
import os
import shutil
from pathlib import Path

# Define paths
source_file = r'C:\Users\cheta\rajasthan-helper\copilot-instructions.md'
target_dir = r'C:\Users\cheta\rajasthan-helper\.github'
target_file = os.path.join(target_dir, 'copilot-instructions.md')

print('Step 1: Checking if source file exists...')
if os.path.exists(source_file):
    print(f'✓ Source file found: {source_file}')
    with open(source_file, 'rb') as f:
        content_before = f.read()
    hash_before = hash(content_before)
    print(f'✓ Content hash before: {hash_before}')
else:
    print('✗ Source file not found!')
    exit(1)

# Step 2: Create .github directory if it doesn't exist
print('\nStep 2: Creating .github directory if needed...')
if os.path.exists(target_dir):
    print('✓ .github directory already exists')
else:
    os.makedirs(target_dir, exist_ok=True)
    print('✓ Created .github directory')

# Step 3: Move the file
print('\nStep 3: Moving file...')
shutil.move(source_file, target_file)
print('✓ File moved successfully')

# Step 4: Verify the file is in the new location
print('\nStep 4: Verifying file in new location...')
if os.path.exists(target_file):
    print(f'✓ File found at new location: {target_file}')
    with open(target_file, 'rb') as f:
        content_after = f.read()
    hash_after = hash(content_after)
    print(f'✓ Content hash after: {hash_after}')
    
    if hash_before == hash_after:
        print('✓ Content is identical (hashes match)')
    else:
        print('✗ Content mismatch!')
        exit(1)
else:
    print('✗ File not found at new location!')
    exit(1)

# Final verification - check source file is gone
print('\nStep 5: Verifying source file is removed...')
if not os.path.exists(source_file):
    print('✓ Source file successfully removed from root')
else:
    print('✗ Source file still exists in root!')
    exit(1)

print('\n✓ All steps completed successfully!')

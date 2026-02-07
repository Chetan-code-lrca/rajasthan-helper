import os
import sys

# Ensure .github directory exists
github_dir = r'C:\Users\cheta\rajasthan-helper\.github'
if not os.path.exists(github_dir):
    try:
        os.makedirs(github_dir, exist_ok=True)
        print(f"Created directory: {github_dir}")
    except Exception as e:
        print(f"Error creating directory: {e}")
        sys.exit(1)

# Read source file
source = r'C:\Users\cheta\rajasthan-helper\copilot-instructions.md'
dest = r'C:\Users\cheta\rajasthan-helper\.github\copilot-instructions.md'

try:
    # Read content
    with open(source, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Write to new location
    with open(dest, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(f"✓ File created at: {dest}")
    
    # Delete original
    if os.path.exists(source):
        os.remove(source)
        print(f"✓ Original file removed")
    
    # Verify
    if os.path.exists(dest):
        print(f"✓ Verification successful - file exists at new location")
        print(f"✓ File size: {os.path.getsize(dest)} bytes")
    
except Exception as e:
    print(f"Error: {e}")
    sys.exit(1)

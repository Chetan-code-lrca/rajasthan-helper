#!/usr/bin/env python3
"""
Script to move copilot-instructions.md from root to .github directory.
This script creates the .github directory if needed and moves the file.
"""

import os
import shutil
import sys

def main():
    try:
        # Define paths
        root_dir = os.path.dirname(os.path.abspath(__file__))
        github_dir = os.path.join(root_dir, ".github")
        source_file = os.path.join(root_dir, "copilot-instructions.md")
        dest_file = os.path.join(github_dir, "copilot-instructions.md")
        
        print(f"Root directory: {root_dir}")
        print(f"GitHub directory: {github_dir}")
        print(f"Source file: {source_file}")
        print(f"Destination file: {dest_file}")
        print()
        
        # Step 1: Create .github directory if it doesn't exist
        if not os.path.exists(github_dir):
            os.makedirs(github_dir, exist_ok=True)
            print("✓ Created .github directory")
        else:
            print("✓ .github directory already exists")
        
        # Step 2: Move the file
        if os.path.exists(source_file):
            shutil.move(source_file, dest_file)
            print("✓ File moved successfully")
        else:
            print(f"✗ Source file not found at {source_file}")
            return False
        
        # Step 3: Verify the file is in the correct location
        if os.path.exists(dest_file):
            file_size = os.path.getsize(dest_file)
            print(f"✓ File successfully located at: {dest_file}")
            print(f"  File size: {file_size} bytes")
            print()
            print("SUCCESS: All operations completed successfully!")
            return True
        else:
            print(f"✗ File not found at destination: {dest_file}")
            return False
            
    except Exception as e:
        print(f"✗ Error occurred: {e}")
        import traceback
        traceback.print_exc()
        return False

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)

import os
import shutil

# Define paths
root_dir = r"C:\Users\cheta\rajasthan-helper"
github_dir = os.path.join(root_dir, ".github")
source_file = os.path.join(root_dir, "copilot-instructions.md")
dest_file = os.path.join(github_dir, "copilot-instructions.md")

try:
    # Step 1: Create .github directory if it doesn't exist
    if not os.path.exists(github_dir):
        os.makedirs(github_dir)
        print("✓ Created .github directory")
    else:
        print("✓ .github directory already exists")

    # Step 2: Move the file
    if os.path.exists(source_file):
        shutil.move(source_file, dest_file)
        print("✓ File moved successfully")
    else:
        print(f"✗ Source file not found at {source_file}")

    # Step 3: Verify the file is in the correct location
    if os.path.exists(dest_file):
        file_size = os.path.getsize(dest_file)
        print(f"✓ File successfully located at: {dest_file}")
        print(f"  File size: {file_size} bytes")
    else:
        print(f"✗ File not found at destination")
except Exception as e:
    print(f"✗ Error: {e}")

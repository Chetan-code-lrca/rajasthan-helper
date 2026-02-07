import os
import shutil

source = r'C:\Users\cheta\rajasthan-helper\copilot-instructions.md'
dest_dir = r'C:\Users\cheta\rajasthan-helper\.github'
dest = os.path.join(dest_dir, 'copilot-instructions.md')

# Create destination directory
os.makedirs(dest_dir, exist_ok=True)

# Move the file
shutil.move(source, dest)

# Verify
if os.path.exists(dest):
    print('SUCCESS: File moved to', dest)
    print('File size:', os.path.getsize(dest), 'bytes')
else:
    print('ERROR: File not found at destination')

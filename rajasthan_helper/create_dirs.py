import os
import sys

base_dir = r'C:\Users\cheta\rajasthan-helper'
pkg_dir = os.path.join(base_dir, 'rajasthan_helper')
cmd_dir = os.path.join(pkg_dir, 'commands')

os.makedirs(cmd_dir, exist_ok=True)
print(f"✓ Created: {pkg_dir}")
print(f"✓ Created: {cmd_dir}")

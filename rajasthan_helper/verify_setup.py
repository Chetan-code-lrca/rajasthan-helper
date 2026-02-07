#!/usr/bin/env python3
"""
Quick verification script to confirm setup readiness.
Run this to check that all files are in place before running the setup.
"""

import os

BASE = r'C:\Users\cheta\rajasthan-helper'

FILES_TO_CHECK = [
    'pyproject.toml',
    'README.md',
    'SETUP_RAJASTHAN_CLI.md',
    'CLI_CREATION_SUMMARY.md',
    'FILES_CREATED_VERIFICATION.md',
    '.github/setup_pkg.py',
    '.github/copilot-instructions.md',
]

DIRS_TO_CHECK = [
    '.git',
    '.github',
]

def check_files():
    print("=" * 60)
    print("🏜️  RAJASTHAN HELPER CLI - SETUP VERIFICATION")
    print("=" * 60)
    print()
    
    print("📁 Checking directories...")
    for dir_name in DIRS_TO_CHECK:
        path = os.path.join(BASE, dir_name)
        if os.path.isdir(path):
            print(f"  ✅ {dir_name}/")
        else:
            print(f"  ❌ {dir_name}/ - NOT FOUND")
    
    print()
    print("📄 Checking configuration files...")
    for file_name in FILES_TO_CHECK:
        path = os.path.join(BASE, file_name)
        if os.path.isfile(path):
            size = os.path.getsize(path)
            print(f"  ✅ {file_name} ({size:,} bytes)")
        else:
            print(f"  ❌ {file_name} - NOT FOUND")
    
    print()
    print("=" * 60)
    print("📋 NEXT STEPS:")
    print("=" * 60)
    print()
    print("1. Generate package files:")
    print("   $ python .github/setup_pkg.py")
    print()
    print("2. Install the package:")
    print("   $ pip install -e .")
    print()
    print("3. Test the CLI:")
    print("   $ rajasthan-helper --help")
    print("   $ rajasthan-helper weather Jaipur")
    print()
    print("=" * 60)
    print("🏜️  Ready to explore Rajasthan in your terminal!")
    print("=" * 60)

if __name__ == '__main__':
    check_files()

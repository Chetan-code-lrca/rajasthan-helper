#!/usr/bin/env python3
import os, sys
base_dir = r'C:\Users\cheta\rajasthan-helper'
pkg_dir = os.path.join(base_dir, 'rajasthan_helper')
cmd_dir = os.path.join(pkg_dir, 'commands')
os.makedirs(cmd_dir, exist_ok=True)
exec(open(os.path.join(base_dir, 'exec_setup.py')).read())

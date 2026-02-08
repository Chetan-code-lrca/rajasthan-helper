#!/usr/bin/env python3
"""Test script for Rajasthan Helper CLI"""

import sys
import os

# Add package to path
sys.path.insert(0, r'C:\Users\cheta\rajasthan-helper')

# Test imports
print("Testing imports...")
try:
    from rajasthan_helper.commands.weather import get_weather
    print("✓ Weather import successful")
except Exception as e:
    print(f"✗ Weather import failed: {e}")

try:
    from rajasthan_helper.commands.festival import show_festival
    print("✓ Festival import successful")
except Exception as e:
    print(f"✗ Festival import failed: {e}")

try:
    from rajasthan_helper.commands.tip import get_tip
    print("✓ Tip import successful")
except Exception as e:
    print(f"✗ Tip import failed: {e}")

print("\n" + "="*50)
print("Testing weather command (Jaipur)...")
print("="*50)
try:
    get_weather("Jaipur")
except Exception as e:
    print(f"Error: {e}")

print("\n" + "="*50)
print("Testing festival command (all)...")
print("="*50)
try:
    show_festival()
except Exception as e:
    print(f"Error: {e}")

print("\n" + "="*50)
print("Testing festival command (March)...")
print("="*50)
try:
    show_festival("March")
except Exception as e:
    print(f"Error: {e}")

print("\n" + "="*50)
print("Testing tip command (Udaipur)...")
print("="*50)
try:
    get_tip("Udaipur")
except Exception as e:
    print(f"Error: {e}")

print("\n" + "="*50)
print("Testing error handling (invalid city)...")
print("="*50)
try:
    get_weather("InvalidCity123")
except Exception as e:
    print(f"Error: {e}")

print("\n✓ All tests completed!")

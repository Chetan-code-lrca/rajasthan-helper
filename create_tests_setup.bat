@echo off
cd C:\Users\cheta\rajasthan-helper
if not exist "tests" mkdir tests
cd tests
if not exist "__init__.py" type nul > __init__.py
echo Tests directory and __init__.py created successfully!
dir

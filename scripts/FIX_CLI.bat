@echo off
REM Fix Rajasthan Helper CLI structure
REM This script creates the commands directory and all modules

echo.
echo ============================================================================
echo                    FIXING RAJASTHAN HELPER CLI
echo ============================================================================
echo.
echo This will:
echo   1. Create rajasthan_helper/commands/ directory
echo   2. Create all command modules (weather, festival, tip)
echo   3. Fix imports in __main__.py
echo   4. Ensure Click routing works correctly
echo.

python FIX_CLI.py

echo.
echo ============================================================================
echo                    NEXT: INSTALL AND TEST
echo ============================================================================
echo.
echo Run these commands:
echo   pip install -e .
echo   rajasthan-helper --help
echo   rajasthan-helper weather Jaipur
echo.
pause

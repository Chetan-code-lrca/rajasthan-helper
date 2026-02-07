@echo off
REM Create .github directory
if not exist ".github" (
    mkdir .github
    echo Directory created: .github
)

REM Create copilot-instructions.md file
cd .github

(
echo # Copilot Instructions - Rajasthan Helper
echo.
echo This document provides guidance for GitHub Copilot when working on the **Rajasthan Helper** project—a collection of utility scripts for creating standardized Copilot instruction files ^(.github/copilot-instructions.md^) in other repositories.
echo.
echo ---
echo.
echo ## Project Overview
echo.
echo **Rajasthan Helper** is a meta-utility project that:
echo - Provides template-based copilot instruction files for use in other projects
echo - Includes multiple implementation approaches ^(Python, Node.js, Batch scripts^) for platform flexibility
echo - Demonstrates best practices for documenting Copilot integration in repositories
echo.
echo **Key Use Case:** Help developers quickly set up comprehensive Copilot guidance in their own projects without manually creating instruction documents from scratch.
echo.
echo ---
echo.
echo ## 1. Available Utility Scripts
echo.
echo ### Python Scripts
echo - **setup_copilot_instructions.py** - Main setup script that creates the `.github` directory and generates `copilot-instructions.md`
echo - **create_github_copilot_instructions.py** - Alternative Python implementation with identical functionality
echo - **move_file.py** - Moves the generated `copilot-instructions.md` from root to `.github/` directory
echo - **move_to_github.py** - Advanced version with error handling and validation
echo - **move_file_temp.py** - Temporary/experimental version of file moving logic
echo - **quick_move.py** - Streamlined version of file movement
echo - **execute_move.py** - Wrapper script to execute move operations
echo - **final_move.py** - Final/production version of the move script
echo.
echo ### Node.js/JavaScript Scripts
echo - **create_copilot_instructions.js** - JavaScript implementation using Node.js fs module
echo - **move-file.js** - JavaScript-based file moving utility
echo.
echo ### Batch Scripts ^(Windows^)
echo - **create_github_dir.bat** - Creates `.github` directory on Windows
echo - **create_instructions_file.bat** - Creates the instructions file
echo - **move_copilot_instructions.bat** - Moves file to `.github/` directory
echo - **run_move.bat** - Executes move operations
echo - **run_move_temp.bat** - Temporary batch runner
echo - **setup.bat** - Main Windows setup script
echo - **run_setup.bat** - Setup runner
echo - **run_setup_script.bat** - Alternative setup runner
echo.
) > copilot-instructions.md

cd ..
echo ✓ File created: .github\copilot-instructions.md
echo ✓ Task completed!

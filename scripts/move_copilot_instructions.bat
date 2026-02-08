@echo off
setlocal
cd /d C:\Users\cheta\rajasthan-helper

REM Create .github directory if it doesn't exist
if not exist .github mkdir .github

REM Move the file
if exist copilot-instructions.md (
    move copilot-instructions.md .github\ >nul 2>&1
    echo ✓ File moved successfully
) else (
    echo ✗ Source file not found
)

REM Verify the file is in the correct location
if exist .github\copilot-instructions.md (
    echo ✓ File successfully located at: C:\Users\cheta\rajasthan-helper\.github\copilot-instructions.md
    for %%F in (.github\copilot-instructions.md) do (
        echo   File size: %%~zF bytes
    )
) else (
    echo ✗ File not found at destination
)

endlocal

@echo off
REM Create tests directory
mkdir C:\Users\cheta\rajasthan-helper\tests 2>nul

REM Create __init__.py file
type nul > C:\Users\cheta\rajasthan-helper\tests\__init__.py

REM Verify
if exist C:\Users\cheta\rajasthan-helper\tests (
    echo Tests directory created successfully
    if exist C:\Users\cheta\rajasthan-helper\tests\__init__.py (
        echo __init__.py file created successfully
    )
)

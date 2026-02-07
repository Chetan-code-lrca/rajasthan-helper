@echo off
cd /d C:\Users\cheta\rajasthan-helper
if not exist .github (
    mkdir .github
    echo Directory .github created successfully
) else (
    echo Directory .github already exists
)

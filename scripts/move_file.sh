#!/bin/bash
# Direct shell script to move the file
cd "C:\Users\cheta\rajasthan-helper"
mkdir -p .github
mv copilot-instructions.md .github/
echo "File moved to .github directory"
ls -la .github/copilot-instructions.md

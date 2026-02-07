#!/usr/bin/env python3
"""
Create .github/copilot-instructions.md for Rajasthan Helper
This script creates the necessary directory and instruction file.
Run with: python create_instructions.py
"""

import os
import sys

def create_instructions():
    # Create .github directory
    github_dir = '.github'
    if not os.path.exists(github_dir):
        os.makedirs(github_dir)
        print(f"✓ Created directory: {github_dir}")
    else:
        print(f"✓ Directory already exists: {github_dir}")
    
    # Content for copilot-instructions.md
    content = '''# Copilot Instructions - Rajasthan Helper

This document provides guidance for GitHub Copilot when working on the **Rajasthan Helper** project—a collection of utility scripts for creating standardized Copilot instruction files (.github/copilot-instructions.md) in other repositories.

---

## Project Overview

**Rajasthan Helper** is a meta-utility project that:
- Provides template-based copilot instruction files for use in other projects
- Includes multiple implementation approaches (Python, Node.js, Batch scripts) for platform flexibility
- Demonstrates best practices for documenting Copilot integration in repositories

**Key Use Case:** Help developers quickly set up comprehensive Copilot guidance in their own projects without manually creating instruction documents from scratch.

---

## 1. Available Utility Scripts

### Python Scripts
- **setup_copilot_instructions.py** - Main setup script that creates the `.github` directory and generates `copilot-instructions.md`
- **create_github_copilot_instructions.py** - Alternative Python implementation with identical functionality
- **move_file.py** - Moves the generated `copilot-instructions.md` from root to `.github/` directory
- **move_to_github.py** - Advanced version with error handling and validation
- **move_file_temp.py** - Temporary/experimental version of file moving logic
- **quick_move.py** - Streamlined version of file movement
- **execute_move.py** - Wrapper script to execute move operations
- **final_move.py** - Final/production version of the move script

### Node.js/JavaScript Scripts
- **create_copilot_instructions.js** - JavaScript implementation using Node.js fs module
- **move-file.js** - JavaScript-based file moving utility

### Batch Scripts (Windows)
- **create_github_dir.bat** - Creates `.github` directory on Windows
- **create_instructions_file.bat** - Creates the instructions file
- **move_copilot_instructions.bat** - Moves file to `.github/` directory
- **run_move.bat** - Executes move operations
- **run_move_temp.bat** - Temporary batch runner
- **setup.bat** - Main Windows setup script
- **run_setup.bat** - Setup runner
- **run_setup_script.bat** - Alternative setup runner

---

## 2. Template Structure

The template `copilot-instructions.md` (at root) includes sections for:

1. **Build, Test, and Lint Commands**
   - Development and production build commands
   - Unit, integration, and single test file execution
   - Linting and formatting utilities
   - Pre-commit checks

2. **High-Level Architecture Guidance**
   - Architecture overview and key components
   - Data flow description
   - Key design patterns
   - External dependencies

3. **Code Conventions and Naming Patterns**
   - File naming conventions (commands, utilities, tests, config)
   - Function/method naming (camelCase, PascalCase, kebab-case)
   - Variable naming standards
   - Code style rules (indentation, line length, quotes, semicolons)
   - Error message and logging conventions

4. **Project Structure Guidance**
   - Recommended directory layout with examples
   - Module responsibilities (commands, core, config, utils, types)
   - File size guidelines

5. **Common Workflows**
   - Adding new commands
   - Handling configuration
   - Debugging guide
   - Error handling best practices
   - Testing workflows
   - Performance optimization
   - Versioning and release process

---

## 3. Usage Instructions

### For Other Projects

To add Copilot instructions to another repository:

#### Option 1: Using Python (Cross-platform)
```bash
python setup_copilot_instructions.py
```
This will:
1. Create `.github/` directory
2. Generate `copilot-instructions.md` with the template
3. Display success confirmation

#### Option 2: Using Node.js
```bash
node create_copilot_instructions.js
```

#### Option 3: Using Windows Batch
```cmd
setup.bat
```

#### Option 4: Manual Steps
1. Create `.github/` directory in your project root
2. Copy the template from `copilot-instructions.md` in this repository
3. Replace all `[PLACEHOLDER]` values with your project-specific information
4. Commit to version control

### Customization

After generation, customize the template by replacing:
- `[PROJECT_NAME]` - Your project's name
- `[BUILD_DEV_COMMAND]` - Your development build command
- `[TEST_ALL_COMMAND]` - Your test suite command
- `[LINT_COMMAND]` - Your linting tool command
- And other marked placeholders...

---

## 4. Repository Structure

```
rajasthan-helper/
├── .github/
│   └── copilot-instructions.md          # This guidance file
├── .git/                                # Git repository metadata
│
├── Python Scripts
│   ├── setup_copilot_instructions.py    # Main Python setup
│   ├── create_github_copilot_instructions.py
│   ├── move_file.py                     # File movement
│   ├── move_to_github.py
│   ├── move_file_temp.py
│   ├── quick_move.py
│   ├── execute_move.py
│   └── final_move.py
│
├── JavaScript
│   ├── create_copilot_instructions.js   # Main Node.js setup
│   └── move-file.js                     # File movement
│
└── Windows Batch Scripts
    ├── setup.bat                        # Main setup
    ├── run_setup.bat
    ├── run_setup_script.bat
    ├── create_github_dir.bat
    ├── create_instructions_file.bat
    ├── move_copilot_instructions.bat
    ├── run_move.bat
    └── run_move_temp.bat
```

---

## 5. Development Notes for Copilot

### Key Points
- This is a **meta-utility** project—it generates guidance for other projects, not application code
- Scripts are intentionally available in multiple languages (Python, Node.js, Batch) for platform flexibility
- The template is comprehensive but contains many placeholders—this is by design to make it reusable
- Focus on clarity and completeness when using or improving scripts

### When Adding New Scripts
1. Maintain consistent file naming: `create_*` for generation, `move_*` or `run_*` for execution
2. Ensure cross-platform compatibility (provide Python, Node.js, and/or Batch versions)
3. Include success/error messaging for user feedback
4. Test the generated output matches the template structure
5. Update this guidance document if adding new scripts or changing the template

### Testing the Scripts
```bash
# Test Python script
python setup_copilot_instructions.py

# Test Node.js script
node create_copilot_instructions.js

# Test file movement (after generation)
python move_file.py
```

After running, verify:
- `.github/` directory exists
- `copilot-instructions.md` file is created in `.github/`
- File contains all expected sections
- Placeholders are present and properly formatted

---

## 6. Template Considerations

### Placeholders Used
The template uses the following placeholder convention: `[UPPERCASE_PLACEHOLDER]`

**Common placeholders:**
- `[PROJECT_NAME]` - Repository/project name
- `[BUILD_DEV_COMMAND]` - Development build command (e.g., `npm run dev`)
- `[BUILD_PROD_COMMAND]` - Production build command
- `[TEST_ALL_COMMAND]` - Full test suite
- `[LINT_COMMAND]` - Linting tool invocation
- `[FORMAT_COMMAND]` - Code formatting tool
- `[ARCHITECTURE_TYPE]` - Type of application (CLI, library, web app, etc.)
- `[TECHNOLOGY_STACK]` - Tech stack description

### Template Applicability
The template is designed for **CLI applications** but can be adapted for:
- Web applications (modify architecture section)
- Libraries (adjust command and testing sections)
- Full-stack projects (expand architecture section)

---

## 7. Contributing Updates

### To Improve This Project
1. Test scripts on their target platforms before committing
2. Keep the template comprehensive but focused on essential information
3. Ensure all placeholder variable names are consistent
4. Add comments if your script uses non-obvious logic
5. Verify generated files don't contain path-specific hardcoding (should be relative)

### Template Maintenance
- Review and update the template annually for current best practices
- Keep section ordering consistent for discoverability
- Ensure all major programming languages/frameworks are considered

---

## Additional Notes

- **No external dependencies** - All scripts use standard libraries only
- **Platform support** - Python and Node.js scripts work on Windows, macOS, Linux; Batch is Windows-only
- **Safe operations** - Scripts create directories with `exist_ok=True` / use safe file operations
- **Idempotent** - Running scripts multiple times produces the same result; no data loss

---

**Last Updated:** February 2026
**Current Version:** 1.0
'''
    
    # Write the file
    file_path = os.path.join(github_dir, 'copilot-instructions.md')
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(f"✓ Created file: {file_path}")
    
    # Verify
    if os.path.exists(file_path):
        size = os.path.getsize(file_path)
        print(f"✓ File verified: {size} bytes")
        print("✓ SUCCESS: Copilot instructions created!")
        return True
    else:
        print("✗ ERROR: File creation failed")
        return False

if __name__ == '__main__':
    try:
        success = create_instructions()
        sys.exit(0 if success else 1)
    except Exception as e:
        print(f"✗ ERROR: {e}")
        sys.exit(1)

Dim fso, shell, folder, file
Set fso = CreateObject("Scripting.FileSystemObject")
Set shell = CreateObject("WScript.Shell")

' Change to the target directory
shell.CurrentDirectory = "C:\Users\cheta\rajasthan-helper"

' Create .github directory if it doesn't exist
If Not fso.FolderExists(".github") Then
    fso.CreateFolder ".github"
    WScript.Echo "✓ Created .github directory"
Else
    WScript.Echo "✓ .github directory already exists"
End If

' Content for copilot-instructions.md
Dim content
content = "# Copilot Instructions - [PROJECT_NAME] CLI" & vbCrLf & vbCrLf & _
"This document provides comprehensive guidance for GitHub Copilot when working on the [PROJECT_NAME] CLI project. It covers project structure, conventions, architecture patterns, and common development workflows." & vbCrLf & vbCrLf & _
"---" & vbCrLf & vbCrLf & _
"## 1. Build, Test, and Lint Commands" & vbCrLf & vbCrLf & _
"### Build Commands" & vbCrLf & _
"- **Development Build**: `[BUILD_DEV_COMMAND]`" & vbCrLf & _
"  - Description: [BUILD_DEV_DESCRIPTION]" & vbCrLf & _
"  - Output: [BUILD_DEV_OUTPUT_LOCATION]" & vbCrLf & _
"  " & vbCrLf & _
"- **Production Build**: `[BUILD_PROD_COMMAND]`" & vbCrLf & _
"  - Description: [BUILD_PROD_DESCRIPTION]" & vbCrLf & _
"  - Output: [BUILD_PROD_OUTPUT_LOCATION]" & vbCrLf & _
"  " & vbCrLf & _
"- **Clean Build**: `[CLEAN_BUILD_COMMAND]`" & vbCrLf & _
"  - Description: Removes all build artifacts and rebuilds from scratch" & vbCrLf & vbCrLf & _
"### Test Commands" & vbCrLf & _
"- **Run All Tests**: `[TEST_ALL_COMMAND]`" & vbCrLf & _
"  - Description: [TEST_ALL_DESCRIPTION]" & vbCrLf & _
"  - Coverage Report: `[TEST_COVERAGE_COMMAND]`" & vbCrLf & _
"  " & vbCrLf & _
"- **Run Unit Tests**: `[TEST_UNIT_COMMAND]`" & vbCrLf & _
"  - Description: [TEST_UNIT_DESCRIPTION]" & vbCrLf & _
"  " & vbCrLf & _
"- **Run Integration Tests**: `[TEST_INT_COMMAND]`" & vbCrLf & _
"  - Description: [TEST_INT_DESCRIPTION]" & vbCrLf & _
"  " & vbCrLf & _
"- **Run Single Test File**: `[TEST_SINGLE_COMMAND] [TEST_FILE_PATH]`" & vbCrLf & _
"  - Description: [TEST_SINGLE_DESCRIPTION]" & vbCrLf & _
"  " & vbCrLf & _
"- **Watch Mode**: `[TEST_WATCH_COMMAND]`" & vbCrLf & _
"  - Description: Runs tests in watch mode, re-running on file changes" & vbCrLf & vbCrLf & _
"### Linting and Formatting" & vbCrLf & _
"- **Lint Code**: `[LINT_COMMAND]`" & vbCrLf & _
"  - Description: [LINT_DESCRIPTION]" & vbCrLf & _
"  - Ignores: [LINT_IGNORE_PATTERNS]" & vbCrLf & _
"  " & vbCrLf & _
"- **Format Code**: `[FORMAT_COMMAND]`" & vbCrLf & _
"  - Description: [FORMAT_DESCRIPTION]" & vbCrLf & _
"  - Configuration: [FORMAT_CONFIG_FILE]" & vbCrLf & _
"  " & vbCrLf & _
"- **Check Formatting**: `[FORMAT_CHECK_COMMAND]`" & vbCrLf & _
"  - Description: Checks if code matches formatting standards without modifying" & vbCrLf & vbCrLf & _
"### Pre-commit Checks" & vbCrLf & _
"- **Run All Pre-commit Checks**: `[PRECOMMIT_COMMAND]`" & vbCrLf & _
"  - Runs: linting, formatting checks, tests" & vbCrLf & _
"  - Should pass before committing code" & vbCrLf & vbCrLf & _
"---" & vbCrLf & vbCrLf & _
"## 2. High-Level Architecture Guidance" & vbCrLf & vbCrLf & _
"### Architecture Overview" & vbCrLf & _
"[PROJECT_NAME] is a [ARCHITECTURE_TYPE] CLI application built with [TECHNOLOGY_STACK]." & vbCrLf & vbCrLf & _
"**Key Components:**" & vbCrLf & _
"- **Command Handler Layer**: Responsible for parsing CLI arguments and routing to appropriate command handlers" & vbCrLf & _
"- **Core Logic Layer**: Contains business logic, data processing, and utilities" & vbCrLf & _
"- **I/O & External Integration Layer**: Manages file I/O, network requests, external APIs" & vbCrLf & _
"- **Configuration Layer**: Handles configuration file parsing and environment variable management" & vbCrLf & _
"- **Error Handling Layer**: Centralized error handling and user-friendly error messages" & vbCrLf & vbCrLf & _
"### Data Flow" & vbCrLf & _
"[DESCRIBE_DATA_FLOW]" & vbCrLf & vbCrLf & _
"### Key Design Patterns" & vbCrLf & _
"1. **Command Pattern**: Each CLI command is implemented as a separate command object/function" & vbCrLf & _
"2. **Dependency Injection**: [DESCRIBE_INJECTION_PATTERN]" & vbCrLf & _
"3. **Configuration Management**: [DESCRIBE_CONFIG_PATTERN]" & vbCrLf & _
"4. **Error Handling**: [DESCRIBE_ERROR_PATTERN]" & vbCrLf & vbCrLf & _
"### External Dependencies" & vbCrLf & _
"- [DEPENDENCY_1]: Version [VERSION], used for [PURPOSE]" & vbCrLf & _
"- [DEPENDENCY_2]: Version [VERSION], used for [PURPOSE]" & vbCrLf & _
"- [DEPENDENCY_3]: Version [VERSION], used for [PURPOSE]" & vbCrLf & vbCrLf & _
"---" & vbCrLf & vbCrLf & _
"## 3. Code Conventions and Naming Patterns" & vbCrLf & vbCrLf & _
"### File Naming Conventions" & vbCrLf & _
"- **Command Files**: `[COMMAND_PATTERN]` (e.g., `command-name.js`, `command_name.py`)" & vbCrLf & _
"- **Utility Files**: `[UTIL_PATTERN]` (e.g., `util-helpers.js`, `common_utils.py`)" & vbCrLf & _
"- **Test Files**: `[TEST_PATTERN]` (e.g., `command.test.js`, `test_command.py`)" & vbCrLf & _
"- **Configuration Files**: `[CONFIG_PATTERN]` (e.g., `.config.yaml`, `config.json`)" & vbCrLf & vbCrLf & _
"### Function/Method Naming" & vbCrLf & _
"- **Command Handlers**: PascalCase for classes, camelCase for functions" & vbCrLf & _
"  - Format: `handle[CommandName]` or `execute[CommandName]`" & vbCrLf & _
"  - Example: `handleDeployCommand()`, `executeUserCreate()`" & vbCrLf & _
"  " & vbCrLf & _
"- **Utility Functions**: camelCase" & vbCrLf & _
"  - Verbs first: `parseConfig()`, `validateInput()`, `formatOutput()`" & vbCrLf & _
"  " & vbCrLf & _
"- **Private Functions**: Prefix with underscore (if convention applies)" & vbCrLf & _
"  - Format: `_helperFunction()`" & vbCrLf & vbCrLf & _
"### Variable Naming" & vbCrLf & _
"- **CLI Arguments/Flags**: kebab-case (e.g., `--output-dir`, `--verbose`)" & vbCrLf & _
"- **Environment Variables**: UPPER_SNAKE_CASE (e.g., `PROJECT_NAME_CONFIG_PATH`)" & vbCrLf & _
"- **Constants**: UPPER_SNAKE_CASE" & vbCrLf & _
"- **Regular Variables**: camelCase" & vbCrLf & vbCrLf & _
"### Code Style Rules" & vbCrLf & _
"- **Indentation**: [INDENTATION_SIZE] spaces (tabs/spaces)" & vbCrLf & _
"- **Line Length**: Maximum [LINE_LENGTH] characters" & vbCrLf & _
"- **Quotes**: [SINGLE/DOUBLE] quotes for strings" & vbCrLf & _
"- **Semicolons**: [REQUIRED/OPTIONAL]" & vbCrLf & _
"- **Trailing Commas**: [RULE]" & vbCrLf & _
"- **Comment Style**: Use `//` for inline, `/* */` for blocks" & vbCrLf & _
"  - JSDoc/Docstring format: [DESCRIBE_DOC_FORMAT]" & vbCrLf & vbCrLf & _
"### Error Messages" & vbCrLf & _
"- Format: Clear, concise, actionable" & vbCrLf & _
"- Structure: `[ERROR_TYPE]: [DESCRIPTION]. [SUGGESTION]`" & vbCrLf & _
"- Example: `Configuration Error: Missing required field 'api_key'. Please check your config file.`" & vbCrLf & _
"- Avoid: Technical jargon, stack traces in user-facing messages" & vbCrLf & vbCrLf & _
"### Logging Convention" & vbCrLf & _
"- **Log Levels**: ERROR, WARN, INFO, DEBUG, TRACE" & vbCrLf & _
"- **Format**: `[LEVEL] [TIMESTAMP] [MODULE] - [MESSAGE]`" & vbCrLf & _
"- **Debug Info**: Include context for DEBUG level logs" & vbCrLf & vbCrLf & _
"---" & vbCrLf & vbCrLf & _
"## 4. Project Structure Guidance" & vbCrLf & vbCrLf & _
"**Last Updated**: [DATE]" & vbCrLf & _
"**Project Version**: [VERSION]"

' Create the file
Dim filePath
filePath = ".github\copilot-instructions.md"

' Delete if exists
If fso.FileExists(filePath) Then
    fso.DeleteFile filePath
End If

' Create the file
Dim objFile
Set objFile = fso.CreateTextFile(filePath, True, True)
objFile.Write content
objFile.Close

WScript.Echo "✓ File created: " & filePath

' Verify the file
If fso.FileExists(filePath) Then
    Set file = fso.GetFile(filePath)
    WScript.Echo "✓ File successfully created at: C:\Users\cheta\rajasthan-helper\.github\copilot-instructions.md"
    WScript.Echo "  File size: " & file.Size & " bytes"
    WScript.Echo ""
    WScript.Echo "✓ TASK COMPLETED SUCCESSFULLY"
Else
    WScript.Echo "✗ File not found after creation"
End If

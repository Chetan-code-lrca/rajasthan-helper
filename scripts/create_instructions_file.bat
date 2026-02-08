@echo off
setlocal EnableDelayedExpansion

cd /d C:\Users\cheta\rajasthan-helper

REM Create .github directory if it doesn't exist
if not exist .github mkdir .github
echo ✓ .github directory created/verified

REM Create the copilot-instructions.md file with content
(
echo # Copilot Instructions - [PROJECT_NAME] CLI
echo.
echo This document provides comprehensive guidance for GitHub Copilot when working on the [PROJECT_NAME] CLI project. It covers project structure, conventions, architecture patterns, and common development workflows.
echo.
echo ---
echo.
echo ## 1. Build, Test, and Lint Commands
echo.
echo ### Build Commands
echo - **Development Build**: `[BUILD_DEV_COMMAND]`
echo   - Description: [BUILD_DEV_DESCRIPTION]
echo   - Output: [BUILD_DEV_OUTPUT_LOCATION]
echo   
echo - **Production Build**: `[BUILD_PROD_COMMAND]`
echo   - Description: [BUILD_PROD_DESCRIPTION]
echo   - Output: [BUILD_PROD_OUTPUT_LOCATION]
echo   
echo - **Clean Build**: `[CLEAN_BUILD_COMMAND]`
echo   - Description: Removes all build artifacts and rebuilds from scratch
echo.
echo ### Test Commands
echo - **Run All Tests**: `[TEST_ALL_COMMAND]`
echo   - Description: [TEST_ALL_DESCRIPTION]
echo   - Coverage Report: `[TEST_COVERAGE_COMMAND]`
echo   
echo - **Run Unit Tests**: `[TEST_UNIT_COMMAND]`
echo   - Description: [TEST_UNIT_DESCRIPTION]
echo   
echo - **Run Integration Tests**: `[TEST_INT_COMMAND]`
echo   - Description: [TEST_INT_DESCRIPTION]
echo   
echo - **Run Single Test File**: `[TEST_SINGLE_COMMAND] [TEST_FILE_PATH]`
echo   - Description: [TEST_SINGLE_DESCRIPTION]
echo   
echo - **Watch Mode**: `[TEST_WATCH_COMMAND]`
echo   - Description: Runs tests in watch mode, re-running on file changes
echo.
echo ### Linting and Formatting
echo - **Lint Code**: `[LINT_COMMAND]`
echo   - Description: [LINT_DESCRIPTION]
echo   - Ignores: [LINT_IGNORE_PATTERNS]
echo   
echo - **Format Code**: `[FORMAT_COMMAND]`
echo   - Description: [FORMAT_DESCRIPTION]
echo   - Configuration: [FORMAT_CONFIG_FILE]
echo   
echo - **Check Formatting**: `[FORMAT_CHECK_COMMAND]`
echo   - Description: Checks if code matches formatting standards without modifying
echo.
echo ### Pre-commit Checks
echo - **Run All Pre-commit Checks**: `[PRECOMMIT_COMMAND]`
echo   - Runs: linting, formatting checks, tests
echo   - Should pass before committing code
echo.
echo ---
echo.
echo ## 2. High-Level Architecture Guidance
echo.
echo ### Architecture Overview
echo [PROJECT_NAME] is a [ARCHITECTURE_TYPE] CLI application built with [TECHNOLOGY_STACK].
echo.
echo **Key Components:**
echo - **Command Handler Layer**: Responsible for parsing CLI arguments and routing to appropriate command handlers
echo - **Core Logic Layer**: Contains business logic, data processing, and utilities
echo - **I/O ^& External Integration Layer**: Manages file I/O, network requests, external APIs
echo - **Configuration Layer**: Handles configuration file parsing and environment variable management
echo - **Error Handling Layer**: Centralized error handling and user-friendly error messages
echo.
echo ### Data Flow
echo [DESCRIBE_DATA_FLOW]
echo.
echo ### Key Design Patterns
echo 1. **Command Pattern**: Each CLI command is implemented as a separate command object/function
echo 2. **Dependency Injection**: [DESCRIBE_INJECTION_PATTERN]
echo 3. **Configuration Management**: [DESCRIBE_CONFIG_PATTERN]
echo 4. **Error Handling**: [DESCRIBE_ERROR_PATTERN]
echo.
echo ### External Dependencies
echo - [DEPENDENCY_1]: Version [VERSION], used for [PURPOSE]
echo - [DEPENDENCY_2]: Version [VERSION], used for [PURPOSE]
echo - [DEPENDENCY_3]: Version [VERSION], used for [PURPOSE]
echo.
echo ---
echo.
echo ## 3. Code Conventions and Naming Patterns
echo.
echo ### File Naming Conventions
echo - **Command Files**: `[COMMAND_PATTERN]` (e.g., `command-name.js`, `command_name.py`)
echo - **Utility Files**: `[UTIL_PATTERN]` (e.g., `util-helpers.js`, `common_utils.py`)
echo - **Test Files**: `[TEST_PATTERN]` (e.g., `command.test.js`, `test_command.py`)
echo - **Configuration Files**: `[CONFIG_PATTERN]` (e.g., `.config.yaml`, `config.json`)
echo.
echo ### Function/Method Naming
echo - **Command Handlers**: PascalCase for classes, camelCase for functions
echo   - Format: `handle[CommandName]` or `execute[CommandName]`
echo   - Example: `handleDeployCommand()`, `executeUserCreate()`
echo   
echo - **Utility Functions**: camelCase
echo   - Verbs first: `parseConfig()`, `validateInput()`, `formatOutput()`
echo   
echo - **Private Functions**: Prefix with underscore (if convention applies)
echo   - Format: `_helperFunction()`
echo.
echo ### Variable Naming
echo - **CLI Arguments/Flags**: kebab-case (e.g., `--output-dir`, `--verbose`)
echo - **Environment Variables**: UPPER_SNAKE_CASE (e.g., `PROJECT_NAME_CONFIG_PATH`)
echo - **Constants**: UPPER_SNAKE_CASE
echo - **Regular Variables**: camelCase
echo.
echo ### Code Style Rules
echo - **Indentation**: [INDENTATION_SIZE] spaces (tabs/spaces)
echo - **Line Length**: Maximum [LINE_LENGTH] characters
echo - **Quotes**: [SINGLE/DOUBLE] quotes for strings
echo - **Semicolons**: [REQUIRED/OPTIONAL]
echo - **Trailing Commas**: [RULE]
echo - **Comment Style**: Use `//` for inline, `/* */` for blocks
echo   - JSDoc/Docstring format: [DESCRIBE_DOC_FORMAT]
echo.
echo ### Error Messages
echo - Format: Clear, concise, actionable
echo - Structure: `[ERROR_TYPE]: [DESCRIPTION]. [SUGGESTION]`
echo - Example: `Configuration Error: Missing required field 'api_key'. Please check your config file.`
echo - Avoid: Technical jargon, stack traces in user-facing messages
echo.
echo ### Logging Convention
echo - **Log Levels**: ERROR, WARN, INFO, DEBUG, TRACE
echo - **Format**: `[LEVEL] [TIMESTAMP] [MODULE] - [MESSAGE]`
echo - **Debug Info**: Include context for DEBUG level logs
echo.
echo ---
echo.
echo ## 4. Project Structure Guidance
echo.
echo ### Recommended Directory Layout
echo ```
echo [PROJECT_NAME]/
echo ^|-- .github/
echo ^|   ^`-- copilot-instructions.md      # This file
echo ^|-- src/
echo ^|   ^|-- commands/                     # CLI command implementations
echo ^|   ^|   ^|-- index.ts                  # Command registry/exports
echo ^|   ^|   ^|-- deploy.ts                 # Example: deploy command
echo ^|   ^|   ^|-- config.ts                 # Example: config command
echo ^|   ^|   ^`-- [other-commands].ts
echo ^|   ^|
echo ^|   ^|-- core/                         # Core business logic
echo ^|   ^|   ^|-- index.ts
echo ^|   ^|   ^|-- processor.ts              # Main processing logic
echo ^|   ^|   ^|-- validator.ts              # Input validation
echo ^|   ^|   ^`-- [domain-logic].ts
echo ^|   ^|
echo ^|   ^|-- config/                       # Configuration management
echo ^|   ^|   ^|-- index.ts
echo ^|   ^|   ^|-- loader.ts                 # Load config from files
echo ^|   ^|   ^|-- schema.ts                 # Config validation schema
echo ^|   ^|   ^`-- defaults.ts               # Default configurations
echo ^|   ^|
echo ^|   ^|-- utils/                        # Utility functions
echo ^|   ^|   ^|-- index.ts
echo ^|   ^|   ^|-- logger.ts                 # Logging utilities
echo ^|   ^|   ^|-- file-system.ts            # File I/O helpers
echo ^|   ^|   ^|-- parser.ts                 # Parsing utilities
echo ^|   ^|   ^`-- [other-utils].ts
echo ^|   ^|
echo ^|   ^|-- types/                        # Type definitions (if TypeScript)
echo ^|   ^|   ^|-- index.ts
echo ^|   ^|   ^|-- command.ts                # Command interface
echo ^|   ^|   ^|-- config.ts                 # Configuration types
echo ^|   ^|   ^`-- [domain-types].ts
echo ^|   ^|
echo ^|   ^`-- index.ts                      # Main entry point
echo ^|
echo ^|-- tests/                            # Test files
echo ^|   ^|-- unit/                         # Unit tests
echo ^|   ^|   ^|-- commands/
echo ^|   ^|   ^|-- core/
echo ^|   ^|   ^`-- utils/
echo ^|   ^|
echo ^|   ^|-- integration/                  # Integration tests
echo ^|   ^|   ^|-- end-to-end.test.ts
echo ^|   ^|   ^`-- [integration-tests].ts
echo ^|   ^|
echo ^|   ^`-- fixtures/                     # Test data and fixtures
echo ^|       ^|-- config-samples/
echo ^|       ^`-- mock-data/
echo ^|
echo ^|-- docs/                             # Documentation
echo ^|   ^|-- README.md                     # User guide
echo ^|   ^|-- DEVELOPMENT.md                # Development setup
echo ^|   ^|-- API.md                        # Command reference
echo ^|   ^`-- [guides].md
echo ^|
echo ^|-- examples/                         # Example configurations and usage
echo ^|   ^|-- basic-config.yaml
echo ^|   ^`-- [example-files]
echo ^|
echo ^|-- .gitignore
echo ^|-- package.json                      # (for Node.js projects)
echo ^|-- tsconfig.json                     # (for TypeScript projects)
echo ^|-- jest.config.js                    # (or equivalent test config)
echo ^|-- [LINTER_CONFIG]                   # (eslint, pylint, etc.)
echo ^|-- [FORMAT_CONFIG]                   # (prettier, black, etc.)
echo ^`-- [LOCK_FILE]                       # (package-lock.json, requirements.txt, etc.)
echo ```
echo.
echo ### Module Responsibilities
echo.
echo #### `commands/`
echo - Each file implements one or more related CLI commands
echo - Exports command object/class with name, description, and handler function
echo - Delegates business logic to core modules
echo - Responsible for argument parsing and formatting output
echo.
echo #### `core/`
echo - Contains pure business logic independent of CLI
echo - No direct file I/O or CLI-specific code
echo - Highly testable, reusable logic
echo - Handles data processing and transformations
echo.
echo #### `config/`
echo - Loads and parses configuration from files and environment
echo - Validates configuration against schema
echo - Provides typed access to configuration values
echo - Handles configuration precedence (CLI args ^> env vars ^> config file ^> defaults)
echo.
echo #### `utils/`
echo - Helper functions used across modules
echo - Logger, file system utilities, parsers
echo - Keep focused and single-purpose
echo - Commonly imported across codebase
echo.
echo #### `types/` (TypeScript)
echo - Type definitions and interfaces
echo - Shared types between modules
echo - Domain-specific types
echo - Command-related types and callbacks
echo.
echo ### File Size Guidelines
echo - **Command files**: 150-300 lines maximum
echo - **Utility files**: 100-200 lines per function
echo - **Longer files**: Consider splitting into smaller modules
echo - Break down complex logic into separate helper functions
echo.
echo ---
echo.
echo ## 5. Common Workflows for CLI Development
echo.
echo ### Adding a New Command
echo.
echo 1. **Create Command File** (`src/commands/new-command.ts`)
echo    ```typescript
echo    // [TEMPLATE_PROVIDED]
echo    export const [CommandName]Command = {
echo      name: '[command-name]',
echo      description: '[Command description]',
echo      options: [
echo        // Define command-specific flags/options
echo      ],
echo      handler: async (args, options) =^> {
echo        // Implement command logic
echo      }
echo    };
echo    ```
echo.
echo 2. **Register Command** in `src/commands/index.ts`
echo    - Add export to command registry
echo    - Register with main command dispatcher
echo.
echo 3. **Create Tests** in `tests/unit/commands/new-command.test.ts`
echo    - Test successful execution
echo    - Test error scenarios
echo    - Test with various argument combinations
echo.
echo 4. **Update Documentation** in `docs/API.md`
echo    - Document command syntax
echo    - Provide usage examples
echo    - List all available options
echo.
echo 5. **Test Manually**
echo    ```bash
echo    [BUILD_DEV_COMMAND]
echo    npm run dev -- [new-command] --help
echo    npm run dev -- [new-command] [test-args]
echo    ```
echo.
echo ### Handling Configuration
echo.
echo 1. **Define Configuration Schema** in `src/config/schema.ts`
echo    - Specify required/optional fields
echo    - Provide default values
echo    - Define validation rules
echo.
echo 2. **Add Config Loader Logic** in `src/config/loader.ts`
echo    - Load from config file (YAML/JSON)
echo    - Merge environment variable overrides
echo    - Apply defaults
echo.
echo 3. **Access Configuration** in Commands
echo    - Use injected config object
echo    - Type-safe access: `config.section.field`
echo    - Validate before use
echo.
echo 4. **Testing Configuration Loading**
echo    ```bash
echo    [TEST_UNIT_COMMAND] -- config
echo    ```
echo.
echo ### Debugging Guide
echo.
echo #### Enable Debug Logging
echo ```bash
echo DEBUG=[PROJECT_NAME]:* npm run dev -- [command]
echo ```
echo.
echo #### Common Debugging Patterns
echo 1. **Check Configuration**
echo    ```bash
echo    npm run dev -- config --show    # Display loaded config
echo    npm run dev -- config --validate # Validate config
echo    ```
echo.
echo 2. **Verbose Output**
echo    ```bash
echo    npm run dev -- [command] --verbose  # Enable verbose logging
echo    npm run dev -- [command] --debug    # Enable debug logging
echo    ```
echo.
echo 3. **Test Specific Scenarios**
echo    ```bash
echo    [TEST_SINGLE_COMMAND] tests/unit/commands/[command].test.ts
echo    [TEST_WATCH_COMMAND] -- --testNamePattern="should handle error"
echo    ```
echo.
echo #### Debugging Steps
echo 1. Identify issue: Read error message and stack trace
echo 2. Add console logs or use debugger at suspected location
echo 3. Run with verbose/debug flags
echo 4. Create minimal test case to reproduce
echo 5. Inspect data at each step using logs or debugger
echo.
echo ### Error Handling Best Practices
echo.
echo 1. **Catch Errors Early**
echo    - Validate input at command entry point
echo    - Check configuration validity
echo    - Verify file/resource existence
echo.
echo 2. **Provide Clear Error Messages**
echo    - Explain what went wrong
echo    - Suggest how to fix it
echo    - Include relevant context (file path, config section, etc.)
echo.
echo 3. **Use Error Classes** (if applicable)
echo    ```typescript
echo    class [ProjectName]Error extends Error {
echo      constructor(message, code, context) { }
echo    }
echo    ```
echo.
echo 4. **Error Recovery**
echo    - Attempt recovery when possible
echo    - Provide rollback options
echo    - Log detailed errors for debugging
echo.
echo ### Testing Workflows
echo.
echo #### Unit Testing
echo ```bash
echo # Test specific module
echo [TEST_UNIT_COMMAND] -- src/core/processor.test.ts
echo.
echo # Test with coverage
echo [TEST_COVERAGE_COMMAND]
echo ```
echo.
echo #### Integration Testing
echo ```bash
echo # Run integration tests
echo [TEST_INT_COMMAND]
echo.
echo # Test full command flow
echo [TEST_SINGLE_COMMAND] tests/integration/end-to-end.test.ts
echo ```
echo.
echo #### Test-Driven Development
echo 1. Write test case first
echo 2. Run test (should fail)
echo 3. Implement functionality
echo 4. Run test (should pass)
echo 5. Refactor and clean up
echo 6. Run full test suite to ensure no regressions
echo.
echo ### Code Review Checklist
echo.
echo Before submitting changes, verify:
echo - [ ] Code follows naming conventions and style guide
echo - [ ] All tests pass: `[TEST_ALL_COMMAND]`
echo - [ ] Code is properly formatted: `[FORMAT_COMMAND]`
echo - [ ] No linting errors: `[LINT_COMMAND]`
echo - [ ] Error messages are user-friendly
echo - [ ] New commands are documented
echo - [ ] Configuration changes are handled correctly
echo - [ ] No sensitive data in logs or error messages
echo - [ ] Performance impact is acceptable
echo - [ ] Backward compatibility maintained (if applicable)
echo.
echo ### Performance Optimization
echo.
echo 1. **Identify Bottlenecks**
echo    - Use built-in profiling: `npm run profile -- [command]`
echo    - Measure execution time: `time npm run dev -- [command]`
echo    - Profile memory usage: `[PROFILE_COMMAND]`
echo.
echo 2. **Common Optimization Areas**
echo    - Lazy load heavy dependencies
echo    - Cache computed values
echo    - Batch file I/O operations
echo    - Optimize data structures for lookups
echo.
echo 3. **Testing Performance**
echo    ```bash
echo    # Benchmark command execution
echo    [BENCHMARK_COMMAND]
echo    ```
echo.
echo ### Versioning and Release Process
echo.
echo 1. **Version Updates**
echo    - Update version in `package.json`: `[VERSION_FORMAT]`
echo    - Update `CHANGELOG.md` with changes
echo    - Tag release: `git tag v[VERSION]`
echo.
echo 2. **Testing Before Release**
echo    ```bash
echo    [TEST_ALL_COMMAND]
echo    [LINT_COMMAND]
echo    [BUILD_PROD_COMMAND]
echo    ```
echo.
echo 3. **Release Checklist**
echo    - [ ] All tests pass
echo    - [ ] Documentation is updated
echo    - [ ] Version number is incremented
echo    - [ ] Changelog is updated
echo    - [ ] Build succeeds
echo    - [ ] Tag created
echo.
echo ---
echo.
echo ## Additional Resources
echo.
echo - **Project Repository**: [REPOSITORY_URL]
echo - **Issue Tracker**: [ISSUES_URL]
echo - **Documentation**: [DOCS_URL]
echo - **Contributing Guide**: [CONTRIBUTING_GUIDE_URL]
echo - **Code of Conduct**: [CONDUCT_URL]
echo.
echo ## Environment Setup
echo.
echo ### Required Tools
echo - [TOOL_1]: Version [MIN_VERSION] or higher
echo - [TOOL_2]: Version [MIN_VERSION] or higher
echo - [TOOL_3]: Version [MIN_VERSION] or higher
echo.
echo ### Installation Steps
echo 1. [STEP_1]
echo 2. [STEP_2]
echo 3. [STEP_3]
echo.
echo ### Verification
echo Run `[VERIFY_SETUP_COMMAND]` to verify environment setup is correct.
echo.
echo ---
echo.
echo ## Notes for Copilot
echo.
echo When working with this project, prioritize:
echo 1. Following the project structure and naming conventions
echo 2. Writing tests alongside implementation
echo 3. Maintaining clear, user-friendly error messages
echo 4. Using dependency injection and avoiding hardcoded values
echo 5. Documenting complex logic with comments
echo 6. Ensuring backward compatibility
echo 7. Running pre-commit checks before suggesting commits
echo.
echo ---
echo.
echo **Last Updated**: [DATE]
echo **Project Version**: [VERSION]
) > .github\copilot-instructions.md

echo.
echo ✓ File created: C:\Users\cheta\rajasthan-helper\.github\copilot-instructions.md

REM Verify the file was created
if exist .github\copilot-instructions.md (
    echo ✓ File successfully created
    for %%F in (.github\copilot-instructions.md) do (
        echo   File size: %%~zF bytes
    )
    echo.
    echo ✓ TASK COMPLETED SUCCESSFULLY
    echo   File Path: C:\Users\cheta\rajasthan-helper\.github\copilot-instructions.md
) else (
    echo ✗ Error: File was not created
)

endlocal

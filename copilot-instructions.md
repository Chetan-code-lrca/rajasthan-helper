# Copilot Instructions - [PROJECT_NAME] CLI

This document provides comprehensive guidance for GitHub Copilot when working on the [PROJECT_NAME] CLI project. It covers project structure, conventions, architecture patterns, and common development workflows.

---

## 1. Build, Test, and Lint Commands

### Build Commands
- **Development Build**: `[BUILD_DEV_COMMAND]`
  - Description: [BUILD_DEV_DESCRIPTION]
  - Output: [BUILD_DEV_OUTPUT_LOCATION]
  
- **Production Build**: `[BUILD_PROD_COMMAND]`
  - Description: [BUILD_PROD_DESCRIPTION]
  - Output: [BUILD_PROD_OUTPUT_LOCATION]
  
- **Clean Build**: `[CLEAN_BUILD_COMMAND]`
  - Description: Removes all build artifacts and rebuilds from scratch

### Test Commands
- **Run All Tests**: `[TEST_ALL_COMMAND]`
  - Description: [TEST_ALL_DESCRIPTION]
  - Coverage Report: `[TEST_COVERAGE_COMMAND]`
  
- **Run Unit Tests**: `[TEST_UNIT_COMMAND]`
  - Description: [TEST_UNIT_DESCRIPTION]
  
- **Run Integration Tests**: `[TEST_INT_COMMAND]`
  - Description: [TEST_INT_DESCRIPTION]
  
- **Run Single Test File**: `[TEST_SINGLE_COMMAND] [TEST_FILE_PATH]`
  - Description: [TEST_SINGLE_DESCRIPTION]
  
- **Watch Mode**: `[TEST_WATCH_COMMAND]`
  - Description: Runs tests in watch mode, re-running on file changes

### Linting and Formatting
- **Lint Code**: `[LINT_COMMAND]`
  - Description: [LINT_DESCRIPTION]
  - Ignores: [LINT_IGNORE_PATTERNS]
  
- **Format Code**: `[FORMAT_COMMAND]`
  - Description: [FORMAT_DESCRIPTION]
  - Configuration: [FORMAT_CONFIG_FILE]
  
- **Check Formatting**: `[FORMAT_CHECK_COMMAND]`
  - Description: Checks if code matches formatting standards without modifying

### Pre-commit Checks
- **Run All Pre-commit Checks**: `[PRECOMMIT_COMMAND]`
  - Runs: linting, formatting checks, tests
  - Should pass before committing code

---

## 2. High-Level Architecture Guidance

### Architecture Overview
[PROJECT_NAME] is a [ARCHITECTURE_TYPE] CLI application built with [TECHNOLOGY_STACK].

**Key Components:**
- **Command Handler Layer**: Responsible for parsing CLI arguments and routing to appropriate command handlers
- **Core Logic Layer**: Contains business logic, data processing, and utilities
- **I/O & External Integration Layer**: Manages file I/O, network requests, external APIs
- **Configuration Layer**: Handles configuration file parsing and environment variable management
- **Error Handling Layer**: Centralized error handling and user-friendly error messages

### Data Flow
[DESCRIBE_DATA_FLOW]

### Key Design Patterns
1. **Command Pattern**: Each CLI command is implemented as a separate command object/function
2. **Dependency Injection**: [DESCRIBE_INJECTION_PATTERN]
3. **Configuration Management**: [DESCRIBE_CONFIG_PATTERN]
4. **Error Handling**: [DESCRIBE_ERROR_PATTERN]

### External Dependencies
- [DEPENDENCY_1]: Version [VERSION], used for [PURPOSE]
- [DEPENDENCY_2]: Version [VERSION], used for [PURPOSE]
- [DEPENDENCY_3]: Version [VERSION], used for [PURPOSE]

---

## 3. Code Conventions and Naming Patterns

### File Naming Conventions
- **Command Files**: `[COMMAND_PATTERN]` (e.g., `command-name.js`, `command_name.py`)
- **Utility Files**: `[UTIL_PATTERN]` (e.g., `util-helpers.js`, `common_utils.py`)
- **Test Files**: `[TEST_PATTERN]` (e.g., `command.test.js`, `test_command.py`)
- **Configuration Files**: `[CONFIG_PATTERN]` (e.g., `.config.yaml`, `config.json`)

### Function/Method Naming
- **Command Handlers**: PascalCase for classes, camelCase for functions
  - Format: `handle[CommandName]` or `execute[CommandName]`
  - Example: `handleDeployCommand()`, `executeUserCreate()`
  
- **Utility Functions**: camelCase
  - Verbs first: `parseConfig()`, `validateInput()`, `formatOutput()`
  
- **Private Functions**: Prefix with underscore (if convention applies)
  - Format: `_helperFunction()`

### Variable Naming
- **CLI Arguments/Flags**: kebab-case (e.g., `--output-dir`, `--verbose`)
- **Environment Variables**: UPPER_SNAKE_CASE (e.g., `PROJECT_NAME_CONFIG_PATH`)
- **Constants**: UPPER_SNAKE_CASE
- **Regular Variables**: camelCase

### Code Style Rules
- **Indentation**: [INDENTATION_SIZE] spaces (tabs/spaces)
- **Line Length**: Maximum [LINE_LENGTH] characters
- **Quotes**: [SINGLE/DOUBLE] quotes for strings
- **Semicolons**: [REQUIRED/OPTIONAL]
- **Trailing Commas**: [RULE]
- **Comment Style**: Use `//` for inline, `/* */` for blocks
  - JSDoc/Docstring format: [DESCRIBE_DOC_FORMAT]

### Error Messages
- Format: Clear, concise, actionable
- Structure: `[ERROR_TYPE]: [DESCRIPTION]. [SUGGESTION]`
- Example: `Configuration Error: Missing required field 'api_key'. Please check your config file.`
- Avoid: Technical jargon, stack traces in user-facing messages

### Logging Convention
- **Log Levels**: ERROR, WARN, INFO, DEBUG, TRACE
- **Format**: `[LEVEL] [TIMESTAMP] [MODULE] - [MESSAGE]`
- **Debug Info**: Include context for DEBUG level logs

---

## 4. Project Structure Guidance

### Recommended Directory Layout
```
[PROJECT_NAME]/
├── .github/
│   └── copilot-instructions.md      # This file
├── src/
│   ├── commands/                     # CLI command implementations
│   │   ├── index.ts                  # Command registry/exports
│   │   ├── deploy.ts                 # Example: deploy command
│   │   ├── config.ts                 # Example: config command
│   │   └── [other-commands].ts
│   │
│   ├── core/                         # Core business logic
│   │   ├── index.ts
│   │   ├── processor.ts              # Main processing logic
│   │   ├── validator.ts              # Input validation
│   │   └── [domain-logic].ts
│   │
│   ├── config/                       # Configuration management
│   │   ├── index.ts
│   │   ├── loader.ts                 # Load config from files
│   │   ├── schema.ts                 # Config validation schema
│   │   └── defaults.ts               # Default configurations
│   │
│   ├── utils/                        # Utility functions
│   │   ├── index.ts
│   │   ├── logger.ts                 # Logging utilities
│   │   ├── file-system.ts            # File I/O helpers
│   │   ├── parser.ts                 # Parsing utilities
│   │   └── [other-utils].ts
│   │
│   ├── types/                        # Type definitions (if TypeScript)
│   │   ├── index.ts
│   │   ├── command.ts                # Command interface
│   │   ├── config.ts                 # Configuration types
│   │   └── [domain-types].ts
│   │
│   └── index.ts                      # Main entry point
│
├── tests/                            # Test files
│   ├── unit/                         # Unit tests
│   │   ├── commands/
│   │   ├── core/
│   │   └── utils/
│   │
│   ├── integration/                  # Integration tests
│   │   ├── end-to-end.test.ts
│   │   └── [integration-tests].ts
│   │
│   └── fixtures/                     # Test data and fixtures
│       ├── config-samples/
│       └── mock-data/
│
├── docs/                             # Documentation
│   ├── README.md                     # User guide
│   ├── DEVELOPMENT.md                # Development setup
│   ├── API.md                        # Command reference
│   └── [guides].md
│
├── examples/                         # Example configurations and usage
│   ├── basic-config.yaml
│   └── [example-files]
│
├── .gitignore
├── package.json                      # (for Node.js projects)
├── tsconfig.json                     # (for TypeScript projects)
├── jest.config.js                    # (or equivalent test config)
├── [LINTER_CONFIG]                   # (eslint, pylint, etc.)
├── [FORMAT_CONFIG]                   # (prettier, black, etc.)
└── [LOCK_FILE]                       # (package-lock.json, requirements.txt, etc.)
```

### Module Responsibilities

#### `commands/`
- Each file implements one or more related CLI commands
- Exports command object/class with name, description, and handler function
- Delegates business logic to core modules
- Responsible for argument parsing and formatting output

#### `core/`
- Contains pure business logic independent of CLI
- No direct file I/O or CLI-specific code
- Highly testable, reusable logic
- Handles data processing and transformations

#### `config/`
- Loads and parses configuration from files and environment
- Validates configuration against schema
- Provides typed access to configuration values
- Handles configuration precedence (CLI args > env vars > config file > defaults)

#### `utils/`
- Helper functions used across modules
- Logger, file system utilities, parsers
- Keep focused and single-purpose
- Commonly imported across codebase

#### `types/` (TypeScript)
- Type definitions and interfaces
- Shared types between modules
- Domain-specific types
- Command-related types and callbacks

### File Size Guidelines
- **Command files**: 150-300 lines maximum
- **Utility files**: 100-200 lines per function
- **Longer files**: Consider splitting into smaller modules
- Break down complex logic into separate helper functions

---

## 5. Common Workflows for CLI Development

### Adding a New Command

1. **Create Command File** (`src/commands/new-command.ts`)
   ```typescript
   // [TEMPLATE_PROVIDED]
   export const [CommandName]Command = {
     name: '[command-name]',
     description: '[Command description]',
     options: [
       // Define command-specific flags/options
     ],
     handler: async (args, options) => {
       // Implement command logic
     }
   };
   ```

2. **Register Command** in `src/commands/index.ts`
   - Add export to command registry
   - Register with main command dispatcher

3. **Create Tests** in `tests/unit/commands/new-command.test.ts`
   - Test successful execution
   - Test error scenarios
   - Test with various argument combinations

4. **Update Documentation** in `docs/API.md`
   - Document command syntax
   - Provide usage examples
   - List all available options

5. **Test Manually**
   ```bash
   [BUILD_DEV_COMMAND]
   npm run dev -- [new-command] --help
   npm run dev -- [new-command] [test-args]
   ```

### Handling Configuration

1. **Define Configuration Schema** in `src/config/schema.ts`
   - Specify required/optional fields
   - Provide default values
   - Define validation rules

2. **Add Config Loader Logic** in `src/config/loader.ts`
   - Load from config file (YAML/JSON)
   - Merge environment variable overrides
   - Apply defaults

3. **Access Configuration** in Commands
   - Use injected config object
   - Type-safe access: `config.section.field`
   - Validate before use

4. **Testing Configuration Loading**
   ```bash
   [TEST_UNIT_COMMAND] -- config
   ```

### Debugging Guide

#### Enable Debug Logging
```bash
DEBUG=[PROJECT_NAME]:* npm run dev -- [command]
```

#### Common Debugging Patterns
1. **Check Configuration**
   ```bash
   npm run dev -- config --show    # Display loaded config
   npm run dev -- config --validate # Validate config
   ```

2. **Verbose Output**
   ```bash
   npm run dev -- [command] --verbose  # Enable verbose logging
   npm run dev -- [command] --debug    # Enable debug logging
   ```

3. **Test Specific Scenarios**
   ```bash
   [TEST_SINGLE_COMMAND] tests/unit/commands/[command].test.ts
   [TEST_WATCH_COMMAND] -- --testNamePattern="should handle error"
   ```

#### Debugging Steps
1. Identify issue: Read error message and stack trace
2. Add console logs or use debugger at suspected location
3. Run with verbose/debug flags
4. Create minimal test case to reproduce
5. Inspect data at each step using logs or debugger

### Error Handling Best Practices

1. **Catch Errors Early**
   - Validate input at command entry point
   - Check configuration validity
   - Verify file/resource existence

2. **Provide Clear Error Messages**
   - Explain what went wrong
   - Suggest how to fix it
   - Include relevant context (file path, config section, etc.)

3. **Use Error Classes** (if applicable)
   ```typescript
   class [ProjectName]Error extends Error {
     constructor(message, code, context) { }
   }
   ```

4. **Error Recovery**
   - Attempt recovery when possible
   - Provide rollback options
   - Log detailed errors for debugging

### Testing Workflows

#### Unit Testing
```bash
# Test specific module
[TEST_UNIT_COMMAND] -- src/core/processor.test.ts

# Test with coverage
[TEST_COVERAGE_COMMAND]
```

#### Integration Testing
```bash
# Run integration tests
[TEST_INT_COMMAND]

# Test full command flow
[TEST_SINGLE_COMMAND] tests/integration/end-to-end.test.ts
```

#### Test-Driven Development
1. Write test case first
2. Run test (should fail)
3. Implement functionality
4. Run test (should pass)
5. Refactor and clean up
6. Run full test suite to ensure no regressions

### Code Review Checklist

Before submitting changes, verify:
- [ ] Code follows naming conventions and style guide
- [ ] All tests pass: `[TEST_ALL_COMMAND]`
- [ ] Code is properly formatted: `[FORMAT_COMMAND]`
- [ ] No linting errors: `[LINT_COMMAND]`
- [ ] Error messages are user-friendly
- [ ] New commands are documented
- [ ] Configuration changes are handled correctly
- [ ] No sensitive data in logs or error messages
- [ ] Performance impact is acceptable
- [ ] Backward compatibility maintained (if applicable)

### Performance Optimization

1. **Identify Bottlenecks**
   - Use built-in profiling: `npm run profile -- [command]`
   - Measure execution time: `time npm run dev -- [command]`
   - Profile memory usage: `[PROFILE_COMMAND]`

2. **Common Optimization Areas**
   - Lazy load heavy dependencies
   - Cache computed values
   - Batch file I/O operations
   - Optimize data structures for lookups

3. **Testing Performance**
   ```bash
   # Benchmark command execution
   [BENCHMARK_COMMAND]
   ```

### Versioning and Release Process

1. **Version Updates**
   - Update version in `package.json`: `[VERSION_FORMAT]`
   - Update `CHANGELOG.md` with changes
   - Tag release: `git tag v[VERSION]`

2. **Testing Before Release**
   ```bash
   [TEST_ALL_COMMAND]
   [LINT_COMMAND]
   [BUILD_PROD_COMMAND]
   ```

3. **Release Checklist**
   - [ ] All tests pass
   - [ ] Documentation is updated
   - [ ] Version number is incremented
   - [ ] Changelog is updated
   - [ ] Build succeeds
   - [ ] Tag created

---

## Additional Resources

- **Project Repository**: [REPOSITORY_URL]
- **Issue Tracker**: [ISSUES_URL]
- **Documentation**: [DOCS_URL]
- **Contributing Guide**: [CONTRIBUTING_GUIDE_URL]
- **Code of Conduct**: [CONDUCT_URL]

## Environment Setup

### Required Tools
- [TOOL_1]: Version [MIN_VERSION] or higher
- [TOOL_2]: Version [MIN_VERSION] or higher
- [TOOL_3]: Version [MIN_VERSION] or higher

### Installation Steps
1. [STEP_1]
2. [STEP_2]
3. [STEP_3]

### Verification
Run `[VERIFY_SETUP_COMMAND]` to verify environment setup is correct.

---

## Notes for Copilot

When working with this project, prioritize:
1. Following the project structure and naming conventions
2. Writing tests alongside implementation
3. Maintaining clear, user-friendly error messages
4. Using dependency injection and avoiding hardcoded values
5. Documenting complex logic with comments
6. Ensuring backward compatibility
7. Running pre-commit checks before suggesting commits

---

**Last Updated**: [DATE]
**Project Version**: [VERSION]

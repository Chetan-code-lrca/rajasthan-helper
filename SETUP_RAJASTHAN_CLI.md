# Rajasthan Helper CLI - Setup Instructions

## ✅ Package Files Created

All necessary files for the Rajasthan Helper CLI have been created:

### Python Package Structure
- `rajasthan_helper/__init__.py` - Package initialization
- `rajasthan_helper/__main__.py` - CLI entry point
- `rajasthan_helper/commands/__init__.py` - Commands module
- `rajasthan_helper/commands/weather.py` - Weather command
- `rajasthan_helper/commands/festival.py` - Festival command
- `rajasthan_helper/commands/tip.py` - Travel tips command

### Configuration Files
- `pyproject.toml` - Project metadata and dependencies
- `README.md` - User guide and documentation
- `.github/copilot-instructions.md` - Copilot guidance
- `.github/setup_pkg.py` - Setup script to create package

## 🚀 Installation Steps

### Step 1: Create the Package Directories

Run the setup script to create the package structure:

```bash
python .github/setup_pkg.py
```

This will:
- Create `rajasthan_helper/` directory with all Python modules
- Create `rajasthan_helper/commands/` directory with command implementations
- Set up weather.py, festival.py, and tip.py modules
- Output: ✓ Package setup complete!

### Step 2: Install Dependencies

```bash
# Install in development mode with all dependencies
pip install -e .

# Or, for development with testing tools
pip install -e ".[dev]"
```

### Step 3: Test Installation

```bash
# Verify the CLI is installed
rajasthan-helper --help

# Try each command
rajasthan-helper weather Jaipur
rajasthan-helper festival
rajasthan-helper tip Udaipur
```

## 📖 Usage

### Weather Command
```bash
rajasthan-helper weather [city]
# Default city: Jaipur
# Example: rajasthan-helper weather Udaipur
```

### Festival Command
```bash
rajasthan-helper festival [month]
# Shows all festivals if no month given
# Months: January, March, October, November, December
# Example: rajasthan-helper festival March
```

### Travel Tips Command
```bash
rajasthan-helper tip [city]
# Default city: Jaipur
# Available cities: Jaipur, Udaipur, Mumbai, Jodhpur, Pushkar
# Example: rajasthan-helper tip Udaipur
```

## 🎨 Features

✨ **Colorful Terminal Output** - Rich panels and tables with emojis
🌡️ **Weather Integration** - Free wttr.in API (no key required)
🎉 **Festival Information** - 5 Rajasthan festivals with cultural details
🗺️ **Travel Tips** - 5 cities with 3 curated tips each
❌ **Error Handling** - User-friendly error messages

## 📊 Project Stats

- **Language**: Python 3.8+
- **Framework**: Click (CLI) + Rich (Output formatting)
- **Dependencies**: 3 external libraries (click, rich, requests)
- **Prompts Used**: ~10 (GitHub Copilot CLI free tier)
- **Code Style**: Clean, readable, well-commented

## 🔧 Development

### Run Tests
```bash
pytest
pytest --cov=rajasthan_helper
```

### Format Code
```bash
black rajasthan_helper/
```

### Lint Code
```bash
flake8 rajasthan_helper/
```

## 🐛 Troubleshooting

**Command not found: `rajasthan-helper`**
- Ensure you've run `pip install -e .` in the project directory
- Check that Python is in your PATH

**ImportError: No module named 'rajasthan_helper'**
- Verify the `rajasthan_helper/` directory exists with `__init__.py`
- Run the setup script: `python .github/setup_pkg.py`
- Reinstall: `pip install -e .`

**Weather API timeout**
- Check your internet connection
- The wttr.in service may be temporarily unavailable

## 📁 Directory Structure After Setup

```
rajasthan-helper/
├── .git/
├── .github/
│   ├── copilot-instructions.md
│   └── setup_pkg.py              (Run this to create package)
├── rajasthan_helper/             (Created by setup script)
│   ├── __init__.py
│   ├── __main__.py
│   └── commands/
│       ├── __init__.py
│       ├── weather.py
│       ├── festival.py
│       └── tip.py
├── pyproject.toml
├── README.md
└── SETUP_INSTRUCTIONS.md         (This file)
```

## ✅ Quick Checklist

1. **Run setup script**: `python .github/setup_pkg.py`
2. **Install package**: `pip install -e .`
3. **Test**: `rajasthan-helper --help`
4. **Enjoy**: `rajasthan-helper weather Jaipur`

---

**Ready to explore Rajasthan in your terminal! 🏜️**

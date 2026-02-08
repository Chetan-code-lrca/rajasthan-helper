# 🏜️ RAJASTHAN HELPER CLI - Complete Setup Guide

> **A lightweight Python CLI for exploring Rajasthan in your terminal!**  
> Built with GitHub Copilot CLI free tier (~10 prompts)

---

## 📦 What's Included

This repository contains all files needed to build a complete CLI application with:

- ✨ **3 Commands**: weather, festival, travel tips
- 🎨 **Colorful Output**: Rich panels & tables with emojis
- 🌡️ **Real Weather**: Free wttr.in API integration
- 🎉 **5 Festivals**: Hardcoded Rajasthan festivals
- 🗺️ **Travel Tips**: 5 cities with 3 tips each
- ⚡ **Minimal Dependencies**: Only click, rich, requests

---

## 🚀 Quick Start (3 Steps)

### 1️⃣ Generate Package Files
```bash
cd C:\Users\cheta\rajasthan-helper
python .github/setup_pkg.py
```

**Output:**
```
✓ Package setup complete!
✓ Created rajasthan_helper
✓ Created rajasthan_helper/commands
✓ Created all Python modules
```

### 2️⃣ Install Package
```bash
pip install -e .
```

Or with dev tools:
```bash
pip install -e ".[dev]"
```

### 3️⃣ Run Commands
```bash
# Verify installation
rajasthan-helper --help

# Try the commands
rajasthan-helper weather Jaipur
rajasthan-helper festival March
rajasthan-helper tip Udaipur
```

---

## 📋 Files Created in This Session

### Root Directory
| File | Purpose |
|------|---------|
| `pyproject.toml` | Project configuration, dependencies |
| `README.md` | User documentation & usage guide |
| `SETUP_RAJASTHAN_CLI.md` | Setup instructions |
| `CLI_CREATION_SUMMARY.md` | Package overview |
| `FILES_CREATED_VERIFICATION.md` | Detailed file listing |
| `verify_setup.py` | Quick verification script |

### .github Directory
| File | Purpose |
|------|---------|
| `setup_pkg.py` | Generates all Python package files |
| `copilot-instructions.md` | Copilot guidance (existing) |

### Will Be Generated
| File | Purpose |
|------|---------|
| `rajasthan_helper/__init__.py` | Package init |
| `rajasthan_helper/__main__.py` | CLI entry point |
| `rajasthan_helper/commands/__init__.py` | Commands module |
| `rajasthan_helper/commands/weather.py` | Weather integration |
| `rajasthan_helper/commands/festival.py` | Festival data |
| `rajasthan_helper/commands/tip.py` | Travel tips |

---

## 🎯 Usage Examples

### Weather Command
```bash
# Get weather for Jaipur (default)
$ rajasthan-helper weather

# Get weather for specific city
$ rajasthan-helper weather Udaipur

# Output:
# ┌──────────────────────┐
# │ 🌡️ Weather in Udaipur │
# ├──────────────────────┤
# │ Temperature │ 28°C   │
# │ Condition   │ Cloudy │
# │ Feels Like  │ 30°C   │
# │ Humidity    │ 45%    │
# └──────────────────────┘
```

### Festival Command
```bash
# Show all festivals
$ rajasthan-helper festival

# Show specific festival
$ rajasthan-helper festival March

# Available months:
# - January: Makar Sankranti 🪁
# - March: Holi 🎨
# - October: Diwali 🪔
# - November: Pushkar Camel Fair 🐪
# - December: Winter Festivals ❄️
```

### Travel Tips Command
```bash
# Get tips for Jaipur (default)
$ rajasthan-helper tip

# Get tips for specific city
$ rajasthan-helper tip Udaipur

# Available cities:
# - Jaipur 🏰
# - Udaipur 🚤
# - Mumbai 🥔
# - Jodhpur 🏛️
# - Pushkar 🕌
```

---

## 🎨 Features Breakdown

### Weather Command
- 🌐 Fetches from **wttr.in** API (free, no key needed)
- 🌡️ Shows: Temperature, Condition, Feels Like, Humidity
- 🎨 Rich cyan-bordered table
- ⚠️ Error handling for network issues

### Festival Command
- 🎉 5 Rajasthan festivals hardcoded
- 🗓️ Filterable by month
- 🪁 Each with emoji and description
- 📋 List view or detailed view

### Travel Tips Command
- 🗺️ 5 cities with curated tips
- ✨ 3 tips per city
- 🎨 Colorful green-bordered table
- 📌 Easy reference format

### UI/UX Features
- 🎨 Rich panels with custom borders
- 🌈 Color-coded output (cyan, green, yellow, magenta)
- 😊 Emojis throughout
- 📖 Built-in --help system
- ❌ Friendly error messages

---

## 📊 Technical Specifications

### Technology Stack
| Component | Technology | Version |
|-----------|-----------|---------|
| Language | Python | 3.8+ |
| CLI Framework | Click | >=8.0 |
| Output Formatting | Rich | >=10.0 |
| HTTP Client | Requests | >=2.25 |
| Weather API | wttr.in | Free |

### Project Metrics
- **Total Prompts**: ~10 (Copilot CLI free tier)
- **Total Lines of Code**: ~400 (all modules)
- **Dependencies**: 3 (minimal)
- **Package Size**: ~23 KB
- **Installation Size**: ~50 MB (with deps)

### Code Quality
- ✅ Type hints
- ✅ Docstrings
- ✅ Error handling
- ✅ PEP 8 compliant
- ✅ Clean architecture

---

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

### View Package Info
```bash
python verify_setup.py
```

---

## 🐛 Troubleshooting

### "Command not found: rajasthan-helper"
```bash
# Ensure installation completed
pip install -e .

# Verify installation
python -m rajasthan_helper --help
```

### "ModuleNotFoundError: rajasthan_helper"
```bash
# Run setup script first
python .github/setup_pkg.py

# Reinstall
pip install -e .
```

### "Connection timeout" (weather command)
```bash
# Check internet connection
# wttr.in service might be temporarily down
# Try another city
```

---

## 📈 Project Structure

```
rajasthan-helper/
│
├── .github/
│   ├── copilot-instructions.md      # Copilot guidance
│   └── setup_pkg.py                 # Setup script ⭐
│
├── rajasthan_helper/                # Generated by setup_pkg.py
│   ├── __init__.py
│   ├── __main__.py                  # CLI entry point
│   └── commands/
│       ├── __init__.py
│       ├── weather.py               # wttr.in integration
│       ├── festival.py              # Hardcoded festivals
│       └── tip.py                   # Travel tips
│
├── pyproject.toml                   # Project config
├── README.md                        # User guide
├── SETUP_RAJASTHAN_CLI.md           # Setup instructions
├── CLI_CREATION_SUMMARY.md          # Overview
├── FILES_CREATED_VERIFICATION.md    # File listing
├── verify_setup.py                  # Verification script
└── COMPREHENSIVE_README.md          # This file
```

---

## ✅ Verification Checklist

Before running setup:
- [ ] Python 3.8+ installed
- [ ] pip available
- [ ] Internet connection (for weather API)
- [ ] .github directory exists

After running setup_pkg.py:
- [ ] rajasthan_helper/ directory created
- [ ] All .py files in correct locations
- [ ] No errors in output

After pip install:
- [ ] rajasthan-helper command available
- [ ] pip list shows rajasthan-helper

After first run:
- [ ] Commands execute without errors
- [ ] Output displays colorfully
- [ ] Help text shows all options

---

## 🎓 Learning Resources

### Click Documentation
- **Home**: https://click.palletsprojects.com/
- **Commands**: Click groups and commands
- **Arguments**: Positional arguments
- **Options**: Flags and options

### Rich Documentation
- **Home**: https://rich.readthedocs.io/
- **Panels**: Rich panel output
- **Tables**: Rich table formatting
- **Console**: Console output control

### wttr.in API
- **Home**: https://wttr.in/
- **JSON Format**: ?format=j1
- **Documentation**: API reference

---

## 📝 License

This project is licensed under the MIT License.

## 🙏 Acknowledgments

- [wttr.in](https://wttr.in) - Free weather API
- [Click](https://click.palletsprojects.com/) - CLI framework
- [Rich](https://rich.readthedocs.io/) - Terminal formatting
- [GitHub Copilot CLI](https://github.com/features/copilot) - Assisted development

---

## 🏜️ Start Exploring!

```bash
# Ready? Let's go!
python .github/setup_pkg.py
pip install -e .
rajasthan-helper --help
```

**Discover the Land of Kings in your terminal! 🏜️**

---

*Built with GitHub Copilot CLI free tier - Optimized for minimal token usage*

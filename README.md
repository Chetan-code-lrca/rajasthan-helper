# 🏜️ Rajasthan Helper CLI – Built in ~20 Prompts on Free GitHub Copilot CLI

**Discover the Land of Kings in your terminal!** 🕌

A lightweight, colorful Python CLI tool for quick information about Rajasthan and India: real-time weather, cultural festivals, and travel tips. Built with Click and Rich for a beautiful terminal experience.

Built entirely on the **free tier of GitHub Copilot CLI** (~20 prompts).

## ✨ Features

- **🌡️ Real-time Weather** - Get current weather for any Indian city using wttr.in API
  - Shows temperature, condition, humidity, wind speed, and wind direction
  - Fallback data for offline or slow connections
  - Beautiful colored panels with emojis

- **🎉 Festival Calendar** - Explore Rajasthan festivals throughout the year
  - All 12 months covered with cultural significance
  - Festival descriptions and traditions
  - Rich table view for browsing or single-month view

- **🗺️ Travel Tips** - Curated travel recommendations for major cities
  - 10+ Indian cities including Jaipur, Udaipur, Delhi, Mumbai, and more
  - 3-4 practical tips per city
  - Emojis and rich formatting for easy scanning

- **⚡ Production-Ready**
  - Error handling with friendly rich-formatted messages
  - Case-insensitive input handling
  - Comprehensive logging for debugging
  - Type hints throughout the codebase

## 📦 Installation

### Requirements
- Python 3.7+

### Install from source

```bash
git clone https://github.com/yourusername/rajasthan-helper.git
cd rajasthan-helper
pip install -e .
```

This installs the package in development mode with all dependencies:
- `click` - Command-line interface creation kit
- `rich` - Beautiful terminal output with colors and tables
- `requests` - HTTP library for API calls

## 🚀 Quick Start

```bash
# Show version (with build info)
rajasthan-helper --version
# Output: rajasthan-helper 0.1.0 - Built with free GitHub Copilot CLI by Chetan Inaganti 🏜️

# Show help
rajasthan-helper --help

# Get weather for a city (with color-coded output)
rajasthan-helper weather jaipur      # ☀️ Hot (red)
rajasthan-helper weather srinagar    # ❄️ Cold (cyan)
rajasthan-helper weather delhi       # 🌧️ Moderate (yellow)

# Get festival info for a month
rajasthan-helper festival march      # Gangaur festival 👩
rajasthan-helper festival october    # Dussehra 🏹
rajasthan-helper festival november   # Pushkar Fair 🐪

# Get travel tips for a city
rajasthan-helper tip jaipur
rajasthan-helper tip udaipur
rajasthan-helper tip agra
rajasthan-helper tip mumbai
```

## 📖 Usage Examples

### Weather Command

```bash
$ rajasthan-helper weather jaipur

╭─ Weather for Jaipur ─────────────────────────╮
│ 🌤️  Sunny                                     │
│ Temperature: 28°C (feels like 30°C)          │
│ 💧 Humidity: 45%                             │
│ 💨 Wind: 15 km/h (NE direction)              │
│ 🌅 Sunrise: 06:45 | 🌇 Sunset: 18:30        │
╰────────────────────────────────────────────────╯
```

### Festival Command

```bash
$ rajasthan-helper festival march

╭─ March Festival ──────────────────────────────╮
│ 🎨 Holi                                        │
│                                               │
│ Festival of colors & joy. Celebrate spring   │
│ with vibrant colored powder, joy, and        │
│ togetherness.                                │
╰────────────────────────────────────────────────╯
```

Show all festivals:

```bash
$ rajasthan-helper festival

┌──────────┬────────────────┬─────────────────────────────────┐
│ Month    │ Festival       │ Description                     │
├──────────┼────────────────┼─────────────────────────────────┤
│ January  │ 🪁 Makar...    │ Kite flying festival...         │
│ February │ 🐪 Desert...   │ Vibrant celebration...          │
│ March    │ 🎨 Holi        │ Festival of colors & joy...     │
│ ...      │ ...            │ ...                             │
└──────────┴────────────────┴─────────────────────────────────┘
```

### Tips Command

```bash
$ rajasthan-helper tip udaipur

╭─ Travel Tips for Udaipur ─────────────────────╮
│ 🚤 Take a romantic boat ride on Lake Pichola  │
│ 🏛️  Visit the magnificent City Palace         │
│ 🍲 Enjoy lakeside street food and local...   │
│ 📸 Watch the sunset from Jheel Fatehnuma...  │
╰────────────────────────────────────────────────╯
```

## 🛠️ Development

### Project Structure

```
rajasthan-helper/
├── rajasthan_helper/
│   ├── __init__.py           # Package metadata
│   ├── __main__.py           # CLI entry point
│   └── commands/
│       ├── __init__.py
│       ├── weather.py        # Weather command
│       ├── festival.py       # Festival command
│       └── tip.py            # Travel tips command
├── tests/                    # Unit tests
├── pyproject.toml            # Project configuration
└── README.md                 # This file
```

### Running Tests

```bash
pip install pytest
pytest tests/
```

### Code Comments & Documentation

Every module, function, and complex logic includes:
- Docstrings explaining *what* and *why*
- Inline comments for non-obvious decisions
- Type hints for better code clarity
- Logging for production debugging

Example from `weather.py`:

```python
def get_weather(city: str = None) -> None:
    """
    Fetch and display weather with fallback support.
    
    Robustness strategy:
    - Try live API first (wttr.in with 3s timeout)
    - If timeout/connection error: use fallback data
    - If city not found: show helpful error message
    
    Args:
        city: City name (e.g., "Jaipur")
    """
```

## 🌐 APIs & Data Sources

### wttr.in API
- **Endpoint:** `https://wttr.in/{city}?format=j1`
- **Rate Limit:** Reasonable for personal use
- **Response Time:** ~1-2s typically
- **Fallback:** Built-in cached data for 8+ cities if API is slow/down

### Hardcoded Data
- **Festivals:** 12 months of Rajasthan cultural celebrations
- **Tips:** 10 cities with 3-4 travel recommendations each
- **Benefits:** Works offline, no API dependencies for this data

## 🐛 Error Handling

The CLI gracefully handles:

- **Network errors** - Shows friendly message with suggestions
- **Invalid cities** - Lists available cities for reference
- **Invalid months** - Suggests valid months or shows all
- **API timeouts** - Falls back to cached weather data
- **JSON parsing errors** - Catches and displays helpful error

All errors use rich-formatted panels with emojis for clarity.

## 📊 Production Features

### Logging
- Logs important events to `rajasthan.log` for debugging
- Tracks API calls, errors, and user actions
- Helps diagnose issues without user screenshots

### Type Hints
- All functions have type annotations
- Catches errors early with static type checkers
- Makes code self-documenting

### Input Validation
- Case-insensitive city and month names
- Helpful error messages with available options
- Smart fallback for common mistakes

## 🎓 Learning Resources

This project demonstrates:

1. **CLI Best Practices**
   - Click framework for command routing
   - Subcommands and arguments
   - Custom callbacks for version/help

2. **Error Handling**
   - Try/except for API failures
   - Fallback data strategies
   - User-friendly error messages

3. **Code Quality**
   - Comprehensive docstrings
   - Type hints for clarity
   - Separation of concerns (commands module)

4. **UX Design**
   - Rich formatting for visual appeal
   - Consistent error styling
   - Helpful messages and suggestions

5. **Testing & Logging**
   - Unit tests with pytest
   - Logging for production debugging
   - Fixture-based testing for API failures

## 📝 Built with

- **Python 3.7+** - Language
- **Click** - CLI framework
- **Rich** - Terminal output formatting
- **Requests** - HTTP library
- **Pytest** - Testing framework
- **GitHub Copilot CLI** - Free tier development tool

## 🏆 Credits

Built by **Chetan Inaganti** with **GitHub Copilot CLI** (Free Tier) - Ready for GitHub Challenge!

This project demonstrates how to build a complete, production-ready CLI tool efficiently using free developer tools and best practices.

## 📜 License

MIT License - Feel free to use, modify, and distribute.

## 🤝 Contributing

Pull requests are welcome! Please:
1. Fork the repository
2. Create a feature branch
3. Add tests for new features
4. Ensure all tests pass
5. Submit a pull request

## 📞 Support

Have questions? Ideas? Found a bug?
- Check the [Usage Examples](#-usage-examples) section
- Review command help: `rajasthan-helper --help`
- Check specific command help: `rajasthan-helper weather --help`

---

**Discover the magic of Rajasthan in your terminal!** 🏜️ 🕌

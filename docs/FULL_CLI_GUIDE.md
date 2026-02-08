# 🏜️ RAJASTHAN HELPER CLI - COMPLETE SETUP GUIDE

## ⚡ Quick Start (Ready Now!)

The **complete CLI implementation** is now ready to deploy with full Click + Rich functionality.

### Option 1: Windows Users (Easiest)
```batch
RUN_FULL_SETUP.bat
pip install -e .
rajasthan-helper --help
```

### Option 2: All Platforms
```bash
python FULL_SETUP.py
pip install -e .
rajasthan-helper --help
```

---

## 📋 What Gets Created

When you run `python FULL_SETUP.py`, it creates a complete CLI package:

### `rajasthan_helper/__init__.py`
- Package metadata
- Version 0.1.0

### `rajasthan_helper/__main__.py` ⭐ Main CLI Entry Point
**Features:**
- ✅ Click @click.group() for command routing
- ✅ Colorful welcome message with Rajasthan theme
- ✅ 3 subcommands: weather, festival, tip
- ✅ Beautiful help text: "Land of Kings in your terminal! 🏜️"
- ✅ Version display (0.1.0)
- ✅ Command delegation to command modules

**Welcome Output:**
```
╔════════════════════════════════════════╗
║ Welcome to Rajasthan Helper! 🏜️        ║
║                                        ║
║ Discover the magic of Rajasthan       ║
║                                        ║
║ Available commands:                   ║
║ weather  - Get real-time weather     ║
║ festival - Explore Rajasthan festivals║
║ tip      - Get travel tips           ║
║                                        ║
║ Use --help for more info              ║
╚════════════════════════════════════════╝
```

### `rajasthan_helper/commands/weather.py` 🌡️ Weather Command
**Features:**
- ✅ Fetches from `https://wttr.in/{city}?format=j1`
- ✅ Parses JSON response safely
- ✅ Displays: Temperature, Condition, Feels Like, Humidity, Wind Speed
- ✅ Rich cyan-bordered panel
- ✅ Emoji support (🌡️, 🌤️, etc.)
- ✅ Comprehensive error handling:
  - Network timeouts (5-second timeout)
  - Connection errors
  - City not found (HTTP 404)
  - Invalid JSON responses
  - Unexpected errors

**Output Example:**
```
┌─────────────────────────────────────┐
│ 🌡️ Weather in Jaipur                │
├─────────────────────────────────────┤
│ Property   │ Value                  │
├─────────────────────────────────────┤
│ Temperature│ 28°C                   │
│ Condition  │ Partly Cloudy          │
│ Feels Like │ 30°C                   │
│ Humidity   │ 45%                    │
│ Wind Speed │ 15 km/h                │
└─────────────────────────────────────┘
```

### `rajasthan_helper/commands/festival.py` 🎉 Festival Command
**Features:**
- ✅ 5 Hardcoded Rajasthan festivals
- ✅ Show all festivals or filter by month
- ✅ Rich magenta-bordered table for all festivals
- ✅ Rich yellow panel for individual festivals
- ✅ Emoji support for each festival

**Festivals Included:**
1. **January: Makar Sankranti** 🪁
   - Festival of kites and joy
   - Sky filled with colorful kites
   - Harvest season celebration

2. **March: Holi** 🎨
   - Festival of colors and fun
   - Spring celebration with vibrant colors
   - Bonfire and sweet treats

3. **October: Diwali** 🪔
   - Festival of lights and sweets
   - Diyas and oil lamps
   - Victory of light over darkness

4. **November: Pushkar Camel Fair** 🐪
   - Sacred pilgrimage fair
   - Colorful markets and camel races
   - Spiritual celebrations

5. **December: Winter Festivals** ❄️
   - Music and cultural festivals
   - Outdoor celebrations
   - Traditional performances

**Output Examples:**

All Festivals:
```
╔════════════════════════════════════════════════╗
║ 🎉 Rajasthan Festivals                         ║
╠════════════════════════════════════════════════╣
║ Month    │ Festival              │ Description │
╠════════════════════════════════════════════════╣
│ January  │ 🪁 Makar Sankranti    │ Kites...   │
│ March    │ 🎨 Holi               │ Colors...  │
│ October  │ 🪔 Diwali             │ Lights...  │
│ November │ 🐪 Pushkar Camel Fair │ Sacred...  │
│ December │ ❄️ Winter Festivals   │ Music...   │
╚════════════════════════════════════════════════╝
```

Single Festival:
```
╔════════════════════════════════════════════════╗
║ March                                          ║
╠════════════════════════════════════════════════╣
║ 🎨 Holi                                        ║
║                                                ║
║ Festival of colors and fun! Celebrate spring  ║
║ with vibrant colors, bonfire, and sweet...    ║
╚════════════════════════════════════════════════╝
```

### `rajasthan_helper/commands/tip.py` 🗺️ Travel Tips Command
**Features:**
- ✅ 5 Cities with 3 curated tips each
- ✅ Rich green-bordered table
- ✅ Emoji prefix for each tip
- ✅ Detailed, actionable travel advice

**Cities & Tips:**

1. **Jaipur** 🏰
   - 🌅 Amber Fort at sunset (panoramic views)
   - 🏪 Johari Bazar (traditional crafts & jewelry)
   - 🍛 Rajasthani thali (dal baati churma)

2. **Udaipur** 🚤
   - 🚤 Lake Pichola boat ride (romantic sunset)
   - 🏛️ Mewar Palace (royal architecture)
   - 🍲 Lakeside street food & sweets

3. **Mumbai** 🥔
   - 🥔 Vada pav from street vendors
   - 🎪 Gateway of India & Marine Drive walk
   - 🐟 Fish markets & seafood restaurants

4. **Jodhpur** 🏛️
   - 🏰 Mehrangarh Fort (panoramic views)
   - 🏢 Blue-painted old city streets
   - 🌶️ Spice markets (authentic flavors)

5. **Pushkar** 🕌
   - 🐪 Pushkar Camel Fair (November)
   - 🕯️ Sacred lake dip & temples
   - 🌅 Sunset from hilltop temples

**Output Example:**
```
┌──────────────────────────────────────────────┐
│ 🚤 Travel Tips for Udaipur                   │
├──────────────────────────────────────────────┤
│ Tip 1: 🚤 Take boat ride on Lake Pichola    │
│ Tip 2: 🏛️ Visit Mewar Palace               │
│ Tip 3: 🍲 Enjoy lakeside street food        │
└──────────────────────────────────────────────┘
```

---

## 🚀 Complete Usage Guide

### Get Help
```bash
rajasthan-helper --help
rajasthan-helper weather --help
rajasthan-helper festival --help
rajasthan-helper tip --help
```

### Weather Command
```bash
# Default (Jaipur)
rajasthan-helper weather

# Specific city
rajasthan-helper weather Udaipur
rajasthan-helper weather Mumbai
rajasthan-helper weather Jodhpur
```

### Festival Command
```bash
# Show all festivals
rajasthan-helper festival

# Show specific festival
rajasthan-helper festival January
rajasthan-helper festival March
rajasthan-helper festival October
rajasthan-helper festival November
rajasthan-helper festival December
```

### Travel Tips Command
```bash
# Default (Jaipur)
rajasthan-helper tip

# Specific city
rajasthan-helper tip Udaipur
rajasthan-helper tip Mumbai
rajasthan-helper tip Jodhpur
rajasthan-helper tip Pushkar
```

---

## 🎨 UI Features

### Color Scheme
- **Magenta borders** - Festival displays
- **Cyan borders** - Weather displays
- **Green borders** - Travel tips displays
- **Yellow text** - Highlights (conditions, festival names)
- **Green text** - Values and tips
- **Red text** - Error messages

### Emoji Integration
- 🌡️ Weather
- 🎉 Festivals
- 🪁 Makar Sankranti
- 🎨 Holi
- 🪔 Diwali
- 🐪 Pushkar Camel Fair
- ❄️ Winter Festivals
- 🗺️ Travel tips
- 🏰 Jaipur
- 🚤 Udaipur
- 🥔 Mumbai
- 🏛️ Jodhpur
- 🕌 Pushkar

### Error Messages
All errors display with:
- ❌ Clear error indicator
- 🔴 Red color styling
- 💬 Helpful suggestion text
- 📝 Dim explanatory text

---

## ⚙️ Technical Details

### Dependencies
```
click>=8.0          # CLI framework
rich>=10.0          # Rich text formatting
requests>=2.25      # HTTP client for weather API
```

### API Integration
- **Weather API:** wttr.in (free, no API key required)
- **Timeout:** 5 seconds per request
- **Response Format:** JSON
- **Data Parsed:** Temperature, condition, feels like, humidity, wind speed

### Error Handling
✅ Timeout protection (5-second limit)
✅ Network connection errors
✅ Invalid city names
✅ Invalid JSON responses
✅ Missing API data
✅ User-friendly error messages

### Code Quality
✅ Type hints on functions
✅ Comprehensive docstrings
✅ PEP 8 compliant
✅ Clean error handling
✅ No hardcoded secrets

---

## 📦 Installation & Deployment

### Step 1: Generate Package (One-time)
```bash
python FULL_SETUP.py
```

**Output:**
```
======================================================================
🏜️  RAJASTHAN HELPER CLI - FULL SETUP
======================================================================

✅ Created: rajasthan_helper/__init__.py
✅ Created: rajasthan_helper/__main__.py
✅ Created: rajasthan_helper/commands/__init__.py
✅ Created: rajasthan_helper/commands/weather.py
✅ Created: rajasthan_helper/commands/festival.py
✅ Created: rajasthan_helper/commands/tip.py

======================================================================
✅ PACKAGE SETUP COMPLETE!
======================================================================

📦 Next steps:

1. Install the package:
   pip install -e .

2. Test the CLI:
   rajasthan-helper --help
   rajasthan-helper weather Jaipur
   rajasthan-helper festival March
   rajasthan-helper tip Udaipur

======================================================================
```

### Step 2: Install Package
```bash
pip install -e .
```

This installs:
- ✅ click, rich, requests dependencies
- ✅ rajasthan-helper command entry point
- ✅ Package in editable mode

### Step 3: Run CLI
```bash
rajasthan-helper --help
```

---

## 🧪 Testing Commands

### Test Weather
```bash
rajasthan-helper weather Jaipur
rajasthan-helper weather Udaipur
rajasthan-helper weather "Invalid City"  # Test error handling
```

### Test Festivals
```bash
rajasthan-helper festival
rajasthan-helper festival March
rajasthan-helper festival invalid  # Test error handling
```

### Test Tips
```bash
rajasthan-helper tip Jaipur
rajasthan-helper tip Udaipur
rajasthan-helper tip invalid  # Test error handling
```

---

## 📊 Project Statistics

- **Lines of Code:** ~450 (well-structured)
- **Functions:** 15+ (modular design)
- **Commands:** 3 (weather, festival, tip)
- **Hardcoded Data:** 5 festivals, 5 cities with tips
- **Error Handlers:** 6+ (comprehensive coverage)
- **Emoji Count:** 25+ (delightful UX)
- **Rich Components:** Panels, Tables, Text styling
- **Dependencies:** 3 external libraries
- **Python Version:** 3.8+

---

## 🎯 Summary

✅ **Complete CLI Implementation**
✅ **Click Framework Setup**
✅ **Rich Output Formatting**
✅ **wttr.in API Integration**
✅ **Comprehensive Error Handling**
✅ **Hardcoded Festivals & Tips**
✅ **Colorful, User-Friendly UI**
✅ **Production-Ready Code**

---

## 🏜️ Ready to Deploy!

```bash
python FULL_SETUP.py
pip install -e .
rajasthan-helper --help
```

**Discover the Land of Kings in your terminal! 🏜️**

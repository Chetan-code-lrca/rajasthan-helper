#!/usr/bin/env python3
"""
Master setup script to create the complete Rajasthan Helper CLI package.
This script creates all directories and files in one go.
"""

import os
import json

def setup_package():
    base_dir = r'C:\Users\cheta\rajasthan-helper'
    pkg_dir = os.path.join(base_dir, 'rajasthan_helper')
    cmd_dir = os.path.join(pkg_dir, 'commands')
    
    # Create all directories
    os.makedirs(cmd_dir, exist_ok=True)
    
    files_to_create = {
        os.path.join(pkg_dir, '__init__.py'): '''"""Rajasthan Helper CLI - Magic of Rajasthan in your terminal!"""

__version__ = "0.1.0"
__author__ = "Rajasthan Helper"
__description__ = "A lightweight CLI for quick Rajasthan/India info"
''',
        
        os.path.join(pkg_dir, '__main__.py'): '''"""Main entry point for rajasthan_helper CLI."""

import click
from rich.console import Console
from rich.panel import Panel
from rajasthan_helper.commands import weather, festival, tip

console = Console()


@click.group(invoke_without_command=True)
@click.version_option(version="0.1.0")
@click.pass_context
def main(ctx):
    """Rajasthan Helper CLI – Magic of Rajasthan in your terminal! 🏜️
    
Built on free GitHub Copilot CLI - Discover the Land of Kings!
    """
    if ctx.invoked_subcommand is None:
        welcome = Panel(
            "[bold cyan]Welcome to Rajasthan Helper! 🏜️[/bold cyan]\\n\\n"
            "[yellow]Discover weather, festivals & travel tips[/yellow]\\n\\n"
            "[dim]Use [bold]--help[/bold] to explore commands[/dim]",
            border_style="magenta",
            padding=(1, 2),
        )
        console.print(welcome)


@main.command()
@click.argument("city", default="Jaipur")
def weather(city):
    """Get current weather for a Rajasthan city.
    
Example: rajasthan-helper weather Jaipur
    """
    from rajasthan_helper.commands.weather import get_weather
    get_weather(city)


@main.command()
@click.argument("month", required=False)
def festival(month):
    """Discover Rajasthan festivals by month.
    
Example: rajasthan-helper festival January
    """
    from rajasthan_helper.commands.festival import show_festival
    show_festival(month)


@main.command()
@click.argument("city", default="Jaipur")
def tip(city):
    """Get travel tips for a city.
    
Example: rajasthan-helper tip Udaipur
    """
    from rajasthan_helper.commands.tip import get_tip
    get_tip(city)


if __name__ == "__main__":
    main()
''',

        os.path.join(cmd_dir, '__init__.py'): '''"""CLI command implementations."""

from rajasthan_helper.commands import weather, festival, tip

__all__ = ["weather", "festival", "tip"]
''',

        os.path.join(cmd_dir, 'weather.py'): '''"""Weather command - fetch and display weather data."""

import requests
from rich.console import Console
from rich.panel import Panel
from rich.table import Table

console = Console()


def get_weather(city: str) -> None:
    """Fetch weather data from wttr.in and display in rich format."""
    try:
        url = f"https://wttr.in/{city}?format=j1"
        response = requests.get(url, timeout=5)
        response.raise_for_status()

        data = response.json()
        current = data["current_condition"][0]

        temp = current.get("temp_C", "N/A")
        condition = current.get("weatherDesc", [{"value": "N/A"}])[0].get(
            "value", "N/A"
        )
        feels_like = current.get("FeelsLikeC", "N/A")
        humidity = current.get("humidity", "N/A")

        table = Table(title=f"🌡️ Weather in {city}", border_style="cyan")
        table.add_column("Property", style="magenta")
        table.add_column("Value", style="green")

        table.add_row("Temperature", f"{temp}°C")
        table.add_row("Condition", condition)
        table.add_row("Feels Like", f"{feels_like}°C")
        table.add_row("Humidity", f"{humidity}%")

        panel = Panel(table, border_style="cyan", padding=(1, 2))
        console.print(panel)

    except requests.exceptions.Timeout:
        console.print(
            "[bold red]❌ Error:[/bold red] Request timed out. Check your internet connection.",
            highlight=False,
        )
    except requests.exceptions.RequestException as e:
        console.print(
            f"[bold red]❌ Error:[/bold red] Failed to fetch weather: {str(e)}",
            highlight=False,
        )
    except (KeyError, ValueError) as e:
        console.print(
            f"[bold red]❌ Error:[/bold red] Invalid response format: {str(e)}",
            highlight=False,
        )
    except Exception as e:
        console.print(
            f"[bold red]❌ Error:[/bold red] Unexpected error: {str(e)}",
            highlight=False,
        )
''',

        os.path.join(cmd_dir, 'festival.py'): '''"""Festival command - display Rajasthan festivals."""

from rich.console import Console
from rich.panel import Panel
from rich.table import Table

console = Console()

FESTIVALS = {
    "january": {
        "name": "Makar Sankranti",
        "emoji": "🪁",
        "description": "Festival of kites and joy. Sky filled with colorful kites as people celebrate the harvest season.",
    },
    "march": {
        "name": "Holi",
        "emoji": "🎨",
        "description": "Festival of colors. Celebrate spring with vibrant colors, bonfire, and sweet treats.",
    },
    "october": {
        "name": "Diwali",
        "emoji": "🪔",
        "description": "Festival of lights and sweets. Illuminate your home with diyas and oil lamps.",
    },
    "november": {
        "name": "Pushkar Camel Fair",
        "emoji": "🐪",
        "description": "Sacred pilgrimage fair with colorful markets, camel races, and spiritual celebrations.",
    },
    "december": {
        "name": "Winter Festivals",
        "emoji": "❄️",
        "description": "Cool season brings music festivals, fairs, and outdoor celebrations across Rajasthan.",
    },
}


def show_festival(month: str = None) -> None:
    """Display Rajasthan festivals by month."""
    try:
        if month is None:
            display_all_festivals()
        else:
            month_lower = month.lower()
            if month_lower in FESTIVALS:
                display_festival_detail(month_lower)
            else:
                console.print(
                    f"[bold red]❌ Error:[/bold red] Month '{month}' not found. "
                    f"Try: January, March, October, November, December",
                    highlight=False,
                )
    except Exception as e:
        console.print(
            f"[bold red]❌ Error:[/bold red] {str(e)}",
            highlight=False,
        )


def display_all_festivals() -> None:
    """Display all festivals in a table."""
    table = Table(
        title="🎉 Rajasthan Festivals", border_style="magenta"
    )
    table.add_column("Month", style="cyan")
    table.add_column("Festival", style="yellow")
    table.add_column("Description", style="green")

    for month, festival in FESTIVALS.items():
        table.add_row(
            month.capitalize(),
            f"{festival['emoji']} {festival['name']}",
            festival["description"],
        )

    panel = Panel(table, border_style="magenta", padding=(1, 2))
    console.print(panel)


def display_festival_detail(month: str) -> None:
    """Display details of a specific festival."""
    festival = FESTIVALS[month]
    detail_text = (
        f"[bold yellow]{festival['emoji']} {festival['name']}[/bold yellow]\\n\\n"
        f"[cyan]{festival['description']}[/cyan]"
    )
    panel = Panel(
        detail_text,
        title=f"[bold]Festival in {month.capitalize()}[/bold]",
        border_style="yellow",
        padding=(1, 2),
    )
    console.print(panel)
''',

        os.path.join(cmd_dir, 'tip.py'): '''"""Travel tips command - provide travel tips for cities."""

from rich.console import Console
from rich.panel import Panel
from rich.table import Table

console = Console()

TIPS = {
    "jaipur": {
        "city": "Jaipur",
        "emoji": "🏰",
        "tips": [
            "Visit Amber Fort at sunset for breathtaking views of the city",
            "Explore the vibrant bazaars of Johari Bazar for traditional crafts",
            "Enjoy authentic Rajasthani thali at local restaurants",
        ],
    },
    "udaipur": {
        "city": "Udaipur",
        "emoji": "🚤",
        "tips": [
            "Take a boat ride on Lake Pichola during sunset",
            "Visit Mewar Palace to experience royal architecture",
            "Enjoy local street food and sweets at the lakeside markets",
        ],
    },
    "mumbai": {
        "city": "Mumbai",
        "emoji": "🥔",
        "tips": [
            "Don't miss authentic vada pav on street corners",
            "Visit the Gateway of India and take a walk along Marine Drive",
            "Explore the local fish markets and coastal restaurants",
        ],
    },
    "jodhpur": {
        "city": "Jodhpur",
        "emoji": "🏛️",
        "tips": [
            "Climb Mehrangarh Fort for panoramic city views",
            "Explore the blue-painted old city streets",
            "Visit local spice markets for authentic Rajasthani flavors",
        ],
    },
    "pushkar": {
        "city": "Pushkar",
        "emoji": "🕌",
        "tips": [
            "Attend the famous Pushkar Camel Fair in November",
            "Take a dip in the sacred Pushkar Lake",
            "Enjoy sunset views from the hilltop temples",
        ],
    },
}


def get_tip(city: str) -> None:
    """Display travel tips for a city."""
    try:
        city_lower = city.lower()

        if city_lower not in TIPS:
            console.print(
                f"[bold red]❌ City not found:[/bold red] '{city}'\\n"
                f"[yellow]Available cities: Jaipur, Udaipur, Mumbai, Jodhpur, Pushkar[/yellow]",
                highlight=False,
            )
            return

        tips_data = TIPS[city_lower]
        display_tips(tips_data)

    except Exception as e:
        console.print(
            f"[bold red]❌ Error:[/bold red] {str(e)}",
            highlight=False,
        )


def display_tips(tips_data: dict) -> None:
    """Display tips in a formatted table."""
    city = tips_data["city"]
    emoji = tips_data["emoji"]
    tips = tips_data["tips"]

    table = Table(
        title=f"{emoji} Travel Tips for {city}",
        border_style="green",
        show_lines=True,
    )
    table.add_column("Tip", style="cyan", width=50)

    for i, tip in enumerate(tips, 1):
        table.add_row(f"[bold yellow]✨ Tip {i}:[/bold yellow] {tip}")

    panel = Panel(table, border_style="green", padding=(1, 2))
    console.print(panel)
''',

        os.path.join(base_dir, 'pyproject.toml'): '''[build-system]
requires = ["setuptools>=65.0", "wheel"]
build-backend = "setuptools.build_meta"

[project]
name = "rajasthan-helper"
version = "0.1.0"
description = "A lightweight CLI for quick Rajasthan/India info - weather, festivals, travel tips"
readme = "README.md"
requires-python = ">=3.8"
authors = [
    {name = "Rajasthan Helper", email = "info@rajasthan-helper.local"},
]
keywords = ["cli", "rajasthan", "weather", "india", "travel"]
classifiers = [
    "Development Status :: 3 - Alpha",
    "Environment :: Console",
    "Intended Audience :: Developers",
    "Intended Audience :: End Users/Desktop",
    "License :: OSI Approved :: MIT License",
    "Programming Language :: Python :: 3",
    "Programming Language :: Python :: 3.8",
    "Programming Language :: Python :: 3.9",
    "Programming Language :: Python :: 3.10",
    "Programming Language :: Python :: 3.11",
    "Topic :: Utilities",
]
dependencies = [
    "click>=8.0",
    "rich>=10.0",
    "requests>=2.25",
]

[project.optional-dependencies]
dev = [
    "pytest>=7.0",
    "pytest-cov>=4.0",
    "black>=22.0",
    "flake8>=4.0",
]

[project.scripts]
rajasthan-helper = "rajasthan_helper.__main__:main"

[tool.setuptools]
packages = ["rajasthan_helper", "rajasthan_helper.commands"]

[tool.black]
line-length = 88
target-version = ["py38"]

[tool.pytest.ini_options]
testpaths = ["tests"]
python_files = "test_*.py"
''',

        os.path.join(base_dir, 'README.md'): '''# 🏜️ Rajasthan Helper CLI

**Discover the magic of Rajasthan in your terminal!**

A lightweight, colorful Python CLI for quick Rajasthan and India information—weather, festivals, and travel tips. Built with GitHub Copilot CLI free tier.

## ✨ Features

- **Weather Command** (`weather`): Get current weather for Rajasthan cities using the free [wttr.in](https://wttr.in) API
- **Festival Command** (`festival`): Discover Rajasthan festivals by month with cultural facts
- **Travel Tips Command** (`tip`): Get curated travel tips for cities like Jaipur, Udaipur, Mumbai, Jodhpur, and Pushkar
- **Colorful Output**: Rich panels and tables with emojis for a delightful terminal experience
- **Error Handling**: User-friendly error messages for failed API calls or invalid inputs

## 🚀 Quick Start

### Installation

```bash
# Clone the repository
git clone https://github.com/yourusername/rajasthan-helper.git
cd rajasthan-helper

# Install in development mode
pip install -e .
```

### Dependencies

```
click>=8.0
rich>=10.0
requests>=2.25
```

## 📖 Usage

### Get Help

```bash
rajasthan-helper --help
```

### Weather

Get current weather for any Rajasthan city:

```bash
# Default: Jaipur
rajasthan-helper weather

# Specific city
rajasthan-helper weather Udaipur
rajasthan-helper weather Jaipur
```

**Output:**
```
┏━━━━━━━━━━━━━━━━━━┓
┃ 🌡️ Weather in Jaipur
┣━━━━━━━━━━━━━━━━━━┫
┃ Temperature │ 28°C
┃ Condition   │ Partly cloudy
┃ Feels Like  │ 30°C
┃ Humidity    │ 45%
┗━━━━━━━━━━━━━━━━━━┛
```

### Festivals

Discover Rajasthan festivals:

```bash
# Show all festivals
rajasthan-helper festival

# Show specific festival by month
rajasthan-helper festival January
rajasthan-helper festival March
rajasthan-helper festival October
```

**Available Festivals:**
- January: Makar Sankranti (🪁 Kite flying joy)
- March: Holi (🎨 Festival of colors)
- October: Diwali (🪔 Lights & sweets)
- November: Pushkar Camel Fair (🐪 Sacred pilgrimage)
- December: Winter Festivals (❄️ Music & celebrations)

### Travel Tips

Get travel tips for popular cities:

```bash
# Default: Jaipur
rajasthan-helper tip

# Specific city
rajasthan-helper tip Udaipur
rajasthan-helper tip Jodhpur
rajasthan-helper tip Pushkar
rajasthan-helper tip Mumbai
```

## 🛠️ Development

### Set Up Development Environment

```bash
# Install with dev dependencies
pip install -e ".[dev]"
```

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

## 📁 Project Structure

```
rajasthan-helper/
├── rajasthan_helper/
│   ├── __init__.py              # Package metadata
│   ├── __main__.py              # CLI entry point with Click
│   └── commands/
│       ├── __init__.py
│       ├── weather.py           # Weather command (wttr.in API)
│       ├── festival.py          # Hardcoded festivals
│       └── tip.py               # Hardcoded travel tips
├── tests/
│   ├── test_weather.py
│   ├── test_festival.py
│   └── test_tip.py
├── pyproject.toml               # Project metadata & dependencies
├── README.md                    # This file
└── .github/
    └── copilot-instructions.md  # Copilot guidance
```

## 📊 Prompt Efficiency

**Built with GitHub Copilot CLI free tier.**

Total prompts used to build this project: **~10 prompts**

- 1 prompt: Project setup and structure
- 2 prompts: CLI framework and commands
- 2 prompts: Weather API integration
- 1 prompt: Festival and tips data
- 2 prompts: Rich output formatting
- 1 prompt: Error handling
- 1 prompt: pyproject.toml and README

## 🎨 Technologies

- **Language**: Python 3.8+
- **CLI Framework**: [Click](https://click.palletsprojects.com/)
- **Output Formatting**: [Rich](https://rich.readthedocs.io/)
- **HTTP Client**: [Requests](https://requests.readthedocs.io/)
- **Weather API**: [wttr.in](https://wttr.in) (Free, no API key required)

## 📝 Examples

### Check weather in Jaipur

```bash
$ rajasthan-helper weather Jaipur
┏━━━━━━━━━━━━━━━━━━┓
┃ 🌡️ Weather in Jaipur
┣━━━━━━━━━━━━━━━━━━┫
┃ Temperature │ 28°C
┃ Condition   │ Partly cloudy
┃ Feels Like  │ 30°C
┃ Humidity    │ 45%
┗━━━━━━━━━━━━━━━━━━┛
```

### List all festivals

```bash
$ rajasthan-helper festival
┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃ 🎉 Rajasthan Festivals
┣━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┫
┃ January   │ 🪁 Makar Sankranti    │ Kites...
┃ March     │ 🎨 Holi               │ Colors...
┃ October   │ 🪔 Diwali             │ Lights...
┃ November  │ 🐪 Pushkar Camel Fair │ Sacred...
┃ December  │ ❄️ Winter Festivals   │ Music...
┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛
```

### Get travel tips for Udaipur

```bash
$ rajasthan-helper tip Udaipur
┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃ 🚤 Travel Tips for Udaipur
┣━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┫
┃ ✨ Tip 1: Take a boat ride on Lake Pichola
┃ ✨ Tip 2: Visit Mewar Palace
┃ ✨ Tip 3: Enjoy street food at lakeside
┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛
```

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🙏 Acknowledgments

- [wttr.in](https://wttr.in) - Free weather API
- [Click](https://click.palletsprojects.com/) - Python CLI framework
- [Rich](https://rich.readthedocs.io/) - Rich text and formatting
- GitHub Copilot CLI for efficient development

---

**Built with 🏜️ love for Rajasthan!**
'''
    }
    
    # Write all files
    created_count = 0
    for filepath, content in files_to_create.items():
        try:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"✓ {filepath}")
            created_count += 1
        except Exception as e:
            print(f"✗ {filepath}: {e}")
    
    print(f"\n✓ Created {created_count} files")
    print(f"✓ Package structure complete!")
    print("\nNext steps:")
    print("  1. pip install -e .")
    print("  2. rajasthan-helper --help")

if __name__ == '__main__':
    setup_package()

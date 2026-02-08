#!/usr/bin/env python3
"""
Complete Rajasthan Helper CLI Setup - Creates full package with Click + Rich implementation
Run this once to generate the complete CLI package ready to use.
"""

import os
import sys

BASE_DIR = r'C:\Users\cheta\rajasthan-helper'
PKG_DIR = os.path.join(BASE_DIR, 'rajasthan_helper')
CMD_DIR = os.path.join(PKG_DIR, 'commands')

# Create all directories
os.makedirs(CMD_DIR, exist_ok=True)

# All files with complete implementations
FILES = {
    os.path.join(PKG_DIR, '__init__.py'): '''"""Rajasthan Helper CLI - Magic of Rajasthan in your terminal!"""

__version__ = "0.1.0"
__author__ = "Rajasthan Helper"
__description__ = "Discover Rajasthan/India info: weather, festivals, travel tips"
''',

    os.path.join(PKG_DIR, '__main__.py'): '''"""Main CLI entry point for Rajasthan Helper."""

import click
from rich.console import Console
from rich.panel import Panel
from rajasthan_helper.commands import weather, festival, tip

console = Console()


@click.group(invoke_without_command=True)
@click.version_option(version="0.1.0", prog_name="rajasthan-helper")
@click.pass_context
def main(ctx):
    """
    [bold cyan]🏜️  Rajasthan Helper CLI[/bold cyan]
    
    [yellow]Discover the Land of Kings in your terminal![/yellow]
    
    [dim]Explore weather, festivals & travel tips of Rajasthan[/dim]
    """
    if ctx.invoked_subcommand is None:
        welcome = Panel.fit(
            "[bold cyan]Welcome to Rajasthan Helper! 🏜️[/bold cyan]\\n\\n"
            "[yellow]Discover the magic of Rajasthan[/yellow]\\n\\n"
            "[dim]Available commands:[/dim]\\n"
            "[green]weather[/green]  - Get real-time weather\\n"
            "[green]festival[/green] - Explore Rajasthan festivals\\n"
            "[green]tip[/green]      - Get travel tips\\n\\n"
            "[dim]Use [bold]--help[/bold] for more info[/dim]",
            border_style="magenta",
            padding=(1, 2),
        )
        console.print(welcome)


@main.command()
@click.argument("city", default="Jaipur", required=False)
def weather(city):
    """
    🌡️  Get current weather for a city
    
    Example: rajasthan-helper weather Jaipur
    """
    weather.get_weather(city)


@main.command()
@click.argument("month", default=None, required=False)
def festival(month):
    """
    🎉 Discover Rajasthan festivals by month
    
    Example: rajasthan-helper festival March
    
    Available months: January, March, October, November, December
    """
    festival.show_festival(month)


@main.command()
@click.argument("city", default="Jaipur", required=False)
def tip(city):
    """
    🗺️  Get travel tips for a city
    
    Example: rajasthan-helper tip Udaipur
    
    Available cities: Jaipur, Udaipur, Mumbai, Jodhpur, Pushkar
    """
    tip.get_tip(city)


if __name__ == "__main__":
    main()
''',

    os.path.join(CMD_DIR, '__init__.py'): '''"""CLI commands for Rajasthan Helper."""

from . import weather, festival, tip

__all__ = ["weather", "festival", "tip"]
''',

    os.path.join(CMD_DIR, 'weather.py'): '''"""Weather command - fetch and display real-time weather."""

import requests
from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from rich.text import Text

console = Console()


def get_weather(city: str) -> None:
    """
    Fetch current weather from wttr.in API and display in rich format.
    
    Args:
        city: City name to fetch weather for
    """
    try:
        # Fetch weather from wttr.in
        url = f"https://wttr.in/{city}?format=j1"
        response = requests.get(url, timeout=5)
        response.raise_for_status()

        data = response.json()
        
        # Extract current weather data
        if "current_condition" not in data or not data["current_condition"]:
            console.print("[bold red]❌ Error:[/bold red] No weather data found for that city", style="red")
            return
            
        current = data["current_condition"][0]

        # Get weather details
        temp = current.get("temp_C", "N/A")
        condition = current.get("weatherDesc", [{"value": "N/A"}])[0].get("value", "N/A")
        feels_like = current.get("FeelsLikeC", "N/A")
        humidity = current.get("humidity", "N/A")
        wind_speed = current.get("windspeedKmph", "N/A")

        # Create rich table
        table = Table(title=f"🌡️  Weather in {city}", border_style="cyan", show_header=True)
        table.add_column("Property", style="magenta", width=15)
        table.add_column("Value", style="green", width=25)

        table.add_row("Temperature", f"[bold]{temp}°C[/bold]")
        table.add_row("Condition", f"[yellow]{condition}[/yellow]")
        table.add_row("Feels Like", f"[bold]{feels_like}°C[/bold]")
        table.add_row("Humidity", f"{humidity}%")
        table.add_row("Wind Speed", f"{wind_speed} km/h")

        # Display in panel
        panel = Panel(table, border_style="cyan", padding=(1, 2))
        console.print(panel)

    except requests.exceptions.Timeout:
        console.print(
            "[bold red]❌ Error:[/bold red] [yellow]Request timed out[/yellow]\\n"
            "[dim]Check your internet connection or try again later[/dim]",
            style="red"
        )
    except requests.exceptions.ConnectionError:
        console.print(
            "[bold red]❌ Error:[/bold red] [yellow]Network connection failed[/yellow]\\n"
            "[dim]Make sure you're connected to the internet[/dim]",
            style="red"
        )
    except requests.exceptions.HTTPError as e:
        console.print(
            f"[bold red]❌ Error:[/bold red] [yellow]City not found: {str(e)}[/yellow]\\n"
            "[dim]Try another city name[/dim]",
            style="red"
        )
    except (KeyError, ValueError) as e:
        console.print(
            "[bold red]❌ Error:[/bold red] [yellow]Invalid response format[/yellow]\\n"
            "[dim]The API returned unexpected data[/dim]",
            style="red"
        )
    except Exception as e:
        console.print(
            f"[bold red]❌ Unexpected Error:[/bold red] {str(e)}",
            style="red"
        )
''',

    os.path.join(CMD_DIR, 'festival.py'): '''"""Festival command - display Rajasthan festivals."""

from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from rich.text import Text

console = Console()

# Hardcoded Rajasthan festivals
FESTIVALS = {
    "january": {
        "name": "Makar Sankranti",
        "emoji": "🪁",
        "description": "Festival of kites and joy. Sky filled with colorful kites as people celebrate the harvest season with sweets and festivities.",
        "month": "January",
    },
    "march": {
        "name": "Holi",
        "emoji": "🎨",
        "description": "Festival of colors and fun! Celebrate spring with vibrant colors, bonfire, and sweet treats. A joyful celebration of love and renewal.",
        "month": "March",
    },
    "october": {
        "name": "Diwali",
        "emoji": "🪔",
        "description": "Festival of lights and sweets. Illuminate your home with diyas and oil lamps, exchange sweets, and celebrate the victory of light over darkness.",
        "month": "October",
    },
    "november": {
        "name": "Pushkar Camel Fair",
        "emoji": "🐪",
        "description": "Sacred pilgrimage fair with colorful markets, camel races, spiritual celebrations, and thousands of pilgrims gathering for cultural festivities.",
        "month": "November",
    },
    "december": {
        "name": "Winter Festivals",
        "emoji": "❄️",
        "description": "Cool season brings vibrant music festivals, cultural fairs, outdoor celebrations, and traditional performances across Rajasthan.",
        "month": "December",
    },
}


def show_festival(month: str = None) -> None:
    """
    Display Rajasthan festivals by month or show all.
    
    Args:
        month: Optional month name to filter festivals
    """
    try:
        if month is None:
            display_all_festivals()
        else:
            month_lower = month.lower()
            if month_lower in FESTIVALS:
                display_festival_detail(month_lower)
            else:
                available = ", ".join(m.capitalize() for m in FESTIVALS.keys())
                console.print(
                    f"[bold red]❌ Month not found:[/bold red] {month}\\n"
                    f"[dim]Available months: {available}[/dim]",
                    style="red"
                )
    except Exception as e:
        console.print(f"[bold red]❌ Error:[/bold red] {str(e)}", style="red")


def display_all_festivals() -> None:
    """Display all festivals in a formatted table."""
    table = Table(
        title="🎉 Rajasthan Festivals",
        border_style="magenta",
        show_header=True,
        header_style="bold magenta"
    )
    table.add_column("Month", style="cyan", width=12)
    table.add_column("Festival", style="yellow", width=25)
    table.add_column("Description", style="green", width=60)

    for festival_key, festival in FESTIVALS.items():
        table.add_row(
            festival["month"],
            f"{festival['emoji']} {festival['name']}",
            festival["description"][:57] + "..." if len(festival["description"]) > 60 else festival["description"]
        )

    panel = Panel(table, border_style="magenta", padding=(1, 2))
    console.print(panel)


def display_festival_detail(month_key: str) -> None:
    """Display details of a specific festival."""
    festival = FESTIVALS[month_key]
    
    detail_text = (
        f"[bold yellow]{festival['emoji']} {festival['name']}[/bold yellow]\\n\\n"
        f"[cyan]{festival['description']}[/cyan]"
    )
    
    panel = Panel(
        detail_text,
        title=f"[bold magenta]{festival['month']}[/bold magenta]",
        border_style="yellow",
        padding=(1, 2),
    )
    console.print(panel)
''',

    os.path.join(CMD_DIR, 'tip.py'): '''"""Travel tips command - provide travel tips for cities."""

from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from rich.text import Text

console = Console()

# Hardcoded travel tips for cities
TIPS = {
    "jaipur": {
        "city": "Jaipur",
        "emoji": "🏰",
        "tips": [
            "🌅 Visit Amber Fort at sunset for breathtaking panoramic views of the Pink City",
            "🏪 Explore vibrant Johari Bazar for traditional Rajasthani crafts and jewelry",
            "🍛 Enjoy authentic Rajasthani thali with dal baati churma at local restaurants",
        ],
    },
    "udaipur": {
        "city": "Udaipur",
        "emoji": "🚤",
        "tips": [
            "🚤 Take a romantic boat ride on Lake Pichola during golden sunset hours",
            "🏛️  Visit historic Mewar Palace to experience royal Rajasthani architecture",
            "🍲 Enjoy delicious street food and sweets at the lakeside markets",
        ],
    },
    "mumbai": {
        "city": "Mumbai",
        "emoji": "🥔",
        "tips": [
            "🥔 Don't miss authentic vada pav from street vendors - Mumbai's beloved snack",
            "🎪 Visit the iconic Gateway of India and take a scenic walk along Marine Drive",
            "🐟 Explore vibrant fish markets and coastal seafood restaurants",
        ],
    },
    "jodhpur": {
        "city": "Jodhpur",
        "emoji": "🏛️",
        "tips": [
            "🏰 Climb Mehrangarh Fort for stunning panoramic views of the blue city below",
            "🏢 Explore the blue-painted old city streets and photograph the unique architecture",
            "🌶️  Visit bustling spice markets for authentic Rajasthani flavors and colors",
        ],
    },
    "pushkar": {
        "city": "Pushkar",
        "emoji": "🕌",
        "tips": [
            "🐪 Attend the famous Pushkar Camel Fair in November for cultural immersion",
            "🕯️  Take a spiritual dip in the sacred Pushkar Lake surrounded by temples",
            "🌅 Enjoy breathtaking sunset views from hilltop temples overlooking the town",
        ],
    },
}


def get_tip(city: str) -> None:
    """
    Display travel tips for a city.
    
    Args:
        city: City name to get tips for
    """
    try:
        city_lower = city.lower()

        if city_lower not in TIPS:
            available = ", ".join(c.capitalize() for c in TIPS.keys())
            console.print(
                f"[bold red]❌ City not found:[/bold red] {city}\\n"
                f"[dim]Available cities: {available}[/dim]",
                style="red"
            )
            return

        display_tips(TIPS[city_lower])

    except Exception as e:
        console.print(f"[bold red]❌ Error:[/bold red] {str(e)}", style="red")


def display_tips(tips_data: dict) -> None:
    """Display tips in a formatted list."""
    city = tips_data["city"]
    emoji = tips_data["emoji"]
    tips_list = tips_data["tips"]

    # Create table for tips
    table = Table(
        title=f"{emoji} Travel Tips for {city}",
        border_style="green",
        show_header=False,
        show_lines=True,
    )
    table.add_column("Tip", style="cyan", width=75)

    for i, tip in enumerate(tips_list, 1):
        table.add_row(f"[bold yellow]Tip {i}:[/bold yellow] {tip}")

    panel = Panel(table, border_style="green", padding=(1, 2))
    console.print(panel)
''',
}

# Write all files
print("=" * 70)
print("🏜️  RAJASTHAN HELPER CLI - FULL SETUP")
print("=" * 70)
print()

try:
    for filepath, content in FILES.items():
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        filename = filepath.replace(BASE_DIR + '\\\\', '').replace('\\\\', '/')
        print(f"✅ Created: {filename}")

    print()
    print("=" * 70)
    print("✅ PACKAGE SETUP COMPLETE!")
    print("=" * 70)
    print()
    print("📦 Next steps:")
    print()
    print("1. Install the package:")
    print("   pip install -e .")
    print()
    print("2. Test the CLI:")
    print("   rajasthan-helper --help")
    print("   rajasthan-helper weather Jaipur")
    print("   rajasthan-helper festival March")
    print("   rajasthan-helper tip Udaipur")
    print()
    print("=" * 70)
    print()

except Exception as e:
    print(f"❌ Error: {e}", file=sys.stderr)
    sys.exit(1)

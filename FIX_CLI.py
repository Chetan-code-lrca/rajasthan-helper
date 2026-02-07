#!/usr/bin/env python3
"""
Fix Rajasthan Helper CLI - Create commands directory and modules with proper imports
Run this to fix the ModuleNotFoundError and get the CLI working
"""

import os
import sys

BASE = r'C:\Users\cheta\rajasthan-helper'
PKG = os.path.join(BASE, 'rajasthan_helper')
CMD = os.path.join(PKG, 'commands')

print("🔧 Fixing Rajasthan Helper CLI...")
print()

# Create commands directory
os.makedirs(CMD, exist_ok=True)
print(f"✅ Created: {CMD}")

# Create commands/__init__.py
commands_init = '''"""Rajasthan Helper CLI commands module."""
'''

with open(os.path.join(CMD, '__init__.py'), 'w', encoding='utf-8') as f:
    f.write(commands_init)
print(f"✅ Created: {os.path.join(CMD, '__init__.py')}")

# Create commands/weather.py
weather_py = '''"""Weather command - fetch and display real-time weather."""

import requests
from rich.console import Console
from rich.panel import Panel
from rich.table import Table

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
            console.print(
                "[bold red]❌ Error:[/bold red] No weather data found for that city",
                style="red"
            )
            return
            
        current = data["current_condition"][0]

        # Get weather details
        temp = current.get("temp_C", "N/A")
        condition = current.get("weatherDesc", [{"value": "N/A"}])[0].get("value", "N/A")
        feels_like = current.get("FeelsLikeC", "N/A")
        humidity = current.get("humidity", "N/A")
        wind_speed = current.get("windspeedKmph", "N/A")

        # Create rich table
        table = Table(
            title=f"🌡️  Weather in {city}",
            border_style="cyan",
            show_header=True,
            header_style="bold cyan"
        )
        table.add_column("Property", style="magenta", width=15)
        table.add_column("Value", style="green", width=25)

        table.add_row("Temperature", f"[bold yellow]{temp}°C[/bold yellow]")
        table.add_row("Condition", f"[cyan]{condition}[/cyan]")
        table.add_row("Feels Like", f"[bold yellow]{feels_like}°C[/bold yellow]")
        table.add_row("Humidity", f"[green]{humidity}%[/green]")
        table.add_row("Wind Speed", f"[green]{wind_speed} km/h[/green]")

        # Display in panel
        panel = Panel(table, border_style="cyan", padding=(1, 2))
        console.print(panel)

    except requests.exceptions.Timeout:
        console.print(
            "[bold red]❌ Error:[/bold red] Request timed out\\n"
            "[dim]Check your internet connection or try again later[/dim]",
            style="red"
        )
    except requests.exceptions.ConnectionError:
        console.print(
            "[bold red]❌ Error:[/bold red] Network connection failed\\n"
            "[dim]Make sure you're connected to the internet[/dim]",
            style="red"
        )
    except requests.exceptions.HTTPError as e:
        console.print(
            f"[bold red]❌ Error:[/bold red] City not found: {city}\\n"
            "[dim]Try another city name[/dim]",
            style="red"
        )
    except (KeyError, ValueError) as e:
        console.print(
            "[bold red]❌ Error:[/bold red] Invalid response format\\n"
            "[dim]The API returned unexpected data[/dim]",
            style="red"
        )
    except Exception as e:
        console.print(
            f"[bold red]❌ Unexpected Error:[/bold red] {str(e)}",
            style="red"
        )
'''

with open(os.path.join(CMD, 'weather.py'), 'w', encoding='utf-8') as f:
    f.write(weather_py)
print(f"✅ Created: {os.path.join(CMD, 'weather.py')}")

# Create commands/festival.py
festival_py = '''"""Festival command - display Rajasthan festivals."""

from rich.console import Console
from rich.panel import Panel
from rich.table import Table

console = Console()

# Hardcoded Rajasthan festivals
FESTIVALS = {
    "january": {
        "name": "Makar Sankranti",
        "emoji": "🪁",
        "description": "Festival of kites and joy. Sky filled with colorful kites as people celebrate the harvest season.",
    },
    "march": {
        "name": "Holi",
        "emoji": "🎨",
        "description": "Festival of colors and fun! Celebrate spring with vibrant colors, bonfire, and sweet treats.",
    },
    "october": {
        "name": "Diwali",
        "emoji": "🪔",
        "description": "Festival of lights and sweets. Illuminate your home with diyas and celebrate light over darkness.",
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
                    f"[dim]Available: {available}[/dim]",
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
    table.add_column("Description", style="green", width=50)

    for festival_key, festival in FESTIVALS.items():
        month = festival_key.capitalize()
        desc = festival["description"][:47] + "..." if len(festival["description"]) > 50 else festival["description"]
        table.add_row(
            month,
            f"{festival['emoji']} {festival['name']}",
            desc
        )

    panel = Panel(table, border_style="magenta", padding=(1, 2))
    console.print(panel)


def display_festival_detail(month_key: str) -> None:
    """Display details of a specific festival."""
    festival = FESTIVALS[month_key]
    month_name = month_key.capitalize()
    
    detail_text = (
        f"[bold yellow]{festival['emoji']} {festival['name']}[/bold yellow]\\n\\n"
        f"[cyan]{festival['description']}[/cyan]"
    )
    
    panel = Panel(
        detail_text,
        title=f"[bold magenta]{month_name}[/bold magenta]",
        border_style="yellow",
        padding=(1, 2),
    )
    console.print(panel)
'''

with open(os.path.join(CMD, 'festival.py'), 'w', encoding='utf-8') as f:
    f.write(festival_py)
print(f"✅ Created: {os.path.join(CMD, 'festival.py')}")

# Create commands/tip.py
tip_py = '''"""Travel tips command - provide travel tips for cities."""

from rich.console import Console
from rich.panel import Panel
from rich.table import Table

console = Console()

# Hardcoded travel tips for cities
TIPS = {
    "jaipur": {
        "city": "Jaipur",
        "emoji": "🏰",
        "tips": [
            "🌅 Visit Amber Fort at sunset for breathtaking panoramic views",
            "🏪 Explore vibrant Johari Bazar for traditional crafts and jewelry",
            "🍛 Enjoy authentic Rajasthani thali with dal baati churma",
        ],
    },
    "udaipur": {
        "city": "Udaipur",
        "emoji": "🚤",
        "tips": [
            "🚤 Take a romantic boat ride on Lake Pichola during sunset",
            "🏛️  Visit historic Mewar Palace to experience royal architecture",
            "🍲 Enjoy delicious street food and sweets at lakeside markets",
        ],
    },
    "mumbai": {
        "city": "Mumbai",
        "emoji": "🥔",
        "tips": [
            "🥔 Don't miss authentic vada pav from street vendors",
            "🎪 Visit Gateway of India and take a scenic Marine Drive walk",
            "🐟 Explore vibrant fish markets and coastal seafood restaurants",
        ],
    },
    "jodhpur": {
        "city": "Jodhpur",
        "emoji": "🏛️",
        "tips": [
            "🏰 Climb Mehrangarh Fort for stunning panoramic city views",
            "🏢 Explore the blue-painted old city streets and photograph",
            "🌶️  Visit bustling spice markets for authentic Rajasthani flavors",
        ],
    },
    "pushkar": {
        "city": "Pushkar",
        "emoji": "🕌",
        "tips": [
            "🐪 Attend the famous Pushkar Camel Fair in November",
            "🕯️  Take a spiritual dip in the sacred Pushkar Lake",
            "🌅 Enjoy sunset views from hilltop temples",
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
    """Display tips in a formatted table."""
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
'''

with open(os.path.join(CMD, 'tip.py'), 'w', encoding='utf-8') as f:
    f.write(tip_py)
print(f"✅ Created: {os.path.join(CMD, 'tip.py')}")

# Now fix __main__.py with correct imports
main_py = '''"""Main CLI entry point for Rajasthan Helper."""

import click
from rich.console import Console
from rich.panel import Panel

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
    """🌡️  Get current weather for a city
    
    Example: rajasthan-helper weather Jaipur
    """
    from rajasthan_helper.commands.weather import get_weather
    get_weather(city)


@main.command()
@click.argument("month", default=None, required=False)
def festival(month):
    """🎉 Discover Rajasthan festivals by month
    
    Example: rajasthan-helper festival March
    
    Months: January, March, October, November, December
    """
    from rajasthan_helper.commands.festival import show_festival
    show_festival(month)


@main.command()
@click.argument("city", default="Jaipur", required=False)
def tip(city):
    """🗺️  Get travel tips for a city
    
    Example: rajasthan-helper tip Udaipur
    
    Cities: Jaipur, Udaipur, Mumbai, Jodhpur, Pushkar
    """
    from rajasthan_helper.commands.tip import get_tip
    get_tip(city)


if __name__ == "__main__":
    main()
'''

with open(os.path.join(PKG, '__main__.py'), 'w', encoding='utf-8') as f:
    f.write(main_py)
print(f"✅ Updated: {os.path.join(PKG, '__main__.py')}")

print()
print("=" * 70)
print("✅ CLI STRUCTURE FIXED!")
print("=" * 70)
print()
print("Next steps:")
print("1. pip install -e .")
print("2. rajasthan-helper --help")
print("3. rajasthan-helper weather Jaipur")
print("4. rajasthan-helper festival March")
print("5. rajasthan-helper tip Udaipur")
print()
print("=" * 70)

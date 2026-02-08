#!/usr/bin/env python3
"""Create complete Rajasthan Helper CLI package with full Click + Rich functionality."""

import os
import sys

BASE = r'C:\Users\cheta\rajasthan-helper'
PKG = os.path.join(BASE, 'rajasthan_helper')
CMD = os.path.join(PKG, 'commands')

# Create commands directory
os.makedirs(CMD, exist_ok=True)

# Create commands/__init__.py
with open(os.path.join(CMD, '__init__.py'), 'w', encoding='utf-8') as f:
    f.write('''"""CLI commands for Rajasthan Helper."""

from . import weather, festival, tip

__all__ = ["weather", "festival", "tip"]
''')

# Create commands/weather.py
with open(os.path.join(CMD, 'weather.py'), 'w', encoding='utf-8') as f:
    f.write('''"""Weather command - fetch and display real-time weather."""

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
        url = f"https://wttr.in/{city}?format=j1"
        response = requests.get(url, timeout=5)
        response.raise_for_status()

        data = response.json()
        
        if "current_condition" not in data or not data["current_condition"]:
            console.print("[bold red]❌ Error:[/bold red] No weather data found for that city", style="red")
            return
            
        current = data["current_condition"][0]

        temp = current.get("temp_C", "N/A")
        condition = current.get("weatherDesc", [{"value": "N/A"}])[0].get("value", "N/A")
        feels_like = current.get("FeelsLikeC", "N/A")
        humidity = current.get("humidity", "N/A")
        wind_speed = current.get("windspeedKmph", "N/A")

        table = Table(title=f"🌡️  Weather in {city}", border_style="cyan", show_header=True)
        table.add_column("Property", style="magenta", width=15)
        table.add_column("Value", style="green", width=25)

        table.add_row("Temperature", f"[bold]{temp}°C[/bold]")
        table.add_row("Condition", f"[yellow]{condition}[/yellow]")
        table.add_row("Feels Like", f"[bold]{feels_like}°C[/bold]")
        table.add_row("Humidity", f"{humidity}%")
        table.add_row("Wind Speed", f"{wind_speed} km/h")

        panel = Panel(table, border_style="cyan", padding=(1, 2))
        console.print(panel)

    except requests.exceptions.Timeout:
        console.print("[bold red]❌ Error:[/bold red] Request timeout. Check internet.", style="red")
    except requests.exceptions.ConnectionError:
        console.print("[bold red]❌ Error:[/bold red] Network failed. Check connection.", style="red")
    except requests.exceptions.HTTPError:
        console.print(f"[bold red]❌ Error:[/bold red] City not found: {city}", style="red")
    except (KeyError, ValueError):
        console.print("[bold red]❌ Error:[/bold red] Invalid response format.", style="red")
    except Exception as e:
        console.print(f"[bold red]❌ Unexpected Error:[/bold red] {str(e)}", style="red")
''')

# Create commands/festival.py
with open(os.path.join(CMD, 'festival.py'), 'w', encoding='utf-8') as f:
    f.write('''"""Festival command - display Rajasthan festivals."""

from rich.console import Console
from rich.panel import Panel
from rich.table import Table

console = Console()

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
    """Display Rajasthan festivals by month or show all."""
    try:
        if month is None:
            display_all_festivals()
        else:
            month_lower = month.lower()
            if month_lower in FESTIVALS:
                display_festival_detail(month_lower)
            else:
                available = ", ".join(m.capitalize() for m in FESTIVALS.keys())
                console.print(f"[bold red]❌ Month not found:[/bold red] {month}\\n[dim]Available: {available}[/dim]", style="red")
    except Exception as e:
        console.print(f"[bold red]❌ Error:[/bold red] {str(e)}", style="red")


def display_all_festivals() -> None:
    """Display all festivals in a formatted table."""
    table = Table(title="🎉 Rajasthan Festivals", border_style="magenta", show_header=True)
    table.add_column("Month", style="cyan", width=12)
    table.add_column("Festival", style="yellow", width=25)
    table.add_column("Description", style="green", width=55)

    for festival_key, festival in FESTIVALS.items():
        desc = festival["description"][:52] + "..." if len(festival["description"]) > 55 else festival["description"]
        table.add_row(festival["month"], f"{festival['emoji']} {festival['name']}", desc)

    panel = Panel(table, border_style="magenta", padding=(1, 2))
    console.print(panel)


def display_festival_detail(month_key: str) -> None:
    """Display details of a specific festival."""
    festival = FESTIVALS[month_key]
    detail_text = f"[bold yellow]{festival['emoji']} {festival['name']}[/bold yellow]\\n\\n[cyan]{festival['description']}[/cyan]"
    panel = Panel(detail_text, title=f"[bold magenta]{festival['month']}[/bold magenta]", border_style="yellow", padding=(1, 2))
    console.print(panel)
''')

# Create commands/tip.py
with open(os.path.join(CMD, 'tip.py'), 'w', encoding='utf-8') as f:
    f.write('''"""Travel tips command - provide travel tips for cities."""

from rich.console import Console
from rich.panel import Panel
from rich.table import Table

console = Console()

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
    """Display travel tips for a city."""
    try:
        city_lower = city.lower()
        if city_lower not in TIPS:
            available = ", ".join(c.capitalize() for c in TIPS.keys())
            console.print(f"[bold red]❌ City not found:[/bold red] {city}\\n[dim]Available: {available}[/dim]", style="red")
            return
        display_tips(TIPS[city_lower])
    except Exception as e:
        console.print(f"[bold red]❌ Error:[/bold red] {str(e)}", style="red")


def display_tips(tips_data: dict) -> None:
    """Display tips in a formatted table."""
    city = tips_data["city"]
    emoji = tips_data["emoji"]
    tips = tips_data["tips"]

    table = Table(title=f"{emoji} Travel Tips for {city}", border_style="green", show_header=False, show_lines=True)
    table.add_column("Tip", style="cyan", width=75)

    for i, tip in enumerate(tips, 1):
        table.add_row(f"[bold yellow]Tip {i}:[/bold yellow] {tip}")

    panel = Panel(table, border_style="green", padding=(1, 2))
    console.print(panel)
''')

print("✅ Complete CLI package created successfully!")
print(f"✅ Created {CMD}")
print("✅ All command modules ready!")
print("\nNext: pip install -e .")
print("Then: rajasthan-helper --help")

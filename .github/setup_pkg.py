#!/usr/bin/env python3
"""Setup Rajasthan Helper package structure."""
import os

BASE = r'C:\Users\cheta\rajasthan-helper'
PKG = os.path.join(BASE, 'rajasthan_helper')
CMD = os.path.join(PKG, 'commands')

# Ensure directories exist
os.makedirs(CMD, exist_ok=True)

# Write init file
with open(os.path.join(PKG, '__init__.py'), 'w') as f:
    f.write('"""Rajasthan Helper CLI"""\n__version__ = "0.1.0"\n')

# Write main file
with open(os.path.join(PKG, '__main__.py'), 'w') as f:
    f.write('''"""Main entry point."""
import click
from rich.console import Console
from rich.panel import Panel
from rajasthan_helper.commands import weather, festival, tip

console = Console()

@click.group(invoke_without_command=True)
@click.version_option(version="0.1.0")
@click.pass_context
def main(ctx):
    """Rajasthan Helper CLI – Magic of Rajasthan! 🏜️"""
    if ctx.invoked_subcommand is None:
        welcome = Panel(
            "[bold cyan]Welcome to Rajasthan Helper! 🏜️[/bold cyan]\\n\\n"
            "[yellow]Discover weather, festivals & travel tips[/yellow]\\n\\n"
            "[dim]Use --help to explore[/dim]",
            border_style="magenta",
            padding=(1, 2),
        )
        console.print(welcome)

@main.command()
@click.argument("city", default="Jaipur")
def weather(city):
    """Get current weather for a city."""
    from rajasthan_helper.commands.weather import get_weather
    get_weather(city)

@main.command()
@click.argument("month", required=False)
def festival(month):
    """Discover Rajasthan festivals by month."""
    from rajasthan_helper.commands.festival import show_festival
    show_festival(month)

@main.command()
@click.argument("city", default="Jaipur")
def tip(city):
    """Get travel tips for a city."""
    from rajasthan_helper.commands.tip import get_tip
    get_tip(city)

if __name__ == "__main__":
    main()
''')

# Write commands init
with open(os.path.join(CMD, '__init__.py'), 'w') as f:
    f.write('"""CLI commands."""\\nfrom rajasthan_helper.commands import weather, festival, tip\\n__all__ = ["weather", "festival", "tip"]\\n')

# Write weather.py
with open(os.path.join(CMD, 'weather.py'), 'w') as f:
    f.write('''"""Weather command."""
import requests
from rich.console import Console
from rich.panel import Panel
from rich.table import Table

console = Console()

def get_weather(city: str) -> None:
    """Fetch and display weather."""
    try:
        url = f"https://wttr.in/{city}?format=j1"
        response = requests.get(url, timeout=5)
        response.raise_for_status()
        data = response.json()
        current = data["current_condition"][0]
        temp = current.get("temp_C", "N/A")
        condition = current.get("weatherDesc", [{"value": "N/A"}])[0].get("value", "N/A")
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
        console.print("[bold red]❌ Error:[/bold red] Request timeout.", highlight=False)
    except requests.exceptions.RequestException as e:
        console.print(f"[bold red]❌ Error:[/bold red] {str(e)}", highlight=False)
    except (KeyError, ValueError) as e:
        console.print(f"[bold red]❌ Error:[/bold red] Invalid response.", highlight=False)
    except Exception as e:
        console.print(f"[bold red]❌ Error:[/bold red] {str(e)}", highlight=False)
''')

# Write festival.py
with open(os.path.join(CMD, 'festival.py'), 'w') as f:
    f.write('''"""Festival command."""
from rich.console import Console
from rich.panel import Panel
from rich.table import Table

console = Console()

FESTIVALS = {
    "january": {"name": "Makar Sankranti", "emoji": "🪁", "description": "Kite flying and harvest joy."},
    "march": {"name": "Holi", "emoji": "🎨", "description": "Festival of colors."},
    "october": {"name": "Diwali", "emoji": "🪔", "description": "Lights and sweets."},
    "november": {"name": "Pushkar Camel Fair", "emoji": "🐪", "description": "Sacred pilgrimage fair."},
    "december": {"name": "Winter Festivals", "emoji": "❄️", "description": "Music and celebrations."},
}

def show_festival(month: str = None) -> None:
    """Show festivals by month."""
    try:
        if month is None:
            display_all_festivals()
        else:
            month_lower = month.lower()
            if month_lower in FESTIVALS:
                display_festival_detail(month_lower)
            else:
                console.print(f"[bold red]❌ Month not found:[/bold red] {month}", highlight=False)
    except Exception as e:
        console.print(f"[bold red]❌ Error:[/bold red] {str(e)}", highlight=False)

def display_all_festivals() -> None:
    """Show all festivals."""
    table = Table(title="🎉 Rajasthan Festivals", border_style="magenta")
    table.add_column("Month", style="cyan")
    table.add_column("Festival", style="yellow")
    table.add_column("Description", style="green")
    for month, fest in FESTIVALS.items():
        table.add_row(month.capitalize(), f"{fest['emoji']} {fest['name']}", fest["description"])
    panel = Panel(table, border_style="magenta", padding=(1, 2))
    console.print(panel)

def display_festival_detail(month: str) -> None:
    """Show festival details."""
    fest = FESTIVALS[month]
    detail = f"[bold yellow]{fest['emoji']} {fest['name']}[/bold yellow]\\n\\n[cyan]{fest['description']}[/cyan]"
    panel = Panel(detail, title=f"[bold]{month.capitalize()}[/bold]", border_style="yellow", padding=(1, 2))
    console.print(panel)
''')

# Write tip.py
with open(os.path.join(CMD, 'tip.py'), 'w') as f:
    f.write('''"""Travel tips command."""
from rich.console import Console
from rich.panel import Panel
from rich.table import Table

console = Console()

TIPS = {
    "jaipur": {"city": "Jaipur", "emoji": "🏰", "tips": ["Amber Fort at sunset", "Johari Bazar bazaars", "Rajasthani thali"]},
    "udaipur": {"city": "Udaipur", "emoji": "🚤", "tips": ["Lake Pichola boat ride", "Mewar Palace", "Lakeside street food"]},
    "mumbai": {"city": "Mumbai", "emoji": "🥔", "tips": ["Vada pav street food", "Gateway of India", "Fish markets"]},
    "jodhpur": {"city": "Jodhpur", "emoji": "🏛️", "tips": ["Mehrangarh Fort", "Blue-painted city", "Spice markets"]},
    "pushkar": {"city": "Pushkar", "emoji": "🕌", "tips": ["Camel Fair", "Sacred Lake", "Temple sunsets"]},
}

def get_tip(city: str) -> None:
    """Show travel tips."""
    try:
        city_lower = city.lower()
        if city_lower not in TIPS:
            console.print(f"[bold red]❌ City not found:[/bold red] {city}", highlight=False)
            return
        display_tips(TIPS[city_lower])
    except Exception as e:
        console.print(f"[bold red]❌ Error:[/bold red] {str(e)}", highlight=False)

def display_tips(tips_data: dict) -> None:
    """Display tips table."""
    city, emoji, tips = tips_data["city"], tips_data["emoji"], tips_data["tips"]
    table = Table(title=f"{emoji} Travel Tips for {city}", border_style="green", show_lines=True)
    table.add_column("Tip", style="cyan")
    for i, tip in enumerate(tips, 1):
        table.add_row(f"[bold yellow]✨ Tip {i}:[/bold yellow] {tip}")
    panel = Panel(table, border_style="green", padding=(1, 2))
    console.print(panel)
''')

print("✓ Package setup complete!")
print(f"✓ Created {PKG}")
print(f"✓ Created {CMD}")
print("✓ Created all Python modules")

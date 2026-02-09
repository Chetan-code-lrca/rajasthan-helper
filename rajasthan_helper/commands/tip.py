"""Tips command – Travel tips for 10+ Indian cities."""

import click
from rich.console import Console
from rich.panel import Panel

console = Console()

TRAVEL_TIPS = {
    "jaipur": {
        "emoji": "🏛️",
        "name": "Jaipur",
        "description": "The Pink City",
        "tips": [
            "Visit Hawa Mahal early morning to beat crowds",
            "Try local Mirchi Bada at street stalls",
            "Shop for textiles at Bapu Bazaar",
            "Explore City Palace & Jantar Mantar",
        ],
    },
    "udaipur": {
        "emoji": "🏰",
        "name": "Udaipur",
        "description": "Venice of the East",
        "tips": [
            "Take sunset boat ride on Lake Pichola",
            "Stay in heritage hotel if budget allows",
            "Visit Old City for stunning views",
            "Explore City Palace museum",
        ],
    },
    "delhi": {
        "emoji": "🏛️",
        "name": "Delhi",
        "description": "Capital of India",
        "tips": [
            "Visit Red Fort & India Gate",
            "Try street food at Chandni Chowk",
            "Use metro for affordable transport",
            "Explore Mughal gardens at Humayun's Tomb",
        ],
    },
    "jodhpur": {
        "emoji": "🏜️",
        "name": "Jodhpur",
        "description": "The Blue City",
        "tips": [
            "Explore blue-painted old city on foot",
            "Climb Mehrangarh Fort early morning",
            "Try Bajra Roti & Dal Baati Churma",
            "Shop at bustling Sardar Market",
        ],
    },
    "jaisalmer": {
        "emoji": "🐫",
        "name": "Jaisalmer",
        "description": "Golden Fort City",
        "tips": [
            "Experience desert safari at Sam Dunes",
            "Watch sunset from sand dunes",
            "Explore havelis in old city",
            "Book accommodation early in peak season",
        ],
    },
    "pushkar": {
        "emoji": "🎪",
        "name": "Pushkar",
        "description": "Holy City & Fair",
        "tips": [
            "Visit Pushkar Fair in October-November",
            "Take camel rides at the fair",
            "Walk around sacred Pushkar Lake",
            "Visit one of India's few Brahma temples",
        ],
    },
    "ajmer": {
        "emoji": "🕌",
        "name": "Ajmer",
        "description": "The Sufi City",
        "tips": [
            "Visit Ajmer Sharif Dargah with respect",
            "Take boat rides on Anasagar Lake",
            "Explore museums & historical sites",
            "Taste authentic Ajmer cuisine",
        ],
    },
    "bikaner": {
        "emoji": "🐪",
        "name": "Bikaner",
        "description": "The Camel City",
        "tips": [
            "Visit Junagarh Fort & palaces",
            "Explore Gajner Palace wildlife sanctuary",
            "Try famous Bikaner's bhujia snack",
            "See camel farms in outskirts",
        ],
    },
    "mumbai": {
        "emoji": "🌊",
        "name": "Mumbai",
        "description": "Bollywood City",
        "tips": [
            "Stroll Marine Drive at sunset",
            "Visit Gateway of India",
            "Eat street food at Vada Pav stalls",
            "Catch a Bollywood film screening",
        ],
    },
    "agra": {
        "emoji": "🕌",
        "name": "Agra",
        "description": "Taj Mahal City",
        "tips": [
            "Watch sunrise at Taj Mahal",
            "Explore Agra Fort & history",
            "Try mughlai cuisine",
            "Visit baby Taj & markets",
        ],
    },
}


@click.command()
@click.argument("city")
def tip(city):
    """
    🧳 Get travel tips for Indian cities.
    
    Supported cities: Jaipur, Udaipur, Delhi, Jodhpur, Jaisalmer,
    Pushkar, Ajmer, Bikaner, Mumbai, Agra
    """
    city_lower = city.lower()
    
    if city_lower not in TRAVEL_TIPS:
        console.print()
        console.print(Panel(
            f"[red]❌ Unknown city: [bold]{city}[/bold][/red]\n\n"
            "[cyan]Try one of these:[/cyan]\n"
            "Jaipur, Udaipur, Delhi, Jodhpur, Jaisalmer,\n"
            "Pushkar, Ajmer, Bikaner, Mumbai, Agra",
            title="[bold red]Invalid Input[/bold red]",
            border_style="red",
            padding=(1, 2),
        ))
        console.print()
        return
    
    info = TRAVEL_TIPS[city_lower]
    console.print()
    
    tip_text = f"[bold cyan]{info['description']}[/bold cyan]\n\n[bold yellow]💡 Travel Tips:[/bold yellow]\n"
    for i, t in enumerate(info["tips"], 1):
        tip_text += f"  {i}. {t}\n"
    
    panel = Panel(
        tip_text,
        title=f"[bold cyan]{info['emoji']} {info['name']}[/bold cyan]",
        border_style="cyan",
        padding=(1, 2),
    )
    console.print(panel)

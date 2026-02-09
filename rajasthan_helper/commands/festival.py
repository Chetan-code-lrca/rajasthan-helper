"""Festival command – Rajasthan festivals by month."""

import click
from rich.console import Console
from rich.panel import Panel
from rich.table import Table

console = Console()

FESTIVALS = {
    "january": {
        "name": "Makar Sankranti",
        "description": "Winter harvest festival & kite flying 🪁",
    },
    "february": {
        "name": "Holi",
        "description": "Festival of colors & joy 🎨",
    },
    "march": {
        "name": "Gangaur",
        "description": "Women's festival celebrating spring 👩",
    },
    "april": {
        "name": "Navratri",
        "description": "Nine nights of goddess worship 🙏",
    },
    "may": {
        "name": "Teej",
        "description": "Swing festival during monsoon rain 🌧️",
    },
    "june": {
        "name": "Eid-ul-Fitr",
        "description": "Islamic festival of joy & sharing 🌙",
    },
    "july": {
        "name": "Hariyali Teej",
        "description": "Monsoon celebration of fertility 🌱",
    },
    "august": {
        "name": "Janmashtami",
        "description": "Krishna's birth anniversary 🕉️",
    },
    "september": {
        "name": "Ganesh Chaturthi",
        "description": "Elephant god festival & processions 🐘",
    },
    "october": {
        "name": "Dussehra",
        "description": "Victory of good over evil 🏹",
    },
    "november": {
        "name": "Pushkar Fair",
        "description": "Camel & cultural fair in Pushkar 🐪",
    },
    "december": {
        "name": "Diwali",
        "description": "Festival of lights & celebrations 🪔",
    },
}


@click.command()
@click.argument("month")
def festival(month):
    """
    🎉 Get Rajasthan festival info for a month.
    
    Examples: "January", "March", "October", "November"
    """
    month_lower = month.lower()
    
    if month_lower not in FESTIVALS:
        console.print()
        console.print(Panel(
            f"[red]❌ Invalid month: [bold]{month}[/bold][/red]\n\n"
            "[cyan]Try one of these:[/cyan]\n"
            "January, February, March, April, May, June,\n"
            "July, August, September, October, November, December",
            title="[bold red]Invalid Input[/bold red]",
            border_style="red",
            padding=(1, 2),
        ))
        console.print()
        return
    
    fest = FESTIVALS[month_lower]
    console.print()
    
    table = Table(title=f"🎉 {month.title()} Festival", show_header=True)
    table.add_column("Festival", style="cyan", no_wrap=False)
    table.add_column("Description", style="yellow")
    
    table.add_row(fest["name"], fest["description"])
    
    console.print(table)
    console.print()

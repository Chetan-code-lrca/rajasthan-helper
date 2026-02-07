"""
Festival command module - Display Rajasthan festivals by month.

This module demonstrates data management best practices:
- Hardcoded data ensures offline availability
- Structured format (dict of dicts) is easy to maintain and test
- Smart fallback handling for invalid months
- Rich formatting for better UX

Why this matters: Festivals are cultural treasures. By including all 12 months,
we educate users about Indian celebrations year-round. Fallback messages
encourage exploration even when a specific month has no major festival.
"""

from datetime import datetime
from rich.console import Console
from rich.panel import Panel
from rich.table import Table
import logging

# Configure logging for production monitoring
logger = logging.getLogger(__name__)
console = Console()

# Comprehensive festival data for all 12 months
# Structure: month_name → {"name": str, "description": str}
# This data is hardcoded for reliability (no API dependency)
FESTIVALS = {
    "January": {
        "name": "🪁 Makar Sankranti",
        "description": "Kite flying festival celebrating the sun god. Colors fill the sky as thousands gather on rooftops!",
    },
    "February": {
        "name": "🐪 Desert Festival",
        "description": "Vibrant celebration in Jaisalmer with camel races, folk music, and cultural performances in golden dunes.",
    },
    "March": {
        "name": "🎨 Holi",
        "description": "Festival of colors & joy. Celebrate spring with vibrant colored powder, joy, and togetherness.",
    },
    "April": {
        "name": "🎭 Mewar Festival",
        "description": "Traditional celebration in Udaipur with swings, traditional music, and cultural performances.",
    },
    "May": {
        "name": "🌞 Summer Fair",
        "description": "Local markets and cultural events across Rajasthan during the hot summer season.",
    },
    "June": {
        "name": "🪁 Teej",
        "description": "Swing festival celebrating monsoon arrival. Women celebrate with traditional swings and folk music.",
    },
    "July": {
        "name": "🌧️ Monsoon Festivals",
        "description": "Local celebrations welcoming rains. Fairs and markets showcase regional crafts and food.",
    },
    "August": {
        "name": "🤝 Raksha Bandhan",
        "description": "Brother-sister bond celebration. Sisters tie protective threads on brothers' wrists, a cherished tradition.",
    },
    "September": {
        "name": "🌾 Ganesh Chaturthi",
        "description": "Celebration of Lord Ganesh with decorations, prayers, and community gatherings.",
    },
    "October": {
        "name": "🪔 Diwali",
        "description": "Festival of lights & sweets. Illuminate your life with happiness, lamps, and family gatherings.",
    },
    "November": {
        "name": "🐪 Pushkar Camel Fair",
        "description": "Sacred camel trading fair. Experience Rajasthani culture with thousands of camels, horses, and folk performances.",
    },
    "December": {
        "name": "❄️ Winter Festivals",
        "description": "Music & dance celebrations. Warm evenings and cool nights filled with cultural programs and markets.",
    },
}


def show_festival(month: str = None) -> None:
    """
    Display Rajasthan festivals by month.
    
    Robustness strategy:
    - If no month: show all 12 festivals in a table (good overview)
    - If specific month: show festival details in a panel
    - If invalid month: show helpful message with month list
    
    Args:
        month: Month name (e.g., "March") or None to show all
    
    Why this approach: Users might not remember which festivals are which.
    By offering both table (all) and panel (single) views, we meet different
    user needs. The fallback message educates users about "hidden" festivals.
    """
    try:
        if month is None:
            # Show all festivals in a rich table (good for exploration)
            # Why table: Compact, scannable, good for comparing festivals
            logger.info("Displaying all festivals")

            table = Table(
                title="🎊 Rajasthan Festivals - All 12 Months",
                border_style="magenta",
            )
            table.add_column("Month", style="cyan", no_wrap=True)
            table.add_column("Festival", style="green", no_wrap=True)
            table.add_column("Description", style="yellow")

            for month_key, festival_data in FESTIVALS.items():
                table.add_row(
                    month_key,
                    festival_data["name"],
                    festival_data["description"],
                )

            console.print(table)

        else:
            # Show specific festival
            # Normalize input: accept "march", "March", "MARCH" etc.
            month_normalized = month.capitalize()
            logger.info(f"Looking up festival for month: {month_normalized}")

            if month_normalized not in FESTIVALS:
                # Invalid month - show helpful message
                available_months = ", ".join(FESTIVALS.keys())
                logger.warning(f"Invalid month requested: {month}")

                console.print(
                    Panel.fit(
                        f"[bold yellow]⚠️  Invalid Month: '{month}'[/bold yellow]\n\n"
                        f"[cyan]Available months:[/cyan]\n"
                        f"[green]{available_months}[/green]\n\n"
                        f"[dim]Tip: Use 'festival' with no month to see all festivals![/dim]",
                        border_style="yellow",
                        padding=(1, 2),
                    )
                )
                return

            # Display the specific festival in a rich panel
            festival_data = FESTIVALS[month_normalized]
            logger.info(f"Displayed festival for {month_normalized}")

            panel = Panel.fit(
                f"[bold green]{festival_data['name']}[/bold green]\n\n"
                f"[yellow]{festival_data['description']}[/yellow]",
                title=f"🎉 {month_normalized} Festival",
                border_style="green",
                padding=(1, 2),
            )
            console.print(panel)

    except Exception as e:
        # Catch-all for unexpected errors
        logger.error(f"Error displaying festival: {e}")

        console.print(
            Panel.fit(
                f"[bold red]❌ Unexpected Error[/bold red]\n"
                f"[yellow]{str(e)}[/yellow]",
                border_style="red",
                padding=(1, 2),
            )
        )


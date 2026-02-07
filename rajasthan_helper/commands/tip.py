"""
Travel tips command module - Display curated tips for major Indian cities.

This module demonstrates content organization best practices:
- Structured data (dict of lists) for easy maintenance
- Multiple tips per city for comprehensive guidance
- Rich formatting with emojis for better visual appeal
- Case-insensitive input for user-friendly experience

Why this matters: Travel tips should be practical and specific. By offering
multiple tips per city, we help users make the most of their visit.
Including diverse cities (major tourism + spiritual destinations) ensures
the app is useful for different user interests.
"""

from rich.console import Console
from rich.panel import Panel
import logging

# Configure logging for production monitoring
logger = logging.getLogger(__name__)
console = Console()

# Travel tips for major Indian cities
# Structure: city_name → [tip1, tip2, tip3, tip4]
# Each tip includes emoji for visual appeal and clarity
TIPS = {
    "Jaipur": [
        "🏰 Visit Amber Fort at sunset for breathtaking views and cool evening temperature",
        "🛍️ Explore the colorful bazaars of the old city for local crafts and textiles",
        "🍲 Try authentic Rajasthani dal baati churma at street markets or local restaurants",
        "🎨 Stay at one of the heritage hotels to experience royal Rajasthani hospitality",
    ],
    "Udaipur": [
        "🚤 Take a romantic boat ride on Lake Pichola with sunset views and floating palaces",
        "🏛️ Visit the magnificent City Palace with both heritage museum and royal sections",
        "🍲 Enjoy lakeside street food and local delicacies, especially gatte ki sabzi",
        "📸 Watch the sunset from Jheel Fatehnuma Kund for stunning photography opportunities",
    ],
    "Delhi": [
        "🕌 Visit the Red Fort (Lal Qila) and Jama Masjid for Mughal history and architecture",
        "🏛️ Explore India Gate and nearby museums for independence history and culture",
        "🍜 Try street food at Chandni Chowk: chaat, kebabs, and traditional sweets",
        "🏰 Discover Humayun's Tomb's stunning architecture and peaceful gardens",
    ],
    "Mumbai": [
        "🥔 Try street vada pav (potato fritter in bread) - Mumbai's beloved street food",
        "🌉 Visit the iconic Gateway of India, especially during evening twilight hours",
        "🛍️ Shop at the bustling Crawford Market for spices, produce, and local crafts",
        "🏖️ Relax at Chowpatty Beach, enjoy bhel puri, and watch the sunset",
    ],
    "Jodhpur": [
        "🏰 Explore the majestic Mehrangarh Fort with panoramic city views and museum exhibits",
        "🔵 Walk through the distinctive blue-painted city streets for photography and local life",
        "🌶️ Shop for authentic Rajasthani spices, textiles, and traditional handicrafts",
        "🌅 Watch the sunset from Mehrangarh Fort to see the entire blue city bathed in golden light",
    ],
    "Jaisalmer": [
        "🏜️ Experience a camel safari in the Thar Desert at sunrise or sunset for magical views",
        "🏰 Explore the intricate golden havelis (mansions) with stunning stone carvings",
        "📸 Capture stunning desert sunset photographs and enjoy folk music performances",
        "🎪 Experience desert night camps with traditional Rajasthani music and dance",
    ],
    "Agra": [
        "🕌 Witness the timeless beauty of Taj Mahal, ideally at sunrise for soft light",
        "🏰 Explore the red sandstone Agra Fort with three levels of history and views",
        "🌅 Visit Taj Mahal at sunrise (before crowds) for the best photography and experience",
        "🍴 Try Agra's famous petha (pumpkin sweet) and local Mughlai cuisine",
    ],
    "Pushkar": [
        "🕌 Visit the sacred Pushkar Lake temples and ghats for spiritual experience",
        "🐪 Experience the famous Pushkar Camel Fair (November) with thousands of animals",
        "🎭 Discover traditional Rajasthani culture through music, dance, and local artisans",
        "🛍️ Shop for unique handicrafts, textiles, and spiritual items from local shops",
    ],
    "Bikaner": [
        "🏰 Visit the impressive Junagarh Fort with stunning architecture and historic charm",
        "🐪 Experience the Bikaner Camel Festival (January-February) with races and performances",
        "🍪 Shop for Bikaner's famous bhujia (snack) and traditional milk sweets",
        "📸 Explore Lalgarh Palace's architectural beauty and heritage hotel experience",
    ],
    "Ajmer": [
        "🕌 Visit Dargah Sharif, one of India's most important pilgrimage sites for Sufism",
        "👥 Experience the diverse religious and cultural significance of this holy city",
        "🌊 Visit Anasagar Lake for peaceful boat rides and beautiful evening views",
        "🕯️ Witness the spiritual devotion during Friday prayers and special occasions",
    ],
}


def get_tip(city: str) -> None:
    """
    Display travel tips for a city.
    
    Robustness strategy:
    - Accept case-insensitive input (user-friendly)
    - If city not found: show helpful list of available cities
    - Display tips in rich panel with emojis (visual appeal)
    
    Args:
        city: City name (e.g., "Jaipur")
    
    Why this approach: Travel planning is subjective. By providing multiple
    curated tips per city, we help users understand diverse attractions
    and experiences. The emoji prefix helps users scan tips quickly.
    """
    try:
        # Normalize city input: accept "jaipur", "Jaipur", "JAIPUR" etc.
        city_normalized = city.capitalize()
        logger.info(f"Looking up tips for city: {city_normalized}")

        if city_normalized not in TIPS:
            # City not found - show helpful error with available cities
            available_cities = ", ".join(TIPS.keys())
            logger.warning(f"City not found: {city}")

            console.print(
                Panel.fit(
                    f"[bold red]❌ City Not Found[/bold red]\n\n"
                    f"[yellow]We don't have tips for '{city}'.[/yellow]\n\n"
                    f"[cyan]Available cities:[/cyan]\n"
                    f"[green]{available_cities}[/green]",
                    border_style="red",
                    padding=(1, 2),
                )
            )
            return

        # Get tips for the city and join with newlines
        # Each tip already has an emoji prefix for visual clarity
        tips_list = TIPS[city_normalized]
        tips_content = "\n".join(tips_list)
        logger.info(f"Displayed tips for {city_normalized}")

        # Display in a rich panel with green border (welcoming color for travel advice)
        panel = Panel.fit(
            tips_content,
            title=f"🗺️  Travel Tips for {city_normalized}",
            border_style="green",
            padding=(1, 2),
        )
        console.print(panel)

    except Exception as e:
        # Catch-all for unexpected errors
        logger.error(f"Error displaying tips: {e}")

        console.print(
            Panel.fit(
                f"[bold red]❌ Unexpected Error[/bold red]\n"
                f"[yellow]{str(e)}[/yellow]",
                border_style="red",
                padding=(1, 2),
            )
        )



"""Display fun facts about Rajasthan cities."""
import click
from rich.console import Console
from rich.panel import Panel

from ..data.facts import CITY_FACTS

console = Console()

@click.command()
@click.argument('city')
def facts(city: str):
    """Show fun facts and trivia about a city.
    
    Example: rajasthan-helper facts jaipur
    """
    city_lower = city.lower()
    
    console.print(f"[bold magenta]✨ Curious about {city.title()}? Here are some fun facts to wow you![/bold magenta]\n")
    
    if city_lower in CITY_FACTS:
        facts_list = CITY_FACTS[city_lower]
        content = "\n\n".join(facts_list)
        
        console.print(Panel(
            content,
            title=f"🌟 Fun Facts: {city.title()}",
            border_style="magenta",
            padding=(1, 2)
        ))
        console.print(f"\n[green]Travel tip: If you're heading to {city.title()}, these facts make the history come alive! Pack your camera and explore. 🏰[/green]")
    else:
        available = ", ".join([c.title() for c in CITY_FACTS.keys()])
        console.print(Panel(
            f"[red]Oops, I don't have facts for '{city}' in my collection yet![/red]\n\n"
            f"📍 But I do have juicy details for: {available}\n\n"
            "💡 Pick one above, or let me know if you'd like me to add more cities—I'm always expanding!",
            title="❌ City Not Found",
            border_style="red"
        ))
CITY_FACTS = {
    # Rajasthan (existing + expanded)
    'jaipur': [
        "🏰 Known as the 'Pink City' - painted pink in 1876 to welcome Prince of Wales",
        "👑 Founded in 1727 by Maharaja Jai Singh II, a brilliant astronomer",
        "🌟 Home to 3 UNESCO World Heritage Sites: Amber Fort, Jantar Mantar, and City Palace",
        "🎨 Famous for traditional block printing and blue pottery"
    ],
    'udaipur': [
        "💎 Called the 'City of Lakes' with 5 major lakes",
        "🎬 Famous Bollywood & Hollywood filming location (Octopussy, The Best Exotic Marigold Hotel)",
        "👑 City Palace is one of the largest palace complexes in Rajasthan",
        "🌅 Known for stunning sunsets over Lake Pichola"
    ],
    'jaisalmer': [
        "🏜️ The 'Golden City' - named for its yellow sandstone architecture",
        "🐪 Gateway to the Thar Desert with stunning sand dunes",
        "🏰 Jaisalmer Fort is one of the few 'living forts' with residents inside",
        "✨ Famous for desert camping and camel safaris"
    ],
    'jodhpur': [
        "💙 The 'Blue City' - many houses painted blue to denote Brahmin caste",
        "🏰 Mehrangarh Fort is one of India's largest forts, 400 feet above the city",
        "🎪 Famous for handicrafts, especially textiles and antiques",
        "☀️ Known as 'Sun City' for bright, sunny weather year-round"
    ],
    'pushkar': [
        "🐪 Hosts the world's largest camel fair every November",
        "🛕 One of few cities with a temple dedicated to Lord Brahma",
        "🌊 Sacred Pushkar Lake with 52 bathing ghats",
        "🕉️ Important pilgrimage site for Hindus"
    ],
    
    # Other Indian States/Cities
    'delhi': [
        "🏛️ Capital of India with over 1,400 years of history",
        "🕌 Home to 3 UNESCO World Heritage Sites: Red Fort, Qutub Minar, and Humayun's Tomb",
        "🍛 Street food paradise - try chaat, parathas, and kebabs",
        "🚇 Has India's largest metro network"
    ],
    'mumbai': [
        "🎬 Bollywood capital - produces over 1,000 films annually",
        "🏝️ Built on 7 islands that were merged together",
        "🌊 Home to Marine Drive, the 'Queen's Necklace'",
        "💼 Financial capital and most populous city in India"
    ],
    'kerala': [
        "🌿 Known as 'God's Own Country' for its natural beauty",
        "🚣 Famous for backwater cruises and houseboats",
        "🍃 Home to spice plantations and Ayurvedic traditions",
        "🏖️ Coastal areas with Chinese fishing nets"
    ],
    'punjab': [
        "🌾 'Breadbasket of India' - major wheat producer",
        "🕌 Birthplace of Sikhism with the Golden Temple",
        "🍛 Famous for Punjabi cuisine like butter chicken",
        "🎉 Vibrant festivals like Baisakhi"
    ],
    
    # Continents (general facts, India/Rajasthan-inspired)
    'asia': [
        "🌏 Largest continent, home to over 4.6 billion people",
        "🏛️ Birthplace of ancient civilizations like India's Indus Valley",
        "🍜 Diverse cuisines, from Rajasthan's thalis to China's dumplings",
        "🏔️ Features deserts (like Thar) and mountains (Himalayas)"
    ],
    'europe': [
        "🏰 Known for castles and medieval history, like Rajasthan's forts",
        "🇪🇺 27 countries in the EU, with rich cultural diversity",
        "🍷 Famous for wines and cheeses, akin to India's regional foods",
        "🌆 Modern cities like Paris, with historical roots"
    ],
    'africa': [
        "🦁 Home to the 'Big Five' animals and vast savannas",
        "🏜️ Includes deserts like the Sahara, similar to Rajasthan's Thar",
        "🎨 Rich in art, music, and ancient pyramids",
        "🌍 54 countries, with diverse climates from jungles to coasts"
    ],
    'north america': [
        "🏔️ Features Rockies and Niagara Falls",
        "🇺🇸 Includes the USA, Canada, and Mexico",
        "🍔 Known for fast food, but also indigenous cultures",
        "🚀 Birthplace of modern technology and space exploration"
    ],
    'south america': [
        "🌳 Amazon Rainforest, the 'lungs of the Earth'",
        "🏔️ Andes Mountains, great for hiking like Rajasthan's hills",
        "🎉 Vibrant festivals like Carnival, with dance and music",
        "🇧🇷 Home to Brazil, Argentina, and ancient Incan ruins"
    ],
    'australia': [
        "🦘 Known for kangaroos and the Great Barrier Reef",
        "🏜️ Includes deserts and unique wildlife",
        "🌊 Surrounded by ocean, with beaches like India's coasts",
        "🇦🇺 Indigenous cultures with ancient Dreamtime stories"
    ],
    'antarctica': [
        "❄️ Coldest continent, covered in ice",
        "🐧 Home to penguins and seals",
        "🔬 No permanent residents, only research stations",
        "🌍 Important for climate studies and global weather"
    ]
}

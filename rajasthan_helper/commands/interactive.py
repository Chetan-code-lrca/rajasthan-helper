"""Interactive mode for Rajasthan Helper CLI."""
import click
from rich.console import Console
from rich.prompt import Prompt, Confirm
from rich.panel import Panel

from .weather import get_weather
from .festival import show_festival
from .tip import get_tip
from .facts import facts

console = Console()

@click.command()
def interactive():
    """Launch interactive mode for exploring Rajasthan."""
    console.print(Panel(
        "[bold cyan]🏜️ Welcome to Rajasthan Helper Interactive Mode![/bold cyan]\n\n"
        "I'm your friendly guide to Rajasthan's wonders. Let's explore weather, festivals, tips, and facts together!",
        title="🕌 Your Rajasthan Adventure Starts Here",
        border_style="cyan"
    ))
    
    while True:
        console.print()
        choice = Prompt.ask(
            "What sparks your curiosity today?",
            choices=["weather", "festival", "tips", "facts", "exit"],
            default="weather"
        )
        
        if choice == "exit":
            console.print("[green]👋 Thanks for exploring with me! Safe travels and come back soon. Rajasthan misses you already! 🌟[/green]")
            break
            
        elif choice == "weather":
            city = Prompt.ask("Which city are you dreaming of?", default="Jaipur")
            from click.testing import CliRunner
            runner = CliRunner()
            runner.invoke(get_weather, [city])
            
        elif choice == "festival":
            month = Prompt.ask(
                "Pick a month to see the celebrations (or press Enter for all)",
                default=""
            )
            from click.testing import CliRunner
            runner = CliRunner()
            runner.invoke(show_festival, [month] if month else [])
            
        elif choice == "tips":
            city = Prompt.ask("Where are you heading for travel advice?", default="Jaipur")
            from click.testing import CliRunner
            runner = CliRunner()
            runner.invoke(get_tip, [city])
            
        elif choice == "facts":
            city = Prompt.ask("Which city's secrets do you want to uncover?", default="Jaipur")
            from click.testing import CliRunner
            runner = CliRunner()
            runner.invoke(facts, [city])
        
        if not Confirm.ask("\n[cyan]Ready for more Rajasthan magic?[/cyan]", default=True):
            console.print("[green]👋 Until next time! Keep the wanderlust alive. 🏜️[/green]")
            break

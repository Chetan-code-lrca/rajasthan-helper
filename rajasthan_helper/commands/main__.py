"""Rajasthan Helper CLI - Main entry point."""
import click
from rich.console import Console

from rajasthan_helper.commands.weather import get_weather
from rajasthan_helper.commands.festival import show_festival
from rajasthan_helper.commands.tip import get_tip
from rajasthan_helper.commands.facts import facts
from rajasthan_helper.commands.interactive import interactive

console = Console()

@click.group()
@click.version_option(version="1.0.0")
def cli():
    """🏜️ Rajasthan Helper - Your guide to Rajasthan travel!

    Get weather updates, festival information, travel tips, and fun facts
    about Rajasthan and India.
    """
    pass

# Register commands
cli.add_command(get_weather)
cli.add_command(show_festival)
cli.add_command(get_tip)
cli.add_command(facts)
cli.add_command(interactive)

if __name__ == "__main__":
    cli()

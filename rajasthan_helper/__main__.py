"""Rajasthan Helper CLI – Main entry point with Click group."""

import click
from rich.console import Console

from rajasthan_helper.commands.weather import weather
from rajasthan_helper.commands.festival import festival
from rajasthan_helper.commands.tip import tip

console = Console()


@click.group()
@click.version_option(
    version="0.1.0",
    prog_name="rajasthan-helper",
    message="%(prog)s %(version)s - Built with free GitHub Copilot CLI by Chetan Inaganti 🏜️"
)
def cli():
    """
    🏜️  Rajasthan Helper CLI – Discover the Land of Kings! 🏜️
    
    Get real-time weather, festivals, and travel tips for Rajasthan & India.
    """
    pass


cli.add_command(weather)
cli.add_command(festival)
cli.add_command(tip)


def main():
    """Main entry point."""
    cli()


if __name__ == "__main__":
    main()

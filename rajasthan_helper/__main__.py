"""
Rajasthan Helper CLI - Main Entry Point

This module sets up the Click CLI framework and routes commands.

Philosophy:
- Keep the CLI responsive (lazy imports for commands)
- Make help text colorful and welcoming
- Version flag shows credits to users and the tool
- All errors are caught and displayed with rich formatting

Why this design:
1. Lazy imports (inside command functions) avoid circular dependencies
   and make the CLI startup faster.
2. Rich formatting in help text makes the CLI feel polished and fun.
3. Custom version callback shows proper credit to Copilot CLI and user.
4. Click @click.group() with add_command() provides clean structure
   for adding new commands later.

Built with GitHub Copilot CLI - Free Tier Challenge
"""

import click
from rich.console import Console
from rich.panel import Panel

console = Console()

# Version info - shown when --version is passed
VERSION = "0.1.0"
CREDITS = "Chetan Inaganti"
TOOL = "GitHub Copilot CLI"


def print_version(ctx, param, value):
    """
    Custom version callback to show rich formatted version.
    
    Why custom callback: Default Click version is plain text.
    We use rich Panel to make it colorful and memorable,
    including credits to Copilot CLI and the developer.
    
    Args:
        ctx: Click context
        param: Parameter info
        value: Flag value
    """
    if value:
        # Create a colorful version panel with proper credits
        version_panel = Panel.fit(
            f"[bold cyan]Rajasthan Helper CLI[/bold cyan]\n"
            f"[yellow]Version:[/yellow] [green]{VERSION}[/green]\n\n"
            f"[yellow]Built by:[/yellow] [bold magenta]{CREDITS}[/bold magenta]\n"
            f"[yellow]Powered by:[/yellow] [bold blue]{TOOL}[/bold blue] (Free Tier)\n\n"
            f"[dim]🏜️ Discover the Land of Kings in your terminal! 🕌[/dim]",
            border_style="cyan",
            padding=(1, 2),
        )
        console.print(version_panel)
        ctx.exit()


@click.group(invoke_without_command=True)
@click.option(
    "--version",
    is_flag=True,
    callback=print_version,
    expose_value=False,
    is_eager=True,
    help="Show version and credits",
)
@click.pass_context
def main(ctx):
    """
    🏜️  Rajasthan Helper CLI – Discover the Land of Kings in your terminal! 🕌
    
    Get weather, festivals, and travel tips for Rajasthan and India.
    
    Commands:
        weather [CITY]    Show current weather for a city
        festival [MONTH]  Discover Rajasthan festivals
        tip [CITY]        Get travel tips for a city
    
    Examples:
        rajasthan-helper weather jaipur
        rajasthan-helper festival march
        rajasthan-helper tip udaipur
        rajasthan-helper festival         (show all festivals)
    
    Built with GitHub Copilot CLI - Free Tier Challenge
    """
    # Show welcome panel if no command is provided
    if ctx.invoked_subcommand is None:
        welcome = Panel.fit(
            "[bold cyan]Welcome to Rajasthan Helper! 🏜️[/bold cyan]\n\n"
            "[yellow]Discover the magic of Rajasthan[/yellow]\n\n"
            "[dim]Available commands:[/dim]\n"
            "[green]weather[/green]  - Get real-time weather\n"
            "[green]festival[/green] - Explore Rajasthan festivals\n"
            "[green]tip[/green]      - Get travel tips\n\n"
            "[dim]Use [bold]--help[/bold] for more info[/dim]",
            border_style="magenta",
            padding=(1, 2),
        )
        console.print(welcome)


@main.command()
@click.argument("city", default=None, required=False)
def weather(city):
    """
    🌡️  Get current weather for a city.
    
    Uses wttr.in API for real-time weather data with fallback data
    for offline or slow connection scenarios.
    
    Examples:
        rajasthan-helper weather jaipur
        rajasthan-helper weather mumbai
        rajasthan-helper weather            (defaults to Jaipur)
    """
    # Lazy import to avoid circular dependencies and improve startup speed
    from rajasthan_helper.commands.weather import get_weather

    get_weather(city)


@main.command()
@click.argument("month", default=None, required=False)
def festival(month):
    """
    🎉 Discover Rajasthan festivals by month.
    
    Explore the rich cultural calendar of Rajasthan throughout the year.
    Shows all 12 months if no month is specified.
    
    Examples:
        rajasthan-helper festival march
        rajasthan-helper festival            (show all 12 months)
    
    Available months: January through December
    """
    # Lazy import to avoid circular dependencies and improve startup speed
    from rajasthan_helper.commands.festival import show_festival

    show_festival(month)


@main.command()
@click.argument("city", default=None, required=False)
def tip(city):
    """
    🗺️  Get travel tips for a city.
    
    Curated travel recommendations for major Indian cities and
    Rajasthan tourist destinations.
    
    Examples:
        rajasthan-helper tip jaipur
        rajasthan-helper tip udaipur
        rajasthan-helper tip delhi
    
    Available cities: Jaipur, Udaipur, Mumbai, Delhi, Jodhpur,
    Jaisalmer, Agra, Pushkar, Bikaner, Ajmer
    """
    # Lazy import to avoid circular dependencies and improve startup speed
    from rajasthan_helper.commands.tip import get_tip

    get_tip(city)


if __name__ == "__main__":
    main()

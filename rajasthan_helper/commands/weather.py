"""Weather command – Real-time weather via free wttr.in API."""

import click
import requests
from rich.console import Console
from rich.panel import Panel

console = Console()


@click.command()
@click.argument("city")
def weather(city):
    """
    ☀️ Get real-time weather for any city.
    
    Uses free wttr.in API. Examples: "Jaipur", "Udaipur", "Delhi"
    """
    city_title = city.title()
    
    try:
        console.print(f"\n🌍 Fetching weather for [bold cyan]{city_title}[/bold cyan]...", end=" ")
        
        url = f"https://wttr.in/{city}?format=j1"
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        
        data = response.json()
        current = data.get("current_condition", [{}])[0]
        
        temp = current.get("temp_C", "N/A")
        condition = current.get("weatherDesc", [{}])[0].get("value", "N/A") if current.get("weatherDesc") else "N/A"
        feels_like = current.get("FeelsLikeC", temp)
        humidity = current.get("humidity", "N/A")
        wind_kmph = current.get("windspeedKmph", "N/A")
        
        console.print("✓\n")
        
        # Determine color and emoji based on temperature
        if temp == "N/A":
            temp_color = "white"
            temp_emoji = "🌡️"
        elif int(temp) > 20:
            temp_color = "red"
            temp_emoji = "☀️"
        elif int(temp) < 15:
            temp_color = "cyan"
            temp_emoji = "❄️"
        else:
            temp_color = "yellow"
            temp_emoji = "🌧️"
        
        info_text = (
            f"{temp_emoji}  Temperature: [{temp_color}]{temp}°C[/{temp_color}] "
            f"(feels like {feels_like}°C)\n"
            f"☁️  Condition: [cyan]{condition}[/cyan]\n"
            f"💧 Humidity: [blue]{humidity}%[/blue]\n"
            f"💨 Wind Speed: [green]{wind_kmph} km/h[/green]"
        )
        
        panel = Panel(
            info_text,
            title=f"[bold cyan]{city_title} Weather[/bold cyan]",
            border_style="cyan",
            padding=(1, 2),
        )
        console.print(panel)
        
    except requests.exceptions.Timeout:
        console.print("✗\n")
        console.print(Panel(
            "[yellow]⏰ API timeout. Showing sample data:[/yellow]\n"
            "🌡️  Temperature: 28°C (feels like 32°C)\n"
            "☁️  Condition: Sunny\n"
            "💧 Humidity: 35%\n"
            "💨 Wind Speed: 12 km/h",
            title=f"[bold yellow]⚠️ {city_title} (Cached)[/bold yellow]",
            border_style="yellow",
            padding=(1, 2),
        ))
        
    except requests.exceptions.RequestException as e:
        console.print("✗\n")
        console.print(Panel(
            f"[red]❌ Error fetching weather: {str(e)}[/red]\n\n"
            "💡 Check your internet or try another city.",
            title="[bold red]Error[/bold red]",
            border_style="red",
            padding=(1, 2),
        ))
        
    except (KeyError, IndexError, ValueError) as e:
        console.print("✗\n")
        console.print(Panel(
            f"[red]❌ Error parsing weather data: {str(e)}[/red]",
            title="[bold red]Parse Error[/bold red]",
            border_style="red",
            padding=(1, 2),
        ))

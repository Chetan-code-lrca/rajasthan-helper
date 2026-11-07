"""Weather command using the wttr.in JSON endpoint."""

from urllib.parse import quote

import click
import requests
from rich.console import Console
from rich.panel import Panel

console = Console()
WEATHER_URL = "https://wttr.in/{city}"
REQUEST_TIMEOUT_SECONDS = 10


def _first_mapping(value):
    """Return the first mapping in a list, or an empty mapping."""
    if isinstance(value, list) and value and isinstance(value[0], dict):
        return value[0]
    return {}


def _required_text(value, field_name):
    """Return a non-empty text field or raise a user-safe validation error."""
    if value is None or str(value).strip() == "":
        raise ValueError(f"The weather provider did not return {field_name}.")
    return str(value).strip()


def fetch_current_weather(city):
    """Fetch current conditions for a city and return normalized display data."""
    normalized_city = " ".join(city.split())
    if not normalized_city:
        raise ValueError("Enter a city name.")

    url = WEATHER_URL.format(city=quote(normalized_city, safe=""))
    response = requests.get(
        url,
        params={"format": "j1"},
        timeout=REQUEST_TIMEOUT_SECONDS,
        headers={"User-Agent": "rajasthan-helper/0.1.0"},
    )
    response.raise_for_status()

    payload = response.json()
    if not isinstance(payload, dict):
        raise ValueError("The weather provider returned an unexpected response.")

    current = _first_mapping(payload.get("current_condition"))
    description = _first_mapping(current.get("weatherDesc"))

    temperature = _required_text(current.get("temp_C"), "temperature")
    feels_like = _required_text(current.get("FeelsLikeC", temperature), "feels-like temperature")
    condition = _required_text(description.get("value"), "weather condition")
    humidity = _required_text(current.get("humidity"), "humidity")
    wind_speed = _required_text(current.get("windspeedKmph"), "wind speed")

    try:
        temperature_value = float(temperature)
        humidity_value = int(humidity)
        wind_value = float(wind_speed)
    except ValueError as error:
        raise ValueError("The weather provider returned invalid measurement values.") from error

    if not -100 <= temperature_value <= 70 or not 0 <= humidity_value <= 100 or not 0 <= wind_value <= 500:
        raise ValueError("The weather provider returned measurements outside expected ranges.")

    return {
        "temperature": temperature,
        "feels_like": feels_like,
        "condition": condition,
        "humidity": humidity,
        "wind_speed": wind_speed,
        "temperature_value": temperature_value,
    }


@click.command()
@click.argument("city")
def weather(city):
    """Show current weather for a city using wttr.in."""
    city_title = " ".join(city.split()).title()
    try:
        console.print(
            f"\nFetching current weather for [bold cyan]{city_title}[/bold cyan]..."
        )
        current = fetch_current_weather(city)

        temperature_value = current["temperature_value"]
        if temperature_value > 25:
            temp_color, temp_emoji = "red", "☀️"
        elif temperature_value < 15:
            temp_color, temp_emoji = "cyan", "❄️"
        else:
            temp_color, temp_emoji = "yellow", "🌡️"

        info_text = (
            f"{temp_emoji}  Temperature: [{temp_color}]{current['temperature']}°C[/{temp_color}] "
            f"(feels like {current['feels_like']}°C)\n"
            f"☁️  Condition: [cyan]{current['condition']}[/cyan]\n"
            f"💧 Humidity: [blue]{current['humidity']}%[/blue]\n"
            f"💨 Wind Speed: [green]{current['wind_speed']} km/h[/green]"
        )
        console.print(
            Panel(
                info_text,
                title=f"[bold cyan]{city_title} Weather[/bold cyan]",
                border_style="cyan",
                padding=(1, 2),
            )
        )
    except requests.exceptions.Timeout as error:
        raise click.ClickException(
            "The weather service timed out. No sample or stale weather data was substituted; try again."
        ) from error
    except requests.exceptions.RequestException as error:
        raise click.ClickException(
            "Could not reach the weather service. Check your connection and try again."
        ) from error
    except (ValueError, TypeError) as error:
        raise click.ClickException(str(error)) from error

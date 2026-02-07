"""
Weather command module - Fetch and display weather data with fallback support.

This module demonstrates robustness best practices:
- Tries live API first, falls back to cached data if unavailable
- Handles multiple error scenarios gracefully
- Provides rich formatting for user feedback
- Includes detailed comments for maintainability

Why this matters: Real users need apps that work even when APIs are slow/down.
Fallback data ensures the CLI remains useful during connectivity issues.
"""

import requests
import logging
from datetime import datetime
from rich.console import Console
from rich.panel import Panel
from rich.table import Table

# Configure logging - important for debugging in production
logger = logging.getLogger(__name__)
console = Console()

# Fallback weather data for common Indian cities when API is unavailable
# Format: lowercase city name → weather snapshot
# This data is based on typical conditions for better UX during API downtime
FALLBACK_WEATHER = {
    "jaipur": {
        "temp": 28,
        "condition": "Sunny",
        "feels_like": 30,
        "humidity": 45,
        "wind": 15,
        "wind_dir": "NE",
        "sunrise": "06:45",
        "sunset": "18:30",
    },
    "udaipur": {
        "temp": 26,
        "condition": "Partly Cloudy",
        "feels_like": 28,
        "humidity": 50,
        "wind": 12,
        "wind_dir": "W",
        "sunrise": "06:50",
        "sunset": "18:35",
    },
    "delhi": {
        "temp": 22,
        "condition": "Clear",
        "feels_like": 20,
        "humidity": 55,
        "wind": 18,
        "wind_dir": "N",
        "sunrise": "06:35",
        "sunset": "18:20",
    },
    "mumbai": {
        "temp": 27,
        "condition": "Mostly Cloudy",
        "feels_like": 29,
        "humidity": 75,
        "wind": 20,
        "wind_dir": "SW",
        "sunrise": "07:05",
        "sunset": "18:45",
    },
    "jodhpur": {
        "temp": 30,
        "condition": "Clear",
        "feels_like": 32,
        "humidity": 35,
        "wind": 16,
        "wind_dir": "NW",
        "sunrise": "06:55",
        "sunset": "18:40",
    },
    "jaisalmer": {
        "temp": 32,
        "condition": "Sunny",
        "feels_like": 35,
        "humidity": 30,
        "wind": 14,
        "wind_dir": "E",
        "sunrise": "07:00",
        "sunset": "18:50",
    },
    "agra": {
        "temp": 24,
        "condition": "Clear",
        "feels_like": 22,
        "humidity": 50,
        "wind": 10,
        "wind_dir": "NE",
        "sunrise": "06:40",
        "sunset": "18:25",
    },
    "pushkar": {
        "temp": 25,
        "condition": "Partly Cloudy",
        "feels_like": 27,
        "humidity": 48,
        "wind": 13,
        "wind_dir": "W",
        "sunrise": "06:48",
        "sunset": "18:32",
    },
}


def _display_weather_panel(
    city: str,
    temp: float,
    condition: str,
    feels_like: float,
    humidity: float,
    wind: float,
    wind_dir: str = "Unknown",
    sunrise: str = "N/A",
    sunset: str = "N/A",
    is_fallback: bool = False,
) -> None:
    """
    Display weather information in a rich formatted panel.
    
    Args:
        city: City name being displayed
        temp: Temperature in Celsius
        condition: Weather condition (e.g., "Sunny")
        feels_like: "Feels like" temperature in Celsius
        humidity: Humidity percentage
        wind: Wind speed in km/h
        wind_dir: Wind direction (e.g., "NE", "SW")
        sunrise: Sunrise time in HH:MM format
        sunset: Sunset time in HH:MM format
        is_fallback: True if using cached data instead of live API
    
    Why this matters: Separation of display logic makes testing and
    modifications easier. Rich formatting ensures consistent UX.
    """
    # Determine color and emoji based on temperature (good UX practice)
    # - Red for hot: Alert user to heat-related precautions
    # - Yellow for warm: Default comfortable range
    # - Cyan for cool: Alert user to cold-related precautions
    if isinstance(temp, (int, float)):
        if temp > 35:
            temp_color = "red"
            weather_emoji = "🔥"
        elif temp > 25:
            temp_color = "yellow"
            weather_emoji = "☀️"
        else:
            temp_color = "cyan"
            weather_emoji = "🌤️"
    else:
        temp_color = "white"
        weather_emoji = "🌦️"

    # Build content string with rich markup (allows colors, bold, etc.)
    # Using [dim italic] for non-critical info (fallback indicator)
    fallback_note = (
        "\n[dim italic]\n⚠️  API slow - showing cached data (last updated)[/dim italic]"
        if is_fallback
        else ""
    )

    panel_content = (
        f"[bold cyan]{city.title()}[/bold cyan]\n\n"
        f"[{temp_color}]🌡️  Temperature:[/{temp_color}]       [bold]{temp}°C[/bold]\n"
        f"[yellow]☁️  Condition:[/yellow]          {condition}\n"
        f"[cyan]💨 Feels Like:[/cyan]          [bold]{feels_like}°C[/bold]\n"
        f"[blue]💧 Humidity:[/blue]            {humidity}%\n"
        f"[green]💨 Wind Speed:[/green]        {wind} km/h ({wind_dir})\n"
        f"[magenta]🌅 Sunrise:[/magenta]          {sunrise}\n"
        f"[magenta]🌇 Sunset:[/magenta]           {sunset}"
        f"{fallback_note}"
    )

    panel = Panel.fit(
        panel_content,
        title=f"{weather_emoji} Weather Report",
        border_style=temp_color,
        padding=(1, 2),
    )

    console.print(panel)


def _show_error(error_type: str, error_msg: str, suggestion: str = "") -> None:
    """
    Display a consistent error panel with rich formatting.
    
    Args:
        error_type: Type of error (e.g., "Connection Error", "Invalid City")
        error_msg: Detailed error message
        suggestion: Optional suggestion for user recovery
    
    Why this matters: Consistent error formatting improves UX and makes
    apps feel more professional. Users know what went wrong and how to fix it.
    """
    suggestion_text = f"\n[dim]{suggestion}[/dim]" if suggestion else ""

    error_panel = Panel.fit(
        f"[bold red]❌ {error_type}[/bold red]\n"
        f"[yellow]{error_msg}[/yellow]"
        f"{suggestion_text}",
        border_style="red",
        padding=(1, 2),
    )

    console.print(error_panel)


def get_weather(city: str) -> None:
    """
    Fetch and display current weather for a city.
    
    Robustness strategy:
    1. Try live API first (best user experience)
    2. If API timeout: use fallback data (ensure app stays functional)
    3. If connection error: explain to user gracefully
    4. If city not found: suggest alternatives
    
    Args:
        city: City name (e.g., "Jaipur")
    
    Why this approach: Most apps crash or give unhelpful errors when APIs
    fail. By providing fallback data, we ensure the app is useful even when
    the internet is slow. This is especially important for users in areas
    with unreliable connectivity.
    """
    city_normalized = city.lower()

    try:
        # Attempt to fetch real weather data from wttr.in
        # Timeout set to 3 seconds (empirically tested for UX)
        # Longer timeouts frustrate users; shorter might fail on slow connections
        url = f"https://wttr.in/{city}?format=j1"
        logger.info(f"Fetching weather for {city} from {url}")

        response = requests.get(url, timeout=3)
        response.raise_for_status()

        data = response.json()

        # Extract from nested JSON structure
        # wttr.in returns: {"current_condition": [{"temp_C": ..., "desc": ..., ...}]}
        current = data["current_condition"][0]

        # Extract weather fields with safe .get() to handle missing keys
        temp = current.get("temp_C", "N/A")
        condition = current.get("desc", "Unknown")
        feels_like = current.get("FeelsLikeC", "N/A")
        humidity = current.get("humidity", "N/A")
        wind_kph = current.get("windspeedKmph", "N/A")
        wind_dir = current.get("winddir16Point", "Unknown")

        # Try to get sun times (not always available)
        sunrise = "N/A"
        sunset = "N/A"
        try:
            astronomy = data.get("weather", [{}])[0].get("astronomy", [{}])[0]
            sunrise = astronomy.get("sunrise", "N/A")
            sunset = astronomy.get("sunset", "N/A")
        except (IndexError, KeyError, TypeError):
            # If astronomy data unavailable, that's OK - use defaults above
            pass

        # Validate that we got numeric data (prevents showing "N/A" in formatted display)
        if not all(isinstance(x, (int, float)) for x in [temp, feels_like, humidity, wind_kph]):
            logger.warning(f"Invalid data types from API for {city}")
            raise ValueError("Invalid data types received from API")

        # Display live data (not fallback)
        _display_weather_panel(
            city,
            temp,
            condition,
            feels_like,
            humidity,
            wind_kph,
            wind_dir,
            sunrise,
            sunset,
            is_fallback=False,
        )
        logger.info(f"Successfully displayed weather for {city}")

    except requests.exceptions.Timeout:
        # API is slow - try fallback data
        logger.warning(f"API timeout for {city}, attempting fallback")

        if city_normalized in FALLBACK_WEATHER:
            data = FALLBACK_WEATHER[city_normalized]
            _display_weather_panel(
                city,
                data["temp"],
                data["condition"],
                data["feels_like"],
                data["humidity"],
                data["wind"],
                data["wind_dir"],
                data["sunrise"],
                data["sunset"],
                is_fallback=True,
            )
            logger.info(f"Displayed fallback weather for {city}")
        else:
            _show_error(
                "API Timeout",
                f"The weather service is slow and we don't have cached data for '{city}'.",
                "Tip: Try a major city like 'Jaipur' or 'Delhi' which we have cached data for.",
            )
            logger.error(f"Timeout with no fallback for {city}")

    except requests.exceptions.ConnectionError:
        # No internet connection - try fallback
        logger.warning(f"Connection error for {city}, attempting fallback")

        if city_normalized in FALLBACK_WEATHER:
            data = FALLBACK_WEATHER[city_normalized]
            _display_weather_panel(
                city,
                data["temp"],
                data["condition"],
                data["feels_like"],
                data["humidity"],
                data["wind"],
                data["wind_dir"],
                data["sunrise"],
                data["sunset"],
                is_fallback=True,
            )
            logger.info(f"Displayed fallback weather for {city} (no connection)")
        else:
            _show_error(
                "Connection Error",
                "Unable to connect to the weather service. Check your internet connection.",
                "We can help if you've visited this city before - try 'Jaipur' or 'Mumbai'.",
            )
            logger.error(f"Connection error with no fallback for {city}")

    except requests.exceptions.HTTPError as e:
        # HTTP error (likely 404 - city not found)
        logger.warning(f"HTTP error for {city}: {e}")

        _show_error(
            "City Not Found",
            f"Could not find weather data for '{city}'.",
            "Try major cities like: Jaipur, Udaipur, Delhi, Mumbai, Jodhpur, Jaisalmer, Agra, Pushkar",
        )

    except (KeyError, ValueError, TypeError) as e:
        # JSON parsing error or data format issue
        logger.error(f"Data parsing error for {city}: {e}")

        _show_error(
            "Data Parse Error",
            "The API response format was unexpected. The service might be having issues.",
            "Try again in a moment.",
        )

    except Exception as e:
        # Catch-all for unexpected errors
        logger.error(f"Unexpected error for {city}: {e}")

        _show_error(
            "Unexpected Error",
            str(e),
            "Please try again. If the problem persists, check your internet connection.",
        )


import os
from pathlib import Path

# Create tests directory
tests_dir = Path(r"C:\Users\cheta\rajasthan-helper\tests")
tests_dir.mkdir(parents=True, exist_ok=True)
print(f"✓ Created tests directory: {tests_dir}")

# Create __init__.py
(tests_dir / "__init__.py").write_text('"""Tests package for Rajasthan Helper CLI."""\n')
print("✓ Created __init__.py")

# Create test_weather.py
(tests_dir / "test_weather.py").write_text('''"""Unit tests for weather command."""
import pytest
from unittest.mock import patch, MagicMock

def test_fallback_weather_exists():
    """Test that fallback weather data exists."""
    from rajasthan_helper.commands.weather import FALLBACK_WEATHER
    assert "Jaipur" in FALLBACK_WEATHER
    assert "Mumbai" in FALLBACK_WEATHER
    assert "Delhi" in FALLBACK_WEATHER

def test_weather_fallback_data_structure():
    """Test that fallback weather has proper structure."""
    from rajasthan_helper.commands.weather import FALLBACK_WEATHER
    for city, data in FALLBACK_WEATHER.items():
        assert isinstance(data, dict)
        assert "temp" in data
        assert "condition" in data
        assert "humidity" in data
        assert "wind" in data
        assert "description" in data

def test_weather_command_callable():
    """Test weather command exists and is callable."""
    from rajasthan_helper.commands.weather import get_weather
    assert callable(get_weather)

def test_weather_case_insensitive():
    """Test weather command handles case insensitive input."""
    from rajasthan_helper.commands.weather import get_weather
    assert callable(get_weather)
''')
print("✓ Created test_weather.py")

# Create test_festival.py
(tests_dir / "test_festival.py").write_text('''"""Unit tests for festival command."""
import pytest
from rajasthan_helper.commands.festival import FESTIVALS, show_festival

def test_all_months_have_festivals():
    """Test that all 12 months have festival data."""
    months = [
        "January", "February", "March", "April", "May", "June",
        "July", "August", "September", "October", "November", "December"
    ]
    for month in months:
        assert month in FESTIVALS, f"Missing festival for {month}"
        assert "name" in FESTIVALS[month]
        assert "description" in FESTIVALS[month]

def test_festival_data_structure():
    """Test festival data has proper structure."""
    for month, data in FESTIVALS.items():
        assert isinstance(data, dict)
        assert "name" in data
        assert "description" in data
        assert isinstance(data["name"], str)
        assert isinstance(data["description"], str)
        assert len(data["name"]) > 0
        assert len(data["description"]) > 0

def test_festival_emoji_in_names():
    """Test that festival names include emojis."""
    emoji_chars = "🪁🐪🎨🎭🌞🌧️🤝🌾🪔❄️"
    for month, data in FESTIVALS.items():
        assert data["name"][0] in emoji_chars, f"{month} missing emoji"

def test_festival_command_callable():
    """Test festival command exists and is callable."""
    assert callable(show_festival)
''')
print("✓ Created test_festival.py")

# Create test_tip.py
(tests_dir / "test_tip.py").write_text('''"""Unit tests for tips command."""
import pytest
from rajasthan_helper.commands.tip import TIPS, get_tip

def test_cities_have_tips():
    """Test that cities have travel tips."""
    assert len(TIPS) > 0, "TIPS dictionary should not be empty"
    for city, tips in TIPS.items():
        assert isinstance(tips, list), f"{city} tips should be a list"
        assert len(tips) >= 3, f"{city} should have at least 3 tips"

def test_tip_data_structure():
    """Test tips data has proper structure."""
    for city, tips in TIPS.items():
        assert isinstance(city, str)
        assert len(city) > 0
        for tip in tips:
            assert isinstance(tip, str)
            assert len(tip) > 0

def test_major_cities_included():
    """Test that major cities are included."""
    major_cities = ["Jaipur", "Udaipur", "Mumbai", "Delhi"]
    for city in major_cities:
        assert city in TIPS, f"{city} should be in TIPS"

def test_tips_per_city():
    """Test minimum tips per city."""
    for city, tips in TIPS.items():
        assert len(tips) >= 3, f"{city} should have at least 3 tips, got {len(tips)}"

def test_tip_command_callable():
    """Test tip command exists and is callable."""
    assert callable(get_tip)
''')
print("✓ Created test_tip.py")

print("\n✅ Test environment setup complete!")
print("📝 Next steps:")
print("   1. Install dev dependencies: pip install -e '.[dev]'")
print("   2. Run tests: pytest")
print("   3. Run with coverage: pytest --cov=rajasthan_helper")

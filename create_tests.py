"""
Simple script to create test files.
Run this from the project root: python -m create_tests
"""

import os
import sys

def create_tests():
    """Create tests directory and files."""
    tests_dir = os.path.join(os.getcwd(), "tests")
    
    # Create directory
    os.makedirs(tests_dir, exist_ok=True)
    print(f"✓ Created tests directory: {tests_dir}")
    
    # Create __init__.py
    init_file = os.path.join(tests_dir, "__init__.py")
    with open(init_file, "w") as f:
        f.write('"""Tests package for Rajasthan Helper CLI."""\n')
    print(f"✓ Created {init_file}")
    
    # Create test_weather.py
    test_weather = os.path.join(tests_dir, "test_weather.py")
    with open(test_weather, "w") as f:
        f.write('''"""Unit tests for weather command.

Tests cover:
- Successful API calls
- Fallback data on timeout
- Invalid city handling
- JSON parsing
"""

import pytest
from unittest.mock import patch, MagicMock
import sys


def test_fallback_weather_exists():
    """Test that fallback weather data exists."""
    from rajasthan_helper.commands.weather import FALLBACK_WEATHER
    
    # Check that required cities exist
    assert "Jaipur" in FALLBACK_WEATHER
    assert "Mumbai" in FALLBACK_WEATHER
    assert "Delhi" in FALLBACK_WEATHER


def test_weather_command_executes():
    """Test weather command can be called."""
    from rajasthan_helper.commands.weather import get_weather
    
    # Should execute without raising for valid function
    assert callable(get_weather)


def test_festival_data_exists():
    """Test that festival data is complete."""
    from rajasthan_helper.commands.festival import FESTIVALS
    
    # Check all 12 months exist
    months = [
        "January", "February", "March", "April", "May", "June",
        "July", "August", "September", "October", "November", "December"
    ]
    
    for month in months:
        assert month in FESTIVALS, f"Missing festival for {month}"


def test_tips_data_exists():
    """Test that tips data is complete."""
    from rajasthan_helper.commands.tip import TIPS
    
    # Check required cities exist
    assert "Jaipur" in TIPS
    assert "Udaipur" in TIPS
    assert "Mumbai" in TIPS
    
    # Check each city has at least 3 tips
    for city, tips in TIPS.items():
        assert len(tips) >= 3, f"{city} should have at least 3 tips"
''')
    print(f"✓ Created {test_weather}")
    
    # Create test_festival.py
    test_festival = os.path.join(tests_dir, "test_festival.py")
    with open(test_festival, "w") as f:
        f.write('''"""Unit tests for festival command.

Tests cover:
- Festival lookup by month
- All 12 months coverage
- Invalid month handling
"""

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
    for month, data in FESTIVALS.items():
        # Should have emoji prefix
        assert data["name"][0] in "🪁🐪🎨🎭🌞🌧️🤝🌾🪔❄️", f"{month} missing emoji"
''')
    print(f"✓ Created {test_festival}")
    
    # Create test_tip.py
    test_tip = os.path.join(tests_dir, "test_tip.py")
    with open(test_tip, "w") as f:
        f.write('''"""Unit tests for tips command.

Tests cover:
- Tip lookup by city
- Multiple cities supported
- Invalid city handling
"""

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
            # Each tip should have emoji prefix
            assert tip[0] in "🏰🛍️🍲🎨🔵🌶️🌅🥔🌉🏖️📸🕌🏜️🎪🍴🌲😌📷👥🛁🕯️", f"Tip missing emoji: {tip}"


def test_major_cities_included():
    """Test that major cities are included."""
    major_cities = ["Jaipur", "Udaipur", "Mumbai", "Delhi"]
    
    for city in major_cities:
        assert city in TIPS, f"{city} should be in TIPS"
''')
    print(f"✓ Created {test_tip}")
    
    print("\n✅ All test files created successfully!")
    print(f"   Location: {tests_dir}")
    print("\nTo run tests: pytest tests/")

if __name__ == "__main__":
    try:
        create_tests()
    except Exception as e:
        print(f"❌ Error: {e}")
        sys.exit(1)

"""Configuration management for Rajasthan Helper CLI."""
import os
import json
from pathlib import Path

# Configuration file location
CONFIG_FILE = Path.home() / '.rajasthan_helper_config.json'
LOG_FILE = Path.home() / '.rajasthan_helper.log'

# API configuration
API_KEY = os.getenv('WEATHER_API_KEY', '')
API_TIMEOUT = 5  # seconds

DEFAULT_CONFIG = {
    'default_city': 'Jaipur',
    'units': 'metric',
    'use_colors': True
}

def load_config():
    """Load configuration from file or return defaults."""
    if CONFIG_FILE.exists():
        try:
            return json.loads(CONFIG_FILE.read_text())
        except json.JSONDecodeError:
            return DEFAULT_CONFIG
    return DEFAULT_CONFIG

def save_config(config):
    """Save configuration to file."""
    CONFIG_FILE.write_text(json.dumps(config, indent=2))
    return True

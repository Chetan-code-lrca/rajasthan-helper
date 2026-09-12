# Rajasthan Helper CLI

A small command-line utility for exploring Rajasthan and other Indian cities from the terminal.

It currently provides three commands:

- `weather` — fetch current weather from [wttr.in](https://wttr.in/)
- `festival` — show a month-based festival entry
- `tip` — show practical travel tips for supported cities

The project is intentionally lightweight and works without a database or account system.

## Features

### Weather

Fetches current conditions for a city and displays:

- temperature
- feels-like temperature
- condition
- humidity
- wind speed

The client uses a network timeout and handles common request, parsing, and timeout failures. A small sample response is shown when the request times out.

### Festivals

The festival command uses a built-in month-to-entry mapping, so it works offline and does not need an external service.

```text
january   -> Makar Sankranti
february  -> Holi
march     -> Gangaur
...
december  -> Diwali
```

The data is illustrative rather than a complete Rajasthan festival calendar.

### Travel tips

The `tip` command contains curated tips for 10 cities:

`Jaipur` · `Udaipur` · `Delhi` · `Jodhpur` · `Jaisalmer` · `Pushkar` · `Ajmer` · `Bikaner` · `Mumbai` · `Agra`

## Installation

### Requirements

- Python 3.8+
- pip

### Install from source

```bash
git clone https://github.com/Chetan-code-lrca/rajasthan-helper.git
cd rajasthan-helper
pip install -e .
```

### Run

```bash
rajasthan-helper --help
rajasthan-helper weather Jaipur
rajasthan-helper festival March
rajasthan-helper tip Udaipur
```

## Development

Install development dependencies:

```bash
pip install -e '.[dev]'
```

Run tests:

```bash
pytest
```

Format with Black:

```bash
black .
```

Run Flake8:

```bash
flake8 .
```

## Project structure

```text
rajasthan-helper/
├── rajasthan_helper/
│   ├── __init__.py
│   ├── __main__.py
│   └── commands/
│       ├── __init__.py
│       ├── festival.py
│       ├── tip.py
│       └── weather.py
├── tests/
├── pyproject.toml
└── README.md
```

## Data and privacy

This project does not require user accounts, passwords, or application API keys.

The weather command sends the city name entered by the user to wttr.in to obtain weather data. No user profile or location history is stored by this application.

Do not add secrets, credentials, private URLs, personal files, or local machine paths to the repository. Keep local configuration outside version control.

## License

MIT License.

See [LICENSE](LICENSE) for the full text.
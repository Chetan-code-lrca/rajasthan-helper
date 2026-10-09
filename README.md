# Rajasthan Helper CLI

Rajasthan Helper is a small terminal app for checking weather, looking up a festival entry by month, and getting travel tips for a handful of Indian cities.

It is built with Python, Click, Rich, and Requests. There is no database, login, or application API key.

## What you can do

### Weather

Get the current weather for a city:

```bash
rajasthan-helper weather Jaipur
```

The command shows temperature, feels-like temperature, condition, humidity, and wind speed. It gets the data from `wttr.in` and uses a 10-second request timeout. If the request times out, the CLI shows sample fallback data instead of stopping with an exception.

### Festivals

Look up the festival entry assigned to a month:

```bash
rajasthan-helper festival March
rajasthan-helper festival November
```

The festival list is stored directly in the application, so this command works without an internet connection. The entries are a simple month-based list, not a complete calendar of Rajasthan festivals.

### Travel tips

Get the built-in tips for a supported city:

```bash
rajasthan-helper tip Jaipur
rajasthan-helper tip Udaipur
rajasthan-helper tip Jaisalmer
```

The current data covers:

```text
Jaipur
Udaipur
Delhi
Jodhpur
Jaisalmer
Pushkar
Ajmer
Bikaner
Mumbai
Agra
```

The tips are static content stored in `rajasthan_helper/commands/tip.py`.

## Requirements

- Python 3.8 or newer
- pip

Runtime dependencies are Click, Rich, and Requests. Development extras are provided for pytest, pytest-cov, Black, and Flake8.

## Install

Clone the repository and install it in editable mode:

```bash
git clone https://github.com/Chetan-code-lrca/rajasthan-helper.git
cd rajasthan-helper
python -m pip install -e .
```

Check the command list with:

```bash
rajasthan-helper --help
```

## Commands

The CLI currently exposes three commands: `weather`, `festival`, and `tip`.

### Weather

```bash
rajasthan-helper weather Jaipur
rajasthan-helper weather Udaipur
```

Weather requests depend on `wttr.in`, so network access is required. If the service is unavailable or a request times out, the command uses its documented fallback behavior; treat fallback values as examples, not live observations.

### Festivals

```bash
rajasthan-helper festival March
rajasthan-helper festival November
```

This is a bundled month-to-entry lookup, not a date-specific or exhaustive festival calendar. Check official event sources before planning around a festival.

### Travel tips

```bash
rajasthan-helper tip Jaipur
rajasthan-helper tip Jodhpur
rajasthan-helper tip Jaisalmer
```

Supported cities are Jaipur, Udaipur, Delhi, Jodhpur, Jaisalmer, Pushkar, Ajmer, Bikaner, Mumbai, and Agra. An unsupported city displays the available choices.

Use the root help to see the commands available in the installed version:

```bash
rajasthan-helper --help
rajasthan-helper --version
```

The command-line entry point is defined in `pyproject.toml`.

## Development setup

Install the development dependencies:

```bash
python -m pip install -e '.[dev]'
```

Run the test suite with:

```bash
pytest
```

Format with Black:

```bash
black .
```

Run Flake8 with:

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
├── pyproject.toml
└── README.md
```

`__main__.py` connects the three Click commands to the `rajasthan-helper` executable.

## Data and privacy

The application does not have user accounts or profile storage.

For the weather command, the city name entered on the command line is sent to `wttr.in` to retrieve weather information. The festival and travel-tip commands use data bundled with the application.

No API key is required by the current version.

## Limitations

The festival information is a simple month-to-festival mapping, not a complete event calendar. The travel section contains a fixed set of tips for ten cities. Weather results depend on the availability of `wttr.in`.

## License

MIT

# Rajasthan Helper CLI

Rajasthan Helper is a small terminal app for checking weather, looking up a festival entry by month, and getting travel tips for a handful of Indian cities.

It is built with Python, Click, Rich, and Requests. There is no database, login, or application API key.

## What you can do

### Weather

Get the current weather for a city:

```bash
rajasthan-helper weather Jaipur
```

The command shows temperature, feels-like temperature, condition, humidity, and wind speed. It gets the data from `wttr.in` and uses a 10-second request timeout. If the request times out, the CLI shows sample fallback data instead of stopping with an exception. fileciteturn740file0

### Festivals

Look up the festival entry assigned to a month:

```bash
rajasthan-helper festival March
rajasthan-helper festival November
```

The festival list is stored directly in the application, so this command works without an internet connection. The entries are a simple month-based list, not a complete calendar of Rajasthan festivals. fileciteturn741file0

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

The tips are static content stored in `rajasthan_helper/commands/tip.py`. fileciteturn742file0

## Requirements

- Python 3.8 or newer
- pip

The package metadata declares Python `>=3.8` and the following runtime dependencies: Click, Rich, and Requests. fileciteturn764file0

## Install

Clone the repository and install it in editable mode:

```bash
git clone https://github.com/Chetan-code-lrca/rajasthan-helper.git
cd rajasthan-helper
python -m pip install -e .
```

After installation, the `rajasthan-helper` command is available in the active Python environment. The entry point is defined in `pyproject.toml`. fileciteturn764file0

Check the command list with:

```bash
rajasthan-helper --help
```

## Development setup

Install the development dependencies:

```bash
python -m pip install -e '.[dev]'
```

The project defines optional tooling for pytest, pytest-cov, Black, and Flake8. fileciteturn764file0

Run the available tests with:

```bash
pytest
```

Format the code with:

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

`__main__.py` wires the three Click commands into the `rajasthan-helper` executable. fileciteturn749file0

## Data and privacy

The CLI does not have user accounts or local profile storage.

For the weather command, the city name entered on the command line is sent to `wttr.in` to retrieve weather information. Other commands use data bundled with the application. fileciteturn740file0

No API key is needed for the current version.

## Limitations

The festival information is a small month-to-festival mapping, and the travel section is a fixed collection of tips for ten cities. The weather result depends on the availability of `wttr.in`.

## License

MIT

import requests
from click.testing import CliRunner

from rajasthan_helper.commands.weather import fetch_current_weather, weather


def sample_payload():
    return {
        "current_condition": [{
            "temp_C": "28",
            "FeelsLikeC": "31",
            "humidity": "45",
            "windspeedKmph": "12",
            "weatherDesc": [{"value": "Partly cloudy"}],
        }]
    }


def test_fetch_current_weather_normalizes_provider_response(monkeypatch):
    captured = {}

    class Response:
        def raise_for_status(self):
            pass

        def json(self):
            return sample_payload()

    def fake_get(url, **kwargs):
        captured["url"] = url
        captured.update(kwargs)
        return Response()

    monkeypatch.setattr("rajasthan_helper.commands.weather.requests.get", fake_get)

    result = fetch_current_weather("  New Delhi  ")

    assert captured["url"] == "https://wttr.in/New%20Delhi"
    assert captured["params"] == {"format": "j1"}
    assert captured["timeout"] == 10
    assert result["temperature"] == "28"
    assert result["condition"] == "Partly cloudy"
    assert result["temperature_value"] == 28.0


def test_timeout_does_not_display_fabricated_weather(monkeypatch):
    def timeout(*_args, **_kwargs):
        raise requests.exceptions.Timeout()

    monkeypatch.setattr("rajasthan_helper.commands.weather.requests.get", timeout)
    result = CliRunner().invoke(weather, ["Jaipur"])

    assert result.exit_code != 0
    assert "No sample or stale weather data was substituted" in result.output
    assert "Temperature: 28°C" not in result.output


def test_provider_schema_errors_are_reported(monkeypatch):
    class Response:
        def raise_for_status(self):
            pass

        def json(self):
            return {"current_condition": []}

    monkeypatch.setattr(
        "rajasthan_helper.commands.weather.requests.get",
        lambda *_args, **_kwargs: Response(),
    )
    result = CliRunner().invoke(weather, ["Udaipur"])

    assert result.exit_code != 0
    assert "temperature" in result.output.lower()


def test_measurement_values_outside_expected_ranges_are_rejected(monkeypatch):
    payload = sample_payload()
    payload["current_condition"][0]["humidity"] = "140"

    class Response:
        def raise_for_status(self):
            pass

        def json(self):
            return payload

    monkeypatch.setattr(
        "rajasthan_helper.commands.weather.requests.get",
        lambda *_args, **_kwargs: Response(),
    )

    try:
        fetch_current_weather("Jaipur")
    except ValueError as error:
        assert "outside expected ranges" in str(error)
    else:
        raise AssertionError("Invalid humidity should be rejected")

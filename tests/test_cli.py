from click.testing import CliRunner
import requests

from rajasthan_helper.__main__ import cli
from rajasthan_helper.commands import weather as weather_module


def test_root_help_lists_supported_commands():
    result = CliRunner().invoke(cli, ["--help"])

    assert result.exit_code == 0
    assert "weather" in result.output
    assert "festival" in result.output
    assert "tip" in result.output


def test_festival_accepts_case_insensitive_month():
    result = CliRunner().invoke(cli, ["festival", "mArCh"])

    assert result.exit_code == 0
    assert "Gangaur" in result.output


def test_festival_handles_invalid_month_without_crashing():
    result = CliRunner().invoke(cli, ["festival", "not-a-month"])

    assert result.exit_code == 0
    assert "Invalid month" in result.output


def test_tip_accepts_case_insensitive_city():
    result = CliRunner().invoke(cli, ["tip", "uDaIpUr"])

    assert result.exit_code == 0
    assert "Lake Pichola" in result.output


def test_tip_handles_unknown_city_without_crashing():
    result = CliRunner().invoke(cli, ["tip", "Atlantis"])

    assert result.exit_code == 0
    assert "Unknown city" in result.output


def test_weather_renders_live_response(monkeypatch):
    class FakeResponse:
        def raise_for_status(self):
            return None

        def json(self):
            return {
                "current_condition": [{
                    "temp_C": "25",
                    "weatherDesc": [{"value": "Sunny"}],
                    "FeelsLikeC": "27",
                    "humidity": "50",
                    "windspeedKmph": "12",
                }]
            }

    def fake_get(url, timeout):
        assert url == "https://wttr.in/Jaipur?format=j1"
        assert timeout == 10
        return FakeResponse()

    monkeypatch.setattr(weather_module.requests, "get", fake_get)
    result = CliRunner().invoke(cli, ["weather", "Jaipur"])

    assert result.exit_code == 0
    assert "25°C" in result.output
    assert "Sunny" in result.output
    assert "50%" in result.output


def test_weather_timeout_uses_explicit_sample_fallback(monkeypatch):
    def timeout(*_args, **_kwargs):
        raise requests.Timeout("simulated timeout")

    monkeypatch.setattr(weather_module.requests, "get", timeout)
    result = CliRunner().invoke(cli, ["weather", "Udaipur"])

    assert result.exit_code == 0
    assert "Showing sample data" in result.output
    assert "28°C" in result.output


def test_weather_http_error_is_reported_without_traceback(monkeypatch):
    class FakeResponse:
        def raise_for_status(self):
            raise requests.HTTPError("503 Service Unavailable")

    monkeypatch.setattr(weather_module.requests, "get", lambda *_a, **_k: FakeResponse())
    result = CliRunner().invoke(cli, ["weather", "Jaipur"])

    assert result.exit_code == 0
    assert "Error fetching weather" in result.output
    assert "Traceback" not in result.output

from click.testing import CliRunner

from rajasthan_helper.__main__ import cli
from rajasthan_helper.commands.festival import FESTIVALS
from rajasthan_helper.commands.tip import TRAVEL_TIPS


def test_help_lists_commands():
    result = CliRunner().invoke(cli, ["--help"])
    assert result.exit_code == 0
    assert "weather" in result.output
    assert "festival" in result.output
    assert "tip" in result.output


def test_festival_accepts_month_case_insensitively():
    result = CliRunner().invoke(cli, ["festival", "mArCh"])
    assert result.exit_code == 0
    assert FESTIVALS["march"]["name"] in result.output


def test_festival_invalid_month_is_helpful():
    result = CliRunner().invoke(cli, ["festival", "Smarch"])
    assert result.exit_code == 0
    assert "Invalid month" in result.output
    assert "January" in result.output


def test_tip_city_case_insensitive():
    result = CliRunner().invoke(cli, ["tip", "jAiPuR"])
    assert result.exit_code == 0
    assert TRAVEL_TIPS["jaipur"]["name"] in result.output


def test_tip_unknown_city_is_helpful():
    result = CliRunner().invoke(cli, ["tip", "Atlantis"])
    assert result.exit_code == 0
    assert "Unknown city" in result.output


def test_weather_formats_live_response(monkeypatch):
    class Response:
        def raise_for_status(self):
            pass

        def json(self):
            return {
                "current_condition": [{
                    "temp_C": "31",
                    "weatherDesc": [{"value": "Sunny"}],
                    "FeelsLikeC": "34",
                    "humidity": "40",
                    "windspeedKmph": "11",
                }]
            }

    monkeypatch.setattr("rajasthan_helper.commands.weather.requests.get", lambda *a, **k: Response())
    result = CliRunner().invoke(cli, ["weather", "Jaipur"])
    assert result.exit_code == 0
    assert "31°C" in result.output
    assert "Sunny" in result.output


def test_weather_timeout_does_not_claim_sample_is_live(monkeypatch):
    import requests

    def timeout(*args, **kwargs):
        raise requests.Timeout("offline")

    monkeypatch.setattr("rajasthan_helper.commands.weather.requests.get", timeout)
    result = CliRunner().invoke(cli, ["weather", "Jaipur"])
    assert result.exit_code == 0
    assert "sample data" in result.output.lower()

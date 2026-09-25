"""Tests for logging configuration and levels."""

import logging

import pytest

from tui.domain.models.logging import LOG_FORMAT_DEBUG, LogLevels, configure_logging


@pytest.mark.unit
class TestLogLevels:
    """Tests for configured log level values."""

    def test_log_levels_are_strings(self):
        """Log levels should behave like string enum values."""
        assert LogLevels.DEBUG == "DEBUG"
        assert LogLevels.INFO == "INFO"
        assert LogLevels.WARNING == "WARNING"
        assert LogLevels.ERROR == "ERROR"

    def test_log_levels_members(self):
        """Expected log level members should be exposed."""
        assert set(LogLevels.__members__) == {"DEBUG", "INFO", "WARNING", "ERROR"}


@pytest.mark.unit
class TestConfigureLogging:
    """Tests for the configure_logging helper."""

    @pytest.mark.parametrize(
        ("log_level", "expected_level", "expected_format"),
        [
            (LogLevels.DEBUG, logging.DEBUG, LOG_FORMAT_DEBUG),
            ("debug", logging.DEBUG, LOG_FORMAT_DEBUG),
            (LogLevels.INFO, "INFO", None),
            ("warning", "WARNING", None),
            (LogLevels.ERROR, "ERROR", None),
        ],
    )
    def test_configure_logging_valid_levels(
        self, monkeypatch, log_level, expected_level, expected_format
    ):
        """Valid log levels should configure the expected level and format."""
        calls = []

        def fake_basic_config(**kwargs):
            calls.append(kwargs)

        monkeypatch.setattr(logging, "basicConfig", fake_basic_config)

        configure_logging(log_level)

        assert len(calls) == 1
        assert calls[0]["level"] == expected_level
        assert calls[0].get("format") == expected_format

    def test_configure_logging_invalid_level_uses_error(self, monkeypatch):
        """Unknown levels should fall back to the error level."""
        calls = []

        def fake_basic_config(**kwargs):
            calls.append(kwargs)

        monkeypatch.setattr(logging, "basicConfig", fake_basic_config)

        configure_logging("TRACE")

        assert len(calls) == 1
        assert str(calls[0]["level"]) == "ERROR"
        assert "format" not in calls[0]

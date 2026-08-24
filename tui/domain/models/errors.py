"""Error Models."""


class TUIError(Exception):
    """Base exception for TUI errors."""

    pass


class EnvironmentVariableError(TUIError):
    """Raised when required environment variable is missing."""

    pass


class OrganizationNotFoundError(TUIError):
    """Raised when organization cannot be found."""

    pass


class ValidationError(TUIError):
    """Raised when validation fails."""

    pass

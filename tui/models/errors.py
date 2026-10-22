"""Error Models."""


class TUIError(Exception):
    """Base exception for TUI errors."""

    pass


class EnvironmentFileError(TUIError):
    """Raised when the required environment file is missing."""

    pass


# Backward compatibility alias for older imports.
EnvironmentVariableError = EnvironmentFileError


class OrganizationNotFoundError(TUIError):
    """Raised when organization cannot be found."""

    pass


class ValidationError(TUIError):
    """Raised when validation fails."""

    pass

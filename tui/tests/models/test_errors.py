"""Tests for custom error models."""

import pytest

from tui.domain.models.errors import (
    EnvironmentVariableError,
    OrganizationNotFoundError,
    TUIError,
    ValidationError,
)


@pytest.mark.unit
class TestTUIError:
    """Tests for TUIError base exception."""

    def test_tui_error_creation(self):
        """Test creating a TUIError instance."""
        error = TUIError("Test error message")
        assert str(error) == "Test error message"

    def test_tui_error_is_exception(self):
        """Test that TUIError is an Exception."""
        error = TUIError("Test")
        assert isinstance(error, Exception)

    def test_tui_error_can_be_raised(self):
        """Test raising a TUIError."""
        with pytest.raises(TUIError):
            raise TUIError("Test error")

    def test_tui_error_empty_message(self):
        """Test TUIError with no message."""
        error = TUIError()
        assert str(error) == ""


@pytest.mark.unit
class TestEnvironmentVariableError:
    """Tests for EnvironmentVariableError."""

    def test_environment_variable_error_creation(self):
        """Test creating an EnvironmentVariableError."""
        error = EnvironmentVariableError("GCP_ORGANIZATION not set")
        assert str(error) == "GCP_ORGANIZATION not set"

    def test_environment_variable_error_is_tui_error(self):
        """Test that EnvironmentVariableError inherits from TUIError."""
        error = EnvironmentVariableError("Test")
        assert isinstance(error, TUIError)
        assert isinstance(error, Exception)

    def test_environment_variable_error_can_be_raised(self):
        """Test raising an EnvironmentVariableError."""
        with pytest.raises(EnvironmentVariableError):
            raise EnvironmentVariableError("GCP_ORGANIZATION not set")

    def test_environment_variable_error_caught_by_tui_error(self):
        """Test that EnvironmentVariableError can be caught as TUIError."""
        with pytest.raises(TUIError):
            raise EnvironmentVariableError("Test")

    def test_environment_variable_error_with_variable_name(self):
        """Test EnvironmentVariableError with variable name in message."""
        var_name = "MY_VAR"
        error = EnvironmentVariableError(f"Environment variable {var_name} is required")
        assert var_name in str(error)


@pytest.mark.unit
class TestOrganizationNotFoundError:
    """Tests for OrganizationNotFoundError."""

    def test_organization_not_found_error_creation(self):
        """Test creating an OrganizationNotFoundError."""
        error = OrganizationNotFoundError("Organization not found")
        assert str(error) == "Organization not found"

    def test_organization_not_found_error_is_tui_error(self):
        """Test that OrganizationNotFoundError inherits from TUIError."""
        error = OrganizationNotFoundError("Test")
        assert isinstance(error, TUIError)
        assert isinstance(error, Exception)

    def test_organization_not_found_error_can_be_raised(self):
        """Test raising an OrganizationNotFoundError."""
        with pytest.raises(OrganizationNotFoundError):
            raise OrganizationNotFoundError("Organization XYZ not found")

    def test_organization_not_found_error_caught_by_tui_error(self):
        """Test that OrganizationNotFoundError can be caught as TUIError."""
        with pytest.raises(TUIError):
            raise OrganizationNotFoundError("Test")

    def test_organization_not_found_error_with_org_id(self):
        """Test OrganizationNotFoundError with organization ID."""
        org_id = "12345"
        error = OrganizationNotFoundError(f"Organization {org_id} not found")
        assert org_id in str(error)


@pytest.mark.unit
class TestValidationError:
    """Tests for ValidationError."""

    def test_validation_error_creation(self):
        """Test creating a ValidationError."""
        error = ValidationError("Invalid input")
        assert str(error) == "Invalid input"

    def test_validation_error_is_tui_error(self):
        """Test that ValidationError inherits from TUIError."""
        error = ValidationError("Test")
        assert isinstance(error, TUIError)
        assert isinstance(error, Exception)

    def test_validation_error_can_be_raised(self):
        """Test raising a ValidationError."""
        with pytest.raises(ValidationError):
            raise ValidationError("Invalid email format")

    def test_validation_error_caught_by_tui_error(self):
        """Test that ValidationError can be caught as TUIError."""
        with pytest.raises(TUIError):
            raise ValidationError("Test")

    def test_validation_error_with_field_name(self):
        """Test ValidationError with field name in message."""
        field = "email"
        error = ValidationError(f"Field {field} is invalid")
        assert field in str(error)


@pytest.mark.unit
class TestErrorHierarchy:
    """Tests for exception hierarchy and catching."""

    def test_all_errors_inherit_from_tui_error(self):
        """Test that all custom errors inherit from TUIError."""
        errors = [
            EnvironmentVariableError("Test"),
            OrganizationNotFoundError("Test"),
            ValidationError("Test"),
        ]
        for error in errors:
            assert isinstance(error, TUIError)

    def test_catch_all_errors_with_tui_error(self):
        """Test that all custom errors can be caught as TUIError."""
        errors_to_raise = [
            EnvironmentVariableError("Env var missing"),
            OrganizationNotFoundError("Org not found"),
            ValidationError("Invalid data"),
        ]

        for error in errors_to_raise:
            with pytest.raises(TUIError):
                raise error

    def test_specific_error_types_can_be_differentiated(self):
        """Test that specific error types can be identified."""
        with pytest.raises(EnvironmentVariableError):
            raise EnvironmentVariableError("Test")

        with pytest.raises(OrganizationNotFoundError):
            raise OrganizationNotFoundError("Test")

        with pytest.raises(ValidationError):
            raise ValidationError("Test")

    def test_multiple_errors_in_sequence(self):
        """Test handling multiple different errors in sequence."""
        error_sequence = [
            (EnvironmentVariableError, "Env error"),
            (OrganizationNotFoundError, "Org error"),
            (ValidationError, "Validation error"),
        ]

        for error_class, message in error_sequence:
            with pytest.raises(error_class):
                raise error_class(message)

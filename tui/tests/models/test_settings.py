"""Tests for Settings model."""

import os

import pytest

from tui.domain.models.settings import Settings

ENVIRONMENT = os.environ.get("ENVIRONMENT")


@pytest.mark.integration
class TestSettings:
    """Tests for Settings model."""

    def test_environment_variables(self):
        """Test loading environment variables."""
        settings = Settings()

        assert settings.environment == ENVIRONMENT
        assert settings.gcp_project is not None
        assert settings.gcp_organization is not None
        assert settings.gcp_organization_json is not None
        assert settings.github_org is not None
        assert settings.github_repo is not None
        assert settings.project_number is not None
        assert settings.workload_identity_pool is not None
        assert settings.service_account is not None
        assert settings.service_account_email is not None
        assert settings.wif_principal is not None
        assert settings.repo_principal is not None

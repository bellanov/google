"""Tests for Settings model."""

import pytest

from tui.domain.models.settings import SETTINGS


@pytest.mark.integration
class TestSettings:
    """Tests for Settings model."""

    def test_environment_variables(self):
        """Test that the environment variables are loaded correctly."""

        assert SETTINGS.gcp_project is not None
        assert SETTINGS.gcp_organization is not None
        assert SETTINGS.gcp_organization_json is not None
        assert SETTINGS.github_org is not None
        assert SETTINGS.github_repo is not None
        assert SETTINGS.project_number is not None
        assert SETTINGS.workload_identity_pool is not None
        assert SETTINGS.service_account is not None
        assert SETTINGS.service_account_email is not None
        assert SETTINGS.wif_principal is not None
        assert SETTINGS.repo_principal is not None

"""Test Folder Service."""

import os

import pytest

from tui.domain.services.folder import get_folders_for_organization

GCP_FOLDER_ID = os.getenv("GCP_FOLDER_ID")
GCP_FOLDER_NAME = os.getenv("GCP_FOLDER_NAME")
GCP_FOLDER_DISPLAY_NAME = os.getenv("GCP_FOLDER_DISPLAY_NAME")
GCP_ORGANIZATION_ID = os.getenv("GCP_ORGANIZATION_ID")


@pytest.mark.integration
def test_get_folders_for_organization():
    """Test get_folders_for_organization returns a generator."""
    for folder in get_folders_for_organization(GCP_ORGANIZATION_ID):
        assert folder.name.startswith("folders/")
        assert folder.display_name is not None

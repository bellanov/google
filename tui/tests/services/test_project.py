"""Test Project Service."""

import os

import pytest

from tui.domain.services.project import get_projects_for_folder


@pytest.mark.integration
def test_get_projects_for_folder():
    """Test project retrieval for a folder."""
    folder_id = "test-folder-id"
    projects = get_projects_for_folder(folder_id)
    assert isinstance(projects, list)

"""Folder View."""

import os
from typing import Generator

from google.cloud import resourcemanager_v3
from tui.domain.models.errors import EnvironmentVariableError
from tui.domain.models.folder import Folder

GCP_ORGANIZATION_JSON = os.environ.get("GCP_ORGANIZATION_JSON")

if not GCP_ORGANIZATION_JSON:
    raise EnvironmentVariableError(
        "GCP_ORGANIZATION_JSON environment variable is not set."
    )


def get_folders_markdown() -> str:

    with open(GCP_ORGANIZATION_JSON, "r") as f:
        FOLDERS = f.read()

    return f"""
```json
{FOLDERS}
```"""


def get_folders_for_organization(organization_id: str) -> Generator[Folder, None, None]:
    """Get all folders for an organization.
    Args:
        organization_id: The ID of the organization.

    Returns:
        A generator of Folder objects.
    """
    client = resourcemanager_v3.FoldersClient()
    request = resourcemanager_v3.ListFoldersRequest(
        parent=f"organizations/{organization_id}",
    )
    page_result = client.list_folders(request=request)

    for response in page_result:
        print(response)
        folder = Folder(
            name=response.name,
            display_name=response.display_name,
            parent=response.parent,
        )
        yield folder

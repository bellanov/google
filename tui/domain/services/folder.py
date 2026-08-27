"""Folder Service."""

from typing import Generator

from google.cloud import resourcemanager_v3
from tui.domain.models.folder import Folder


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

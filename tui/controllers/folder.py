"""Folder Controller."""

from typing import Generator

from google.cloud import resourcemanager_v3
from tui.models.folder import Folder
from tui.models.settings import SETTINGS

GCP_ORGANIZATION_JSON = SETTINGS.gcp_organization_json


def get_folders_markdown() -> str:
    """Get the folders for the organization in markdown format.

    This function is a placeholder and should be implemented to
    fetch the folders from the GCP organization.

    Returns:
        A string containing the folders in markdown format.
    """
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


from google.cloud import storage

# Initializes the client using Application Default Credentials (ADC)
client = storage.Client()

# Reference and create a bucket
# bucket = client.create_bucket("my-new-bucket-bellanov")

# Upload a file
# blob = bucket.blob("remote-file-name.txt")
# blob.upload_from_filename("local-file-name.txt")


def get_project_details(project_id: str):
    # Initialize the ProjectsClient
    client = resourcemanager_v3.ProjectsClient()

    # Format the request payload name field correctly
    request = resourcemanager_v3.GetProjectRequest(name=f"projects/{project_id}")

    # Fetch data
    project_info = client.get_project(request=request)
    print(f"Project Number: {project_info.name}")
    print(f"State: {project_info.state}")

    return project_info


get_project_details(SETTINGS.gcp_project)  # Replace with your actual project ID


def list_folder_contents(folder_id: str):
    # 1. Fetch and list all Sub-Folders
    folders_client = resourcemanager_v3.FoldersClient()
    folder_request = resourcemanager_v3.ListFoldersRequest(
        parent=f"folders/{folder_id}"
    )

    print("--- SUB-FOLDERS ---")
    for folder in folders_client.list_folders(request=folder_request):
        print(f"Name: {folder.display_name} | ID: {folder.name.split('/')[-1]}")

    # 2. Fetch and list all Projects
    projects_client = resourcemanager_v3.ProjectsClient()
    project_request = resourcemanager_v3.SearchProjectsRequest(
        query=f"parent:folders/{folder_id}"
    )

    print("\n--- PROJECTS ---")
    for project in projects_client.search_projects(request=project_request):
        print(f"Name: {project.display_name} | ID: {project.project_id}")


list_folder_contents("283856628432")  # Replace with your actual folder ID

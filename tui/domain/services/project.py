"""Project Service."""

from google.cloud import resourcemanager_v3
from tui.domain.models.project import Project


def get_projects_for_folder(folder_id: str) -> list[Project]:
    """Get projects for a folder.

    Args:
        folder_id: The ID of the folder the projects belong to.

    Returns:
        A list of Project objects.
    """
    client = resourcemanager_v3.ProjectsClient()
    request = resourcemanager_v3.ListProjectsRequest(parent=f"folders/{folder_id}")
    projects = []
    for project in client.list_projects(request=request):
        projects.append(project)
    return projects

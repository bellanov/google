"""Project View."""

import logging
import os

from google.cloud import resourcemanager_v3
from google.cloud.resourcemanager_v3.types import Project

from tui.domain.models.errors import EnvironmentVariableError

GCP_ORGANIZATION = os.environ.get("GCP_ORGANIZATION")

if not GCP_ORGANIZATION:
    raise EnvironmentVariableError("GCP_ORGANIZATION environment variable is not set.")


def get_projects_markdown() -> str:
    PROJECTS = get_projects_for_folder(
        "569065457832"
    )  # TODO: Replace with dynamic folder_id

    logging.info(f"Projects: {PROJECTS}")

    MARKDOWN = "## Projects\n\n| Project ID | Name |\n| --- | --- |\n"
    for project in PROJECTS:
        MARKDOWN += f"| {project.project_id} | {project.name} |\n"
    return MARKDOWN


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

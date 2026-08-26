"""Project View."""

import logging
import os

from tui.domain.models.errors import EnvironmentVariableError
from tui.services.project import get_projects_for_folder

GCP_ORGANIZATION = os.environ.get("GCP_ORGANIZATION")

if not GCP_ORGANIZATION:
    raise EnvironmentVariableError("GCP_ORGANIZATION environment variable is not set.")


def get_projects_markdown() -> str:
    PROJECTS = get_projects_for_folder("569065457832")  # TODO: Replace with dynamic folder_id

    logging.info(f"Projects: {PROJECTS}")

    MARKDOWN = "## Projects\n\n| Project ID | Name |\n| --- | --- |\n"
    for project in PROJECTS:
        MARKDOWN += f"| {project.project_id} | {project.name} |\n"
    return MARKDOWN


PROJECTS_MARKDOWN = get_projects_markdown()

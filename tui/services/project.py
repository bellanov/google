"""Project Service."""

# from google.cloud import resourcemanager_v3

from tui.domain.models.project import Project


def get_projects_for_organization(organization_id: str) -> list[Project]:
    """Get projects for an organization.

    Args:
        organization_id: The ID of the organization the projects belong to.

    Returns:
        A list of Project objects.
    """
    pass

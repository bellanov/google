"""Organization View."""

import os

from google.cloud import resourcemanager_v3

from tui.domain.models.errors import EnvironmentVariableError
from tui.domain.models.organization import Organization
from tui.domain.services.organization import get_organization

GCP_ORGANIZATION = os.environ.get("GCP_ORGANIZATION")

if not GCP_ORGANIZATION:
    raise EnvironmentVariableError("GCP_ORGANIZATION environment variable is not set.")


def get_organization_data() -> Organization:
    return get_organization(GCP_ORGANIZATION)


def get_organization_v2(organization_id: str) -> Organization:
    """Get an organization by ID.
    Args:
        organization_id: The ID of the organization.

    Returns:
        An Organization object.
    """
    # Create a client
    client = resourcemanager_v3.OrganizationsClient()

    # Initialize request argument(s)
    request = resourcemanager_v3.GetOrganizationRequest(
        name=f"organizations/{organization_id}",
    )

    # Make the request
    response = client.get_organization(request=request)

    # Handle the response
    return Organization(
        name=response.name,
        display_name=response.display_name,
    )
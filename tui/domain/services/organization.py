"""Organization Service."""

from google.cloud import resourcemanager_v3
from tui.domain.models.organization import Organization


def get_organization(organization_id: str) -> Organization:
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

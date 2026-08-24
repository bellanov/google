"""Organization Model."""

from pydantic import Field

from tui.domain.models.pydantic import CamelCaseModel

GCP_ORGANIZATION = r"^organizations/\d+$"


class Organization(CamelCaseModel):
    """Represents an organization.

    Attributes:
        id: The ID of the organization.
        name: The name of the organization.
        display_name: The display name of the organization.
    """

    name: str = Field(..., pattern=GCP_ORGANIZATION)
    display_name: str

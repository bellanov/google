"""Organization View."""

import os

from tui.domain.models.errors import EnvironmentVariableError
from tui.domain.models.organization import Organization
from tui.domain.services.organization import get_organization

GCP_ORGANIZATION = os.environ.get("GCP_ORGANIZATION")

if not GCP_ORGANIZATION:
    raise EnvironmentVariableError("GCP_ORGANIZATION environment variable is not set.")


def get_organization_data() -> Organization:
    return get_organization(GCP_ORGANIZATION)

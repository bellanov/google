"""Organization View."""

import os

from tui.domain.models.errors import EnvironmentVariableError
from tui.services.organization import get_organization

GCP_ORGANIZATION = os.environ.get("GCP_ORGANIZATION")

if not GCP_ORGANIZATION:
    raise EnvironmentVariableError("GCP_ORGANIZATION environment variable is not set.")


ORGANIZATION = get_organization(GCP_ORGANIZATION)
print(f"Organization: {ORGANIZATION}")

ORGANIZATION_MARKDOWN = f"""\
## {ORGANIZATION.display_name}

## Organization

|             |                         |
| --------------- | ---------------------------- |
| name      | {ORGANIZATION.name}   |
| display_name   | {ORGANIZATION.display_name}   |
"""

"""Organization View."""

import os

from tui.domain.models.errors import EnvironmentVariableError
from tui.services.organization import get_organization

GCP_ORGANIZATION = os.environ.get("GCP_ORGANIZATION")

if not GCP_ORGANIZATION:
    raise EnvironmentVariableError("GCP_ORGANIZATION environment variable is not set.")


def get_organization_markdown() -> str:
    ORGANIZATION = get_organization(GCP_ORGANIZATION)
    print(f"Organization: {ORGANIZATION}")

    MARKDOWN = f"""## {ORGANIZATION.display_name}

| Field | Value |
| --- | --- |
| name | {ORGANIZATION.name} |
| display_name | {ORGANIZATION.display_name} |
"""
    return MARKDOWN


ORGANIZATION_MARKDOWN = get_organization_markdown()

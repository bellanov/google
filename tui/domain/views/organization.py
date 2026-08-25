"""Organization View."""

import os

from tui.domain.controllers.organization import get_organization_markdown
from tui.domain.models.errors import EnvironmentVariableError

GCP_ORGANIZATION = os.environ.get("GCP_ORGANIZATION")

if not GCP_ORGANIZATION:
    raise EnvironmentVariableError("GCP_ORGANIZATION environment variable is not set.")

ORGANIZATION_MARKDOWN = get_organization_markdown()

"""Folder View."""

import os

from tui.domain.models.errors import EnvironmentVariableError

GCP_ORGANIZATION_JSON = os.environ.get("GCP_ORGANIZATION_JSON")

if not GCP_ORGANIZATION_JSON:
    raise EnvironmentVariableError(
        "GCP_ORGANIZATION_JSON environment variable is not set."
    )


def get_folders_markdown() -> str:

    with open(GCP_ORGANIZATION_JSON, "r") as f:
        FOLDERS = f.read()

    return f"""
```json
{FOLDERS}
```"""

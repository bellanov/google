"""Settings Model."""

import os
from pathlib import Path

from pydantic_settings import BaseSettings, SettingsConfigDict

from tui.domain.models.errors import EnvironmentFileError

ENV_FILE = os.environ.get("ENV_FILE")

if not ENV_FILE:
    raise EnvironmentFileError("ENV_FILE environment variable is not set.")


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=Path(ENV_FILE),
        env_file_encoding="utf-8",
        case_sensitive=False,  # Default is False (case-insensitive mapping)
    )

    environment: str

    # Project
    gcp_project: str
    gcp_organization: str
    gcp_organization_json: str
    github_org: str
    github_repo: str

    # Workload Identity Federation (WIF)
    project_number: str
    workload_identity_pool: str
    service_account: str
    service_account_email: str
    wif_principal: str
    repo_principal: str

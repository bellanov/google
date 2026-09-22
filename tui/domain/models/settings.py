"""Settings Model."""

import os
from pathlib import Path

from pydantic_settings import BaseSettings, SettingsConfigDict

ENVIRONMENT = os.environ.get("ENVIRONMENT")


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=Path(
            Path(__file__).resolve().parents[1] / "environments" / f".env.{ENVIRONMENT}"
        ),
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

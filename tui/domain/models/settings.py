"""Settings Model."""


from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    """Import environment variables."""

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


SETTINGS = Settings()

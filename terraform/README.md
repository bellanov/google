# Terraform Deployment

_Terraform_ is used to deploy infrastructure into the `development`, `staging`, and `production` environments.

| Environment   | Description                                         |
| ------------- | --------------------------------------------------- |
| _development_ | Manages infrastructure undergoing **development**.  |
| _staging_     | Manages infrastructure undergoing **validation**.   |
| _production_  | Manages infrastructure that is **customer-facing**. |

Various _Scripts_ are available to support the deployment of infrastructure.

| Script    | Description                                                      |
| --------- | ---------------------------------------------------------------- |
| _ci_      | Scripts to **lint** and **format** the codebase.                 |
| _project_ | Scripts to establish the **Workload Identity Federation (WIF)**. |

# Workload Identity Federation (WIF)

Summary of the steps to establish WIF for Terraform.

*Prerequisites:*

- The `GCP_PROJECT` environment variable must be set to the Google Cloud project ID.
- The `SERVICE_ACCOUNT` environment variable must be set to the desired name of the *Service Account*.
- The `SERVICE_ACCOUNT_EMAIL` environment variable must be set to the email of the *Service Account*.
- The `WORKLOAD_IDENTITY_PROVIDER` environment variable must be set to the desired name of the *Workload Identity Provider*.
- The `WORKLOAD_IDENTITY_POOL` environment variable must be set to the desired name of the *Workload Identity Pool*.
- The `WIF_PRINCIPAL` environment variable must be set to the desired principal for the *Workload Identity Provider*.
- The `REPO_PRINCIPAL` environment variable must be set to the desired principal for the *GitHub Repository*.

1. Create a **Service Account** in the Google Cloud project.

```sh
terraform/scripts/wif/create_service_account.sh
```

2. Create a **Workload Identity Pool** in the Google Cloud project.

```sh
terraform/scripts/wif/create_workload_identity_pool.sh
```

3. Create a **Workload Identity Provider** in the Google Cloud project.

```sh
terraform/scripts/wif/create_workload_identity_provider.sh
```

4. Grant the **Service Account** the necessary **roles** to access resources.

```sh
terraform/scripts/wif/grant_service_account_roles.sh
```

5. Configure Terraform to use the **Workload Identity Federation (WIF)** for authentication.

```sh
terraform/scripts/wif/configure_terraform_wif.sh
```



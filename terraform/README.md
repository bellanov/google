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

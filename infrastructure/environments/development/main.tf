
resource "google_project_service" "service" {
  for_each = toset(local.services)
  project  = var.project_id
  service  = each.key
}

resource "google_service_account" "service_account" {
  for_each     = local.service_accounts
  project      = var.project_id
  account_id   = each.key
  description  = each.value.description
  display_name = each.value.description
}

locals {
  services = []

  service_accounts = {
    developer = {
      description = "Developer Service Account"
    }
  }

}
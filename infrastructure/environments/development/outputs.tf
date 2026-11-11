
output "services" {
  description = "List of enabled services"
  value       = { for service in resource.google_project_service.service : service.id => service }
}

output "service_accounts" {
  description = "List of created service accounts"
  value       = { for sa in resource.google_service_account.service_account : sa.account_id => sa }
}

output "roles" {
  description = "List of IAM members"
  value       = { for member in resource.google_project_iam_member.developer : member.id => member }
}

output "tags" {
  description = "List of created tags"
  value = {
    key   = google_tags_tag_key.tag_key.name
    value = google_tags_tag_value.tag_value.name
  }
}
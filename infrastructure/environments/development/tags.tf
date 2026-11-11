
resource "google_tags_tag_key" "tag_key" {
  parent     = "projects/${var.project_id}"
  short_name = "environment"
}

resource "google_tags_tag_value" "tag_value" {
  parent     = "tagKeys/${google_tags_tag_key.tag_key.name}"
  short_name = "development"
}
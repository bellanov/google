terraform {
  backend "gcs" {
    bucket = var.project_id
    prefix = "terraform/state"
  }

  required_providers {
    google = {
      source  = "hashicorp/google"
      version = "7.44.0"
    }
  }
}

provider "google" {
  project = var.project_id
}
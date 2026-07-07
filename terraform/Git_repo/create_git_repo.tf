provider "github" {
  token = "abcde1234"
}

resource "github_repository" "jaga_repo" {
  name        = "terraform-git-repo"
  description = "My new repository created with Terraform"
  visibility  = "public"
}
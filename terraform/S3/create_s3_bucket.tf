provider "aws" {
  region = "ap-south-2"
  access_key = "abcde1234"
  secret_key = "123456tfgrd"
}

resource "aws_s3_bucket" "jaga_bucket" {
    bucket = "jaga-bucket-terraform"
}
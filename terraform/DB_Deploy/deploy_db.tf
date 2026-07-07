provider "aws" {
  region = "ap-south-2"
  access_key = "abcde"
  secret_key = "aDSffsvsd123"
}

resource "aws_db_instance" "jaga_rds" {
    allocated_storage    = 5
    db_name = "jaga_rds_db"
    engine = "mysql"
    engine_version = "8.0"
    instance_class = "db.t3.micro"
    username = "admin"
    password = "admin123"
}
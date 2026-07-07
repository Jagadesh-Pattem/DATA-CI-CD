provider "aws" {
  region = "ap-south-2"
  access_key = "abcde"
  secret_key = "aDSffsvsd123"
}

resource "aws_instance" "jaga_ec2" {
    ami = "ami-0ffa797f35095b9f7"
    instance_type = "t3.micro"
    tags = {
        Name = "jaga_ec2"
    }
}
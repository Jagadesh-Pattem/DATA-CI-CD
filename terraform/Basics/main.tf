# Setup provider block
## Provider can be AWS, Azure, GCP, Oracle, GitHub, Linode

provider "aws" {
  region = "ap-south-2"
  access_key = "ABCD"
  secret_key = "AVDFRSdaaaEFdf12dsf"
}

# Setup resources block
# Create user
resource "aws_iam_user" "terraform_created_user" {
    name = "soumya"
}

# Create Policy
resource "aws_iam_policy" "s3_create_bucket_policy" {
    name = "s3_create_bucket_policy"
    description = "Policy to allow creating S3 buckets"
    policy = jsonencode({
        Version = "2012-10-17"
        Statement = [
            {
                Effect = "Allow"
                Action = [
                    "s3:CreateBucket"
                ]
                Resource = "*"
            }
        ]
    })
}

# Attach policy to user
resource "aws_iam_user_policy_attachment" "attach_policy_to_user" {
    user = aws_iam_user.terraform_created_user.name
    policy_arn = aws_iam_policy.s3_create_bucket_policy.arn
}

# Create S3 bucket
resource "aws_s3_bucket" "my_first_bucket" {
  bucket = "my-first-bucket-terraform-jaga"
}
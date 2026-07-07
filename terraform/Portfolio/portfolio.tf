provider "aws" {
    region = "ap-south-2"
    access_key = "acvdse"
    secret_key = "12345sddggh"
}

resource "aws_s3_bucket" "portfolio_bucket" {
    bucket = "jaga-portfolio-bucket"
}

# Setup ownership controls to the owner
resource "aws_s3_bucket_ownership_controls" "portfolio_bucket_ownership" {
    bucket = aws_s3_bucket.portfolio_bucket.id
    rule {
        object_ownership = "BucketOwnerPreferred"
    }
}

# Make the bucket public
resource "aws_s3_bucket_public_access_block" "bucket_access" {
    bucket = aws_s3_bucket.portfolio_bucket.id
    block_public_acls = false
    block_public_policy = false
    ignore_public_acls = false
    restrict_public_buckets = false
}

resource "aws_s3_bucket_acl" "portfolio_bucket_acl" {
    depends_on = [
        aws_s3_bucket_ownership_controls.portfolio_bucket_ownership,
        aws_s3_bucket_public_access_block.bucket_access
    ]
    bucket = aws_s3_bucket.portfolio_bucket.id
    acl    = "public-read"
}

resource "aws_s3_object" "portfolio_index" {
    bucket = aws_s3_bucket.portfolio_bucket.id
    key = "index.html"
    source = "index.html"
    acl = "public-read"
    content_type = "text/html"
}

resource "aws_s3_object" "portfolio_error" {
    bucket = aws_s3_bucket.portfolio_bucket.id
    key = "error.html"
    source = "error.html"
    acl = "public-read"
    content_type = "text/html"
}

resource "aws_s3_bucket_website_configuration" "portfolio_website" {
    bucket = aws_s3_bucket.portfolio_bucket.id
    index_document {
        suffix = "index.html"
    }
    error_document {
        key = "error.html"
    }
    depends_on = [aws_s3_bucket_acl.portfolio_bucket_acl]
}
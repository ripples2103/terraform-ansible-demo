# terraform-ansible-demo

Create the Terraform Remote State S3 Bucket

export TERRAFORM_BUCKET="honeyenditsolutions-terraform-dev"


aws s3api create-bucket --bucket ${TERRAFORM_BUCKET} \
     --region eu-west-2 \
     --create-bucket-configuration \
     LocationConstraint=eu-west-2

Enable S3 Bucket Encryption

aws s3api put-bucket-encryption \
    --bucket ${TERRAFORM_BUCKET} \
    --server-side-encryption-configuration={\"Rules\":[{\"ApplyServerSideEncryptionByDefault\":{\"SSEAlgorithm\":\"AES256\"}}]}

Enable S3 Bucket versioning

aws s3api put-bucket-versioning --bucket ${TERRAFORM_BUCKET} --versioning-configuration Status=Enabled

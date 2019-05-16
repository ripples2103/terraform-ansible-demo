#!/usr/bin/env python3

"""
This module creates an Amazon S3 bucket to hold Terraform State. It is configured with
Server Side Encryption(AES256) and Object versioning enabled.

Set the bucket name via the S3BUCKET_NAME variable below.
"""

import boto3


__author__ = "Jason Morgan"
__version__ = "1.0.0"
__license__ = "MIT"

S3BUCKET_NAME = '<ENTER BUCKET NAME HERE>'


def create_bucket():
    """ Create S3 bucket to hold Terraform Remote State """
    s3 = boto3.client('s3')
    s3.create_bucket(
        ACL='private',
        Bucket=(S3BUCKET_NAME),
        CreateBucketConfiguration={
            'LocationConstraint': 'eu-west-2'
        }
    )

    s3.put_bucket_versioning(
        Bucket=(S3BUCKET_NAME),
        VersioningConfiguration={
            'Status': 'Enabled'
        }
    )

    s3.put_bucket_encryption(
        Bucket=(S3BUCKET_NAME),
        ServerSideEncryptionConfiguration={
            'Rules': [
                {
                    'ApplyServerSideEncryptionByDefault': {
                        'SSEAlgorithm': 'AES256',
                    }
                },
            ]
        }
    )


def main():
    """ Create S3 bucket to hold Terraform Remote State """
    create_bucket()


if __name__ == "__main__":
    main()

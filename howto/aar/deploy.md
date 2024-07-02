(howto-deploy-aar)=
# How to deploy an AAR

An Anbox Application Registry (AAR) should be deployed on a single unit. After deploying, you can continue to configure and connect it with all AMS units that you want to synchronise.

Use the following commands to deploy an AAR:

    juju deploy aar
    juju config aar ua_token=<your Ubuntu Pro token>

## Using the AWS S3 storage backend

The AAR has support for hosting application images on AWS S3.

When using the S3 storage backend, image downloads will be redirected to S3 instead of being served directly by the AAR. The AAR will only be asked for metadata by its clients.

### Create and configure an S3 bucket

To use the AWS S3 storage backend, you must create a dedicated S3 bucket for the AAR first. See the [AWS documentation](https://docs.aws.amazon.com/AmazonS3/latest/userguide/creating-bucket.html) for instructions on how to do this.

If you don’t plan to use the {ref}`CloudFront CDN <sec-aws-cloudfront-cdn>`, you should use a region close to your Anbox Cloud deployment to keep download times low.

### Configure bucket access for AAR

To allow the AAR to access the S3 bucket, create an IAM Policy. See [AWS documentation on IAM](https://docs.aws.amazon.com/IAM/latest/UserGuide/introduction.html) for more information:

```json
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "VisualEditor0",
            "Effect": "Allow",
            "Action": [
                "s3:ListBucketMultipartUploads",
                "s3:ListBucket",
                "s3:GetBucketLocation"
            ],
            "Resource": "arn:aws:s3:::aar0"
        },
        {
            "Sid": "VisualEditor1",
            "Effect": "Allow",
            "Action": [
                "s3:PutObject",
                "s3:GetObject",
                "s3:AbortMultipartUpload",
                "s3:DeleteObject",
                "s3:ListMultipartUploadParts"
            ],
            "Resource": "arn:aws:s3:::aar0/*"
        }
    ]
}
```

Replace `aar0` in the policy with the name of your bucket.

There are two ways to configure the bucket access for AAR using the policy created earlier:

1. Create an IAM user and an access key for this user, which the AAR will use. See the [AWS documentation on managing access keys for IAM users](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_access-keys.html) for more information. Assign the policy created earlier to this user.

2. Create an instance profile using the IAM policy created earlier and attach the instance profile to the instance where AAR is deployed. See the [AWS documentation on using instance profiles](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_switch-role-ec2_instance-profiles.html) for more information.

### Configure AAR

Add the following configuration to the `config.yaml` file:

```yaml
aar:
  storage_config: |
    storage:
      s3:
        region: eu-west-3
        bucket: aar0
        # Access Key and Secret Access Key are only required if an IAM user is
        # used to access the bucket. They can be omitted if an instance profile
        # is going to be attached to the instance.
        access-key: <your access key>
        secret-access-key: <your secret access key>
```

Finally, update the AAR configuration via the charm configuration:

    juju config aar -f config.yaml

(sec-aws-cloudfront-cdn)=
### AWS CloudFront CDN support

The distribution of the images can be highly improved by adding support for the AWS CloudFront CDN, which brings the images closer to your Anbox Cloud deployments in a more world wide context. See the [Getting Started Guide on Amazon CloudFront](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/GettingStarted.html) for more information.

Once you have set up a CloudFront distribution for your S3 bucket, you only need the base URL, public key and key pair ID to configure the AAR to use CloudFront to serve image downloads.

Add the credentials to the `config.yaml` file:

```yaml
aar:
  storage_config: |
    storage:
      s3:
        region: eu-west-3
        bucket: aar0
        # Access Key and Secret Access Key are only required if an IAM user is
        # used to access the bucket. They can be omitted if an instance profile
        # is going to be attached to the instance.
        access-key: <your access key>
        secret-access-key: <your secret access key>
        cloudfront:
          base-url: d1dfsdfjmcefekdotjm.cloudfront.net
          private-key: |
            -----BEGIN RSA PRIVATE KEY-----
            ...
            -----END RSA PRIVATE KEY-----
          keypair-id: ADF443JOEF3423JF
          duration: 1m
```

Then update the AAR configuration via the charm configuration:

    juju config aar -f config.yaml

## Related topics

* {ref}`exp-aar`
* {ref}`howto-configure-aar`
* {ref}`howto-revoke-aar`
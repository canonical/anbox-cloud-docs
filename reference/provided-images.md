(ref-provided-images)=
# Provided Anbox Cloud images

Anbox Cloud provides images based on different Android versions and different architectures (amd64, arm64). Anbox Management Service (AMS) manages these images, which can be individually selected by applications. When an image is updated, all applications using the image are automatically updated and rebased on the new image version.

Anbox Cloud images are regular [Ubuntu cloud images](https://cloud-images.ubuntu.com/) where Anbox Cloud and its dependencies are installed. Unnecessary packages are removed to improve images size, boot time and security. Officially released images are available from the [official image server](https://images.anbox-cloud.io) hosted by Canonical. It is currently not possible to build custom images for Anbox Cloud.

## Supported Anbox Cloud images

The following table lists supported images available on the official image server, along with their corresponding image type, Android and Ubuntu versions.

| Name                        | Based on | Android Version | Ubuntu Version | Available since |
|-----------------------------|----------|-----------------|----------------|---------------|
| `jammy:aaos13:amd64`        | AAOS     | 13              | 22.04          | 1.21.0 |
| `jammy:aaos13:arm64`        | AAOS     | 13              | 22.04          | 1.21.0 |
| `jammy:android13:amd64`     | AOSP     | 13              | 22.04          | 1.16.0 |
| `jammy:android13:arm64`     | AOSP     | 13              | 22.04          | 1.16.0 |
| `jammy:android12:amd64`     | AOSP     | 12              | 22.04          | 1.14.0 |
| `jammy:android12:arm64`     | AOSP     | 12              | 22.04          | 1.14.0 |

## Support for Anbox Cloud images

Currently, Anbox Cloud provides images based on Ubuntu 22.04 (jammy). Deprecations, if any, are announced at least two releases in advance.

Android versions are supported as long as Google provides security updates for the respective versions.

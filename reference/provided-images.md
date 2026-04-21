(ref-provided-images)=
# Provided Anbox Cloud images

Anbox Cloud provides images based on different Android versions and different architectures (amd64, arm64). Anbox Management Service (AMS) manages these images, which can be individually selected by applications. When an image is updated, all applications using the image are automatically updated and rebased on the new image version.

Anbox Cloud images are regular [Ubuntu cloud images](https://cloud-images.ubuntu.com/) where Anbox Cloud and its dependencies are installed. Unnecessary packages are removed to improve images size, boot time and security. Officially released images are available from the official image server hosted by Canonical at `https://images.anbox-cloud.io`. For information on custom Anbox Cloud images, see {ref}`exp-custom-images`.

## Supported Anbox Cloud images

The following table lists supported images available on the official image server, along with their corresponding image type, Android and Ubuntu versions.

| Name                        | Based on | Android Version | Ubuntu Version | Available since |
|-----------------------------|----------|-----------------|----------------|---------------|
| `jammy:aaos15:amd64`        | AAOS     | 15              | 22.04          | 1.26.0 |
| `jammy:aaos15:arm64`        | AAOS     | 15              | 22.04          | 1.26.0 |
| `jammy:android15:amd64`     | AOSP     | 15              | 22.04          | 1.26.0 |
| `jammy:android15:arm64`     | AOSP     | 15              | 22.04          | 1.26.0 |
| `jammy:aaos14:amd64`        | AAOS     | 14              | 22.04          | 1.24.0 |
| `jammy:aaos14:arm64`        | AAOS     | 14              | 22.04          | 1.24.0 |
| `jammy:android14:amd64`     | AOSP     | 14              | 22.04          | 1.24.0 |
| `jammy:android14:arm64`     | AOSP     | 14              | 22.04          | 1.24.0 |

## Support for Anbox Cloud images

Currently, Anbox Cloud provides images based on Ubuntu 22.04 (Jammy Jellyfish). Deprecations, if any, are announced at least two releases in advance.

Android versions are supported as long as Google provides security updates for the respective versions.

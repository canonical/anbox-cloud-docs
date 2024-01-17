Anbox Cloud provides images based on different Android versions and different architectures (amd64, arm64). Anbox Management Service (AMS) manages these images, which can be individually selected by applications. When an image is updated, all applications using the image are automatically updated and rebased on the new image version.

Anbox Cloud images are regular [Ubuntu cloud images](https://cloud-images.ubuntu.com/) where Anbox Cloud and its dependencies are installed. Unnecessary packages are removed to improve images size, boot time and security. Officially released images are available from the [official image server](https://images.anbox-cloud.io) hosted by Canonical. It is currently not possible to build custom images for Anbox Cloud.

## Supported Anbox Cloud images

The following table lists supported images available on the official image server, along with their corresponding Android and Ubuntu versions.

| Name                        | Android Version | Ubuntu Version | Available since |
|-----------------------------|-----------------|----------------|---------------|
| `jammy:android13:amd64`     | 13              | 22.04          | 1.16 |
| `jammy:android13:arm64`     | 13              | 22.04          | 1.16 |
| `jammy:android12:amd64`     | 12              | 22.04          | 1.14 |
| `jammy:android12:arm64`     | 12              | 22.04          | 1.14 |

## Deprecated Anbox Cloud images

The following table lists the images that are available on the official image server but are deprecated. They will become unsupported after two releases.

| Name                        | Android Version | Ubuntu Version | Available since | Deprecated since |
|-----------------------------|-----------------|----------------|-----------------|--------------------|
| `jammy:android11:amd64`     | 11              | 22.04          | 1.14            | 1.19 |
| `jammy:android11:arm64`     | 11              | 22.04          | 1.14            | 1.19 |

## Support for Anbox Cloud images

Currently, Anbox Cloud provides images based on Ubuntu 22.04 (jammy). Deprecations, if any, are announced at least two releases in advance.

Android versions are supported as long as Google provides security updates for the respective versions.

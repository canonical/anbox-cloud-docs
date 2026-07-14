---
myst:
  html_meta:
    "description": "How to manage Anbox Cloud images, including adding from the Canonical server, publishing custom images, and pinning releases."
---

(howto-manage-images)=
# Manage images

An image is the base for an instance running in Anbox Cloud. It contains all necessary components, like Anbox or the Android root file system. Each release of Anbox Cloud comes with an updated image.

## Add and configure

Set up access to the image server and add images to your deployment.

- {ref}`howto-add-image`
- {ref}`howto-configure-image-server`
- {ref}`howto-use-specific-release`
- {ref}`howto-delete-image`

## Customize and publish

Create custom images from running instances or build your own Android image from source.

- {ref}`howto-publish-instance-as-image`
- {ref}`howto-package-custom-android-build`


See {ref}`ref-provided-images` for information about which images Anbox Cloud provides.

```{toctree}
:hidden:

configure-image-server
add-image
publish-instance-as-image
delete-image
use-specific-release
package-custom-android-build
```

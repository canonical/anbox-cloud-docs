---
myst:
  html_meta:
    "description": "Explanation of images in Anbox Cloud, which bundle the Anbox runtime and Android root file system to form the base for instances."
---

(exp-images)=
# Images

An image represents the Anbox Cloud image available in the AMS node. An image is the base for an instance, which contains all necessary components like Anbox or the Android root file system. The image type can be container or virtual machine.

## Possible image statuses

The following table lists the different statuses that an image can have depending on its state and what each status means:

| Image status | Description |
|--------------------|-------------|
| `initializing` | The image is currently being created. |
| `created` | The image was uploaded to AMS but not yet available on all LXD nodes. |
| `available` | The image is present on the remote but not in the LXD cluster. |
| `queued` | The image operation is queued for a download. |
| `active` | The image is available on all LXD nodes. |
| `deleted` | The image has been deleted and no longer available for use. |
| `error` | The image has encountered an error. |
| `unknown` | A possible error occurred and the real state of the image cannot be determined. |

If you encounter the `error` or the `unknown` status, [file a bug](https://bugs.launchpad.net/anbox-cloud).

## Image variants

Anbox Cloud provides two variants of images that use different Android execution environments:

- **Images with containerized Android** (`jammy:*`) run Android directly in the LXD container and support the full application model, addons, and platform plugins.
- **Images with virtualized Android** (`resolute:*-cf:*`) run Android inside a virtual machine within the LXD instance.

The image variant determines which execution environment is used. See {ref}`exp-android-execution-environments` for an explanation of the two environments and {ref}`ref-feature-support-by-image-type` for a detailed feature comparison.

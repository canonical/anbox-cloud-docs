(exp-images)=
# Images

An image represents the Anbox Cloud image available in the AMS node. An image is the base for an instance, which contains all necessary components like Anbox or the Android root file system. The image type can be container or virtual machine.

# Possible image statuses

The following table lists the different statuses that an image can have depending on its state and what each status means:

| Image status | Description |
|--------------------|-------------|
| `initializing` | The image is currently being created. |
| `created` | The image was uploaded to AMS but not yet available on all LXD nodes. |
| `available` | The image is present on the remote but not in the LXD cluster. |
| `active` | The image is available on all LXD nodes. |
| `deleted` | The image has been deleted and no longer available for use. |
| `error` | The image has encountered an error. |
| `unknown` | A possible error occurred and the real state of the image cannot be determined. |

If you encounter the `error` or the `unknown` status, [file a bug](https://bugs.launchpad.net/anbox-cloud).

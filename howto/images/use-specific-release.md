(howto-use-specific-release)=
# Use a specific release

With every new Anbox Cloud release, updated images are published. By default, the latest image release is pulled by AMS, but you can request a specific release with the following syntax:

    amc image add <local image name> <remote image name>@<version>

For instance, to fetch the arm64 Android 15 image of the 1.29.1 release:

    amc image add foobar jammy:android15:amd64@1.29.1-20260309214816.git3a659fb

Please refer to [component versions](https://documentation.ubuntu.com/anbox-cloud/reference/component-versions/) for all available image versions.

You can then use the `foobar` image as you would any other image.

```{important}
Image updates contain important security patches and optimizations. Use older images only when strictly necessary.
```

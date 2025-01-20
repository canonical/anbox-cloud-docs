(howto-use-specific-release)=
# How to use a specific release

With every new Anbox Cloud release, updated images are published. By default, the latest image release is pulled by AMS, but you can request a specific release with the following syntax:

    amc image add <local image name> <remote image name>@<release>

For instance, to fetch the arm64 Android 13 image of the 1.24.2 release:

    amc image add foobar jammy:android13:arm64@1.24.2-<hash>

You can then use the `foobar` image as you would any other image.

```{important}
Image updates contain important security patches and optimizations. Use older images only when strictly necessary.
```

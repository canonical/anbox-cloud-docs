(howto-manage-images)=
# How to manage Anbox Cloud images

An image is the base for an instance running in the Anbox Cloud. It contains all necessary components, like Anbox or the Android root file system. Each release of Anbox Cloud comes with an updated image.

See {ref}`ref-provided-images` for information about which images Anbox Cloud provides.

## Configure image server

The Canonical image server provides different Anbox Cloud images that are updated regularly. AMS automatically synchronizes new image versions in regular intervals and updates your applications to use these new versions. The images on the image server are updated for important security updates or bug fixes, and with every release of Anbox Cloud.

Access to the image server is automatically configured as part of your Ubuntu Pro subscription during the charm deployment. No further manual steps are necessary.

AMS will automatically start importing the images available on the image server. The `images.update_interval` configuration option allows to customize how often AMS looks for new images. You can set it to a desired interval with the following command:

    amc config set images.update_interval 5m

You can see the synchronized images with the `amc image list` command:

```bash
+----------------------+------------------------+--------+----------+--------------+---------+
|          ID          |          NAME          | STATUS | VERSIONS | ARCHITECTURE | DEFAULT |
+----------------------+------------------------+--------+----------+--------------+---------+
| cgrqjd6k9eqlsruefcng | jammy:android13:arm64  | active | 1        | aarch64      | true    |
+----------------------+------------------------+--------+----------+--------------+---------+
| cgrqjnmk9eqlsruefco0 | jammy:android12:arm64  | active | 1        | aarch64      | false   |
+----------------------+------------------------+--------+----------+--------------+---------+
| cgrqk2uk9eqlsruefcog | jammy:android11:arm64  | active | 1        | aarch64      | false   |
+----------------------+------------------------+--------+----------+--------------+---------+
```

## Set default image

The first image that is synchronized (usually the newest image) is marked as the default image.
The default image is used when you create an application without the `image` field or launch a raw instance without specifying any ID.

You can set any image as your default with the following command:

    amc image switch jammy:android13:arm64

Running `amc image list` will now show this image marked as default.

## Delete an image

Deleting an image will make it unavailable to Anbox Cloud. However, it will not affect any application based on the image directly, as the application keeps a copy of the image internally. As the image is not available to AMS anymore after deleting it, updating the underlying image of applications with a new version is not possible anymore.

Deleting a specific image can be achieved with the following command, where `image-name` is the name of the image to delete:

    amc image delete image-name

Images that are synchronized from the image server are marked as immutable. To delete such images, add the `--force` flag:

    amc image delete --force io.anbox-cloud:nougat:amd64

If you're not using `--force`, the command will fail.

```{note}
Unless you have only one image left, you cannot delete an image that is marked as default. You must set a new default image first.
```

### Delete an image version

Specific image versions can be deleted too, which is useful when all applications were migrated to a newer version and the old version is not needed anymore. The only requirement is that a single version of the image is available at all times.

The following command removes version `1` of the image with the name `image-name`:

    amc image delete image-name --version=1

## Use a specific release

With every new Anbox Cloud release, updated images are published. By default, the latest image release is pulled by AMS, but you can request a specific release with the following syntax:

    amc image add <local image name> <remote image name>@<release>

For instance, to fetch the arm64 Android 13 image of the 1.18.0 release:

    amc image add foobar jammy:android13:arm64@1.18.0

You can then use the `foobar` image as you would any other image.

```{important}
Image updates contain important security patches and optimizations. Use older images only when strictly necessary.
```

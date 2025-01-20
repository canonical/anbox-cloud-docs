(howto-add-image)=
# How to add an image

````{tabs}

```{group-tab} CLI

An image can be added with the following command:

    amc image add <name> <image_path>

The first image that you add is marked as the default image. The default image is used when you create an application without the `image` field or launch a raw instance without specifying any ID.

You can set any image as your default with the following command:

    amc image switch jammy:android13:arm64

Running `amc image list` will now show this image marked as default.

```

```{group-tab} Dashboard

You can add an image from the *Images* page of the Anbox Cloud dashboard. While adding an image, you can also edit its name and set it as a default.

Clicking the image name opens the image's details page that displays information about the specific image including the number of applications using the image, its versions and their details.

Default images can be set per type of the image: one for images of type *VM* and another for images of type *Container*.

To set an image as the default, click the *Set as default* button ( ![sync image icon](/images/icons/set-default-image-icon.png) ) on the *Images* page or the *Image details* page. Default images cannot be deselected without selecting another image of the same type as the default.

Click the *Sync* button ( ![sync image icon](/images/icons/sync-image-icon.png) ) either in the *Images* page or the *Image details* page. This will initiate a synchronization of the image with the remote server, causing the image to be downloaded to the cluster.

The *Sync* button is enabled only for images with the *available* status.

```
````

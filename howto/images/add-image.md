(howto-add-image)=
# How to add an image

````{tabs}

```{group-tab} CLI

The first image that is synchronised (usually the newest image) is marked as the default image.
The default image is used when you create an application without the `image` field or launch a raw instance without specifying any ID.

You can set any image as your default with the following command:

    amc image switch jammy:android13:arm64

Running `amc image list` will now show this image marked as default.

```

```{group-tab} Dashboard

You can add an image from the *Images* page of the Anbox Cloud dashboard. While adding an image, you can edit the image name and set it as a default.

Clicking the image name opens the *Image details* page that displays information about the specific image including the number of applications using the image, its versions and their details.

Default images can be set for two types: one for images of type *VM* and another for images of type *Container*. 

To set an image as the default, click the *Set as default* button ( ![sync image icon](/images/icons/set-default-image-icon.png) ) either in the actions column of the table on the *Images* page or in the *Image details* page. Default images cannot be deselected without selecting another image of the same type as the default.

Click the *Sync* button ( ![sync image icon](/images/icons/sync-image-icon.png) ) either in the *Images* page or the *Image details* page. This will initiate a synchronization of the image with the remote server, causing the image to be downloaded to the cluster.

The *Sync* button is enabled only for images with the *available* status.

```
````

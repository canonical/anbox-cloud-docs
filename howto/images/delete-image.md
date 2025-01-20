(howto-delete-image)=
# How to delete an image

````{tabs}

```{group-tab} CLI

Deleting an image will make it unavailable to Anbox Cloud. However, it will not affect any application based on the image directly, as the application keeps a copy of the image internally. As the image is not available to AMS anymore after deleting it, updating the underlying image of applications with a new version is not possible anymore.

Deleting a specific image can be achieved with the following command, where `image-name` is the name of the image to delete:

    amc image delete image-name

Images that are synchronized from the image server are marked as immutable. To delete such images, add the `--force` flag:

    amc image delete --force io.anbox-cloud:nougat:amd64

If you're not using `--force`, the command will fail.


Specific image versions can be deleted too, which is useful when all applications were migrated to a newer version and the old version is not needed anymore. The only requirement is that a single version of the image is available at all times.

The following command removes version `1` of the image with the name `image-name`:

    amc image delete image-name --version=1

```

```{group-tab} Dashboard

To delete an image, click the *Delete* button ( ![delete application icon](/images/icons/delete-icon.png) ) either in the actions column of the table on the *Images* page or in the header of the *Image details* page. Deleting an image will remove all of its versions.

To delete a specific version, go to *Images > Image details > Versions >  ![delete application icon](/images/icons/delete-icon.png)*.

Images can not be deleted in the following scenarios:

- Default images cannot be deleted. To delete a default image, change the default to another image of the same type, then proceed with the deletion.
- Images currently in use by applications cannot be deleted until all the associated applications are deleted first.
- Specific versions of images that are immutable cannot be deleted. However, the entire immutable image can still be force-deleted.

```
````

```{note}
Unless you have only one image left, you cannot delete an image that is marked as default. You must set a new default image first.
```
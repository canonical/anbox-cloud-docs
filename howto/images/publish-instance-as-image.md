(howto-publish-instance-as-image)=
# Publish an instance as an image

Publishing an instance as an image allows you to capture the current state of an instance, including any file system modifications, and create a reusable image from it. This is useful for creating custom base images with pre-installed software, configuration changes, or other modifications.

Consider these best practices before publishing instances as images:

* Remove any temporary files, logs, sensitive data before publishing the instance
* Test the published image by launching an instance based on it and verifying all the modifications are working as intended.
* Use meaningful names for your images to indicate the purpose and modifications they contain.

## Publish an instance

To publish an instance as an image, follow these steps:

::::{tab-set}

:::{tab-item} CLI
:sync: cli

### Create and prepare an instance

First, create a new instance from an existing image:

    amc launch --name=test0 jammy:android15:amd64

Wait until the instance is up and running. You can check the instance status with:

    amc list

### Modify the instance

Make any modifications you want to include in the new image. For example, you can access the instance and modify files:

    amc shell test0

Inside the instance, you can install additional software, modify configuration files, add custom files or data and make any other changes you want in your snapshot.

For example, install additional APT packages

    sudo apt install -y adb

Exit the instance shell when you're done.

### Publish the instance

Publish the instance as a new image:

    amc publish test0 --name test --force

The `--force` flag stops the instance automatically if it is still running. Without this flag, you must stop the instance manually before publishing.

```{note}
The publishing process can take some time depending on the size of the instance and the modifications made.
```

### Verify that the image was created

Check that the instance is now stopped:

    amc show test0

Verify that the new image exists in the image list:

    amc image ls

You should see the `test` image in the output.

### Test the published image

Launch a new instance from the published image:

    amc launch --name test1 test

Once the instance is running, verify that your modifications are present:

    amc shell test1

List Android devices within Anbox instance with adb:

    adb devices
    List of devices attached
    emulator-5558   device

:::

:::{tab-item} Dashboard
:sync: dashboard

Navigate to the *Instances* page. Create and start an instance from an existing image.
Alternatively, you can also navigate to the *Images* page, find the image you want to use as a base, and create an instance ( ![create instance icon](/images/icons/create-instance-icon.png) ).

Wait until the instance starts *running*, then click on the instance name. In *Instance details > *Terminal*, make any modifications you want to include in the new image (e.g. install a package, create a file).

When you're done, publish ( ![publish instance icon](/images/icons/publish-instance-icon.png) ) the instance from the *Instances* page. When publishing, you will be able to customize the image name.

To verify if your publish was successful, check if it appears in the list of images. You should also be able to create and start an instance from the published image.

Once the instance is running, visit the *Terminal* tab from its *Instance details* page to confirm that your modifications are present.

## Related topics

* {ref}`howto-create-instance`
* {ref}`howto-stop-instance`
* {ref}`howto-add-image`
* {ref}`howto-delete-image`

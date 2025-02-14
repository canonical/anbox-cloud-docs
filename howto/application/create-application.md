(howto-create-application)=
# How to create an application

An application can be created using the Anbox Cloud dashboard or through the CLI.

Any application must be created first to be available on the Anbox Cloud cluster. The internal process will prepare an instance based on the currently available image with the application package installed. This instance is then used for any newly launched instances to support fast boot times.

## Prerequisites

To create a new application, you need an {ref}`ref-application-manifest` and optionally an Android Package (APK) with support for target architecture.

The application manifest is a `yaml` file and is used to define various attributes of your application.

A default application manifest is created based on the *Resource type* you choose for your application. You can further customize various attributes of your application including the resource requirements for your application.

An example manifest file:

```yaml
name: candy
image: default
boot-activity: com.canonical.candy.GameApp
required-permissions:
  - android.permission.WRITE_EXTERNAL_STORAGE
  - android.permission.READ_EXTERNAL_STORAGE
addons:
  - ssh
tags:
  - game
extra-data:
  com.canonical.candy.obb:
    target: /data/app/com.canonical.candy-1/lib
  game-data-folder:
    target: /sdcard/Android/data/com.canonical.candy/
watchdog:
  disabled: false
  allowed-packages:
    - com.android.settings
services:
  - name: adb
    port: 5559
    protocols: [tcp]
    expose: false
resources:
  cpus: 4
  memory: 4GB
  disk-size: 8GB
```

`````{tabs}
````{group-tab} CLI

An application can be created from a directory, a zip archive or a tarball file. If you cannot use a directory, the second best option is to use a zip archive that provides better optimization when compared to a tarball.

If you are using a directory or a zip archive, ensure that the directory/zip contains the `manifest.yaml` file. You can also optionally include `app.apk` and `extra-data`.

If you are using a tarball file, compress the file with bzip2 and use the same components and structure as the directory.

A zip archive file can be created with the following command:

    zip -r foo.zip <package-folder-path> app.apk extra-data manifest.yaml

A tarball can be created with the following command:

    tar cvjf foo.tar.bz2 -C <package-folder-path> app.apk extra-data manifest.yaml

```{note}
Due to Snap strict confinement, the directory/zip archive/tarball must be located in the home directory.
```

When you are ready, run:

    amc application create <path/to/application_content>

When the `create` command returns, the application package is uploaded to the Anbox Management Service (AMS) which starts the bootstrap process.

Remember that the application is not yet ready to be used. You can watch the status of the application with the following command:

    amc application show <application_id>

The returned output looks similar to the following:

```bash
id: bcmap7u5nof07arqa2ag
name: candy
status: initializing
published: false
config:
  instance-type: a4.3
  boot-package: com.canonical.candy
versions:
  0:
    image: bf7u4cqkv5sg5jd5b2k0 (version 0)
    published: false
    status: initializing
    addons:
    - ssh
    boot-activity: com.canonical.candy.GameApp
    required-permissions:
    - android.permission.WRITE_EXTERNAL_STORAGE
    - android.permission.READ_EXTERNAL_STORAGE
    extra-data:
      com.canonical.candy.obb:
        target: /data/app/com.canonical.candy-1/lib
      game-data-folder:
        target: /sdcard/Android/data/com.canonical.candy/
    watchdog:
      disabled: false
      allowed-packages:
      - com.android.settings
    services:
    - port: 5559
      protocols:
      - tcp
      expose: false
      name: adb
resources:
  cpus: 4
  memory: 4GB
  disk-size: 8GB
```

````

```{group-tab} Dashboard

Click *Create application* on the applications page, enter the required and any optional details that you want to provide and confirm with *Create*.

An application can be created either in a VM or a container. Selecting one of these options will update the image field to only show images of the chosen type. The default image for the selected type is automatically populated in the image field.

The advanced fields allows you to define a {ref}`version <ref-application-manifest>`, specify a {ref}`boot package <ref-application-manifest>`, add multiple {ref}`tags <ref-application-manifest>`, and disable {ref}`sec-application-manifest-watchdog`.

The *Create application* form also provides an option to customize your application manifest.

There may be more advanced scenarios while creating an application that cannot be performed using the dashboard and may require using the `amc` CLI.

After you create an application, the *Applications* page lists all the available applications. Clicking an application name opens the *Application details* page that displays information about the application, its configuration, and deployment features in the *Overview* section.

The *Versions* section lists all created versions of the application. Use the *Actions* menu to either upload to the registry, unpublish, or delete a specific version. Click a specific version to open the version side panel, which provides detailed information about the version related to the parent image and watchdog.
```
`````

Once the status of the application switches to `ready`, the application is ready and can be used. See {ref}`howto-wait-for-application` for information about how to monitor the application status.

## Related topics

* {ref}`sec-application-bootstrap`

Every application which should be available on an Anbox Cloud cluster must be created first.

The internal process will prepare an instance based on the currently available image with the application package installed. This instance is then used for any newly launched instances to support fast boot times.

## Preparation

To create an application, you need an Android package (APK) with support for the target architecture. If your resource requirements are different from the default resource preset, define them using the [`resources` attribute](https://discourse.ubuntu.com/t/application-manifest/24197#resources-7) in your application manifest.

To create a new application, you must first create a manifest file to define the various attributes the new application should have. The manifest is a simple [YAML](http://yaml.org/) file and looks like this:

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
  memory: 4GB
  disk-size: 8GB
```

See [Application manifest](https://discourse.ubuntu.com/t/application-manifest/24197) for detailed information about all available attributes.

## Create from a directory

When creating an application from a directory, the directory should contain the `manifest.yaml` component and optionally, `app.apk` and `extra-data` components.

[note type="information" status="Note"]Due to Snap strict confinement, the directory must be located in the home directory.[/note]

With everything in place, create the application by entering the following command:

    amc application create <path/to/application-content>

When the `create` command returns, the application package is uploaded to the AMS service and the [bootstrap process](https://discourse.ubuntu.com/t/managing-applications/17760#bootstrap-process-2) is started. The application is not yet ready to be used. You can watch the status of the application with the following command:

    amc application show bcmap7u5nof07arqa2ag

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
  memory: 4GB
  disk-size: 8GB
```

Once the status of the application switches to `ready`, the application is ready and can be used. See [How to wait for an application](https://discourse.ubuntu.com/t/wait-for-an-application/24202) for information about how to monitor the application status.


## Create from a zip archive or a tarball file

An application can also be created from a zip archive or a tarball file. It is recommended to use a zip archive instead of a tarball file for better optimisation. The files must fulfil the following requirements:

* In case of a tarball file, the file must be compressed with bzip2 and must use the same components and structure as the directory.
* In case of a zip archive, the file must use the same components and structure as the directory.

[note type="information" status="Note"]Due to Snap strict confinement, the tarball or the zip archive file must be located in the home directory.[/note]

### Example: Create an application from a zip archive file

A zip archive file can be created with the following command:

    zip -r foo.zip <package-folder-path> app.apk extra-data manifest.yaml

Once the zip archive file is created, you can create the application:

    amc application create foo.zip

### Example: Create an application from a tarball file

A tarball can be created with the following command:

    tar cvjf foo.tar.bz2 -C <package-folder-path> app.apk extra-data manifest.yaml

Once the tarball is created, you can create the application:

    amc application create foo.tar.bz2


The AMS service now starts the application [bootstrap process](https://discourse.ubuntu.com/t/managing-applications/17760#bootstrap-process-2). See [How to wait for an application](https://discourse.ubuntu.com/t/wait-for-an-application/24202) for information about how to monitor the application status.

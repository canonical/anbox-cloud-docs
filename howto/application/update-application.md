(howto-update-application)=
# Update an application

Updating an existing application works similar to creating a new one. Each time an existing application is updated, it is extended with a new version. All versions that an application currently has are individually usable, but only one can be launched at a time.

::::{tab-set}
:::{tab-item} CLI
:sync: cli

When you want to update an existing application with a new manifest or APK, provide both in the same format as when the application was created. The `amc application update` command accepts both a directory and an absolute file path.

From a path:

    amc application update bcmap7u5nof07arqa2ag $PWD/foo

From a file:

    amc application update bcmap7u5nof07arqa2ag foo.tar.bz2

AMS will start the update process internally. You can watch the status of the new version with the following command:

    amc application show bcmap7u5nof07arqa2ag

The output shows detailed information about the application and all of its versions:

```bash
id: bcmap7u5nof07arqa2ag
name: candy
status: ready
published: false
config:
  instance-type: a4.3
  boot-package: com.canonical.candy
versions:
  0:
    image: bf7u4cqkv5sg5jd5b2k0 (version 0)
    published: false
    status: active
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
  1:
    image: bf7u4cqkv5sg5jd5b2k0 (version 0)
    published: false
    status: active
    addons:
    - ssh
    boot-activity: com.canonical.candy.GameApp
    required-permissions:
    - android.permission.READ_EXTERNAL_STORAGE
    - android.permission.READ_EXTERNAL_STORAGE
    extra-data:
      com.canonical.candy.obb:
        target: /data/app/com.canonical.candy-1/lib
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

:::

:::{tab-item} Dashboard
:sync: dashboard

You can edit an application from the *Applications* list page.

In the guided form, you can customize most of the fields that are available during {ref}`application creation <howto-create-application>`. Some of the fields, like the application name, or the container/VM option, cannot be modified and are disabled. When a field is disabled, hovering over it will display a tooltip explaining the reason.

Similar to the application creation process, you can unlock advanced customization capabilities by toggling the *Customize manifest.yaml* switch at the bottom of the page. Note that customizing the manifest or updating one of the following fields will create a new version of the application:

- APK
- {ref}`manifest version name <ref-application-manifest>`
- {ref}`boot activity <ref-application-manifest>`
- {ref}`features <ref-feature-flags>`
- {ref}`sec-application-manifest-watchdog`

When you click *Update*, you will be redirected either to the *Overview* tab of the application detail page - if the fields changed did not trigger a new version creation - or to the *Versions* tab of that page, when a new version of the application was created.

:::
::::

Each version gets a monotonically increasing number assigned (here we have version `0` and version `1`).
In addition, each version has a status which indicates the status of the bootstrap process AMS is performing for it. Once an application version is marked as `active`, it is ready to be used.

(sec-publish-app-versions)=
## Publish application versions

The most important part of an application version is the `published` field. If a version is marked as published, it is available to launch and use. Generally when launching instances by using the AMS REST API, if no specific application version is given, by default, the latest published version of an application is used to create the instance.

If `application.auto_publish` (in {ref}`ref-ams-configuration`) is set to `true` (the default), new versions are automatically published. Otherwise, you need to publish them manually.

You can mark an application version as published with the following command:

    amc application publish bcmap7u5nof07arqa2ag 1

To revoke an application version, use the following command:

    amc application revoke bcmap7u5nof07arqa2ag 1

If an application has only a single published version and that version is revoked, the application can't be used by any users anymore. AMS will still list the application but will mark it as not published as it has no published versions.

## Delete application versions

Each version takes up space on the LXD nodes. To free up space and remove old and unneeded versions, you can individually remove them, with the only requirement that an application must have at least a single version at all times. Removing a specific application version is possible with the following command:

    amc application delete --version=1 bcmap7u5nof07arqa2ag

The command will ask for your approval before the version is removed as it might affect your users. If you want to bypass the check, you can add the `--yes` flag to the command.

(sec-configure-automatic-app-updates)=
## Configure automatic updates

AMS automatically updates an application whenever any of its dependencies (parent image, addons, global configuration) changes. This produces a new version for the application, which is automatically published if the `application.auto_publish` configuration item is enabled.

In some cases, an automatic update is not wanted. To support this, AMS allows disabling automatic application updates via the `application.auto_update` configuration update.

To disable automatic updates:

    amc config set application.auto_update false

To enable automatic updates:

    amc config set application.auto_update true

When automatic updates are disabled, applications must be manually updated for any changed dependencies. To do this, use the following command:

    amc application update <application_id_or_name> <path_of_new_application_payload>

This will initiate the update process and create a new application version.

## Change base image

The image an application is based on can be changed with the following command:

    amc application set com.canonical.candy image <image_name_or_id>

Changing the image will cause AMS to generate a new version for the application. Previous versions will continue using the image the application used before.

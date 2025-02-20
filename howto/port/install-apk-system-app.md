(howto-install-apk-system-app)=
# How to install an APK as a system app

Usually, Anbox Cloud installs APKs as user apps in the Android container. It is possible to install apps as system apps though.

```{note}
Installing apps as system apps is not supported on AAOS images.
```

A user app is normally signed by the developer and has restricted permissions at runtime. A system app, on the other hand, is usually [signed with the platform key](https://source.android.com/devices/tech/ota/sign_builds) when building an Android image. It is pre-installed under the system partition and runs a process with some ["signature" protection level permissions](https://developer.android.com/guide/topics/manifest/permission-element.html#plevel) in the Android container.

An application must be running as a system app if:

- The app requires access to hidden Android APIs.
- The app gains some "signature" protection level permissions.

Installing a user app as a system app in an Android container requires the following preparations:

1. Create an addon.
2. Call the `aam install-system-app` command in the `pre-start` hook of the addon.
3. Include the addon in an application after adding it to AMS.
4. Enable the `allow_custom_system_signatures` feature in the application manifest file.
5. Create the application.

When the application is created successfully, the APK will be installed as a system app in the Android container.

## Make a system app

To build your app as a system app instead of a user app, add the attribute `android:sharedUserId="android.uid.system"` into the `<manifest>` tag in the `AndroidManifest.xml` file of your Android app. This attribute will allow the app to run a process with system privileges.

```xml
...
<manifest xmlns:android="http://schemas.android.com/apk/res/android"
    xmlns:tools="http://schemas.android.com/tools"
    package="<package_name>"
    android:sharedUserId="android.uid.system">
...
```

Then build and sign the application alongside with other Android applications when building your Android image. Alternatively, sign it with [Android Studio](https://developer.android.com/studio/publish/app-signing). This method does not require the system platform key. Instead, you can use the keys that are generated from Android Studio to sign the application.

## Create an addon

To install the signed APK as a system app in the Android container, create an addon and invoke the `aam install-system-app` command in a `pre-start` hook.

Follow the steps in {ref}`howto-create-addon` to create the basic layout of an addon, with a `manifest.yaml` file and a `hooks` folder. Place the APK into the addon folder and create a `pre-start` hook with the following content (assuming that the APK file is named `app.apk`):

```bash
#!/bin/bash -ex

# Only install the APK as a system app when bootstrapping an application.
if  [ "$INSTANCE_TYPE" = "regular" ]; then
  exit 0
fi

aam install-system-app \
  --apk="${ADDON_DIR}"/app.apk \
  --permissions=<comma-separated list of permissions that the application requires> \
  --package-name=<package_name>
```

The values of the `package-name` and the `permissions` parameters must match the ones defined in the `AndroidManifest.xml` file of the Android project. If the app requires access to hidden Android APIs to function, add the `--access-hidden-api` parameter to the above command. Use `aam install-system-app --help` for details about this command.

The final layout of the addon should look as follows:

```bash
.
├── app.apk
├── hooks
│   └── pre-start
└── manifest.yaml
```

Add this addon to AMS with the following command:

    amc addon add install-system-app .

## Include the addon in an application

To use this addon in an application, include the addon name under `addons` in the application manifest file when creating an application. You must also enable the feature `allow_custom_system_signatures`, which ensures that the `aam install-system-app` command that is invoked in the `pre-start` hook of the addon works properly.

```yaml
...
addons: [ install-system-app ]
features: [ allow_custom_system_signatures ]
...
```

Then create the application with the `amc` command:

    amc application create .

Use the `--vm` flag to create the application in a virtual machine. If you create the application with a specific image, make sure that it is a virtual machine image.

After the AMS application is created successfully, the APK is installed as a proper system app. It will run as a system app in the Android container when you start it from an instance launched from the newly created application.

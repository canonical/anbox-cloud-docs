(howto-port-apk-oob)=
# How to port APKs with OBB files

Google Play has a limit on how big an APK file can be (see [APK Expansion Files](https://developer.android.com/google/play/expansion-files.html)). Larger Android apps must be split up into the main part as an APK file and the expansion part as an OBB file:

- APK: Contains the executables and native libraries (`*.so` files), plugins, basic assets and data required by the application to load for the first time.
- OBB: Contains the remaining assets (high-fidelity graphics, media files or other large resource files) for the full user experience.

Anbox Cloud supports creating applications for such apps, but it requires additional steps.

Let's assume that you have an application that consists of an APK file and an OBB file:

```
.
├── com.foo.bar.apk
└── main.203779.com.foo.bar.obb
```

1. Rename `com.foo.bar.apk` to `app.apk`.
1. Create a folder named `extra-data` and move the `.obb` file into that folder:

   ```
   .
   ├── app.apk
   ├── extra-data
   │   └── main.203779.com.foo.bar.obb
   ├── manifest.yaml
   ```
1. Declare the OBB file as extra data in the application manifest:

   ```yaml
   name: com.foo.bar
   required-permissions: ['*']
   resources:
     cpus: 4
     memory: 3GB
     disk-size: 3GB
   extra-data:
     main.203779.com.foo.bar.obb:
       target: /sdcard/Android/obb/com.foo.bar/
   ```

   The target location of the OBB file varies depending on the app. Some apps load the OBB file from the SD card (`/sdcard/Android/obb/`), while others load it from the device's internal storage (`/data/media/obb`).

   If an OBB file is not properly installed in the instance, the app might not function as expected. Some apps exit immediately if the required OBB file is not found, which triggers the watchdog (see {ref}`sec-application-manifest-watchdog`) and causes the instance to end up in an error state.

1. Create the application:

        amc application create .

Use the `--vm` flag to create the application in a virtual machine.

When installing the application, the `.obb` file is copied to the destination folder as defined in `manifest.yaml`. When launching an instance from the application, the `.obb` file is loaded on startup.

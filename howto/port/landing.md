(howto-port-android-apps)=
# How to port Android apps

When porting an Android app to Anbox Cloud (usually in the form of an APK), there are a few issues that might cause your app to not function properly:

* Missing dependencies, most importantly to Google Play services. Google Play services are not supported by Anbox Cloud, and apps that require Google Play services can therefore not be ported to Anbox Cloud.
* Missing runtime permissions. See {ref}`howto-grant-runtime-permissions` for instructions on how to grant the required permissions.
* Mismatched architecture. See {ref}`howto-choose-apk-architecture` for information on which architecture you should choose.
* App size. See {ref}`howto-exchange-oob-data` for instructions on how to port large APKs.
* Strict watchdog restrictions. See {ref}`howto-configure-watchdog` if you want to turn the watchdog off for debugging or configure it to not trigger for specific apps.
* Install an APK as a system app. See {ref}`howto-install-apk-system-app` if you want to install a user app as a system app running in an Android container.

```{toctree}
:hidden:

Choose APK architecture <architecture>
Configure Watchdog <configure-watchdog>
Grant runtime permissions to app <permissions>
Install APK as system app <install-system-app>
Port APKs with OBB file <obb-files>
```

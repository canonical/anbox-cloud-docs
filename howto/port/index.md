---
myst:
  html_meta:
    "description": "How to port Android APKs to Anbox Cloud, including architecture selection, watchdog configuration, and OBB files."
---

(howto-port-android-apps)=
# Port Android apps

When porting an Android app to Anbox Cloud (usually in the form of an APK), you might encounter some issues that prevent your app from working as expected.

Common issues include:

- **Unsupported dependencies**  
  Google Play services are not supported by Anbox Cloud. Apps that require Google Play services cannot be ported to Anbox Cloud.

- **Missing runtime permissions**  
  See {ref}`howto-grant-runtime-permissions` to grant the permissions required by your app.

- **Incorrect APK architecture**  
  See {ref}`howto-choose-apk-architecture` to choose the appropriate architecture.

- **Large application size**  
  See {ref}`howto-port-apk-oob` to port large APKs.

- **Watchdog restrictions**  
  See {ref}`howto-configure-watchdog` to turn the watchdog off for debugging or configure it to not trigger for specific apps.

- **Installing an APK as a system app**  
  See {ref}`howto-install-apk-system-app` to install a user app as a system app in an Android container.

```{toctree}
:hidden:

choose-apk-architecture
configure-watchdog
grant-runtime-permissions
install-apk-system-app
port-apk-obb-files
```

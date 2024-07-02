(howto-configure-watchdog)=
# How to configure the watchdog

The {ref}`sec-application-manifest-watchdog` monitors the app installed by the boot package. By default, it terminates the instance if the app crashes or is moved to the background.

## Disable the watchdog

When you create an application, the watchdog is enabled by default. However, when the watchdog is enabled, it's difficult to identify a problem or debug a porting issue, because the instance is terminated when the watchdog is triggered.

To overcome this problem, temporarily disable the watchdog in the application manifest:

```yaml
...
watchdog:
  disabled: true
...
```

When you finish debugging your application, make sure to enable the watchdog again. The watchdog must be running for Anbox Cloud to collect tombstones or [ANR](https://developer.android.com/topic/performance/vitals/anr) if a crash happens during the application runtime, and to terminate the failing instance.

## Add exceptions for allowed apps

Some Android apps require to interact with other apps, for example, for setting up accounts or granting permissions in the Android settings. However, calling another app from the boot package moves the running app to the background, which causes the watchdog to trigger.

You can add exceptions for apps that your app interacts with to the application manifest. These other apps will then not trigger the watchdog. To do so, specify `allowed-packages` under the top-level key `watchdog` in the application manifest. For example:

```yaml
...
watchdog:
  disabled: false
  allowed-packages:
    - com.android.settings
...
```

This configuration allows the boot package app to launch the Android settings app without triggering the watchdog.

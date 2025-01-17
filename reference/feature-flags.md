(ref-feature-flags)=
# Feature flags

Some features are not enabled by default but can be conditionally enabled. Such features are enabled by flags which are configured through the Anbox Management Service (AMS). You can configure these flags globally for all instances or per application.

To configure a feature globally for all instances, use a syntax similar to the following:

    amc config set instance.features foo,bar

To configure a feature for one application in the manifest, use a syntax similar to the following:

    name: my-app
    resources:
      cpus: 4
      memory: 3GB
      disk-size: 3GB
    features: ["foo", "bar"]

### `enable_system_ui`

*since 1.10.2, supported on AOSP images only*

By default, Anbox hides the Android system UI when an application is running in foreground mode. In some use cases, however, it's required to have the system UI available for navigation purposes. This can be enabled with the `enable_system_ui` feature flag.

The feature flag will be considered by all new launched instances once set.

On AAOS, the Android Car system UI is always enabled and cannot be disabled.

### `enable_virtual_keyboard`

*since 1.9.0, supported on AOSP images only*

The Android virtual keyboard is disabled by default but can be enabled with the `enable_virtual_keyboard` feature flag.

For the feature to be considered, applications must be manually updated, because changes to allow the feature to work are only applied during the application {ref}`bootstrap process <sec-application-bootstrap>`.

On AAOS, the Android virtual keyboard is always enabled and cannot be disabled.

### `enable_anbox_ime`

*since 1.11.0, supported on AOSP images only*

The client-side virtual keyboard is disabled by default but can be enabled with the `enable_anbox_ime` feature flag. It requires the client application to embed {ref}`Anbox WebView <sec-application-bootstrap>` which interacts with the client-side virtual keyboard for text editing and sends the text to the Android container.

For the feature to be considered, applications must be manually updated, because changes to allow the feature to work are only applied during the application {ref}`bootstrap process <sec-application-bootstrap>`.

### `disable_wifi`

*since 1.13.0*

By default, Anbox sets up a virtual WiFi device, which sits on top of an Ethernet connection and simulates a real WiFi connection. This WiFi support can be optionally disabled with the `disable_wifi` feature flag.

The feature flag will be considered by all newly launched instances once set.

### `allow_android_reboot`

*since 1.12.0*

By default, Android is not allowed to reboot. With the `allow_android_reboot` feature flag, this can be allowed.

Note that you must disable the {ref}`sec-application-manifest-watchdog` if reboots are allowed.

The feature flag will be considered by all newly launched instances once set.

### `disable_development_settings`

*since 1.18.0*

The Android development settings (which include an ADB connection) are enabled by default. Some applications require these settings to be disabled, which you can do with the `disable_development_settings` feature flag.

Once set, this feature flag will be considered by all newly launched instances.

### `android.allow_custom_android_id`

*since 1.18.0, supported on AOSP images only*

To enable the Android container to use a custom Android ID, add the feature flag `android.allow_custom_android_id` upon application creation. A system app can influence the Android ID of a specific app during the Android runtime by setting the system property in the format of:
  ```
  `anbox.custom_android_id.<index>=<package_name>:<android_id>`
  ```

 * The `<index>` is a number in the range from 0 to 126, which allows you to have multiple overrides for different packages. If the same `<package_name>` with the different `<android_id>` is given for multiple system properties `anbox.custom_android_id.<index>`, the Android ID read from the system property which has the highest suffixing index that will be used in the end.
 * The `<package_name>` is the package name of the application.
 * The `<android_id>` is a unique ID that represents the Android ID for the targeting application. It must be at least 16 characters in length.

Once set, this feature flag will be considered by all newly launched instances.

(sec-gl-async-swap)=
### `emugl.enable_async_swap_support`

*since 1.21.0*

GL Async swap support is disabled by default for explicit signals of buffer swaps completion. To enable the GL async swap feature, add the feature flag `emugl.enable_async_swap_support` upon application creation. Once the async swap support is enabled, Anbox Cloud will use the host GL driver fence commands and file descriptors to synchronize the finished frames between the host and guest instead fully relying on the host GPU driver to do so. The environment variable `ANBOX_ASYNC_SWAP_ENABLED_PACKAGES` that accepts a comma-separated list of package names can be used to allow certain packages to use the GL async swap feature.

Once set, this feature flag will be considered by all newly launched instances.

### `webrtc.enable_ice_logging`

*since 1.20.2*

```{caution}
Enabling this will print IP addresses of WebRTC clients connecting to the Anbox Cloud instances in the logs without masking in clear text.
```

For debugging purposes, Anbox Cloud can log ICE candidates from the server and client inside the system log of an instance. This is disabled by default and needs to be explicitly turned on with the feature flag `webrtc.enable_ice_logging`.

Once set, this feature flag will be considered by all newly launched instances.
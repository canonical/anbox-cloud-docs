AMS provides various configuration items to customise its behaviour. The following table lists the available configuration items and their meaning.

<!-- GENERATED_TABLE all -->

## Node-specific configuration

In a cluster setup, there are configuration items that can be customised for each node. The following table lists the available configuration items and their meaning.

<!-- GENERATED_TABLE node -->

See [Configure cluster nodes](https://discourse.ubuntu.com/t/configure-cluster-nodes/28716) for instructions on how to set these configuration items.

## Features

Anbox Cloud includes some features which are not enabled by default but can be conditionally enabled. The features are enabled by flags which are configured through AMS. You can configure the feature flags either globally for all instances or per application.

To configure a feature globally for all instances, use a command similar to the following:

    amc config set instance.feature foo,bar

To configure a feature for one application in the manifest, use a syntax similar to the following:

    name: my-app
    instance-type: a4.3
    features: ["foo", "bar"]

#### System UI

By default, Anbox hides the Android system UI when an application is running in foreground mode. In some use cases, however, it's required to have the system UI available for navigation purposes. This can be enabled with the `enable_system_ui` feature flag.

The feature flag will be considered by all new launched instances once set.

#### Virtual Keyboard

The Android virtual keyboard is disabled by default but can be enabled with the `enable_virtual_keyboard` feature flag.

For the feature to be considered, applications must be manually updated, because changes to allow the feature to work are only applied during the [application bootstrap process](https://discourse.ubuntu.com/t/managing-applications/17760#bootstrap-process-2).

#### Client-Side Virtual Keyboard

The client-side virtual keyboard is disabled by default but can be enabled with the `enable_anbox_ime` feature flag. It requires the client application to embed [Anbox WebView](https://discourse.ubuntu.com/t/integrate-a-client-side-virtual-keyboard/23643) which interacts with the client-side virtual keyboard for text editing and sends the text to the Android container.

For the feature to be considered, applications must be manually updated, because changes to allow the feature to work are only applied during the [application bootstrap process](https://discourse.ubuntu.com/t/managing-applications/17760#bootstrap-process-2).

#### WiFi

By default, Anbox sets up a virtual WiFi device, which sits on top of an Ethernet connection and simulates a real WiFi connection. This WiFi support can be optionally disabled with the `disable_wifi` feature flag.

The feature flag will be considered by all newly launched instances once set.

#### Android reboot

By default, Android is not allowed to reboot. With the `allow_android_reboot` feature flag, this can be allowed.

Note that you must disable the [watchdog](https://discourse.ubuntu.com/t/application-manifest/24197#watchdog-5) if reboots are allowed.

The feature flag will be considered by all newly launched instances once set.

#### AV1 software encoder

*since 1.17.0*

The AV1 software encoder is disabled by default but can be enabled with the `experimental.force_av1_software_encoding` feature flag. To transcode the video stream encoded in AV1 codec, all clients must support AV1 decoding.

Once set, this feature flag will be considered by all newly launched instances.

#### Development settings

*since 1.18.0*

The Android development settings (which include an ADB connection) are enabled by default. Some applications require these settings to be disabled, which you can do with the `disable_development_settings` feature flag.

Once set, this feature flag will be considered by all newly launched instances.

#### Custom Android ID

*since 1.18.0*

To enable the Android container to use a custom Android ID, add the feature flag `android.allow_custom_android_id` upon application creation. A system app can influence the Android ID of a specific app during the Android runtime by setting the system property in the format of:
  ```
  `anbox.custom_android_id.<index>=<package_name>:<android_id>`
  ```

 * The `<index>` is a number in the range from 0 to 126, which allows you to have multiple overrides for different packages. If the same `<package_name>` with the different `<android_id>` is given for multiple system properties `anbox.custom_android_id.<index>`, the Android ID read from the system property which has the highest suffixing index that will be used in the end.
 * The `<package_name>` is the package name of the application.
 * The `<android_id>` is a unique ID that represents the Android ID for the targeting application. It must be at least 16 characters in length.

Once set, this feature flag will be considered by all newly launched instances.

#### GL Async Swap Support

*since 1.19.0*

GL Async swap support is enabled by default for explicit signals of buffer swaps completion. To disable the GL async object feature, add the feature flag `emugl.disable_async_swap_support` upon application creation. Once the async swap support is disabled, Anbox Cloud will not use the host GL driver fence commands and file descriptors to synchronise the finished frames between the host and guest. Instead, it will fully rely on the host GPU driver to do so. The environment variable `ANBOX_ASYNC_SWAP_DISABLED_PACKAGES` that accepts a comma-separated list of package names can be used to prevent certain packages from using the async object.

Once set, this feature flag will be considered by all newly launched instances.

#### WebRTC ICE candidate logging

*since 1.20.2*

For debugging purposes, Anbox Cloud can log ICE candidates from the server and client inside the system log of an instance. This is disabled by default and needs to be explicitly turned on with the feature flag `webrtc.enable_ice_logging`.

Once set, this feature flag will be considered by all newly launched instances.

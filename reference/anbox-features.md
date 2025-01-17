(ref-aosp-aaos)=
# Supported features for AOSP vs AAOS images

Anbox Cloud provides images based on the Android Open Source Project (AOSP), an operating system typically used in mobile devices or an Anbox Cloud AAOS image which is based on the Android Automotive OS (AAOS), an infotainment platform used in automobiles. Supported Anbox features differ depending what a given image is based on.

The following table lists some Anbox features and whether they are supported for a given base.

|Feature   | AOSP | AAOS |
|--------|------|------|
| boot-package and boot-activity in {ref}`ref-application-manifest` | ✓    |   -   |
| {ref}`howto-install-apk-system-app`             | ✓    |   -   |
| [Custom Android ID](#custom-android-id)                    | ✓    |   -   |
| [System UI](#system-ui)                    | ✓    |   -   |
| [Virtual Keyboard](#virtual-keyboard)                    | ✓    |   -   |
| [Client-Side Virtual Keyboard](#client-side-virtual-keyboard)                    | ✓    |   -   |
| {ref}`VHAL HTTP API <sec-anbox-https-api-vhal>`                                   | -    |   ✓   |
| [VhalConnector](https://canonical.github.io/anbox-cloud.github.com/latest/anbox-platform-sdk/classanbox_1_1VhalConnector.html) in Platform SDK API                                                    | -    |   ✓   |
| {ref}`exp-custom-images`     | -    |   ✓   | 

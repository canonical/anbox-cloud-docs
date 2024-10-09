(ref-android-features)=
# Supported Android features

Anbox Cloud implements support for various Android features. The following table lists certain Android features and if they are supported in Anbox Cloud.

| Feature           | Supported | Notes  |
|--------------------|-----------------|-------------|
| [OpenGL ES](https://source.android.com/devices/graphics/arch-egl-opengl) <= 3.2   |  ✓  | |
| [Vulkan](https://source.android.com/devices/graphics/arch-vulkan) 1.1 |  ✓  | |
| [Camera](https://source.android.com/devices/camera) |  ✓  |     |
| [Sensors](https://source.android.com/devices/sensors) |  ✓  |   |
| Location           |  ✓  |          |
| [VHAL](https://source.android.com/docs/automotive/vhal) |  ✓  | Only on AAOS images (See {ref}`ref-provided-images`). |
| NFC                |      |            |
| [Bluetooth](https://source.android.com/devices/bluetooth) | | |
| WiFi               |  ✓  | Only simulated WiFi is provided to the Android instance. |
| [Multi-Display](https://source.android.com/devices/tech/display/multi_display) | | |
| [Data use](https://source.android.com/devices/tech/datausage)| | |
| Telephony / mobile connectivity | | |
| Hardware-accelerated video decoding (H.264) | ✓ | |
| Hardware-accelerated video encoding (H.264) | | |
| [`fs-verity`](https://www.kernel.org/doc/html/latest/filesystems/fsverity.html) | | |
| [Disk encryption](https://source.android.com/security/encryption) | | |
| [Verified Boot](https://source.android.com/security/verifiedboot) | | |
| [Trusted Execution Environment (TEE)](https://source.android.com/security/trusty) | | |
| [64-bit only support](https://developer.android.com/ndk/guides/abis) |  ✓  | 64-bit only systems/kernels are automatically detected and Android support adjust accordingly |
| [Secure lock screen](https://source.android.com/docs/core/display/multi_display/lock-screen) | ✓                 | The secure lock screen is not configured by default and requires manual setup through the Android Settings app when needed. |

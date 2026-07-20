(exp-android-execution-models)=
# Android execution models

Anbox Cloud supports two ways of running Android inside an instance: **containerized Android** and **virtualized Android**. The execution model is determined by the image that an instance is based on - you choose an image when creating an instance, and the image determines how Android runs.

Both execution models provide access to Android through the same streaming infrastructure and can coexist in the same Anbox Cloud deployment.

## Containerized Android

With containerized Android, the Android system runs directly inside the LXD container. This is the execution model used by `jammy:*` images (for example, `jammy:android14:amd64`).

Containerized Android supports the full set of Anbox Cloud features:

- {ref}`Applications <exp-applications>` and the application lifecycle (bootstrap, updates, versions)
- {ref}`Addons <exp-addons>` for image customisation
- {ref}`Platform plugins <exp-platforms>` for custom rendering and input pipelines
- Shell access to the Android environment through `anbox-shell`

This is the execution model that Anbox Cloud has used since its first release. The Android system shares the kernel with the host through LXD's container isolation, which keeps resource overhead low and allows high instance density.

## Virtualized Android

With virtualized Android, the Android system runs inside a [Cuttlefish](https://source.android.com/docs/devices/cuttlefish) virtual machine within the LXD instance. This is the execution model used by `resolute:*-cf:*` images (for example, `resolute:android16-cf:amd64`). The `-cf` suffix in the image name indicates that the image uses the Cuttlefish virtual device.

Cuttlefish is Google's reference virtual Android device. Running Android through Cuttlefish means you get a standard, unmodified Android environment with no Anbox-specific changes to the Android system itself — the Android system image comes directly from Google's build infrastructure. This is the right choice when you need Android to behave exactly as it does on a physical device or in Google's own test environments.

Virtualized Android supports {ref}`instances <sec-application-raw-instances>`. To access the Android shell, use `adb shell` instead of `anbox-shell`. See {ref}`ref-feature-support-by-image-type` for the full feature comparison.

Virtualized Android is a good fit for the following scenarios:

- **Standard Android environments** where you need Android to behave exactly as it does on a real device, without any Anbox-specific modifications to the Android system.
- **Custom Android or AAOS builds** where you want to run your own Android system image inside Anbox Cloud. See {ref}`howto-package-custom-android-build` for instructions.
- **VHAL development** where native gRPC support for the vehicle HAL simplifies automotive development.
- **Workloads that benefit from stronger isolation** where the additional virtualisation boundary between Android and the host is desirable.

## Choosing between the two execution models

Use **virtualized Android** when you need a standard Android environment that behaves exactly like a physical device or Google's reference implementation, when you want to run a custom Android or AAOS build, or when you need native VHAL support for automotive use cases.

Use **containerized Android** when you are building on top of Anbox Cloud's application and addon model for managed APK deployment, or when you need platform plugins for custom rendering and input pipelines.

Both image types can coexist in the same AMS deployment. You can register and use images of both types simultaneously and launch instances from either type as needed.

## Related topics

- {ref}`ref-feature-support-by-image-type`
- {ref}`tut-getting-started-virtualized-android`
- {ref}`howto-package-custom-android-build`
- {ref}`ref-provided-images`

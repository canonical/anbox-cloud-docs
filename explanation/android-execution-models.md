(exp-android-execution-models)=
# Android execution models

Anbox Cloud supports two ways of running Android inside an instance: **containerized Android** and **virtualized Android**. The execution model is determined by the image that an instance is based on — you choose an image when creating an instance, and the image determines how Android runs.

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

Virtualized Android currently supports only {ref}`raw instances <sec-application-raw-instances>`. It does not support applications, addons, or platform plugins. To access the Android shell, use `adb shell` instead of `anbox-shell`.

Virtualized Android is a good fit for the following scenarios:

- **Raw instance workflows** where you do not need the application or addon abstractions and want to work directly with Android instances.
- **Custom Android or AAOS builds** where you want to run your own Android system image inside Anbox Cloud. See {ref}`howto-package-custom-android-build` for instructions.
- **Workloads that benefit from stronger isolation** where the additional virtualisation boundary between Android and the host is desirable.

Virtualized Android instances require a minimum of 5 GB of memory and KVM support on the host. See {ref}`ref-feature-support-by-image-type` for the full comparison.

## Choosing between the two models

If you need the application model (managed APK deployment, versioning, bootstrapping), addons, or platform plugins, use containerized Android.

If you are working with raw instances, want to run a custom Android build, or need native VHAL support for automotive use cases, use virtualized Android.

Both image types can coexist in the same AMS deployment. You can register and use images of both types simultaneously and launch instances from either type as needed.

## Runtime convergence

The two execution models currently use different runtime implementations. This is an implementation detail — both models present the same user-facing capabilities through AMS and the streaming stack.

The runtime that currently powers virtualized Android will also support containerized Android in a future release, converging the two implementations into a single runtime. The two execution models — containerized and virtualized — will remain as distinct choices for users.

## Related topics

* {ref}`ref-feature-support-by-image-type`
* {ref}`tut-getting-started-virtualized-android`
* {ref}`howto-package-custom-android-build`
* {ref}`ref-provided-images`

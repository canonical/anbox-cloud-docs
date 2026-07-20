(ref-feature-support-by-image-type)=
# Image types reference

Anbox Cloud provides two types of images, each using a different {ref}`Android execution model <exp-android-execution-models>`. This page describes the capabilities, naming, and requirements for each type.

## Image naming

| Pattern | Execution model | Example |
|---------|----------------|---------|
| `jammy:*` | Containerized Android | `jammy:android14:amd64` |
| `resolute:*-cf:*` | Virtualized Android | `resolute:android16-cf:amd64` |

The `-cf` suffix identifies a Cuttlefish-based image using virtualized Android.

See {ref}`ref-provided-images` for the full list of available images.

## Images with containerized Android

The Android system runs directly in the LXD container. These images support:

- {ref}`Applications <exp-applications>` — managed APK deployment with versioning, bootstrapping, and the full application lifecycle
- {ref}`Addons <exp-addons>` — customising images with hooks tied to instance lifecycle events
- {ref}`Platform plugins <exp-platforms>` — custom rendering and input pipelines via the Anbox Platform SDK
- Streaming
- Custom Android builds (see {ref}`exp-custom-images`)
- Shell access via `anbox-shell`
- VHAL support via adapter

**Minimum resource requirements:**
- 2 CPU cores per instance.
- 3GB memory per instance.
- 3GB disk space per instance.
- KVM not required.

## Images with virtualized Android

The Android system runs inside a Cuttlefish virtual machine within the LXD instance, providing a standard, unmodified Android environment. These images support:

- Streaming
- Custom Android or AAOS builds (see {ref}`howto-package-custom-android-build`)
- Shell access via `adb shell`
- VHAL support with native gRPC
- QEMU-based isolation between Android and the host

**Minimum resource requirements:**
- 4 CPU cores per instance.
- 5GB memory per instance.
- 15GB disk space per instance.
- KVM required on the host.

## Shell access

For containerized Android:

    amc exec <instance_id> -- anbox-shell

For virtualized Android:

    amc exec <instance_id> -- adb shell

## Related topics

* {ref}`exp-android-execution-models`
* {ref}`ref-provided-images`
* {ref}`ref-requirements`

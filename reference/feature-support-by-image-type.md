(ref-feature-support-by-image-type)=
# Feature support by image type

Anbox Cloud provides two types of images that use different {ref}`Android execution models <exp-android-execution-models>`: images with containerized Android and images with virtualized Android.

## Image naming

| Pattern | Execution model | Example |
|---------|----------------|---------|
| `jammy:*` | Containerized Android | `jammy:android14:amd64` |
| `resolute:*-cf:*` | Virtualized Android | `resolute:android16-cf:amd64` |

The `-cf` suffix indicates a Cuttlefish-based image that uses virtualized Android.

See {ref}`ref-provided-images` for the full list of available images.

## Feature support

| Feature | Containerized (`jammy:*`) | Virtualized (`resolute:*-cf:*`) |
|---------|---------------------------|--------------------------------|
| {ref}`Applications <exp-applications>` | ✓ | ✗ |
| {ref}`Addons <exp-addons>` | ✓ | ✗ |
| {ref}`Platform plugins <exp-platforms>` | ✓ | ✗ |
| Raw instances | ✓ | ✓ |
| Streaming | ✓ | ✓ |
| Custom Android builds | ✓ (see {ref}`exp-custom-images`) | ✓ (see {ref}`howto-package-custom-android-build`) |
| VHAL support | Via adapter | Native gRPC |

## Shell access

| Method | Containerized | Virtualized |
|--------|---------------|-------------|
| `anbox-shell` | ✓ | ✗ |
| `adb shell` (port 6520) | ✗ | ✓ |

For containerized Android, access the Android shell with:

    amc exec <instance_id> -- anbox-shell

For virtualized Android, connect through ADB:

    adb connect <instance_ip>:6520
    adb shell

## Resource requirements

| Requirement | Containerized | Virtualized |
|-------------|---------------|-------------|
| Minimum memory per instance | 3 GB | 5 GB |
| KVM support required | No | Yes |

## Related topics

* {ref}`exp-android-execution-models`
* {ref}`ref-provided-images`
* {ref}`ref-requirements`

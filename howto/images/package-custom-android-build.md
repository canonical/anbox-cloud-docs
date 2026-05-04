---
myst:
  html_meta:
    "description": "How to package a custom Android Cuttlefish build."
---

(howto-package-custom-android-build)=
# Package a custom Android build

You can package a custom [Cuttlefish](https://source.android.com/docs/devices/cuttlefish) Android build as a [snap](https://snapcraft.io/) and install it in a running virtualized Android instance. This lets you run your own Android system image while using the Anbox Cloud infrastructure for streaming and instance management.

For background on how virtualized Android works in Anbox Cloud, see {ref}`exp-android-execution-environments`.

## Prerequisites

- An Anbox Cloud deployment with a virtualized Android image available (see {ref}`tut-getting-started-virtualized-android`)
- Android Cuttlefish build artifacts from your own build:
  * `cvd-host_package.tar.gz` - Cuttlefish host tools from the Android build
  * Android images (such as `super.img`, `boot.img`, `vbmeta.img`, and other system images produced by the build)
- The `snap` command-line tool installed on your build machine

## Prepare the snap directory structure

Create the directory structure for the snap:

```bash
mkdir -p my-android-snap/host-tools
mkdir -p my-android-snap/images
mkdir -p my-android-snap/meta
```

Extract the Cuttlefish host tools:

    tar xf cvd-host_package.tar.gz -C my-android-snap/host-tools/

Copy the Android system images:

    cp super.img boot.img vbmeta.img vendor_boot.img android-info.txt \
        my-android-snap/images/

Include all image files that your Cuttlefish build produced and that are required to launch a virtual device.

## Create the snap metadata

Create the file `my-android-snap/meta/snap.yaml`:

```yaml
name: my-custom-android
version: '1.0'
summary: Custom Android Cuttlefish images and host tools
description: |
  Provides custom Android system images and Cuttlefish host tools
  for use with the Anbox Cloud runtime.
type: app
base: bare
architectures:
  - amd64
confinement: strict
grade: stable
slots:
  host-tools:
    interface: content
    content: android-host-tools
    read:
      - $SNAP/host-tools
  images:
    interface: content
    content: android-images
    read:
      - $SNAP/images
```

The snap defines two content interface slots that provide the Cuttlefish host tools and Android system images to the Anbox runtime snap. If you are targeting ARM64, change the `architectures` field to `arm64`.

## Pack the snap

Use `snap pack` to create the snap:

    snap pack my-android-snap/

This produces a file like `my-custom-android_1.0_amd64.snap` in the current directory.

## Launch an instance and install the snap

Launch a virtualized Android instance in development mode so that you can push files to it:

    id="$(amc launch --devmode resolute:android16-cf:amd64)"

Or, for an automotive Android build:

    id="$(amc launch --devmode resolute:aaos16-cf:amd64)"

Wait for the instance to reach the `running` state:

    amc wait "${id}" --timeout 15m

See {ref}`sec-dev-mode` for more information about development mode.

Push the snap into the instance:

    cat my-custom-android_1.0_amd64.snap \
      | amc exec "${id}" -- sh -c "cat - > /tmp/my-custom-android_1.0_amd64.snap"

Install the snap inside the instance:

    amc exec "${id}" -- snap install --dangerous /tmp/my-custom-android_1.0_amd64.snap

The `--dangerous` flag is required because the snap is not signed by the Snap Store.

## Connect snap interfaces and restart the runtime

Disconnect the existing Android snap from the runtime:

    amc exec "${id}" -- snap disconnect anbox-runtime:android-images
    amc exec "${id}" -- snap disconnect anbox-runtime:android-host-tools

Connect your custom Android snap to the runtime:

    amc exec "${id}" -- snap connect anbox-runtime:android-images my-custom-android:images
    amc exec "${id}" -- snap connect anbox-runtime:android-host-tools my-custom-android:host-tools

Restart the runtime to load the new Android images:

    amc exec "${id}" -- snap restart anbox-runtime

## Verify

Connect to the instance and verify that your custom Android build is running:

    amc exec "${id}" -- adb shell getprop ro.build.display.id

The output should show the build ID of your custom Android build.

## Troubleshooting

### Snap content interface connection fails

If `snap connect` fails, verify that the content interface names in your snap match what the runtime expects:
- The `content` field for host tools must be `android-host-tools`
- The `content` field for images must be `android-images`

Use `snap connections anbox-runtime` inside the instance to inspect the expected interfaces.

### Runtime fails to start after connecting custom snap

Check the runtime logs:

    amc exec "${id}" -- snap logs anbox-runtime -n 100

Common issues include missing image files or incompatible Cuttlefish host tool versions.

### Snap installation fails

Verify that the snap was built for the correct architecture and that the directory structure is correct. The snap must contain `host-tools/` and `images/` directories at its root.

## Related topics

- {ref}`exp-android-execution-environments`
- {ref}`tut-getting-started-virtualized-android`
- {ref}`ref-feature-support-by-image-type`

---
myst:
  html_meta:
    "description": "Learn how to start a virtualized Android instance."
---

(tut-getting-started-virtualized-android)=
# Get started with virtualized Android

In this tutorial, we will go through launching our first instance with virtualized Android and connecting to it. At the end, we will have a running Android instance that we can interact with through ADB.

## Prerequisites

To proceed with the tutorial, we need:

- A working Anbox Cloud deployment (appliance or charmed). If you haven't set one up yet, see {ref}`tut-installing-appliance`. It needs at least:
  * 4 CPU cores
  * 5GB of memory
  * 15 GB of disk space
- KVM support on the machine running Anbox Cloud. Verify by checking that `/dev/kvm` exists:

    ls /dev/kvm

## Launch an instance

Launch an instance from the image:

    amc launch resolute:android16-cf:amd64 --name test0

Note the instance ID in the output. Wait for the instance to reach the `running` state:

    amc wait test0 --timeout 15m

## Connect to the instance

Open a shell inside the `test0` instance by running

    amc shell test0

Connect to the Android shell through ADB

    adb shell

## Success

We have successfully launched a virtualized Android instance with ADB shell access.

## Next steps

- Read {ref}`exp-android-execution-models` to understand how virtualized Android differs from containerized Android.
- See {ref}`howto-package-custom-android-build` to learn how to run your own Android build in Anbox Cloud.
- Consult {ref}`ref-feature-support-by-image-type` for a full comparison of supported features.

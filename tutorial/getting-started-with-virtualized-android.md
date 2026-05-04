(tut-getting-started-virtualized-android)=
# Get started with virtualized Android

This tutorial guides you through launching your first instance with virtualized Android and connecting to it. At the end, you will have a running Android instance that you can interact with through ADB.

## Prerequisites

- A working Anbox Cloud deployment (appliance or charmed). If you haven't set one up yet, see {ref}`tut-installing-appliance`.
- KVM support on the machine running Anbox Cloud. Verify by checking that `/dev/kvm` exists:

      ls /dev/kvm

## Launch an instance

Launch an instance from the image. Virtualized Android instances require at least 4 CPU cores, 5 GB of memory and 15 GB of disk space:

    amc launch resolute:android16-cf:amd64 --cpus 4 --memory 5GB --disk-size 15GB --name test0

Note the instance ID in the output. Wait for the instance to reach the `running` state:

    amc wait test0 --timeout 5m

## Connect to the instance

Open a shell inside the `test0` instance by running

    amc shell test0

Connect to the Android shell through ADB

    adb shell

You now have a shell inside the Android system running in your instance.

## View Android logs

To view the Android system logs:

    adb logcat

## Clean up

When you are done, delete the instance:

    amc delete test0

## Next steps

- Read {ref}`exp-android-execution-models` to understand how virtualized Android differs from containerized Android.
- See {ref}`howto-package-custom-android-build` to learn how to run your own Android build in Anbox Cloud.
- Consult {ref}`ref-feature-support-by-image-type` for a full comparison of supported features.

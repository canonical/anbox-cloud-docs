(tut-getting-started-virtualized-android)=
# Get started with virtualized Android

This tutorial guides you through launching your first instance with virtualized Android and connecting to it. At the end, you will have a running Android instance that you can interact with through ADB.

## Prerequisites

- A working Anbox Cloud deployment (appliance or charmed). If you haven't set one up yet, see {ref}`tut-installing-appliance`.
- KVM support on the host machine. Verify by checking that `/dev/kvm` exists:

      ls /dev/kvm

## Add a virtualized Android image

Register a virtualized Android image with AMS:

    amc image add resolute:android16-cf:amd64

For ARM64 hosts, use:

    amc image add resolute:android16-cf:arm64

Wait for the image to become available:

    amc image list

The image status should show `active` when it is ready.

## Launch an instance

Launch a raw instance from the image. Virtualized Android instances require at least 5 GB of memory:

    amc launch --raw resolute:android16-cf:amd64 --memory 5GB

Note the instance ID in the output. Wait for the instance to reach the `running` state:

    amc wait <instance_id> --timeout 5m

## Connect to the instance

Find the instance IP address:

    amc show <instance_id>

Connect to the Android shell through ADB on port 6520:

    adb connect <instance_ip>:6520
    adb shell

You now have a shell inside the Android system running in your instance.

## View Android logs

To view the Android system logs:

    adb logcat

## Clean up

When you are done, delete the instance:

    amc delete <instance_id>

## Next steps

- Read {ref}`exp-android-execution-models` to understand how virtualized Android differs from containerized Android.
- See {ref}`howto-package-custom-android-build` to learn how to run your own Android build in Anbox Cloud.
- Consult {ref}`ref-feature-support-by-image-type` for a full comparison of supported features.

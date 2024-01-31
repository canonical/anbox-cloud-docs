Anbox Cloud provides a platform SDK that allows the development of custom platform plugins for the Anbox runtime, for use cases where the [default platforms](https://discourse.ubuntu.com/t/18733) don't fit. For example, a custom platform can be used to integrate a custom streaming protocol with the Anbox runtime.

This guide assumes that all steps are run on an Ubuntu 22.04 machine that hosts the [Anbox Cloud Appliance](https://discourse.ubuntu.com/t/install-appliance/22681).

## Preparation

A platform module must be built on the same version of Ubuntu as the Anbox runtime. This means that if you're using one of the Anbox images based on Ubuntu 22.04 (for example, `jammy:android12:arm64`), you must build on Ubuntu 22.04.

However, if you're running the Anbox Cloud Appliance on a machine with a different Ubuntu version, you can build the platform on a separate system (for example, in a LXD or docker instance or on another machine).

To get started, you must first install the [Anbox Platform SDK](https://github.com/anbox-cloud/anbox-platform-sdk). To do so, follow the [installation instructions](https://discourse.ubuntu.com/t/anbox-cloud-sdks/17844#anbox-platform-sdk-1).

## Build the example platform

The [Anbox Platform SDK](https://github.com/anbox-cloud/anbox-platform-sdk) comes with various examples that demonstrate different features. The following steps use the `minimal` example. Alternatively, choose the `nvidia` example if you're working with NVIDIA GPUs and want to see graphical output.

To build the `minimal` platform example, run the following commands:

    triplet=$(dpkg-architecture -qDEB_BUILD_MULTIARCH)
    cmake \
        -G Ninja \
        -B build \
        -DCMAKE_PREFIX_PATH=../../lib/anbox-platform-sdk/ \
        -DCMAKE_INSTALL_LIBDIR=lib/${triplet} \
        -DCMAKE_INSTALL_PREFIX=/usr examples/minimal/
    ninja -C build

The build process creates a `platform_minimal.so` module in the `build` directory.

## Install the example platform

[AMS](https://discourse.ubuntu.com/t/about-ams/24321) allows launching instances in a special [development mode](https://discourse.ubuntu.com/t/17763#dev-mode), which is helpful when developing, for example, addons or platforms. In development mode, the Anbox runtime does not terminate the instance when it detects failures or other problems.

To try out the `minimal` platform, complete the following steps:

1. Start a [raw instance](https://discourse.ubuntu.com/t/17763#application-vs-raw) with development mode turned on:

        amc launch --raw --devmode --instance-type=a4.3

   If you chose the `nvidia` example, you must select an [instance type](https://discourse.ubuntu.com/t/application-manifest/24197#instance-type-1) that supports GPUs:

        amc launch --raw --devmode --instance-type=g4.3

    [note type="information" status="Note"]Use the `--vm` option to launch a VM instance.[/note]

   The command prints out the ID of the instance. Note down this ID; you will need it in the next step.

   The start of the raw instance takes some time, because it runs through the full [bootstrap process](https://discourse.ubuntu.com/t/managing-applications/17760#bootstrap-process-2) before the instance is ready to be used.

1. When the instance is fully up and running, copy the `platform_minimal.so` module to it:

        id=<ID_of_the_instance>
        triplet=$(dpkg-architecture -qDEB_BUILD_MULTIARCH)
        amc exec "${id}" mkdir "/usr/lib/${triplet}/anbox/platforms/minimal"
        lxc file push build/platform_minimal.so "ams-${id}/usr/lib/${triplet}/anbox/platforms/minimal/"

1. With the platform plugin present inside the instance, configure the Anbox runtime to make use of it. For that, change the `/var/lib/anbox/session.yaml` configuration file within the instance:

        cat << EOF | amc exec "${id}" tee /var/lib/anbox/session.yaml
        log-level: debug
        platform: minimal
        EOF

   This command rewrites the Anbox runtime configuration to use the new `minimal` platform instead of the default one.

1. Restart Anbox inside the instance:

        amc exec "${id}" -- systemctl restart anbox

1. When the Anbox runtime was restarted, verify from the instance system log that it now uses the new `minimal` platform:

        amc logs "${id}"

   Inside the log, there should be a line similar to the following:

        [ 2022-12-07 14:00:18] [anbox-session] [base_platform.cpp:34@create] Using platform 'minimal'

   This line shows that the platform was successfully loaded and is in use by Anbox.

When developing a new platform, you can also directly invoke the Anbox runtime rather than start it via `systemd`. For that, stop the `anbox.service` unit first:

    amc exec "${id}" -- systemctl stop anbox

Then start the Anbox runtime directly by running:

    amc exec "${id}" -- anbox-starter

When you want to stop Anbox, you can use `CTRL`+`C` to send it the signal to terminate.

## Package the platform

To ship the platform to actual instance via AMS, you must create an [addon](https://discourse.ubuntu.com/t/managing-addons/17759) package that installs the platform into the instance.

A very simple addon to install the created `minimal` platform looks as follows:

    mkdir hooks
    cat << EOF > hooks/pre-start
    #!/bin/sh -ex

    # Only run for base instance
    [ "$INSTANCE_TYPE" = "regular" ] && exit0

    # Install the platform plugin into the right location
    # NOTE: Please adjust the path for the right architecture you're targeting
    mkdir -p /usr/lib/aarch64-linux-gnu/anbox/platforms/minimal
    cp "$ADDON_DIR"/platform_minimal.so /usr/lib/aarch64-linux-gnu/anbox/platforms/minimal/
    EOF
    chmod +x hooks/pre-start
    tar cjf minimal-addon.tar.bz2 hooks platform_minimal.so

Load this addon into AMS so that it can be used by applications and instances:

    amc addon add minimal minimal-addon.tar.bz2

When launching an instance, you must explicitly specify the platform that the Anbox runtime inside the instance should use with the `--platform` argument. If not specified, Anbox will use its default. To launch an instance with the `minimal` platform, run the following command:

    amc launch --raw --addon minimal --platform minimal

Use the `--vm` option to launch a VM instance.

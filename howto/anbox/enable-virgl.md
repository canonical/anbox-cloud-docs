Starting from the 1.21 release, Anbox Cloud has introduced a new rendering path to provide [Vulkan API](https://www.vulkan.org/) support for NVIDIA GPUs. This new stack is called VirGL as it is based on the open source Mesa [Venus driver](https://docs.mesa3d.org/drivers/venus.html) and the [virglrenderer](https://gitlab.freedesktop.org/virgl/virglrenderer) project. You can find more details in [Rendering architecture](https://discourse.ubuntu.com/t/35129).

In order to provide a migration path for existing users, the new rendering pipeline based on the VirGL stack is disabled by default in the 1.21 release of Anbox Cloud. With future releases, this will become the default.

The following describes steps necessary to enable the VirGL rendering pipeline.

## Upgrade to supported NVIDIA driver series

VirGL support in Anbox Cloud requires the NVIDIA driver series 545 or newer. With the 545 series, NVIDIA introduced support for the `VK_EXTERNAL_FENCE_HANDLE_TYPE_SYNC_FD_BIT` handle type which is essential for Android.

[note type="caution" status="Warning"]
The 545 series is a [feature branch](https://docs.nvidia.com/datacenter/tesla/drivers/index.html#comparison) and only supported for a short period of time by NVIDIA. Only the 550 series is going to be supported for a longer time period and should be used as soon as available as a stable release. Please note that not all driver releases are qualified for all GPU models.
[/note]

By default, Anbox Cloud installs the current long term release series of the NVIDIA driver, which is 535 (as of Anbox Cloud 1.21). To install 545 or newer, we need to upgrade an existing Anbox Cloud installation which is currently only supported for the Anbox Cloud Appliance. Support for upgrading an existing deployment of regular Anbox Cloud is planned for the [1.21.1 release](https://discourse.ubuntu.com/t/19359).

Before performing the driver upgrade, you have to stop all active instances on your installation. You do not have to delete them but need to stop them, for example by running:

    amc stop <instance id>

To upgrade the NVIDIA driver to the 545 driver series, run:

    /snap/anbox-cloud-appliance/current/bin/gpu-support.sh nvidia upgrade --driver-series=545 --no-server

This will remove the currently installed driver release and install the 545 driver packages from the Ubuntu archive. The `--no-server` option instructs the script to install the UDA driver variant. Without the option, the script will attempt to install the ERD variant of the given series. See the [official Ubuntu documentation](https://help.ubuntu.com/community/NvidiaDriversInstallation) for more information.

[note type="caution" status="Warning"]
NVIDIA does not provide an official qualified release of the 545 for datacenter GPUs. Please consult the NVIDIA documentation for more information on which GPUs are qualified and which not.
[/note]

Once the driver installation has been completed. You can start any existing instances again, for example by running

    amc start <instance id>

## Enable VirGL support

Support for the VirGL rendering pipeline is currently kept behind a feature flag and needs to be explicitly enabled. The feature flag `virgl.enable` can be set for individual instances, for applications or globally for all instances and applications.

To set the feature flag for a new instance, run:

    amc launch --features virgl.enable ...

To set the feature for an application, include the following in the `manifest.yaml`

    features: [virgl.enable]

To enable the feature flag globally for all instances, run:

    amc config set instance.features virgl.enable

## Related information

* [Rendering architecture](https://discourse.ubuntu.com/t/35129)

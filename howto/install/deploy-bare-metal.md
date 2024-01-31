To deploy Anbox Cloud on a public cloud (such as AWS, Azure or Google) or using MAAS or OpenStack, see the instructions in [How to deploy Anbox Cloud with Juju](https://discourse.ubuntu.com/t/deploy-anbox-cloud-with-juju/17744).

Alternatively, you can follow the instructions in this document to use the [manual cloud provider](https://jaas.ai/docs/manual-cloud) that Juju offers. This method allows you to deploy Anbox Cloud with Juju on a set of SSH connected machines.

## Prerequisites

Before you start the installation, ensure that you have the required prerequisites:

* At least three Ubuntu machines. See [Minimum hardware](https://discourse.ubuntu.com/t/requirements/17734#minimum-hardware-11) for details and recommendations.
* Your Ubuntu Pro token for an Ubuntu Pro subscription. If you don't have one yet, [speak to your Canonical representative](https://anbox-cloud.io/contact-us). If you already have a valid Ubuntu Pro token, log in to https://ubuntu.com/pro to retrieve it.
  [note type="caution" status="Warning"]The *Ubuntu Pro (Infra-only)* token does **NOT** work and will result in a failed deployment. You need an *Ubuntu Pro* subscription.[/note]

## Install Juju

Juju is a tool for deploying, configuring and operating complex software on public or private clouds.

You must install a Juju client on the machine that you use to run the deployment commands. To install Juju 2.9, enter the following command:

    sudo snap install --classic --channel=2.9/stable juju

See [Juju version](https://discourse.ubuntu.com/t/installation-requirements/17734#juju-version-10) for information about which Juju version is required for your version of Anbox Cloud.

## Add a controller and model

The [Juju controller](https://juju.is/docs/olm/controllers) is used to manage the software deployed through Juju, from deployment to upgrades to day-two operations. One Juju controller can manage multiple projects or workspaces, which in Juju are known as [models](https://juju.is/docs/olm/models).

You should dedicate one machine as the Juju controller. Run the following command to bootstrap the controller onto that machine:

    juju bootstrap manual/<user>@<controller IP address> anbox-cloud

Juju will connect to the machine via SSH as the specified user and install all necessary requirements.

When the controller is set up, create a model to hold the Anbox Cloud deployment:

    juju add-model main

## Add all machines

Before starting the deployment, you must add all machines to the Juju model. See [Minimum hardware](https://discourse.ubuntu.com/t/requirements/17734#minimum-hardware-11) for the list of machines that you need.

When adding the machines, start with the machine that you want to host the management layer of Anbox Cloud. Then add all LXD worker nodes. Run the following command for each machine:

    juju add-machine ssh:<user>@<machine IP address>

The user (for example, `ubuntu`) must have administrator rights on the machine and have permission to SSH to the machine.

[note type="caution" status="Warning"]Make sure to add the machines by their IP addresses rather than their DNS names. Adding a machine by DNS name does currently not work.[/note]

Juju will add the machines to its list of usable machines, which you can display with the `juju list-machines` command. Make sure that all machines are in the `started` state before you proceed. If any of the machines are still in `down` state, wait until they switch to `started`:

    Machine  State    DNS           Inst id              Series AZ Message
    0        started  192.168.1.9   manual:192.168.1.9   jammy     Manually provisioned machine
    1        started  192.168.1.10  manual:192.168.1.10  jammy     Manually provisioned machine

## Attach your Ubuntu Pro subscription

Create an `ua.yaml` overlay file as described in [How to deploy Anbox Cloud with Juju](https://discourse.ubuntu.com/t/deploy-anbox-cloud-with-juju/17744#ua-overlay).

You must provide this file when deploying Anbox Cloud.

## Determine the machine mapping

When running the deployment command, you must map the machines to the ones described in the [Juju bundle](https://discourse.ubuntu.com/t/about-anbox-cloud/17802#juju-bundles-7) that you are deploying.

Run `juju list-machines` to display the available machines:

    Machine  State    DNS            Inst id              Series  AZ             Message
    0        started  192.168.0.9   i-09a2fdb5e7a2e8385   jammy   localhost-1a   running
    1        started  192.168.0.10  i-00a05065e2768be5d   jammy   localhost-1b   running

The `anbox-cloud-core` deployment bundle requires two machines: `0` and `1`. `0` is supposed to host the AMS service. `1` is used for LXD. Check the `bundle.yaml` file in the bundle for details.

The `anbox-cloud` bundle requires two additional machines to host the load balancer (`0`) and the extra services required for streaming (`1`). For this bundle, the AMS machine is `2` and the LXD machine is `3`. Check the `bundle.yaml` file in the bundle for details.

The `--map-machine` argument for the `juju deploy` command maps the machines defined inside the bundle to those your Juju controller has registered in the model. See the [Juju documentation](https://jaas.ai/docs/charm-bundles) for more details. If you added the machines in the order Juju expects them, the mapping is very straight-forward: `--map-machines 0=0,1=1` for the `anbox-cloud-core` bundle or `--map-machines 0=0,1=1,2=2,3=3` for the `anbox-cloud` bundle.

<a name="customise-storage"></a>
## Customise storage

By default, Anbox Cloud uses a loop file with an automatically calculated size for LXD storage. For optimal performance, however, you should use a dedicated block storage device. See [LXD storage](https://discourse.ubuntu.com/t/anbox-cloud-overview/17802#lxd-storage-6) for more information.

There are different ways of configuring a dedicated block storage device:

- Use an existing LXD storage pool (recommended - see [Existing storage pool](#existing-storage-pool) below)
- Use a dedicated storage device (see [Dedicated storage device](#dedicated-storage-device) below)
- Use a storage device defined by Juju (see the *Customise storage* section in [How to deploy Anbox Cloud with Juju](https://discourse.ubuntu.com/t/install-with-juju/17744#customise-storage) for instructions)

<a name="existing-storage-pool"></a>
### Existing storage pool

To use an existing LXD storage pool, set the [`storage_pool`](https://charmhub.io/ams/configure#storage_pool) configuration on the AMS charm to the name of the LXD storage pool that you want Anbox Cloud to use.

For example, to use an existing LXD storage pool with the name `my-zfs-pool`, use an overlay file with the following content:

```
applications:
  ams:
    options:
      storage_pool: my-zfs-pool
```

[note type="information" status="Important"]
The LXD storage pool must use the ZFS storage driver. Other storage drivers are not supported by Anbox Cloud.
[/note]

<a name="dedicated-storage-device"></a>
### Dedicated storage device

To use a dedicated storage device that is not defined by Juju for LXD storage, set the [`storage_device`](https://charmhub.io/ams/configure#storage_device) configuration on the AMS charm to the path of the storage device.

For example, to use `/dev/sdb` as the dedicated storage device, use an overlay file with the following content:

```
applications:
  ams:
    options:
      storage_device: /dev/sdb
```

[note type="information" status="Important"]
The path to the dedicated storage device must be identical for all machines that are part of the cluster.
[/note]

You do not need to prepare the storage device in any way. AMS takes care of creating the LXD storage pool on the device.

## Deploy Anbox Cloud

Now you can deploy Anbox Cloud. The deployment is entirely handled by Juju and does not need any manual involvement other than running the actual deploy command.

Choose between the available [Juju bundles](https://discourse.ubuntu.com/t/about-anbox-cloud/17802#juju-bundles-7):

* For a minimised version of Anbox Cloud without the streaming stack, run the following command to deploy the `anbox-cloud-core` bundle:

        juju deploy anbox-cloud-core --overlay ua.yaml --map-machines 0=0,1=1

* For the full version of Anbox Cloud, run the following command to deploy the `anbox-cloud` bundle:

        juju deploy anbox-cloud --overlay ua.yaml --map-machines 0=0,1=1,2=2,3=3

You can watch the status of the deployment with the following command:

     watch -c juju status --color --relations=true

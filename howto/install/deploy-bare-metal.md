(howto-deploy-anbox-baremetal)=
# Deploy on bare metal

This document guides you through the steps to install Anbox Cloud on a [manual cloud](https://canonical-juju.readthedocs-hosted.com/en/latest/user/reference/cloud/list-of-supported-clouds/the-manual-cloud-and-juju/) that Juju offers i.e., you can deploy Anbox Cloud with Juju on a set of SSH connected machines.

## Prerequisites

Before you start the installation, ensure that you have the required prerequisites:

* At least three Ubuntu machines. See {ref}`sec-minimum-hardware-requirements` for details and recommendations.
* Your Ubuntu Pro token for an Ubuntu Pro subscription. If you don't have one yet, [speak to your Canonical representative](https://anbox-cloud.io/contact-us). If you already have a valid Ubuntu Pro token, log in to [Ubuntu Pro](https://ubuntu.com/pro) to retrieve it.
  ```{caution}
  The *Ubuntu Pro (Infra-only)* token does **NOT** work and will result in a failed deployment. You need an *Ubuntu Pro* subscription.
  ```

## Install Juju

Juju is a tool for deploying, configuring and operating complex software on public or private clouds.

To install Juju 3.x, enter the following command:

    sudo snap install --channel=3/stable juju

See {ref}`sec-juju-version-requirements` for information about which Juju version is required for your version of Anbox Cloud.

## Add a controller and model

The [Juju controller](https://canonical-juju.readthedocs-hosted.com/en/latest/user/reference/controller/) is used to manage the software deployed through Juju, including deployments, upgrades and other operations. One Juju controller can manage multiple projects or workspaces, known as [models](https://canonical-juju.readthedocs-hosted.com/en/latest/user/reference/model/).

You should dedicate one machine as the Juju controller. Run the following command to bootstrap the controller onto that machine:

    juju bootstrap manual/<user>@<controller IP address> anbox-cloud

Juju will connect to the machine via SSH as the specified user and install all necessary requirements.

When the controller is set up, create a model to hold the Anbox Cloud deployment:

    juju add-model main

## Add all machines

Before starting the deployment, you must add all machines to the Juju model. See {ref}`sec-minimum-hardware-requirements` for the list of machines that you need.

When adding the machines, start with the machine that you want to host the management layer of Anbox Cloud. Then add all LXD worker nodes. Run the following command for each machine:

    juju add-machine ssh:<user>@<machine IP address>

The user (for example, `ubuntu`) must have administrator rights on the machine and have permission to SSH to the machine.

```{caution}
Make sure to add the machines by their IP addresses rather than their DNS names. Adding a machine by DNS name does currently not work.
```

Juju will add the machines to its list of usable machines, which you can display with the `juju list-machines` command. Make sure that all machines are in the `started` state before you proceed. If any of the machines are still in `down` state, wait until they switch to `started`:

    Machine  State    DNS           Inst id              Series AZ Message
    0        started  192.168.1.9   manual:192.168.1.9   jammy     Manually provisioned machine
    1        started  192.168.1.10  manual:192.168.1.10  jammy     Manually provisioned machine

## Attach your Ubuntu Pro subscription

Create an `ua.yaml` overlay file as described in {ref}`sec-attach-pro-subscription`.

You must provide this file when deploying Anbox Cloud.

## Determine the machine mapping

When running the deployment command, you must map the machines to the ones described in {ref}`sec-juju-bundles` that you are deploying.

Run `juju list-machines` to display the available machines:

    Machine  State    DNS            Inst id              Series  AZ             Message
    0        started  192.168.0.9   i-09a2fdb5e7a2e8385   jammy   localhost-1a   running
    1        started  192.168.0.10  i-00a05065e2768be5d   jammy   localhost-1b   running

The `anbox-cloud-core` deployment bundle requires two machines: `0` and `1`. `0` is supposed to host the AMS service. `1` is used for LXD. Check the `bundle.yaml` file in the bundle for details.

The `anbox-cloud` bundle requires two additional machines to host the load balancer (`0`) and the extra services required for streaming (`1`). For this bundle, the AMS machine is `2` and the LXD machine is `3`. Check the `bundle.yaml` file in the bundle for details.

The `--map-machine` argument for the `juju deploy` command maps the machines defined inside the bundle to those your Juju controller has registered in the model. See the [Juju documentation](https://canonical-juju.readthedocs-hosted.com/en/latest/user/reference/bundle/) for more details. If you added the machines in the order Juju expects them, the mapping is very straight-forward: `--map-machines 0=0,1=1` for the `anbox-cloud-core` bundle or `--map-machines 0=0,1=1,2=2,3=3` for the `anbox-cloud` bundle.

(sec-customize-storage-bare-metal)=
## Customize storage

By default, Anbox Cloud uses a loop file with an automatically calculated size for LXD storage. For optimal performance, however, you should use a dedicated block storage device or [Ceph](https://ceph.io/). See {ref}`sec-lxd-storage` and {ref}`howto-use-ceph-storage` for more information.

### Local storage

There are different ways of configuring a dedicated block storage device:

- Use an {ref}`existing LXD storage pool <sec-existing-storage-pool>` (recommended)
- Use a {ref}`dedicated storage device <sec-dedicated-storage-device>`
- Use a storage device defined by Juju (see {ref}`sec-customize-storage-juju` for instructions)

(sec-existing-storage-pool)=
#### Existing storage pool

To use an existing LXD storage pool, set the [`storage_pool`](https://charmhub.io/ams/configuration#storage_pool) configuration on the AMS charm to the name of the LXD storage pool that you want Anbox Cloud to use.

For example, to use an existing LXD storage pool with the name `my-zfs-pool`, use an overlay file with the following content:

```
applications:
  ams:
    options:
      storage_pool: my-zfs-pool
```

```{important}
The LXD storage pool must use the ZFS storage driver. Other storage drivers are not supported by Anbox Cloud.
```
(sec-dedicated-storage-device)=
#### Dedicated storage device

To use a dedicated storage device that is not defined by Juju for LXD storage, set the [`storage_device`](https://charmhub.io/ams/configuration#storage_device) configuration on the AMS charm to the path of the storage device.

For example, to use `/dev/sdb` as the dedicated storage device, use an overlay file with the following content:

```
applications:
  ams:
    options:
      storage_device: /dev/sdb
```

```{important}
The path to the dedicated storage device must be identical for all machines that are part of the cluster.
```

You do not need to prepare the storage device in any way. AMS takes care of creating the LXD storage pool on the device.

## Deploy Anbox Cloud

Now you can deploy Anbox Cloud. The deployment is entirely handled by Juju and does not need any manual involvement other than running the actual deploy command.

Choose between the available Juju bundles (see {ref}`sec-juju-bundles`):

* For a minimized version of Anbox Cloud without the streaming stack, run the following command to deploy the `anbox-cloud-core` bundle:

        juju deploy anbox-cloud-core --overlay ua.yaml --map-machines 0=0,1=1

* For the full version of Anbox Cloud, run the following command to deploy the `anbox-cloud` bundle:

        juju deploy anbox-cloud --overlay ua.yaml --map-machines 0=0,1=1,2=2,3=3

## Monitor the deployment

After starting the deployment, Juju will create instances, install software and connect the different parts of the cluster together. This can take several minutes. You can monitor what's going on by running the following command:

    watch -c juju status --color --relations=true

## Perform necessary reboots

In some cases, a reboot of the LXD machines is necessary.

Check the output of the `juju status` command to see whether you need to reboot:

```sh
...
Unit       Workload  Agent  Machine  Public address  Ports      Message
lxd/0*     active    idle   3        10.75.96.23     8443/tcp   Actions: Reboot Required
...
```
To reboot the machine hosting LXD, run the following command:

    juju ssh lxd/0 -- sudo reboot

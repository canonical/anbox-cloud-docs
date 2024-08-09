(howto-upgrade-anbox-cloud)=
# How to upgrade Anbox Cloud

```{note}
If you're interested in getting notified for the latest Anbox Cloud releases, make sure you subscribe to notifications on the [announcements category](https://discourse.ubuntu.com/c/anbox-cloud/announcements/55) on the Anbox Cloud discourse.
```

Anbox Cloud allows upgrades from older versions to newer version. This describes the steps necessary to perform the upgrade.

The upgrade instructions detail the revisions each charm needs to be upgraded to, to bring it to the latest version. Next to the upgrade of the charms any used images or addons need to be updated as well.

## Prerequisites

As with all upgrades, there is a possibility that there may be unforeseen difficulties. It is highly recommended that you make a backup of any important data, including any running workloads.

You should also make sure that:

* Your deployment is running normally.
* Your Juju client and controller/models are running the latest version.
* You have read the release notes for the version you are upgrading to, which will alert you to any important changes to the operation of your cluster.

```{note}

The following assume you're using Juju >= 3.1. If you're using Juju 2.9, you have to map the following commands:

| Juju 3.x | Juju 2.9 |
|----------|----------|
| `juju refresh` | `juju upgrade-charm` |
| `juju exec` | `juju run` |

```

## Upgrade OS

Before you run the upgrade of the charms, you should make sure all packages on the machines that are part of the deployment are up-to-date. To do so, run the following commands on each machine:

    sudo apt update
    sudo apt upgrade

You can either run the package update manually or use the Juju command to run it for all machines.

    juju exec --all -- /bin/sh -c 'sudo apt update && sudo apt upgrade -y'

If the LXD charm is deployed on a machine that has an NVIDIA GPU installed, running the above command for the machine may upgrade the NVIDIA drivers, which accidentally suspends running instances with GPU support. Starting with the 1.17.1 release, the NVIDIA drivers are held from being upgraded until you upgrade the LXD charm using the Juju command. To check if the currently installed NVIDIA drivers are held from being upgraded:

    apt-mark showhold "libnvidia-.*-$(nvidia-smi --query-gpu=driver_version --format=csv,noheader | cut -d'.' -f1)"

If they are not, run the following command to do so:

    sudo apt-mark hold 'linux-modules-nvidia-*' 'nvidia-*' 'libnvidia-*'

## Check Juju version

Before you upgrade, check the required {ref}`sec-juju-version-requirements`.

If your deployment uses an earlier Juju version, you must upgrade your controller and all models first. See the [Juju documentation](https://juju.is/docs/olm/upgrade-models) for instructions on how to upgrade the Juju controller and all models to a newer Juju version.

## Upgrade all charms

The deployed Juju charms need to be upgraded next.

```{note}
- You can find a list of all charm, snap, bundle and Debian package versions for each Anbox Cloud release in the {ref}`ref-component-versions` overview. This also includes the charm and bundle revisions and channels for each release.

- If you want to deploy a particular revision of a charm, you can do so by adding `--revision=<rev>` to the `juju upgrade-charm` command.

- Starting with the 1.21 release, the NATS charm has been switched from its [older version](https://charmhub.io/nats-charmers-nats) to a [newer version](https://charmhub.io/nats) on Charmhub. This switch does not have any breaking changes from a user's perspective but since the framework of the charm has been overhauled, the upgrade to the new charm would require users to `switch` the charm's source while refreshing/updating the charm.

- Starting with the 1.22 release, the `anbox-stream-agent` charm has a new relation `client` which can be used to register new clients for the Anbox Stream Agent. This new relation is used by the new AMS charm to create stream-enabled instances using the `--enable-streaming` option. For deployments using the bundles from or after 1.22 release, the relation is created automatically. For users upgrading from older versions of Anbox Cloud, the relation needs to be manually created using `juju relate anbox-stream-agent:client ams:agent` after upgrading both the `ams` and the `anbox-stream-agent` charms to 1.22.
```

For any of the charm upgrades, you can watch the upgrade status by running:

     juju status

Continue with the next step only when the current step has completed successfully and all units in the output are marked as **active**.

```{note}
If you don't run Anbox Cloud in a high availability configuration, upgrading the charms will cause a short down time of individual service components during the process.
```

### Upgrade infrastructure components

As a first step, we will update all infrastructure components. This includes deployed internal certificate authorities and etcd.

First we update easyrsa:

    juju refresh internal-ca --revision=26
    juju refresh etcd-ca --revision=26

### Upgrade application registry

The Anbox Application Registry (AAR) can be updated independently of the other services. The upgrade process will cause a short down time of the service providing the registry API but connected AMS instances will retry connecting with it automatically.

To upgrade the registry, run

    juju refresh --channel=1.22/stable aar

### Upgrade control plane

If you have the streaming stack deployed, you need to update the charms responsible for the control plane next. If you do not use the streaming stack, you can skip this step.

```{note}
If you don't run any of the services in a high availability configuration, upgrading the charms will cause a short down time of the service.
```

To upgrade all charms, run the following commands:

    juju refresh --channel=1.23/stable anbox-cloud-dashboard
    juju refresh --channel=1.23/stable anbox-stream-gateway
    juju refresh --channel=1.23/stable anbox-stream-agent
    juju refresh --channel=1.23/stable coturn
    juju refresh --channel=latest/stable nats

```{note}
Since the NATS charm has been overhauled to use the modern charm framework (Ops Framework), a new charm source is needed to upgrade to its latest version. The charm source can be switched or replaced using the following command:

    juju refresh nats --switch=nats  --channel=stable
```

### Upgrade AMS

The AMS service needs to be updated independently of the other service components to ensure minimal down time. The charm can be upgraded by running the following command.

    juju refresh --channel=1.23/stable ams

### Upgrade LXD

As the last step, you have to upgrade the LXD cluster. Upgrading LXD will not restart running instances but it's recommended to take a backup before continuing.

As the first step, you need to upgrade the AMS node controller by running:

    juju refresh --channel=1.23/stable ams-node-controller

Once the upgrade is completed, you can continue upgrading LXD:

    juju refresh --channel=1.23/stable lxd

In some cases, specifically when you maintain bigger LXD clusters or want to keep a specific set of LXD nodes active until users have dropped, it makes sense to run the upgrade process manually on a per node basis. To enable this, you can set the following configuration option for the LXD charm before running the refresh command above:

    juju config lxd enable_manual_upgrade=true

This will allow you to run the actual upgrade process for each deployed LXD instance separately.

If you want to remove any nodes from the LXD cluster as part of the manual upgrade process, follow the instructions in {ref}`howto-scale-down-cluster` to prepare a node for removal and then remove it from the cluster.

Once the unnecessary nodes are dropped, the upgrade for a single LXD deployment unit can be triggered by running:

    juju run --wait=30m lxd/0 upgrade

Once the upgrade has completed, the unit will be marked as active.

For major and minor version upgrades, an update of the LXD charm may upgrade kernel modules or GPU drivers. This requires stopping any running instances before applying the upgrade and performing a reboot of the machine once the upgrade completed.

In case a reboot of the machine is required, a status message will be shown. When the machine has been rebooted, the status message can be cleared by running:

    juju run --wait=1m lxd/0 clear-notification

If the LXD charm is deployed on a machine with an NVIDIA GPU installed, by default, the NVIDIA drivers are held from being upgraded in case of downtime for all running instances due to either a manual upgrade or an [unattended-upgrade](https://wiki.debian.org/UnattendedUpgrades). The downside to this is that the machine may miss security updates for the NVIDIA drivers. To manually upgrade the NVIDIA drivers, you need to run the following Juju action:
    
    juju run --wait=30m lxd/0 upgrade-gpu-drivers

## Upgrade Debian packages

Some parts of Anbox Cloud are distributed as Debian packages coming from the [Anbox Cloud Archive](https://archive.anbox-cloud.io). In order to apply all pending upgrades, run the following commands on your machines:

    sudo apt update
    sudo apt upgrade

or apply the updates via [Landscape](https://landscape.canonical.com/) if available.

## Upgrade LXD images

LXD images are automatically being fetched by AMS from the image server once they are published.

Existing applications will be automatically updated by AMS as soon as the new image is uploaded. Watch out for new versions being added for any of the existing applications based on the new image version.

You can check for the status of an existing application by running:

    amc application show <application id or name>

In case automatic updates are disabled for applications, AMS cannot update the application. See {ref}`sec-configure-automatic-app-updates` to enable automatic updates or to manually update the applications.

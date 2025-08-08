(howto-upgrade-anbox-cloud)=
# Upgrade charmed deployment

```{note}
If you're interested in getting notified for the latest Anbox Cloud releases, make sure you subscribe to the [Anbox Cloud category](https://discourse.ubuntu.com/c/anbox-cloud/49) on the Ubuntu discourse.
```

Anbox Cloud supports only the latest release. This means that we support upgrades from n-1 to nth minor version, where n is the most recent minor version released.

If you are on an earlier version of Anbox Cloud than the most recent one, we recommend upgrading to the latest version as soon as possible. If you are multiple versions behind the supported version, there could be potential disruptions if you upgrade directly to the current version. The best practice in such a scenario is to upgrade incrementally, version by version.

This guide contains upgrade instructions for the charmed Anbox Cloud deployment. In addition to the upgrade of the charms, any used images or addons need to be updated as well.

## Prerequisites

As with all upgrades, there is a possibility that there may be unforeseen difficulties. It is highly recommended that you make a backup of any important data, including any running workloads.

Check if your deployment is running normally without any instances in an error state.

Read the release notes for your target version to learn about important changes that may affect your cluster operations.

### Upgrade Juju

Check the [required Juju version](https://documentation.ubuntu.com/anbox-cloud/reference/requirements/#juju).
If your deployment uses an earlier Juju version, you must upgrade your controller and all models first. See the [Juju documentation](https://canonical-juju.readthedocs-hosted.com/en/latest/user/howto/manage-models/#upgrade-a-model) for instructions on how to upgrade the Juju controller and all models to a newer Juju version.

### Upgrade OS

Before you run the upgrade of the charms, you should make sure all packages on the machines that are part of the deployment are up-to-date. To do so, run the following commands on each machine:

    sudo apt update
    sudo apt upgrade

You can either run the package update manually or use the Juju command to run it for all machines.

    juju exec --all -- /bin/sh -c 'sudo apt update && sudo apt upgrade -y'

To ensure NVIDIA drivers are upgraded only when the LXD charm is upgraded, the NVIDIA driver upgrades are held until you upgrade the LXD charm. So if the LXD charm is deployed on a machine that has an NVIDIA GPU installed, running this command on that machine may upgrade the NVIDIA drivers, which accidentally suspends running instances with GPU support.

To check if NVIDIA driver upgrades are held, run:

    apt-mark showhold "libnvidia-.*-$(nvidia-smi --query-gpu=driver_version --format=csv,noheader | cut -d'.' -f1)"

If the upgrades are not held, run the following command to hold them until the LXD charm is upgraded:

    sudo apt-mark hold 'linux-modules-nvidia-*' 'nvidia-*' 'libnvidia-*'


## Upgrade all charms

You can find a list of all charm, snap, bundle and Debian package versions for each Anbox Cloud release in the {ref}`ref-component-versions` overview. This also includes the charm and bundle revisions and channels for each release.

Before you run the `juju refresh` command to upgrade the charms, there are a few points you should know:

* If you don't run Anbox Cloud in a high availability configuration, upgrading the charms will cause a short down time of individual service components during the process.
* Starting with the 1.21 release, the NATS charm has been switched from its [older version](https://charmhub.io/nats-charmers-nats) to a [newer version](https://charmhub.io/nats) on Charmhub. This switch does not have any breaking changes from a user's perspective but since the framework of the charm has been overhauled, the upgrade to the new charm would require users to `switch` the charm's source while refreshing/updating the charm.
* Starting with the 1.22 release, the `anbox-stream-agent` charm has a new relation `client` which can be used to register new clients for the Anbox Stream Agent. This new relation is used by the new AMS charm to create stream-enabled instances using the `--enable-streaming` option. For deployments using the bundles from or after 1.22 release, the relation is created automatically. For users upgrading from older versions of Anbox Cloud, the relation needs to be manually created using `juju relate anbox-stream-agent:client ams:agent` after upgrading both the `ams` and the `anbox-stream-agent` charms to 1.22.
* If you want to deploy a particular revision of a charm, you can do so by adding `--revision=<rev>` to the `juju upgrade-charm` command.
* For any of the charm upgrades, you can watch the upgrade status by running `juju status`.

  At any point during the upgrade process, proceed to the next step only when the current step has completed successfully and all units in the `juju status` output are marked as **active**.

### Upgrade infrastructure components

As a first step, upgrade all infrastructure components. This includes deployed internal certificate authorities and etcd.

Upgrade easyrsa:

    juju refresh internal-ca --channel=1.31/stable --revision=66
    juju refresh etcd-ca --channel=1.31/stable --revision=66

### Upgrade application registry

The Anbox Application Registry (AAR) can be upgraded independently of other services. The upgrade process will cause a short downtime of the service providing the registry API but AMS instances that are already connected will retry connecting with the service automatically.

Upgrade the registry:

    juju refresh --channel=1.26/stable aar

### Upgrade control plane

If you have the streaming stack deployed, the next step is to update the charms responsible for the control plane. If you do not use the streaming stack, you can skip this step and proceed to upgrading AMS.

```{note}
If you don't run any of the services in a high availability configuration, upgrading the charms will cause a short down time of the service.
```

To upgrade all charms, run the following commands:

    juju refresh --channel=1.26/stable anbox-cloud-dashboard
    juju refresh --channel=1.26/stable anbox-stream-gateway
    juju refresh --channel=1.26/stable anbox-stream-agent
    juju refresh --channel=1.26/stable coturn
    juju refresh --channel=latest/stable nats

```{note}
Since the NATS charm has been overhauled to use the modern charm framework (Ops Framework), a new charm source is needed to upgrade to its latest version. The charm source can be switched or replaced using the following command:

    juju refresh nats --switch=nats  --channel=stable
```

### Upgrade AMS

Upgrade the AMS service independently of the other service components to ensure minimal down time:

    juju refresh --channel=1.26/stable ams

### Upgrade LXD

As the last step, upgrade the LXD cluster. Upgrading LXD will not restart running instances but it's recommended to take a backup before continuing.

```{note}
In Anbox Cloud's 1.25.0 release, the LXD charm has been reworked and hence there are changes in the upgrade instructions for the charm.
```

<details>
<summary>Click here for upgrade instructions for Anbox Cloud versions < 1.25.0 </summary>
In some cases, specifically when you maintain bigger LXD clusters or want to keep a specific set of LXD nodes active until users have dropped, it is pragmatic to run the upgrade process manually on a per node basis. To manually upgrade individual nodes, run the following command before running the `juju refresh` command:

    juju config lxd enable_manual_upgrade=true

This will allow you to run the actual upgrade process for each deployed LXD instance separately.

If you want to remove any nodes from the LXD cluster as part of the manual upgrade process, follow the instructions in {ref}`howto-scale-down-cluster` to prepare a node for removal and then remove it from the cluster.

Once the unnecessary nodes are dropped, the upgrade for a single LXD deployment unit can be triggered by running:

    juju run --wait=30m lxd/0 upgrade

Once the upgrade has completed, the unit will be marked as active.

Major and minor version upgrades may include upgrades to kernel modules or GPU drivers. This requires stopping any running instances before applying the upgrade and performing a reboot of the machine once the upgrade completed.

In case a reboot is required, a notification is displayed. When the machine is rebooted, you can clear the notification by running:

    juju run --wait=1m lxd/0 clear-notification

If the LXD charm is deployed on a machine with an NVIDIA GPU installed, by default, the NVIDIA drivers are held from being upgraded as it may cause downtime for all running instances. The downside to this held upgrade is that security updates for the NVIDIA drivers could be missed. To manually upgrade the NVIDIA drivers, run:

    juju run --wait=30m lxd/0 upgrade-gpu-drivers

</details>

```{important}
If you are running LXD clusters with the LXD snap from a channel other than 5.21/stable, you need to set the current LXD channel before running the `upgrade-cluster` command. You can set this by running a command like

    juju config lxd channel=5.0/stable

where `5.0/stable` is the currently installed LXD snap channel. Not doing this might lead to a broken LXD cluster.
```

To start, upgrade the AMS LXD charm to the latest revision using:

    juju refresh --channel=1.26/stable lxd

Upgrading the charm does not upgrade the LXD snap or any of the internal packages on the LXD node. After updating the charm, check which nodes have package updates available using:

    juju run lxd/0 upgrade-info

Make a note of all the Juju units having available updates. Before proceeding, make sure that there are no active instances on the nodes. Then mark each LXD node that has updates available as unschedulable in AMS.

    juju run ams/leader node-start-maintenance node=”<node_name>”

where `<node_name>` refers to the LXD node name stored in AMS, e.g. `lxd0` if the Juju unit is `lxd/0`. This ensures that no new instances are spawned on those LXD nodes.

After a node is successfully marked as unschedulable, we can safely upgrade it. To do this, run:

    juju run lxd/<unit_number> --wait=30m upgrade-machine reboot=<true_or_false>

where `<unit_number>` refers to the Juju unit number on the corresponding node.

Upgrading a node will also upgrade the GPU drivers and the installed kernel modules. When done, this action might require a reboot to successfully load the new modules and drivers. If you want to set the reboot to happen automatically, set `reboot=true`. Otherwise, run `juju exec lxd/<unit_number> -- sudo reboot` when you are ready to reboot the node.

After the upgrades to all the nodes have finished, upgrade the LXD snap on the node using:

    juju run lxd/<unit_number> --wait=30m upgrade-cluster

Finally after all the upgrades finish and the nodes are healthy, run:

    juju run ams/leader node-end-maintenance node=”<node_name>”

where `<node_name>` refers to the LXD node name stored within AMS.

As a subordinate charm deployed alongside the LXD charm, and following the [deprecation of the node controller charm](https://documentation.ubuntu.com/anbox-cloud/reference/deprecation-notices/#node-controller-charm) in the Anbox Cloud 1.26.0 release, the node controller will no longer manage port forwarding for service exposure on Anbox instances.

For security reasons, any ports previously exposed by the node controller will be closed after upgrading it via:

       juju refresh --channel=1.26/stable ams-node-controller

If there is no need to expose services from Anbox instances, revokes the application's exposure to the public network after the AMS node controller is upgraded:

       juju unexpose ams-node-controller

If you do need to allow external access to services running inside LXD nodes, run:

       juju expose lxd
       juju config lxd exposed_instance_ports=10000-11000

To revoke external access to services after enabling it for the LXD charm, run:

       juju unexpose lxd


## Upgrade Debian packages

Some parts of Anbox Cloud are distributed as Debian packages coming from the [Anbox Cloud Archive](https://archive.anbox-cloud.io). In order to apply all pending upgrades, run the following commands on your machines:

    sudo apt update
    sudo apt upgrade

or apply the updates via [Landscape](https://landscape.canonical.com/), if available.

## Upgrade LXD images

LXD images are automatically being fetched by AMS from the image server once they are published.

Existing applications will be automatically updated by AMS as soon as the new image is uploaded. Watch out for new versions being added for any of the existing applications.

You can check the status of an existing application by running:

    amc application show <application_id_or_name>

In case automatic updates are disabled for applications, AMS cannot update the application. You need to manually update the applications using:

    amc application update <application_id_or_name> <path_of_new_application_payload>

See {ref}`sec-configure-automatic-app-updates` for instructions on enabling automatic updates.

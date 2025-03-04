(ref-requirements)=
# Requirements

To run Anbox Cloud, you must fulfill a few minimum requirements, which differ depending on whether you plan to use charmed Anbox Cloud or the appliance.

See {ref}`sec-variants` for an explanation of the differences between both variants.

## General requirements

The following requirements apply to both variants of Anbox Cloud.

### Ubuntu Pro token

After registering to Anbox Cloud, you should have received an [Ubuntu Pro](https://ubuntu.com/pro) token. If you haven't received one, please contact [support](https://support.canonical.com/) or your Canonical account representative as you'll need it to deploy Anbox Cloud.

### Ubuntu OS

Anbox Cloud is supported only on the [Ubuntu](https://ubuntu.com/) operating system. Other Linux-based operating systems are not supported. You must run either the [server](https://ubuntu.com/download/server) or the [cloud](https://ubuntu.com/download/cloud) variant of Ubuntu. Running Anbox Cloud on an Ubuntu Desktop installation is not supported and could cause issues.

The later sections of this topic provide information about the supported Ubuntu versions.

## Requirements for the appliance

### Ubuntu

The appliance supports the following Ubuntu versions:

* Ubuntu 22.04 (Jammy Jellyfish)
* Ubuntu 24.04 (Noble Numbat)

### LXD 

The appliance supports LXD >= 5.0.

By default, LXD is installed from the `5.21/stable` track.

If LXD is already installed but the version is earlier than 5.0, run `snap refresh --channel=5.21/stable lxd` to update it. If you are already on LXD version 5.21, [do not downgrade it as it may render LXD unusable](https://documentation.ubuntu.com/lxd/en/latest/installing/#upgrade-lxd).

### Hardware requirements

The following hardware specifications are required for running the appliance:

* 64 bit x86 or Arm CPU with >= 4 CPU cores
* 8 GB of memory
* 30 GB of free disk space on the main disk
* (optional) 100GB block volume to host instance storage

The above recommendation is the minimum requirement to run the appliance. As Anbox Cloud is dependent on available resources to launch its Android containers, the available resources dictate the maximum number of possible Android containers. See {ref}`exp-capacity-planning` for an explanation on how to plan for a specific capacity on your appliance.

On public clouds, it is always recommended to allocate an additional storage volume for instance storage. If no additional storage volume is available, the appliance creates an on-disk image and uses it for instance storage. This is sufficient for very simple cases but does not provide optimal performance and will slow down operations and instance startup time.

For external access, you must expose a couple of network ports on the machine where the appliance is running. See {ref}`ref-network-ports` for the list of ports that must be exposed. How to allow incoming traffic on the listed ports differs depending on the cloud used. See the documentation of the cloud for further information on how to change the firewall.

## Requirements for charmed Anbox Cloud

Anbox Cloud deployments are managed by Juju. They can be created on all the [supported clouds](https://canonical-juju.readthedocs-hosted.com/en/latest/user/reference/cloud/) as well as manually provided machines as long as the minimum requirements are met.

### Ubuntu

Charmed Anbox Cloud supports Ubuntu 22.04 (Jammy Jellyfish).

```{note}
The HAProxy load balancer currently has no support for Ubuntu 22.04. Therefore, the Juju bundle uses Ubuntu 20.04 for the machine that runs the load balancer.
```

### LXD

Charmed Anbox Cloud requires LXD version >= 5.0.

(sec-juju-version-requirements)=
### Juju

The charmed Anbox Cloud requires [Juju 2.9 or later](https://juju.is/) to manage the different components and their dependencies. You can install Juju with the following command:

    snap install --classic --channel=3.1/stable juju

If you wish to install a different version, replace `3.1` in the command with the desired version.

To switch to the 2.9 series, use the following command:

    snap refresh --channel=2.9/stable juju

See the [Juju documentation](https://canonical-juju.readthedocs-hosted.com/en/latest/user/howto/manage-juju/#install-juju) for more information.

(sec-minimum-hardware-requirements)=
### Hardware requirements

While you can run Anbox Cloud on a single machine, we strongly recommend using several machines for a production environment.

To run an Anbox Cloud deployment including the streaming stack, we recommend the following setup:

| ID | Architecture   | CPU cores | RAM  | Disk       | GPUs |  FUNCTION |
|----|----------------|-----------|------|------------|------|------------|
| -  | amd64 or arm64 | 4         | 4GB  | 50GB SSD   | no   |  Hosts the  [Juju controller](https://juju.is/docs/juju/controller)  |
| 0  | amd64 or arm64 | 2         | 2GB  | 100GB SSD  | no   |  Hosts the load balancer |
| 1  | amd64 or arm64 | 4         | 8GB  | 100GB SSD  | no   |  Hosts the streaming stack control plane |
| 2  | amd64 or arm64 | 4         | 8GB  | 100GB SSD  | no   |  Hosts the management layer of Anbox Cloud (for example, AMS) |
| 3  | amd64 or arm64 | 8         | 16GB | 200GB NVMe | optional   |  LXD worker node that hosts the actual containers or virtual machines  |

To run the core version of Anbox Cloud without the streaming stack, we recommend the following setup:

| ID | Architecture   | CPU cores | RAM  | Disk       | GPUs |  FUNCTION |
|----|----------------|-----------|------|------------|------|------------|
| -  | amd64 or arm64 | 4         | 4GB  | 50GB SSD   | no   |  Hosts the  [Juju controller](https://juju.is/docs/juju/controller)  |
| 0  | amd64 or arm64 | 4         | 8GB  | 100GB SSD  | no   |  Hosts the management layer of Anbox Cloud (for example, AMS)  |
| 1  | amd64 or arm64 | 8         | 16GB | 200GB NVMe | optional   |  LXD worker node that hosts the actual containers or virtual machines  |

Some additional information:

- The ID in the table corresponds to the ID that the Juju bundle uses.
- You can mix architectures for the different machines. However, if you have several LXD nodes, all of them must have the same architecture.
- The specified number of cores and RAM is only the minimum required to run Anbox Cloud at a sensible performance.

  More CPU cores and more RAM on the machine hosting LXD will allow to run a higher number of instances. See {ref}`exp-capacity-planning` for an introduction of how many resources are necessary to host a specific number of instances.
- If you require GPU support, see {ref}`ref-rendering-resources` for a list of supported GPUs.

Applications not maintained by Anbox Cloud may have different hardware recommendations:
 - **etcd**: [Hardware recommendations](https://etcd.io/docs/v3.5/op-guide/hardware/)
 - **HAProxy** (load balancer for the Stream Gateway and the dashboard): [Installation](https://www.haproxy.com/documentation/hapee/latest/getting-started/hardware/)

Please note that these are just baselines and should be adapted to your workload. No matter the application, monitoring and tuning the performance is always important. See {ref}`exp-performance` for more information.

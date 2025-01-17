(exp-anbox-cloud)=
# Anbox Cloud

Anbox Cloud provides a rich software stack that enables you to run Android applications in the cloud for different use cases, including high-performance streaming of graphics to desktop and mobile client devices.

Anbox Cloud maintains a single Android system per instance, providing higher density and better performance per host while ensuring security and isolation of each instance. Depending on the target platform, payload, and desired application performance (for example, frame rate), Anbox Cloud can run more than 100 instances on a single machine.

Watch [this video](https://youtu.be/P7md88WhOC0?si=eUGiQtQ-9uXmZOQu) to learn more about how you can deploy Anbox Cloud with charms.

(sec-variants)=
## Variants

Anbox Cloud comes in two variants that serve different purposes:

**Anbox Cloud Appliance**

The Anbox Cloud Appliance is a self-contained deployment variant of Anbox Cloud. It combines all elements of Anbox Cloud in a single snap package for installation and management on a single machine. In this way, the Anbox Cloud Appliance allows simple and fast development and prototyping.

**Anbox Cloud**

The charmed Anbox Cloud uses [Juju](https://juju.is/) for deployment and operations. It provides rich features and is best suited for a large scale deployment.

See the following table for a comparison of features for the different variants:

| Feature | Anbox Cloud Appliance | Anbox Cloud |
|---------|-----------------------|-------------|
| {ref}`exp-application-streaming` | ✓ | ✓ |
| {ref}`exp-web-dashboard` | ✓ | ✓ |
| {ref}`Android versions <ref-provided-images>` | 12, 13, 14 | 12, 13, 14 |
| [Security updates](https://ubuntu.com/support) | ✓ | ✓ |
| [Community support](https://discourse.ubuntu.com/c/anbox-cloud/users/148) | ✓ | ✓ |
| [Vendor support available](https://ubuntu.com/support) | ✓* | ✓ |
| {ref}`exp-clustering`| - | ✓ |
| {ref}`exp-custom-images`| ✓ | ✓ |

*\* When purchasing the Anbox Cloud Appliance through the AWS Marketplace, the Ubuntu Pro subscription does not include vendor support.*

We recommend starting with the Anbox Cloud Appliance. You can choose to expand to a charmed Anbox Cloud installation later.

## Anbox Cloud Components

Anbox Cloud consists of the core stack, the streaming stack, and user-specific components that complete the streaming stack. The core stack includes all components that are required for a basic deployment of Anbox Cloud and also some additional, optional components. The streaming stack includes components which are optional but required for streaming.

An Anbox Cloud cluster can consist of the core stack or if streaming functionality is required, the streaming stack along with the core stack. An Anbox Cloud cluster can have multiple subclusters. The components inside a subcluster are explained in detail further in this topic.

The diagrams used to explain the architecture in this topic show the recommended way of collocating components. However, it is possible to collocate more components on the same machine, or to have separate machines for components that are collocated in the picture.

### Core stack

The diagram below depicts the core stack and its components:

![Anbox Cloud core stack|690x398](/images/anbox-cloud-architecture-diagrams/core_stack.png)

The core stack contains one or more Anbox subclusters, a Juju controller, and the Anbox Application Registry (AAR).

Inside each Anbox subcluster, the following components are present:

* **Anbox Management Service (AMS)** - AMS is the management tool for Anbox Cloud. It handles all aspects of the application and instance life cycle, including application and image update, while ensuring high density, performance, and fast startup times.

  Users can connect to AMS via CLI or HTTP API calls on port 8444. AMS is installed as a snap on each of the control nodes and interacts with the instances, requesting and releasing resources as per demand.

* **Anbox Management Client (AMC)**  - You can choose to install AMC on other machines to {ref}`control AMS remotely <howto-access-ams-remote>`, but it is generally installed together with AMS. A developer or system administrator will manage AMS through the command line interface (AMC) or through custom-built tools interacting with the AMS HTTP API.

* **etcd** - etcd is the database that is used to store the data managed by AMS. It provides a reliable way to store data across a cluster of machines. It gracefully handles primary node selections when a network is split into subnets and will tolerate machine failure. For more information, see [etcd](https://etcd.io/).

* **Control node** - Control node is the machine on which the AMS, AMC, and etcd are installed. These three components inside the control node make up the management layer of Anbox Cloud.

Each Anbox subcluster also has a number of LXD worker nodes that form a LXD cluster. Each LXD worker node runs the following components:

* **LXD** - The LXD daemon spawns a number of LXD instances containing Anbox-related configuration. These instances provide an Ubuntu environment that uses the hardware of the LXD worker node, including CPUs, disks, networks, and if available, GPUs. Each LXD instance runs exactly one Android instance that the end user can access/stream.

   ```{note}
   The term LXD instance means that they are LXD containers or virtual machines that contain configuration related to Anbox Cloud. Within the context of Anbox Cloud, the term Anbox Cloud images is used interchangeably with LXD images in the sense that they are LXD images containing specific configuration related to Anbox Cloud.
   ```

* **AMS node controller** – The AMS node controller puts the appropriate firewall rules in place when an instance is started or stopped to control ingress and egress traffic.

Outside the Anbox subcluster, you have the following machines:

  * **Juju controller**, which controls how Anbox Cloud is deployed and managed.
  * **Anbox Application Registry (AAR)**, which provides a central repository for applications created on Anbox Cloud. Using an AAR is very useful for larger deployments involving multiple subclusters, in order to keep applications in sync. This component is not mandatory, but strongly recommended in a production deployment, to keep applications in sync across the different subclusters.

### Streaming stack

The diagram below depicts the streaming stack along with the core stack and user specific components:

![Anbox Cloud streaming stack|690x440](/images/anbox-cloud-architecture-diagrams/core_and_streaming_stack.png)

When the streaming stack is in use, each Anbox subcluster has the following additional components:

* **TURN/STUN servers** - Servers that find the most optimal network path between a client and the application running on Anbox Cloud. The streaming stack provides secure STUN and TURN servers, but you can use public ones as well.

* **Stream agent** - Serves as an entry point that the gateway can connect to to talk to the AMS of the Anbox subcluster.

You also need an additional machine to host the streaming stack control plane with the following components:

  * **Stream gateway** - The central component that connects clients with agents. Its role is to choose the best possible subcluster depending on the user location and server capacities.
  * **NATS** - A messaging system that the different components use to communicate. NATS is  responsible for the communication between the stream gateway and the stream agent. For more information, see [NATS protocol](https://docs.nats.io/reference/reference-protocols/nats-protocol).

You will be required to provide one or more frontend services. A frontend service authenticates the client with the stream gateway and can provide other functionality, such as, selecting a game.

For example, your web client can be a mobile app used to access the provided Android containers. We provide the {ref}`sec-streaming-sdk` as a starting point for creating a web client. The web dashboard in Anbox Cloud is an example for a frontend service and web client, combined into one.

## LXD

Anbox Cloud includes LXD for hosting and managing the Ubuntu instances that run the nested Android containers.

LXD is installed through the [`ams-lxd` charm](https://charmhub.io/ams-lxd), which adds some Anbox-specific configuration to LXD. AMS configures LXD automatically and fully manages it, which means that in most scenarios, you do not need to worry about LXD at all.

If you want to monitor LXD, you can always run `lxc list` to display the existing instances. For the full deployment, LXD hosts the instances created by AMS. If you run the Anbox Cloud Appliance, LXD hosts instances for the different Juju machines that Anbox Cloud requires:

```
+--------------------------+---------+------------------------+------+-----------+-----------+----------+
|           NAME           |  STATE  |          IPV4          | IPV6 |   TYPE    | SNAPSHOTS | LOCATION |
+--------------------------+---------+------------------------+------+-----------+-----------+----------+
| ams-cdr3292j841mb72gksog | RUNNING | 192.168.96.1 (eth0)    |      | CONTAINER | 0         | lxd0     |
|                          |         | 192.168.250.1 (anbox0) |      |           |           |          |
+--------------------------+---------+------------------------+------+-----------+-----------+----------+
| juju-73e292-0            | RUNNING | 240.0.233.254 (eth0)   |      | CONTAINER | 0         | lxd0     |
+--------------------------+---------+------------------------+------+-----------+-----------+----------+
| juju-73e292-1            | RUNNING | 240.0.98.38 (eth0)     |      | CONTAINER | 0         | lxd0     |
+--------------------------+---------+------------------------+------+-----------+-----------+----------+
| juju-73e292-2            | RUNNING | 240.0.61.208 (eth0)    |      | CONTAINER | 0         | lxd0     |
+--------------------------+---------+------------------------+------+-----------+-----------+----------+
| juju-34631c-0            | RUNNING | 240.0.180.30 (eth0)    |      | CONTAINER | 0         | lxd0     |
+--------------------------+---------+------------------------+------+-----------+-----------+----------+
```
(sec-lxd-storage)=
### LXD storage

For LXD storage, Anbox Cloud uses a ZFS storage pool, which it creates automatically. This storage pool can be located on either a dedicated block storage device or a loop file. See [Data storage location](https://documentation.ubuntu.com/lxd/en/latest/explanation/storage/#data-storage-location) in the LXD documentation for more information.

While a loop file is easy to set up, it is much slower than a block device. Therefore, we recommend using a block device that is dedicated to LXD storage only.

If you are doing a full deployment, configure the storage before starting the deployment. See {ref}`customize storage when deploying with Juju <sec-customize-storage-juju>` or {ref}`customize storage when deploying on bare metal <sec-customize-storage-bare-metal>` for instructions. If you skip the configuration, Anbox Cloud sets up a loop-file with an automatically calculated size, which is not recommended.

If you are using the Anbox Cloud Appliance, you are prompted during the initialization process to specify the storage location, and, if you choose a loop file, its size. When choosing a size, keep in mind that the loop file cannot be larger than the root disk, and that it will cause the disk to fill up as the loop file grows to its maximum size over time. The created storage pool is used to store all Anbox Cloud content, including the instances created by Juju.

(sec-juju-bundles)=
## Juju bundles

The charmed Anbox Cloud variant provides two different Juju bundles:

* The `anbox-cloud-core` bundle provides a minimized version of Anbox Cloud. This version is sufficient if you don't want to use the Anbox Cloud streaming stack.

  For more information, see the [charm page](https://charmhub.io/anbox-cloud-core).

* The `anbox-cloud` bundle provides the full version of Anbox Cloud, including its streaming stack.

  For more information, see the [charm page](https://charmhub.io/anbox-cloud).

```{tip}
For detailed information about the charm, check the `bundle.yaml` file in the bundle.

You can download the bundle with `juju download <charm_name>`, thus `juju download anbox-cloud-core` or `juju download anbox-cloud`. Unzip the bundle to access the `bundle.yaml` file.
```

If you don't need to stream the visual output of the Android containers, you can use the `anbox-cloud-core` bundle. Otherwise, you should use the `anbox-cloud` bundle. However, even without the streaming stack, there are still ways to get visual access for inspection purposes. See {ref}`howto-access-instance` for more information.

## Related topics

* {ref}`exp-instances`

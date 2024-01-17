While it is possible to install Anbox Cloud on a single machine, you usually want to distribute the load over several machines in a cluster.

The Anbox Cloud Appliance provides only basic and experimental support for multi-node setups, however, Anbox Cloud provides full clustering support.

<a name="multi-node-appliance"></a>
## Multi-node support for the Anbox Cloud Appliance

If you're running the Anbox Cloud Appliance and you want to extend the available instance capacity, you can [join additional machines to the appliance](https://discourse.ubuntu.com/t/how-to-join-a-machine-to-the-anbox-cloud-appliance/29054).

The appliance uses [FAN networking](https://wiki.ubuntu.com/FanNetworking) to spawn an overlay network that allows instances on different machines to communicate with each other. This setup extends the capacity, but currently, it does not provide support for high availability (HA).

[note type="information" status="Note"]FAN networking requires a `/16` or `/24` subnet on the network interface. If the appliance is installed on a machine that is not on such a subnet, the appliance disables FAN networking. In such cases, extending the appliance with additional nodes is be possible.[/note]

<a name="clustering-anbox-cloud"></a>
## Clustering for full Anbox Cloud deployments

In a clustering setup for a full Anbox Cloud deployment, one node is dedicated as the management node to host the Anbox Management Service (AMS). If you use the Streaming Stack, two additional nodes are dedicated to host the extra services required for streaming. All other nodes are used as worker nodes.

Each worker node runs [LXD](https://ubuntu.com/lxd) in [clustering mode](https://documentation.ubuntu.com/lxd/en/latest/clustering/), and this LXD cluster is used to host the Android containers.

### Cluster capacity

Anbox Cloud is optimised to provide instances at high density per host. To determine how many cluster nodes you need and what resources they should have, you must estimate the capacity that you require for your use case. See [About capacity planning](https://discourse.ubuntu.com/t/about-capacity-planning/28717) for more information.

### LXD auto scaling

Different use cases for Anbox Cloud require elasticity of the LXD cluster to deal with dynamic user demand throughout a certain time period. This involves increasing the number of nodes of the LXD cluster when demand increases and reducing the number of nodes when demand decreases. As Anbox Cloud provides fine-grained capacity management to have tight control over how many users/instances are running on a single node, the driving factor for an auto scaling implementation cannot be deduced from CPU, memory or GPU load but from the planned capacity of the currently available nodes in the cluster.

The current release of Anbox Cloud has no built-in auto scaling implementation but comes with all needed primitives to build one. In a future version, Anbox Cloud will provide an auto scaling framework that will simplify various aspects of an implementation.

#### Guidelines for auto scaling

The following guidelines are both recommended and must-have aspects of an auto scaling implementation. Make sure that your auto scaling implementation follows these to stay within a supported and tested scope.

1. Don't scale the LXD cluster to less than three nodes. You should keep three active nodes at all times to ensure the database that LXD uses can achieve a quorum and is highly available. If you scale down to less than three nodes, your cluster is very likely to get into a non-functional state or be lost completely. In case this happens, see [LXD documentation](https://documentation.ubuntu.com/lxd/en/latest/howto/cluster_recover/) on how to recover a cluster.
1. A single LXD cluster should take no more than 40 nodes.
1. If you need more than 40 nodes, you should create a separate cluster in a separate Juju model with its own AMS.
1. Scaling a cluster up with multiple new nodes in parallel is fine and recommended if you need to quickly increase your cluster capacity.
1. Scaling down **MUST** strictly happen in a sequential order with no other scaling operations (for example, scale up) running in parallel.
1. Before removing a LXD node from the cluster you **MUST** delete all instances on it.

### Scaling up or down the cluster

The decision of when to scale a cluster up or down is not simple and is different for each use case. The traditional approach to measure CPU, memory or GPU load does not apply for Anbox Cloud as capacity is well-planned and the number of instances per node is configured ahead of time. Furthermore, user patterns are hard to predict and will be different in each case. Hence, custom logic is required to take a decision when a cluster should be scaled up or down.

Anbox Cloud provides [various metrics](https://discourse.ubuntu.com/t/prometheus-metrics/19521) to help decide when to scale up or down. Based on these metrics, together with data from a production system, you can build a model trying to predict when auto scaling should trigger.

Future versions of Anbox Cloud will provide a framework which will help to implement such a model.

See [How to scale up a LXD cluster](https://discourse.ubuntu.com/t/scale-up-a-lxd-cluster/24322) and [How to scale down a LXD cluster](https://discourse.ubuntu.com/t/scale-down-a-lxd-cluster/24323) for instructions on how to add or remove nodes from the cluster.

## Related information
* [Manage cluster nodes](https://discourse.ubuntu.com/t/how-to-manage-cluster-nodes/24334)

(exp-clustering)=
# Clustering

While it is possible to install Anbox Cloud on a single machine, Anbox Cloud Appliance does not support multi-node setups. If you intend to distribute the load across multiple machines in a cluster, it is recommended to use Anbox Cloud for full deployments instead.

## Clustering for full Anbox Cloud deployments

In a clustering setup for a full Anbox Cloud deployment, one node is dedicated as the management node to host the Anbox Management Service (AMS). If you use the Streaming Stack, two additional nodes are dedicated to host the extra services required for streaming. All other nodes are used as worker nodes.

Each worker node runs [LXD](https://ubuntu.com/lxd) in [clustering mode](https://documentation.ubuntu.com/lxd/en/latest/clustering/), and this LXD cluster is used to host the Android containers.

### Cluster capacity

Anbox Cloud is optimised to provide instances at high density per host. To determine how many cluster nodes you need and what resources they should have, you must estimate the capacity that you require for your use case. See {ref}`exp-capacity-planning` for more information.

(sec-lxd-auto-scaling)=
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

Anbox Cloud provides various metrics to help decide when to scale up or down. Based on these metrics, together with data from a production system, you can build a model trying to predict when auto scaling should trigger. See {ref}`ref-prometheus-metrics` for more information.

Future versions of Anbox Cloud will provide a framework which will help to implement such a model.

See {ref}`howto-scale-up-cluster` and {ref}`howto-scale-down-cluster` for instructions on how to add or remove nodes from the cluster.

## Related topics

* {ref}`howto-manage-cluster`

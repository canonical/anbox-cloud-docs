(howto-scale-up-cluster)=
# How to scale up a LXD cluster

Scaling up a LXD cluster can be achieved via Juju. Juju automates the deployment of the individual units and links them together.

Adding additional LXD units or removing existing ones is not an instant operation. Adding a new node, for example, can take 5-10 minutes and must be planned in advance. The deployment of a single node will include the following steps:

1. Allocation of a new machine from the underlying cloud provider
2. Machine startup and first time initialization
3. LXD installation
4. Registration of the LXD node with the existing cluster and AMS
5. Synchronization of necessary artifacts from other nodes in the LXD cluster (for example, images)

To add additional LXD nodes, run the following commands:

    number_of_units=3
    juju add-unit -n “$number_of_units” lxd

This will trigger the deployment of the nodes. You can use the following commands to wait until the deployment has settled:

    snap install --classic juju-wait
    juju wait -w

Due to internal implementation details, waiting for just the units to settle and report status “active” is not enough. You must also check that the unit is correctly added to AMS and is itself part of the LXD cluster. You can do that with code similar to the following script:

```bash
#!/bin/bash -ex
unit=$1
# Drop slash from the unit name
node_name=${unit/\//}
while true; do
  if juju ssh ams/0 -- /snap/bin/amc node ls | grep -q "${node_name}.*online" ; then
    break
  fi
  sleep 5
done
while true ; do
  if juju ssh "$unit" -- lxc cluster ls ; then
    break
  fi
  sleep 5
done
```

Save the script with the file name `wait-for-unit.sh` and run it with the following commands:

    chmod +x wait-for-unit.sh
    ./wait-for-unit.sh "lxd/1"

The script just serves as an example and you should implement a similar check in your auto scaling implementation. If you scale up with multiple nodes at a time, your implementation should check for all new nodes to be fully added to both AMS and the LXD cluster.

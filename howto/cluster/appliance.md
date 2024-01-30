If you're running the Anbox Cloud Appliance and you want to extend the available instance capacity, you can join additional machines to the appliance.

The following instructions describe how to add a machine. Also see [Multi-node support for the Anbox Cloud Appliance](https://discourse.ubuntu.com/t/capacity-planning/17765#clustering-for-full-anbox-cloud-deployments-2).

## Allow internal network communication

To allow communication between the different machines, you must configure the internal network that the machines use to allow incoming traffic.

How to do this depends on your network configuration. On AWS, for example, you can modify the security group attached to the instance to allow all incoming traffic on the internal subnet that it sits on:

![AWS security group](https://assets.ubuntu.com/v1/0e1ce070-appliance_multi_node_aws_ports.png)

In this example, incoming traffic is allowed when it originates in the internal subnet `172.31.0.0/16`.

## Generate a join token

To add a machine to the appliance, you need a join token that provides the necessary information and authentication details to join the appliance.

You must generate such a token on the existing machine that runs the Anbox Cloud Appliance. Use the following command:

    anbox-cloud-appliance cluster add <name>

The name you pick here is important because it will identify the node in both LXD and AMS.

[note status="information" status="Tip"]
The first node of the appliance is always called `lxd0`. It can be helpful to name additional nodes `lxd<n>` for consistency reasons.
[/note]

## Join a machine

To join a machine to an existing Anbox Cloud Appliance, run `sudo anbox-cloud-appliance init` as usual to start the initialisation process. When you are asked whether you want to join the node to an existing Anbox Cloud Appliance, answer "yes" and provide the join token that you generated:

```
Welcome to the Anbox Cloud Appliance!

The following questions will guide you through the initial setup of the
appliance. If you don't care about answering any of them you can just
accept the defaults.

For any further questions please have a look a the official Anbox Cloud
documentation at https://discourse.ubuntu.com/t/17029

Are you joining this node to an existing Anbox Cloud Appliance installation? (EXPERIMENTAL) [default=no] yes
Please enter the join token: eyJsdCI6ImV5SnpaWEoyWlhKZmJtRnRaU0k2SW14NFpERWlMQ0ptYVc1blpYSndjbWx1ZENJNkltWXhPVEpqTm1Ga09XVm1PVGRoTXpnNU9XVmxOelF6WW1NeU5ESmxaak5sWkRaaVpXTm1abUV4T0dFNFlqRTVNalE1TjJaalkyRTBaREUzWlRRMk5HWWlMQ0poWkdSeVpYTnpaWE1pT2xzaU1UY3lMak14TGpJeExqVTZPRFEwTXlKZExDSnpaV055WlhRaU9pSmxOMlZrTldZd00yWTVPVEF5WXpKbVpETmlNRFV6TmpJeE5tTmpOV1JsWmprelptVTVPV05pTWpBM1lqRXlOekk1TVRneU1UTTVOV1EwTWpNeVpqQXdJbjA9IiwianQiOiJNRTRUQ1d4NFpERXROMkUyWXpBVUV4SXlOREF1TWpFdU5TNHlNelk2TVRjd056QUVJSmhzeVo5QjlrWGRKX0dOOWJQd09pTHlLV1VXdXM1Y092cDdST29INzdIWEV3bGhjSEJzYVdGdVkyVUEiLCJmIjp7Im0iOnRydWV9fQ==

...
```

Afterwards, the machine automatically connects to the existing appliance and sets everything up. The initialisation process should be quicker than for the first machine. It should finish after no more than a few minutes.

Once the initialisation has finished, the second machine is ready to be used. To access the [web dashboard](https://discourse.ubuntu.com/t/web-dashboard/20871), you can use the IP or DNS of any node in the cluster.

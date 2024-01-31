Anbox Cloud comes with support for High Availability (HA) for both Core and the Streaming Stack.
Next to [Juju's support for high availability of the Juju controller](https://juju.is/docs/controller-high-availability), you can add HA for the [Anbox Management Service (AMS)](https://discourse.ubuntu.com/t/about-ams/24321) and the Anbox Stream Gateway to ensure fault tolerance and higher uptime.

Enabling High Availability (HA for short) is achieved by [adding new units via Juju](https://juju.is/docs/olm/manage-applications#heading--scale-an-application).
This will allocate a new machine, run new instances of the scaled application and configure the cluster automatically.

Adding a unit is done with the following syntax:

    juju add-unit <application name> -n <number of units to add>

For example, to go from 1 to 5 AMS units, you would run the following:

    juju add-unit ams -n 4

[note type="information" status="Tip"]
By default, Juju allocates small machines to limit costs but you can request better resources by [enforcing constraints](https://juju.is/docs/olm/constraints):

`juju set-constraints anbox-stream-gateway cores=4 memory=8GB`

This is heavily recommended on production environments.
[/note]


## Anbox Cloud Core

Anbox Cloud Core HA requires additional AMS instances as well as a load balancer to spread out requests:

    juju deploy ams-load-balancer
    juju relate ams ams-load-balancer
    juju add-unit ams -n 2

If you are using the `amc` snap on your machine, you can tell it to use the load balancer instead of talking directly to AMS:

    amc remote add lb https://10.75.96.23:8444
    amc remote set-default lb

The port to use is always `8444`, the same AMS is listening on.

## Anbox Streaming Stack

In the Streaming Stack, both the Agent and the Gateway can be run in HA. We recommend a minimum of 3 machines for the Streaming Stack.

    juju add-unit anbox-stream-gateway -n 2
    juju add-unit anbox-stream-agent -n 2
    juju relate anbox-stream-gateway:api anbox-stream-gateway-lb:reverseproxy

This would give you 3 instances of both the Stream Gateway and the Stream Agent.

## Checking status

When adding new units, Juju will create new machine so it may take a few minutes for
your cluster to be fully operational.
You can check `juju status` to see the current deployment status:

```
Model    Controller      Cloud/Region         Version  SLA          Timestamp
default  anbox-cloud     localhost/localhost  2.8.0    unsupported  19:18:10Z

App                      Version  Status   Scale  Charm                 Store       Rev  OS      Notes

anbox-stream-agent                active       3  anbox-stream-agent    jujucharms   80  ubuntu
anbox-stream-gateway              active       3  anbox-stream-gateway  jujucharms   90  ubuntu
anbox-stream-gateway-lb           active       1  haproxy               jujucharms   56  ubuntu  exposed
...

Unit                        Workload  Agent  Machine  Public address  Ports               Message
anbox-stream-agent/0*       active    idle   0       10.212.218.11
anbox-stream-agent/1        active    idle   6       10.212.218.178
anbox-stream-agent/2        active    idle   5       10.212.218.193
anbox-stream-gateway-lb/0*  active    idle   2       10.212.218.104  80/tcp,443/tcp      Unit is ready
anbox-stream-gateway/0*     active    idle   1       10.212.218.221  4000/tcp,7003/tcp
anbox-stream-gateway/1      active    idle   3       10.212.218.105  4000/tcp,7004/tcp
anbox-stream-gateway/2      active    idle   4       10.212.218.136  4000/tcp,7005/tcp
...
```

*Notice the `scale` of each application indicating how much units an application has.*

## Scaling down

Scaling down can be done by [removing units via Juju](https://juju.is/docs/olm/manage-applications#heading--scale-an-application). You have to specifically target the unit that you want to remove:

    juju remove-unit anbox-stream-agent/2

The cluster will reconfigure itself to work with the removed unit.

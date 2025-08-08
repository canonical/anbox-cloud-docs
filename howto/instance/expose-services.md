(howto-expose-services)=
# Expose services on an instance

AMS allows an instance to expose a service to the outer network using instance services. You can do this by defining a port to expose on the instance endpoints.

## Prerequisites

By default, external access to Anbox instances is restricted for security reasons. If you need to allow external access, you must enable access manually.

For charmed deployments, external access is blocked by the [LXD charm](https://charmhub.io/ams-lxd). To allow access, expose this charm and configure the allowed port range:

    juju expose lxd
    juju config lxd exposed_instance_ports=10000-11000

For appliance deployments on public clouds, external access is controlled by the [cloud platform](https://documentation.ubuntu.com/anbox-cloud/howto/install-appliance/#supported-cloud-platforms). To enable access to Anbox instances, you must manually update the firewall or security group settings:

For AWS, [configure the associated security group](https://docs.aws.amazon.com/vpc/latest/userguide/working-with-security-group-rules.html) to allow inbound traffic on ports 10000-11000.

For Google Cloud, [adjust the firewall rules](https://documentation.ubuntu.com/anbox-cloud/howto/install-appliance/install-on-google-cloud/#firewall-setup) to open the port range 10000-11000.

For Azure, perform the following action depending on whether you are doing this for a fresh deployment or an existing deployment:
- If you are using the [template](https://github.com/Azure/azure-quickstart-templates/tree/master/quickstarts/canonical/anbox) for a fresh deployment, set `exposeAnboxContainerServices` to `true`.
- For existing deployments, [update the network security group](https://learn.microsoft.com/en-us/azure/virtual-network/manage-network-security-group?tabs=network-security-group-portal#create-a-security-rule) to include 10000–11000 in the `Destination port range`.


## Expose a service

The set of services to expose is defined when the instance is launched. For example, the following command exposes port `22` on the instance's private endpoint:

    amc launch -s tcp:22 bdp7kmahmss3p9i8huu0

```{note}
The specified port is exposed only on the IP address assigned to the instance. As the instance is normally not accessible from outside, the LXD node it is running on AMS sets up port forwarding rules on the node and maps the specified port to one in a higher port range (`10000 - 110000`).
```

The list of instances (`amc ls`) will now show the instance and the exposed port `22`:

```bash
+----------------------+----------------+---------+---------+------+---------------+------------------------+
|          ID          |  APPLICATION   |  TYPE   | STATUS  | NODE |    ADDRESS    |       ENDPOINTS        |
+----------------------+----------------+---------+---------+------+---------------+------------------------+
| bdpaqaqhmss611ruq6kg |      candy     | regular | running | lxd0 | 192.168.100.2 | 192.168.100.2:22/tcp   |
|                      |                |         |         |      |               | 10.103.46.41:10000/tcp |
+----------------------+----------------+---------+---------+------+---------------+------------------------+
```

As described above, the port `22` is exposed only on the IP address assigned to the instance.
In addition, it was mapped onto port `10000` on the address of the LXD node `lxd0`.

To help identifying services later on you can give them a name. For the example above we can simply name the service `ssh`:

    amc launch -s ssh:tcp:22 bdp7kmahmss3p9i8huu0

This will help to identify which endpoint is used for which service:

```bash
+----------------------+----------------+---------+---------+------+---------------+----------------------------+
|          ID          |  APPLICATION   |  TYPE   | STATUS  | NODE |    ADDRESS    |       ENDPOINTS            |
+----------------------+----------------+---------+---------+------+---------------+----------------------------+
| bdpaqaqhmss611ruq6kg |      candy     | regular | running | lxd0 | 192.168.100.2 | ssh:192.168.100.2:22/tcp   |
|                      |                |         |         |      |               | ssh:10.103.46.41:10000/tcp |
+----------------------+----------------+---------+---------+------+---------------+----------------------------+
```

If we want to expose the service on the public endpoint of a LXD node, we must slightly change the service definition when the instance is launched:

    amc launch -s +tcp:22 bdp7kmahmss3p9i8huu0


Notice the `+` in front of the port definition. This tells AMS to expose the service on the public endpoint of the LXD node on which the instance is scheduled. The instance list shows the public address of the node on which the instance is running, in the list of endpoints:

```bash
+----------------------+----------------+---------+---------+------+---------------+------------------------+
|          ID          |  APPLICATION   |  TYPE   | STATUS  | NODE |    ADDRESS    |       ENDPOINTS        |
+----------------------+----------------+---------+---------+------+---------------+------------------------+
| bdpaqaqhmss611ruq6kg |      candy     | regular | running | lxd0 | 192.168.100.2 | 192.168.100.2:22/tcp   |
|                      |                |         |         |      |               | 147.3.23.6:10000/tcp   |
+----------------------+----------------+---------+---------+------+---------------+------------------------+
```

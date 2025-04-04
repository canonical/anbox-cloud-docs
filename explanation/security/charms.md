(exp-security-charms)=
# Charms

## Communication

All communication between Juju units and the Juju controller happens over TLS-encrypted websockets. The certificate for the TLS connection to the controller is added as explicitly trusted to each machine as part of the bootstrap process using a combination of cloud-init and SSH.

With this secure channel, Juju charms can communicate with each other using relation data. The data published by one unit is sent to the controller, which then makes it available for all other units on the same relation. The data for each relation is scoped by ID and is only visible to units participating in the specific relation on which it is set.

See [Security with Juju](https://canonical-juju.readthedocs-hosted.com/en/latest/user/explanation/juju-security/) for more information.


## Cryptography

The following charms for Anbox Cloud make use of cryptographic technology for creation of TLS certificates:

* [`ams`](https://charmhub.io/ams)
* [`ams-lxd`](https://charmhub.io/ams-lxd)
* [`ams-node-controller`](https://charmhub.io/ams-node-controller)
* [`anbox-stream-gateway`](https://charmhub.io/anbox-stream-gateway)
* [`anbox-stream-agent`](https://charmhub.io/anbox-stream-agent)
* [`anbox-cloud-dashboard`](https://charmhub.io/anbox-cloud-dashboard)
* [`lxd-integrator`](https://charmhub.io/lxd-integrator)

When Anbox Cloud is deployed without the use of an external CA, the charms will generate self-signed certificates using the [cryptography](https://pypi.org/project/cryptography/) Python package. The private key used for signing has a size of 4096 bits.

### Packages used

* [cryptography from PyPI](https://pypi.org/project/cryptography/)

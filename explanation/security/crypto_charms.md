(exp-security-crypto-charms)=
# Anbox Cloud Charms

The following charms for Anbox Cloud are captured in this explanation:

* [`ams`](https://charmhub.io/ams)
* [`ams-lxd`](https://charmhub.io/ams-lxd)
* [`ams-node-controller`](https://charmhub.io/ams-node-controller)
* [`anbox-stream-gateway`](https://charmhub.io/anbox-stream-gateway)
* [`anbox-stream-agent`](https://charmhub.io/anbox-stream-agent)
* [`anbox-cloud-dashboard`](https://charmhub.io/anbox-cloud-dashboard)
* [`lxd-integrator`](https://charmhub.io/lxd-integrator)

The charms for Anbox Cloud make use of cryptographic technology for creation of TLS certificates.

When Anbox Cloud is deployed without the use of an external CA, the charms will generate self-signed certificates using the [cryptography](https://pypi.org/project/cryptography/) Python package. The private key used for signing has a size of 4096 bits.

## Packages used

* [cryptography from PyPI](https://pypi.org/project/cryptography/)

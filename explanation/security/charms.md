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

## Juju secrets

Confidential data such as private keys, API tokens, or credentials managed by the charm or passed through relations between charms is securely handled using [Juju secrets](https://documentation.ubuntu.com/juju/3.6/reference/secret/) if you deploy Anbox Cloud with Juju 3.0 or later. You can use the following command to view the secrets used by charms:

```
juju list-secrets
```

Currently, all Juju secrets are managed by the charms themselves, not by the model. This means you can view them, but you cannot rotate or remove them.

### Use Juju secrets across model

When using Juju secrets to protect data shared across units in different models, you need to establish a cross-model relation. For example, the `nats` charm provides messaging services, and the `anbox-stream-agent` charm acts as a NATS client. If `anbox-stream-agent` and `nats` are deployed in different models, follow the steps below:

1. Switch to the model containing `nats` and create an offer:

    ```
    juju switch <model containing nats>
    juju offer nats:client
    ```

    This command returns the offer name, for example: `my-controller/my-model.nats`
2. Switch to the model containing `anbox-stream-agent` and relate it to the offer:

    ```
    juju switch <model containing anbox-stream-agent>
    juju relate anbox-stream-agent <offer name>
    ```

This establishes the relation and allows secrets to be securely shared across models.

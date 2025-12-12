(howto-use-ceph-storage)=
# Use Ceph storage

By default, the LXD charm in Anbox Cloud uses local storage (ZFS or directory-based) on each node. For production deployments requiring shared storage, improved scalability, or better resource utilization, you can configure the LXD charm to use [Ceph storage](https://ceph.io/en/) instead.

Ceph provides distributed storage that allows multiple LXD nodes to share a common storage pool, enabling features like live migration and simplified storage management across the cluster.

```{caution}
The storage type must be configured at deployment time and cannot be changed afterwards. Changing the `storage_type` configuration option after deployment will have no effect.
```

## Prerequisites

Before configuring Ceph storage for Anbox Cloud, ensure that you have:

* A machine running a {ref}`supported Ubuntu version <ref-requirements>`.
* Juju 3.x installed (see {ref}`howto-deploy-anbox-juju` for installation instructions).
* A Juju controller and model set up (see {ref}`sec-setup-juju-controller`).
* Your Ubuntu Pro token (see {ref}`sec-attach-pro-subscription`).
* One of the following Ceph deployment options:
  * A [microceph](https://charmhub.io/microceph) deployment for testing or single-server setups.
  * A [ceph-mon](https://charmhub.io/ceph-mon) cluster for production deployments.
  * Access to an existing Ceph cluster via [ceph-proxy](https://charmhub.io/ceph-proxy).

## Deploy Anbox Cloud with Ceph storage

Before deploying Anbox Cloud, ensure your Ceph provider is deployed and configured according to its respective documentation. You can find instructions on how to do this for microceph in [its documentation](https://charmhub.io/microceph).

To enable Ceph storage for the LXD charm, create an overlay file named `ceph-storage.yaml` in the current directory with the following content:

```yaml
applications:
  lxd:
    options:
      ua_token: <your token>
      storage_type: ceph
```

Deploy Anbox Cloud with the overlay:

    juju deploy anbox-cloud --overlay ua.yaml --overlay ceph-storage.yaml

See {ref}`howto-customize-installation` for more information about using overlay files.

After deployment, integrate the LXD charm with your Ceph provider. The integration command depends on which Ceph provider you are using:

For microceph:

    juju integrate lxd:ceph microceph:ceph

For ceph-mon:

    juju integrate lxd:ceph ceph-mon:client

For ceph-proxy:

    juju integrate lxd:ceph ceph-proxy:client

Wait for the deployment to complete and all units to reach active status:

    juju status --watch 5s

## Verify the deployment

After the deployment is complete, verify that the LXD nodes are using Ceph storage.

Connect to one of the LXD units:

    juju ssh lxd/0

Check the storage pools:

    lxc storage list

You should see a storage pool named `ams0` with the driver set to `ceph`.

View detailed storage pool information:

    lxc storage info ams0

The output should show `driver: ceph`, `ceph.osd.pool_name: anbox-cloud-lxd`, and `ceph.user.name: lxd`.

Your Anbox Cloud deployment is now configured to use Ceph storage. The LXD charm automatically created a Ceph pool named `anbox-cloud-lxd` for storing LXD instances.

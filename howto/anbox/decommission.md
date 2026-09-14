---
myst:
  html_meta:
    "description": "How to decommission an Anbox Cloud Appliance or charmed deployment and remove its resources."
---

(howto-decommission)=
# Decommission your Anbox Cloud deployment securely

Decommission an Anbox Cloud deployment by removing the deployment and its associated resources.

The procedure differs depending on whether you are using the Anbox Cloud Appliance or a charmed deployment.

```{caution}
The following steps remove deployment resources and may permanently delete data. Make sure that you do not need this data or that you have backups before proceeding.
```

## Anbox Cloud Appliance

### Remove the appliance snap

Remove the appliance snap and its data:

    sudo snap remove --purge anbox-cloud-appliance

This removes all Anbox Cloud Appliance configuration, databases, credentials, secrets, identities and logs.

### Clean up LXD resources

Removing the Appliance snap does not currently remove all LXD resources created by Anbox Cloud. Remove these resources manually.

```{caution}
The following commands permanently delete resources in the `anbox-cloud` LXD project. Make sure that you do not need this data before proceeding.
```

Delete all instances in the Anbox Cloud project:

    for instance in $(lxc ls --project=anbox-cloud -c n --format=csv); do
      lxc delete --project=anbox-cloud --force "$instance"
    done

Delete all images in the Anbox Cloud project:

    for image in $(lxc image ls --project=anbox-cloud -c f --format=csv); do
      lxc image delete --project=anbox-cloud "$image"
    done

Delete the Anbox Cloud network, profile, and project:

    lxc network delete amsbr0
    lxc profile delete ams0 --project=anbox-cloud
    lxc project delete anbox-cloud

### Verify the removal

Verify that the Anbox Cloud Appliance snap is no longer installed:

    snap list | grep -E "anbox|amc"

The command should not return any Anbox Cloud-related snaps.

Verify that the Anbox Cloud LXD project has been removed:

    lxc project list

The `anbox-cloud` project should no longer be listed.

### Remove external integrations

If you configured OIDC authentication with an external identity provider, remove the Anbox Cloud application registration from that provider.

If you integrated the Anbox Cloud Appliance with [COS](https://canonical.com/anbox-cloud/docs/howto/monitor/#integrate-cos-with-anbox-cloud-appliance), remove the `anbox-appliance-metrics` application from the COS model.

    juju switch cos
    juju remove-application anbox-appliance-metrics

## Charmed deployment

### Destroy the Juju controller

```{caution}
The `--destroy-all-models` flag destroys all models managed by the controller, not just the Anbox Cloud model. If the controller manages other workloads, use `juju destroy-model` to remove only the Anbox Cloud model instead.
```

Find the Juju controller used for the Anbox Cloud deployment:

    juju controllers

Destroy the Juju controller, including all models and storage:

    juju destroy-controller <controller-name> --no-prompt --destroy-all-models --destroy-storage --force

Replace `<controller-name>` with the name of the Juju controller used for your Anbox Cloud deployment.

This command removes the Anbox Cloud deployment, including all models, persistent storage, instances, applications, identities, credentials, secrets and logs managed by the controller. This includes the Anbox Application Registry, subclusters and their cross-model relations. On public cloud providers, the machines used by the deployment are also removed.

For more information about this command and its options, see [Destroy a controller](https://canonical.com/juju/docs/juju-cli/latest/user/howto/manage-controllers/#destroy-a-controller) in the Juju documentation. For an overview of what the `--destroy-storage` flag removes, see [Manage storage](https://canonical.com/juju/docs/juju-cli/latest/user/howto/manage-storage/) in the Juju documentation.

```{note}
If `juju destroy-controller` encounters a deadlock or repeatedly fails, manual cleanup may be required. For example, on the controller machine,remove the Juju snap:

    sudo snap remove --purge juju

If resources remain on a public cloud after the controller is destroyed,terminate them directly through your cloud provider.
```

### Verify the removal

Verify that the Juju controller has been removed, run:

    juju controllers

The controller used for the Anbox Cloud deployment should no longer be listed.

### Remove external integrations

If you configured OIDC authentication with an external identity provider, remove the Anbox Cloud application registration from that provider.

## Related topics

- {ref}`howto-harden`
- {ref}`exp-security`

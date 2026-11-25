---
myst:
  html_meta:
    "description": "Reference documentation for Anbox Cloud deprecation notices, covering features and APIs scheduled for removal."
---

(ref-deprecation-notes)=
# Deprecation notices

This document contains a list of deprecation notices for Anbox Cloud and its components.

(sec-dashboard-deprecation)=
## `anbox-cloud-dashboard` snap and charm
*Deprecated in 1.31.0* ; *Unsupported in 1.33.0*

The `anbox-cloud-dashboard` snap and the `anbox-cloud-dashboard` charm are deprecated as of 1.31.0 and will no longer be supported in 1.33.0. Starting with the 1.33.0 release, dashboard functionality will remain available as a built-in component of the `ams` snap.

(sec-anbox-connect-deprecation)=
## `anbox-connect`
*Deprecated in 1.31.0* ; *Unsupported in 1.33.0*

Support for `anbox-connect` is deprecated as of 1.31.0 and will be removed in 1.33.0. Use `amc connect` instead. 

## Multiple subclusters from the dashboard
*Deprecated in 1.30.2* ; *Unsupported in 1.31.0*

Support for multiple subclusters from the dashboard was deprecated in 1.30.2 and has been removed in 1.31.0.

## VM images
*Deprecated in 1.28.0* ; *Unsupported in 1.30.0*

The VM variant of Anbox images for all versions was deprecated in 1.28.0 and is no longer supported as of 1.30.0. Use the container based images instead.

## Bundles
*Deprecated in 1.28.0* ; *Unsupported in 1.30.0*

The bundles [Anbox Cloud](https://charmhub.io/anbox-cloud) and [Anbox Cloud Core](https://charmhub.io/anbox-cloud-core) were deprecated in 1.28.0 and are no longer supported as of 1.30.0.

## Android 12, Android 13, and AAOS 13
*Deprecated in 1.27.1* ; *Unsupported in 1.29.0*

Support for the Android 12, Android 13, and AAOS 13 images was deprecated in 1.27.1 and these images are no longer supported as of 1.29.0.

(node-controller-charm)=
## Node controller charm
*Deprecated in 1.26.0* ; *Unsupported in 1.28.0*

The [AMS node controller charm](https://charmhub.io/ams-node-controller) was deprecated in 1.26.0 and is no longer supported as of 1.28.0. The charm was mainly responsible for installing the `ams-node-controller` snap, which is now installed by the `ams-lxd` charm.

## Juju 2.9
*Deprecated in 1.25.1* ; *Unsupported in 1.27.0*

Juju 2.9 was deprecated in 1.25.1 and is no longer supported as of 1.27.0. Upgrade to Juju 3.6 instead. See [Juju upgrade documentation](https://canonical.com/juju/docs/juju-cli/latest/user/howto/manage-your-deployment/upgrade-your-deployment/) for detailed instructions.

For all new deployments, use the Juju snap from 3/stable or the latest/stable channel.

## Kernels older than 6.8
*Deprecated in 1.25.0* ; *Unsupported in 1.27.0*

The support for kernels older than 6.8 was deprecated in 1.25.0. Starting from 1.27.0, Anbox Cloud is only supported on kernels with version 6.8 and later.

## LXD 5.0
*Deprecated in 1.25.0* ; *Unsupported in 1.28.0*

The support for LXD 5.0 snap was deprecated in 1.25.0 and is no longer supported as of 1.28.0. Upgrade your deployment to use LXD 5.21 instead.

(sec-appliance-deprecation)=
## Anbox Cloud Appliance `epoch=0` snap
*Deprecated in 1.22.0* ; *Unsupported in 1.25.0*

The Anbox Cloud Appliance was reworked and the new implementation is provided using [Snap epochs](https://ubuntu.com/docs/snapcraft/9/how-to/crafting/manage-data-compatibility/).

The snap with `epoch=0` is the previous implementation that was deprecated in 1.22.0. Installations of the appliance using this snap received updates until Anbox Cloud 1.24.2 and are no longer supported as of 1.25.0.

Starting from 1.23.0, the snap with `epoch=1` is the new implementation and the default for new appliance installations. This implementation of the appliance no longer uses the Juju charmed operators internally but packages all necessary service components directly within the snap. This simplifies the installation process and reduces overall footprint.

## Ubuntu 20.04 LTS (Focal Fossa)
*Deprecated in 1.22.0* ; *Unsupported in 1.24.0*

Support for Ubuntu 20.04 LTS (Focal Fossa) was deprecated in 1.22.0 and has been removed in Anbox Cloud 1.24.0.

## EmuGL
*Deprecated in 1.22.0* ; *Unsupported in 1.23.0*

Support for the EmuGL renderer was deprecated in 1.22.0 and has been removed in Anbox Cloud 1.23.0. Starting with 1.22.0, VirGL is the default renderer for NVIDIA GPUs with driver version 545 and later.

(etcd-and-easyrsa-charms)=
## etcd and EasyRSA charms
*Deprecated in 1.29.0* ; *Unsupported in 1.35.0*

Legacy charms, specifically the [`etcd`](https://charmhub.io/etcd) and the [`easyrsa`](https://charmhub.io/easyrsa) charms, are deprecated as of Anbox Cloud 1.29.0 release. This aligns with the transition toward modernized, operator-based Anbox Cloud deployment.

Starting from 1.29.0, all new Anbox Cloud deployments must use modernized operator charms to replace their legacy counterparts. Specifically:

- [charmed-etcd](https://charmhub.io/charmed-etcd) to replace `etcd`
- [self-signed-certificates](https://charmhub.io/self-signed-certificates) to replace `easyrsa`

This transition provides a two-year migration window before legacy charms become completely unsupported. Anbox Cloud 1.34.2 will be the last release that supports deployments using legacy charms. Starting from Anbox Cloud 1.35.0, Anbox Cloud deployments will exclusively support modernized charms.

## Applications, Addons and Registry in AMS
*Deprecated in 1.32.0* ; *Unsupported in 1.34.0*

Support for [applications](/howto/application/index.md), [addons](/howto/addons/index.md), and Anbox Application Registry [AAR](/howto/aar/index.md) will be deprecated starting with 1.32.0.
- In 1.32.0: Creating applications and registry management will be removed from the Anbox Cloud dashboard. However, applications, addons, and registry management will remain functional through the CLI for transition purposes.
- In 1.33.0: Applications, addons and registry management will be supported in the CLI but disabled by default.
- In 1.34.0: All support for applications, addons, hooks and registry will be officially removed. Users will no longer be able to create, manage, or utilize these features via the CLI or dashboard.

See {ref}`howto-migrate-from-addon-and-app-hooks` for how to replicate addon hook behavior using a custom image instead.

(ref-deprecation-notes)=
# Deprecation notices

This document contains a list of deprecation notices for Anbox Cloud and its components.

## Juju 2.9
*Deprecated in 1.25.1* ; *Unsupported in 1.27.0*

Juju 2.9 is deprecated as of 1.25.1. Upgrade to Juju 3.0 instead. See [Juju upgrade documentation](https://canonical-juju.readthedocs-hosted.com/en/latest/user/howto/manage-your-deployment/upgrade-your-deployment/) for detailed instructions.

For all new deployments, use the Juju snap from 3/stable or the latest/stable channel.

## Kernels older than 6.8
*Deprecated in 1.25.0* ; *Unsupported in 1.27.0*

The support for kernels older than 6.8 is deprecated as of 1.25.0. Starting from 1.27.0, Anbox Cloud will only be supported on kernels with version 6.8 and later.

## LXD 5.0
*Deprecated in 1.25.0* ; *Unsupported in 1.28.0*

The support for LXD 5.0 snap is deprecated as of 1.25.0. Upgrade your deployment to use LXD 5.21 instead

(sec-appliance-deprecation)=
## Anbox Cloud Appliance `epoch=0` snap
*Deprecated in 1.22.0* ; *Unsupported in 1.25.0*

The Anbox Cloud Appliance is being reworked. We will provide the new Anbox Cloud Appliance implementation using [Snap epochs](https://snapcraft.io/docs/snap-epochs). 

The snap with `epoch=0` is the existing implementation that was deprecated in 1.22.0. Existing installations of the appliance will receive updates until Anbox Cloud 1.24.2.

Starting from 1.23.0, the snap with `epoch=1` will be the new implementation which is the default for new appliance installations. This implementation of the appliance will no longer use the Juju charmed operators internally but package all necessary service components directly within the snap. This helps to simplify the installation process and reduce overall footprint.

## Ubuntu 20.04 (Focal Fossa)
*Deprecated in 1.22.0* ; *Unsupported in 1.24.0*

Support for Ubuntu 20.04 (Focal Fossa) is deprecated in 1.22.0 and is planned to be removed in Anbox Cloud 1.24.0.

## EmuGL
*Deprecated in 1.22.0* ; *Unsupported in 1.23.0*

Support for the EmuGL renderer is deprecated in 1.22.0 and planned to be removed in Anbox Cloud 1.23.0. Starting with 1.22.0, VirGL will be the default renderer for NVIDIA GPUs with driver version 545 and later.

## Node Controller charm
*Deprecated in 1.26.0* ; *Removal in 1.28.0*

Use of node controller charm to manage the port forwarding from an instance to expose a service is deprecated in 1.26.0. Instead, the Anbox Management Service (AMS) will use a LXD proxy device to manage the port forwarding.

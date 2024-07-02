# Deprecation notices

This document contains a list of deprecation notices for Anbox Cloud and its components.

## Ubuntu 20.04 (focal)
Support for Ubuntu 20.04 (focal) is deprecated in 1.22.0 and is planned to be removed in Anbox Cloud 1.24.0.

## EmuGL
Support for the EmuGL renderer is deprecated in 1.22.0 and planned to be removed in Anbox Cloud 1.23.0. Starting with 1.22.0, VirGL will be the default renderer for NVIDIA GPUs with driver version 545 and later.

## Anbox Cloud Appliance gets new implementation
The Anbox Cloud Appliance is being reworked and the current implementation is deprecated in 1.22.0. Existing installations of the current implementation will receive updates until Anbox Cloud 1.24.2. Starting from 1.23.0, new installations will receive the new implementation of the appliance.

  The new implementation of the appliance will no longer use the Juju charmed operators internally but package all necessary service components directly within the snap. This helps to simplify the installation process and reduce overall footprint.

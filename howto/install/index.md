---
myst:
  html_meta:
    "description": "How to install charmed Anbox Cloud with Juju, including deployment on bare metal or public cloud and enabling high availability."
---

(howto-install-anbox-cloud)=
# Install Anbox Cloud

This section focuses on installing **charmed Anbox Cloud**. For the **Anbox Cloud Appliance**, see {ref}`tut-installing-appliance`. For a comparison of both variants, see {ref}`sec-variants`.

Check {ref}`ref-requirements` before you start your installation.

## Deploy

- {ref}`howto-deploy-anbox-juju`
- {ref}`howto-deploy-anbox-baremetal`
- {ref}`howto-deploy-anbox-terraform`

## Configure and validate

- {ref}`howto-customize-installation`
- {ref}`howto-enable-ha`
- {ref}`howto-use-ceph-storage`
- {ref}`howto-validate-deployment`

```{toctree}
:hidden:

customize-installation
deploy-bare-metal
deploy-juju
deploy-terraform
enable-high-availability
use-ceph-storage
validate-deployment
```

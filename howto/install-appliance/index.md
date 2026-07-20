---
myst:
  html_meta:
    "description": "How to install the Anbox Cloud Appliance on AWS, Azure, Google Cloud, or inside a GitHub Actions workflow."
---

(howto-install-appliance)=
# Install the appliance

The Anbox Cloud Appliance provides a deployment of Anbox Cloud on a single machine. It is suited for initial prototyping and small-scale deployments.

If you need a charmed deployment managed with Juju, see {ref}`howto-install-anbox-cloud`. For a comparison of the Anbox Cloud Appliance and charmed Anbox Cloud, see {ref}`sec-variants`.

We recommend that you first follow the {ref}`tut-installing-appliance` tutorial before installing the appliance on a cloud or CI/CD platform. The tutorial guides you through the installation process and introduces the main concepts of the Anbox Cloud Appliance.

Check the {ref}`ref-requirements` before you start your installation.

(supported-cloud-platforms)=
## Supported cloud platforms

The Anbox Cloud Appliance is currently available for the following cloud platforms:

- {ref}`howto-install-appliance-aws`

Other cloud platforms are supported, but the appliance is not available from their application directories yet. To install it, install the Anbox Cloud Appliance snap on a cloud machine:

- For [Azure](https://azure.microsoft.com/) : {ref}`howto-install-appliance-azure`
- For [Google Cloud](https://cloud.google.com/) : {ref}`howto-install-appliance-google-cloud`

## Supported CI/CD platforms

The Anbox Cloud Appliance is currently available on the following CI/CD platforms:

- {ref}`howto-install-appliance-github`

```{toctree}
:hidden:

install-on-aws
install-on-azure
install-on-google-cloud
install-on-github
```

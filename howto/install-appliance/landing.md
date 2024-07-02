(howto-install-appliance)=
# How to install the Anbox Cloud Appliance

The Anbox Cloud Appliance provides a deployment of Anbox Cloud to a single machine. This offering is well suited for initial prototype and small scale deployments.

The guides in this section describe how to install the Anbox Cloud Appliance on different cloud platforms. There is a difference between the full Anbox Cloud installation and the Anbox Cloud Appliance (see {ref}`sec-variants`). This section focuses on the **Anbox Cloud Appliance**. For instructions on how to install **Anbox Cloud**, see {ref}`howto-install-anbox-cloud`.

We strongly recommend that you follow the {ref}`tut-installing-appliance` tutorial before you install the appliance on a cloud platform. The tutorial guides you through installing the appliance on a machine dedicated to Anbox Cloud and makes you familiar with the installation process and the general concepts of the Anbox Cloud Appliance.

Also, see {ref}`ref-requirements` before you start your installation.

## Supported cloud platforms

The Anbox Cloud Appliance is currently available for the following cloud platforms:

* {ref}`howto-install-appliance-aws`

Other clouds are also supported, but the Anbox Cloud Appliance is not available from their application directories yet. Therefore, to install the appliance on such a cloud, install the Anbox Cloud Appliance snap on a cloud machine. See the following instructions:

* For [Azure](https://azure.microsoft.com/) : {ref}`howto-install-appliance-azure`
* For [Google Cloud](https://cloud.google.com/) : {ref}`howto-install-appliance-google-cloud`

For all other cloud platforms, follow the steps detailed in {ref}`tut-installing-appliance`.

```{toctree}
:hidden:

AWS <aws>
Azure <azure>
Google Cloud <google-cloud>
```

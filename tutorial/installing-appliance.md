The Anbox Cloud Appliance provides a deployment of Anbox Cloud to a single machine. This offering is well suited for initial prototype and small scale deployments.

There are differences between the Anbox Cloud Appliance and the full Anbox Cloud installation (see [Variants](https://discourse.ubuntu.com/t/anbox-cloud-overview/17802#variants)). This tutorial focuses on installing the **Anbox Cloud Appliance** on a single dedicated machine.

If you want to install **Anbox Cloud** instead, see [How to install Anbox Cloud](https://discourse.ubuntu.com/t/install-anbox-cloud/24336) or if you want to install the appliance on a cloud platform, see [How to install the Anbox Cloud Appliance](https://discourse.ubuntu.com/t/how-to-install-the-anbox-cloud-appliance/29702).

This tutorial guides you through the steps that are required to install and initialise the Anbox Cloud Appliance on the machine from the [snap](https://snapcraft.io/anbox-cloud-appliance):

1. [Check the prerequisites](#prerequisites)
2. [Install the appliance](#install)
3. [Initialise the appliance](#initialise)
4. [Register with the dashboard](#register)

<a name="prerequisites"></a>
## Check the prerequisites

Make sure you have the following prerequisites:

* An Ubuntu SSO account. If you don't have one yet, create it [here](https://login.ubuntu.com).
* A virtual or bare metal machine running Ubuntu 20.04 or 22.04. See the detailed requirements [here](https://discourse.ubuntu.com/t/requirements/17734).
* [note type="caution" status="Warning"]It is not recommended to run Anbox Cloud on an Ubuntu desktop appliance. Always use the [server](https://ubuntu.com/download/server) or the [cloud](https://ubuntu.com/download/cloud) variant.[/note]
* Your Ubuntu Pro token for an Ubuntu Pro subscription. If you don't have one yet, [speak to your Canonical representative](https://anbox-cloud.io/contact-us). If you already have a valid Ubuntu Pro token, log in to https://ubuntu.com/pro to retrieve it.
  [note type="caution" status="Warning"]The *Ubuntu Pro (Infra-only)* token does **NOT** work and will result in a failed deployment. You need an *Ubuntu Pro* subscription.[/note]

<a name="install"></a>
## Install the appliance

The following instructions guide you through all relevant steps to install the Anbox Cloud Appliance from the [snap](https://snapcraft.io/anbox-cloud-appliance).

### 1. Update your system

On your machine, run the following commands to ensure that all installed packages on your system are up-to-date:

    sudo apt update
    sudo apt upgrade

<a name="attach-ubuntu-pro"></a>
### 2. Attach your machine to the Ubuntu Pro subscription

The Anbox Cloud Appliance requires a valid Ubuntu Pro subscription.

Before installing the appliance, you must attach the machine on which you want to run the Anbox Cloud Appliance to your Ubuntu Pro subscription. To do so, run the following command, replacing *<pro_token>* with your Ubuntu Pro token:

    sudo pro attach <pro_token>

<a name="enable-anbox-service"></a>
### 3. Enable the `anbox-cloud` service using the Ubuntu Pro client.

On your machine, run the following command to install the Anbox Cloud Appliance and additional dependencies.

    pro enable anbox-cloud

Running this command does the following:

1. Installs the following tools and dependencies, if they are not installed already:
    * [snapd](https://snapcraft.io/snapd)
    * [Anbox Management Client (AMC)](https://snapcraft.io/amc)
    * [LXD](https://snapcraft.io/lxd)

        [note type="information" status="Important"] The Anbox Cloud Appliance requires LXD >= 5.0 and hence LXD is installed from the `5.0/stable` track by default. If LXD is already installed but the version is earlier than 5.0, run `snap refresh --channel=5.0/stable lxd` to update it. However, if LXD version is later than 5.0, [do not downgrade it as it may render LXD unusable](https://documentation.ubuntu.com/lxd/en/latest/installing/#upgrade-lxd).[/note]

1. Installs `anbox-cloud-appliance` snap from the `latest/stable` track.
1. Configures the `apt` repositories for Anbox Cloud.

<a name="initialise"></a>
## Initialise the appliance

After the installation, access the appliance in your web browser by entering the IP of your machine (in the following steps referred to as `https://your-machine-address`). This web page provides status information for the following initialisation process.

[note type="information" status="Note"]By default, the Anbox Cloud Appliance uses self-signed certificates, which might cause a security warning in your browser. Use the mechanism provided by your browser to proceed to the web page.[/note]

![Appliance welcome screen|690x343, 100%](https://assets.ubuntu.com/v1/f35744dc-install_appliance_initialise.png)

### 1. Start the initialisation process

On your machine, enter the following command to invoke the initialisation process of the Anbox Cloud Appliance:

    sudo anbox-cloud-appliance init

You will be asked a few questions. If you don't want to make any specific changes, you can safely stay with the offered default answers. When the command returns, the initialisation process will run fully automatically in the background. 

### 2. Monitor the progress

You can watch the status web page at `https://your-machine-address` for progress information.

![Anbox Cloud deployment|690x442](https://assets.ubuntu.com/v1/279e12e3-install_appliance_status.png)

Alternatively, you can also use the `anbox-cloud-appliance status` command to monitor the progress information on the command line.

```bash
status: initializing
progress: 60
update-available: false
reboot-needed: false
version: 1.19.1
```
<a name="register"></a>
## Register with the dashboard

Once the initialisation process has finished, you are presented with a welcome page on `https://your-machine-address` with instructions on how to register a user account with your installation. This registration is needed to access the [web dashboard](https://discourse.ubuntu.com/t/web-dashboard/20871).

![Instructions for registering Ubuntu SSO account|690x442](https://assets.ubuntu.com/v1/93b47634-install_appliance_register.png)

### 1. Register your Ubuntu SSO account

Enter the following command to register your Ubuntu SSO account:

    anbox-cloud-appliance dashboard register <your Ubuntu SSO email address>

The output provides a link that you must open in your web browser to finish the account creation. By default, the registration link expires after one hour. After registering, you can log into the appliance dashboard with your Ubuntu SSO account.

### 2. Log into the appliance dashboard

After registering, you can log into the appliance dashboard at `https://your-machine-address` with your Ubuntu SSO account.

## Done!

Your Anbox Cloud Appliance is now fully set up and ready to be used! Next, you should check out the [Get started with Anbox Cloud (web dashboard)](https://discourse.ubuntu.com/t/getting-started-with-anbox-cloud-web-dashboard/24958) or the [Get started with Anbox Cloud (CLI)](https://discourse.ubuntu.com/t/getting-started/17756) tutorial to familiarise yourself with how to use Anbox Cloud.

You can find more information about how to use the appliance in the documentation. The appliance installation is nearly identical to installing via Juju, so all the commands and examples not relating directly to Juju will apply.

If you want to increase the capacity of your Anbox Cloud Appliance deployment, you can add more machines to it. See [How to join a machine to the Anbox Cloud Appliance](https://discourse.ubuntu.com/t/how-to-join-a-machine-to-the-anbox-cloud-appliance/29054) for instructions.

(tut-installing-appliance)=
# Install the appliance on a dedicated machine

The Anbox Cloud Appliance provides a deployment of Anbox Cloud to a single machine. This offering is well suited for initial prototype and small scale deployments.

There are differences between the Anbox Cloud Appliance and the full Anbox Cloud installation (see {ref}`sec-variants`). This tutorial focuses on installing the **Anbox Cloud Appliance** on a single dedicated machine.

```{caution}
Remember that installing the Anbox Cloud Appliance will take over the entire instance, install packages and override existing components to configure them as required. If you have existing components, for example, LXD containers, installing and initialising the appliance could override any existing configuration. Hence, it is important to try this tutorial on a machine dedicated for Anbox Cloud.
```

If you want to install **Anbox Cloud** instead, see {ref}`howto-install-anbox-cloud` or if you want to install the appliance on a cloud platform, see {ref}`howto-install-appliance`.

This tutorial guides you through the steps that are required to install and initialise the Anbox Cloud Appliance on the machine from the [snap](https://snapcraft.io/anbox-cloud-appliance).

## Preparation

Make sure you have the following prerequisites:

* An Ubuntu SSO account. If you don't have one yet, [create it](https://login.ubuntu.com).
* A virtual or bare metal machine running Ubuntu 20.04 or 22.04. See the detailed {ref}`ref-requirements`.
```{caution}
It is not recommended to run Anbox Cloud on an Ubuntu desktop appliance. Always use the [server](https://ubuntu.com/download/server) or the [cloud](https://ubuntu.com/download/cloud) variant.
```
* Your Ubuntu Pro token for an Ubuntu Pro subscription. If you don't have one yet, [speak to your Canonical representative](https://anbox-cloud.io/contact-us). If you already have a valid Ubuntu Pro token, log in to [Ubuntu Pro](https://ubuntu.com/pro) to retrieve it.
```{caution}
The *Ubuntu Pro (Infra-only)* token does not work and will result in a failed deployment. You need an *Ubuntu Pro* subscription.
```

## Install the appliance

The following instructions guide you through all relevant steps to install the Anbox Cloud Appliance from the [snap](https://snapcraft.io/anbox-cloud-appliance).

### Update your system

On your machine, run the following commands to ensure that all installed packages on your system are up-to-date:

    sudo apt update
    sudo apt upgrade

### Attach your machine to Ubuntu Pro

The Anbox Cloud Appliance requires a valid Ubuntu Pro subscription.

Before installing the appliance, you must attach the machine on which you want to run the Anbox Cloud Appliance to your Ubuntu Pro subscription. To do so, run the following command, replacing *<pro_token>* with your Ubuntu Pro token:

    sudo pro attach <pro_token>

(sec-enable-anbox-pro)=
### Enable the `anbox-cloud` service

On your machine, run the following command to install the Anbox Cloud Appliance and additional dependencies.

    sudo pro enable anbox-cloud

Running this command does the following:

1. Installs the following tools and dependencies, if they are not installed already:
    * [snapd](https://snapcraft.io/snapd)
    * [LXD](https://snapcraft.io/lxd)

        ```{important}
        The Anbox Cloud Appliance requires LXD >= 5.0 and hence LXD is installed from the `5.0/stable` track by default. If LXD is already installed but the version is earlier than 5.0, run `snap refresh --channel=5.0/stable lxd` to update it. However, if LXD version is later than 5.0, [do not downgrade it as it may render LXD unusable](https://documentation.ubuntu.com/lxd/en/latest/installing/#upgrade-lxd).
        ```

1. Installs `anbox-cloud-appliance` snap from the `latest/stable` track.
1. Configures the `apt` repositories for Anbox Cloud.

### Prepare the machine

In order to prepare the machine and install additional required packages, run the following command to review the generated preparation script:

    anbox-cloud-appliance prepare-node-script

The generated bash script will perform the following operations:

1. Install `linux-modules-extra` packages to ensure that the binder kernel driver is available.
2. Install additional Anbox Cloud specific kernel modules.
3. (If GPU is available) Install GPU driver packages from the Ubuntu archive and apply tuning settings for the driver.

To apply the script after reviewing it, you can run:

    anbox-cloud-appliance prepare-node-script | sudo bash -ex

(sec-initialise-appliance)=
## Initialise the appliance

After preparation of the machine has been completed, you can now initialise the Anbox Cloud Appliance itself.

### Run the `init` command

On your machine, enter the following command to invoke the initialisation process of the Anbox Cloud Appliance:

    sudo anbox-cloud-appliance init

You will be asked a few questions. If you don't want to make any specific changes, you can safely stay with the offered default answers. When the command returns, the initialisation process has been completed.

## Register with the dashboard

Once the initialisation process has finished, you are presented with a welcome page on `https://your-machine-address` with instructions on how to register a user account with your installation. This registration is needed to access the {ref}`exp-web-dashboard`.

![Instructions for registering Ubuntu SSO account|690x442](https://assets.ubuntu.com/v1/93b47634-install_appliance_register.png)

### Register your Ubuntu SSO account

Enter the following command to register your Ubuntu SSO account with the appliance dashboard:

    sudo anbox-cloud-appliance dashboard register <your Ubuntu SSO email address>

The output provides a link that you must open in your web browser to finish the account creation. By default, the registration link expires after one hour. After registering, you can log into the appliance dashboard with your Ubuntu SSO account.

### Log into the appliance dashboard

After registering, you can log into the appliance dashboard at `https://your-machine-address` with your Ubuntu SSO account.

## Done!

Your Anbox Cloud Appliance is now fully set up and ready to be used! Next, you should check out the {ref}`tut-getting-started-dashboard` or the {ref}`tut-getting-started-cli` tutorial to familiarise yourself with how to use Anbox Cloud.

You can find more information about how to use the appliance in the documentation. The appliance installation is nearly identical to installing via Juju, so all the commands and examples not relating directly to Juju will apply.

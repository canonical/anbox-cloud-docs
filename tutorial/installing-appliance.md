(tut-installing-appliance)=
# Install the appliance

In this tutorial, we will install the [Anbox Cloud Appliance snap](https://snapcraft.io/anbox-cloud-appliance), initialize the appliance within a [Multipass](https://canonical.com/multipass) virtual machine. By the end of this tutorial, we should be able to interact with the appliance using the Anbox Cloud dashboard.

Before beginning the tutorial, it is important to understand that:

- There are differences between the appliance and the charmed Anbox Cloud installation (see {ref}`sec-variants`). If you want to install the charmed version instead, see {ref}`howto-install-anbox-cloud`.

- Remember that installing the appliance will take over the entire instance, install packages and override existing components. For example, if you have existing LXD containers, installing and initializing the appliance could override any existing configuration.

## Prerequisites

To proceed with the tutorial, we need:

- An Ubuntu SSO account. If you don't have one yet, [create one now](https://login.ubuntu.com).
- Your Ubuntu Pro token for an Ubuntu Pro subscription. If you don't have one yet, [speak to your Canonical representative](https://anbox-cloud.io/contact-us). If you already have a valid Ubuntu Pro token, log in to [Ubuntu Pro](https://ubuntu.com/pro) to retrieve it.
```{note}
The *Ubuntu Pro (Infra-only)* token does not work and will result in a failed deployment. You need an *Ubuntu Pro* subscription.
```
- A virtual or a bare metal machine running Ubuntu 22.04. We will be using a Multipass virtual machine.

## Prepare a Multipass instance

1. Install Multipass:

        snap install multipass

2. Create a virtual machine:

        multipass launch anbox

3. Shell into the virtual machine:

        multipass shell anbox

## Attach the machine to Ubuntu Pro

Run the following command by replacing `$token` with your Ubuntu Pro token:

    sudo pro attach $token

The machine is now successfully attached to Ubuntu Pro.

(sec-enable-anbox-pro)=
## Enable the `anbox-cloud` service

The `anbox-cloud` service is disabled by default. Run:

    sudo pro enable anbox-cloud

Running this command first installs necessary tools and dependencies such as [snapd](https://snapcraft.io/snapd) and [LXD](https://snapcraft.io/lxd), if they are not already installed.

Then, it installs the `anbox-cloud-appliance` snap from the `latest/stable` track and configures the necessary `apt` repositories.

(sec-install-additional-packages)=
## Install additional packages

After enabling the `anbox-cloud` service, we still need some additional packages, kernel modules and optionally GPU driver packages

To do all this, we offer a script that helps prepare machines. Let's first review the script:

    anbox-cloud-appliance prepare-node-script

The generated bash script will do the following:

1. Install `linux-modules-extra` packages to ensure that the binder kernel driver is available.
2. Install additional Anbox Cloud specific kernel modules.
3. (If GPU is available) Install GPU driver packages from the Ubuntu archive and apply tuning settings for the driver.

To apply the script after reviewing it, run:

    anbox-cloud-appliance prepare-node-script | sudo bash -ex

When this script is applied, we have completed the installation part successfully.

(sec-initialize-appliance)=
## Initialize the appliance

After installation, we need to initialize the appliance to use it. Run:

    sudo anbox-cloud-appliance init

Here, the initialization process asks a few questions regarding the configuration of networking options and LXD storage pools.

For the purpose of this tutorial, let's leave the default answers for all questions except the one about providing access to the AMS API:

*Do you want to setup access to the AMS API for your current user (ubuntu, uid=1000)?*

The reason we switch from the default answer *No* to *Yes* for this question is that the snap strict confinement policy requires the application manifest and other necessary files such as the APK to be located in the home directory of the user executing the commands. If this answer is not set, you will still be able to use the dashboard path of the {ref}`tut-create-virtual-device` tutorial but you will not be able to use the command line path.

For everything else, accept the defaults for everything else until the bootstrap process starts.

(sec-register-dashboard)=
## Register with the dashboard

When the initialization process has finished, we can see the welcome page on the local host. Try accessing `https://multipass-machine-address` using a browser.

To start using Anbox Cloud, there is still one last command we need to run to register a user account. Run the following command with your Ubuntu SSO account email address:

    sudo anbox-cloud-appliance dashboard register your_email@email.com

The command outputs a link to finish the registration. By default, this registration link expires after one hour.

When the registration is complete, you can use Ubuntu SSO to sign in to the dashboard.

## Success!

After registering, you can log into the appliance dashboard at `https://multipass-machine-address` with your Ubuntu SSO account.

The appliance is now fully set up and ready to be used!

> Next: {ref}`tut-create-virtual-device`

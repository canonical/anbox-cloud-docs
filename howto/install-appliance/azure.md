(howto-install-appliance-azure)=
# How to install the appliance on Azure

The Anbox Cloud Appliance is not yet available from the Azure Marketplace. However, you can install the Anbox Cloud Appliance snap on an Azure machine.

## Deploy using a quickstart template
<!-- wokeignore:rule=master -->
An [Azure quickstart template](https://github.com/Azure/azure-quickstart-templates/tree/master/quickstarts/canonical/anbox) is available for deploying the Anbox Cloud Appliance on Azure. The template automatically deploys and configures the necessary settings for the Anbox Cloud Appliance.
<!-- wokeignore:rule=master -->
Once you have completed the [deployment steps](https://github.com/Azure/azure-quickstart-templates/tree/master/quickstarts/canonical/anbox#deployment-steps), finish the installation by performing the following steps:

1. {ref}`Initialise the appliance <sec-initialise-appliance>`
1. {ref}`Register your Ubuntu SSO account with the appliance dashboard <sec-register-dashboard>`.

    ```{Tip}
    The output from the template will contain the public IP address of the VM that is required to complete this step.
    ```

## Deploy manually

An alternate option to using the quickstart template is to deploy manually. If you wish to deploy Anbox Cloud Appliance manually on Azure, the following instructions guide you through all relevant steps.

<details>
<summary>Click for details</summary>

The entire deployment process will take 20-30 minutes, depending on the selected hardware and the network conditions.

### Prerequisites

Check the hardware requirements listed in {ref}`ref-requirements` for the Anbox Cloud Appliance.

In addition, make sure you have the following prerequisites:

* An Ubuntu SSO account. If you don't have one yet, create it [here](https://login.ubuntu.com).
* Your Ubuntu Pro token for an Ubuntu Pro subscription. If you don't have one yet, [speak to your Canonical representative](https://anbox-cloud.io/contact-us). If you already have a valid Ubuntu Pro token, log in to [Ubuntu Pro](https://ubuntu.com/pro) to retrieve it.

```{caution}
  The *Ubuntu Pro (Infra-only)* token does **NOT** work and will result in a failed deployment. You need an *Ubuntu Pro* subscription.
```
* An Azure account that you use to create the virtual machine.

Once you have the prerequisites, the first step is to create a virtual machine on which you can install the Anbox Cloud Appliance.

### 1. Create a Linux virtual machine

Log on to the [Microsoft Azure Portal](https://portal.azure.com/) and select the **Quickstart Center** service.

![Quickstart Center](https://assets.ubuntu.com/v1/0ca30941-azure_quickstart-co.png)

In the Quickstart Center, select **Deploy a virtual machine**. On the resulting screen, select **Create a Linux virtual machine**.

![Deploy a virtual machine](https://assets.ubuntu.com/v1/d0ac4cf5-azure_deploy-vm-co.png)

### 2. Configure basic settings

On the **Basics** tab of the virtual machine configuration, specify the required information. Several of the options are specific to how and where you want to deploy your virtual machine. In most cases you can keep the default values, but make sure to set the following configurations:

* Select the latest Ubuntu image (Ubuntu Server 22.04 LTS) for the architecture that you want to use. The following instructions and screenshots use the Arm64 architecture.
* Select a size that matches the hardware requirements(see {ref}`sec-minimum-hardware-requirements`). For example, select `Standard_D16ps_v5`, which has 16 vCPUs and 64 GB of RAM.
* Change the user name of the administrator account to `ubuntu`.
* Accept the defaults for the inbound port rules for now; these rules will be configured later in the setup process.

![Basics tab](https://assets.ubuntu.com/v1/9c8844a2-azure_config-basics-co.png)

Click **Next: Disks** to continue to the next tab.

### 3. Configure disks

Azure separates the main disk for the operating system and any data disks. On the **Disks** tab of the virtual machine configuration, you can configure the OS disk and attach data disks.

For the Anbox Cloud Appliance, you should attach a separate data disk of at least 50 GB. To do so, click **Create and attach a new disk**. You can accept the default settings and change the disk size according to your requirements. For performance reasons, we recommend using 100 GB or more.

![Create and attach a new disk](https://assets.ubuntu.com/v1/8fea8b11-azure_config-disk.png)

Click **Next: Networking** to continue to the next tab.

### 4. Configure networking

For networking, the Anbox Cloud Appliance requires the following change to the default settings:

1. For the **NIC network security group**, select **Advanced** and create a network security group.
1. Add an inbound security rule that allows access to the following destination port ranges: `80,443,8444,5349,10000-11000,60000-60100`
1. Change the name of the rule and, if relevant for your setup, adapt the priority of the rule.

![Network security group configuration](https://assets.ubuntu.com/v1/a7be81a2-azure_config-secgroup-co.png)

### 5. Finalise the configuration

Check the configuration settings on the remaining tabs and make sure they are suitable for your deployment. The Anbox Cloud Appliance does not require any changes to the default configuration for these areas.

### 6. Review and create

On the **Review + create** tab, check the final configuration. If everything looks good, click **Create** to launch the virtual machine.

![Review + create](https://assets.ubuntu.com/v1/c6ff12de-azure_config-review.png)

Azure will prompt you to download your private key before it starts creating the virtual machine. Make sure to save the private key in a secure location and with secure permissions (0600).

![Deployment](https://assets.ubuntu.com/v1/fafd883f-azure_progress.png)

When deployment is complete, you can log on to the machine and install the Anbox Cloud Appliance.

For additional information, see the [Microsoft documentation](https://docs.microsoft.com/en-gb/azure/virtual-machines/) about creating virtual machines in Azure.

### Connect to the virtual machine using SSH

To install the Anbox Cloud Appliance, you must connect to the virtual machine that you just created, using SSH.

To do so, go to the resource page of your virtual machine and find its public IP address. Then use SSH to log on to the machine, using the user name `ubuntu` and the private key file that you downloaded during the creation of the virtual machine. For example:

    ssh -i Downloads/anbox-cloud-appliance_key.pem ubuntu@192.0.2.15

### Finish the installation

Perform the following steps to finish the appliance installation on the virtual machine. If you are not already familiar with how to perform these steps, see {ref}`tut-installing-appliance` for detailed instructions.

1. Install the Anbox Cloud Appliance on the virtual machine.
    ```{note}
    Remember to attach the virtual machine to your Ubuntu Pro subscription, while installing the appliance.
    ```
1. Initialise the appliance.
1. Register your Ubuntu SSO account with the appliance dashboard.

</details>

When you are done, you can log into the appliance dashboard using `https://your-machine-address` with your Ubuntu SSO account.

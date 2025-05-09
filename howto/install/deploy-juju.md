(howto-deploy-anbox-juju)=
# How to deploy Anbox Cloud with Juju

Anbox Cloud supports various public clouds, such as AWS, Azure and Google. To deploy Anbox Cloud in a cloud environment, you use Juju.

See the following sections for detailed instructions. If you want to install Anbox Cloud on bare metal instead of a public cloud, see {ref}`howto-deploy-anbox-baremetal` instead.

```{note}
There are differences between the charmed Anbox Cloud installation and the Anbox Cloud Appliance (see {ref}`sec-variants`). This section focuses on **Anbox Cloud**. For instructions on how to install the **Anbox Cloud Appliance**, see {ref}`tut-installing-appliance`.
```

## Prerequisites

Before you start the installation, ensure that you have the required credentials and prerequisites:

* A machine running a {ref}`supported Ubuntu version <ref-requirements>`.
* Account credentials for one of the following public clouds:
  * [Amazon Web Services](https://aws.amazon.com/) (including AWS-China)
  * [Google Cloud platform ](https://cloud.google.com/)
  * [Microsoft Azure](https://azure.microsoft.com/)
* Your Ubuntu Pro token for an Ubuntu Pro subscription. If you don't have one yet, [speak to your Canonical representative](https://anbox-cloud.io/contact-us). If you already have a valid Ubuntu Pro token, log in to [Ubuntu Pro website](https://ubuntu.com/pro) to retrieve it.
  ```{caution}
  The *Ubuntu Pro (Infra-only)* token does **NOT** work and will result in a failed deployment. You need an Ubuntu Pro subscription.
  ```

## Install Juju

Juju is a tool for deploying, configuring and operating complex software on public or private clouds.

To install Juju 3.x, enter the following command:

    sudo snap install --classic --channel=3/stable juju

See {ref}`sec-juju-version-requirements` for information about which Juju version is required for your version of Anbox Cloud.

## Authenticate with your cloud

Juju has baked in knowledge of many public clouds, such as AWS, Azure and Google. You can see which ones are ready to use by running the following command:

    juju clouds

Most clouds require credentials so that the cloud knows which operations are authorized, so you will need to supply these for Juju. If you choose to use AWS, for example, you would run:

    juju add-credential aws

For a different cloud, just substitute the cloud name (use the name returned by  the `juju clouds` command). The data you need to supply varies depending on the cloud.

(sec-setup-juju-controller)=
## Add a controller and model

The [Juju controller](https://canonical-juju.readthedocs-hosted.com/en/latest/user/reference/controller/) is used to manage the software deployed through Juju, from deployment to upgrades to day-two operations. One Juju controller can manage multiple projects or workspaces, which in Juju are known as [models](https://canonical-juju.readthedocs-hosted.com/en/latest/user/reference/model/).

For example, run the following command to bootstrap the controller for AWS:

    juju bootstrap aws my-controller

A Juju model holds a specific deployment. It is a good idea to create a new one specifically for each deployment:

    juju add-model anbox-cloud

You can have multiple models on each controller, which means that you can deploy multiple versions of Anbox Cloud, or other applications.

(sec-attach-pro-subscription)=
## Attach your Ubuntu Pro subscription

Every deployment of Anbox Cloud must be attached to the Ubuntu Pro service Canonical provides. This provides your deployment with the correct licenses you're granted as part of your license agreement with Canonical, next to other services available through your subscription like [Livepatch](https://ubuntu.com/livepatch).

You can retrieve your Ubuntu Pro token at [`https://ubuntu.com/pro`](https://ubuntu.com/pro) after logging in. You should record the token as you will need it for every deployment of Anbox Cloud.

```{caution}
The *Ubuntu Pro (Infra-only)* token will result in a failed deployment. You need an *Ubuntu Pro* subscription.
```

To provide your token when deploying with Juju, you need an overlay file (see {ref}`howto-customize-installation`) named `ua.yaml`. For the `anbox-cloud` bundle, the `ua.yaml` file should look like this:

```yaml
applications:
  ams:
    options:
      ua_token: <your token>
  ams-node-controller:
    options:
      ua_token: <your token>
  lxd:
    options:
      ua_token: <your token>
  anbox-stream-agent:
    options:
      ua_token: <your token>
  anbox-stream-gateway:
    options:
      ua_token: <your token>
  anbox-cloud-dashboard:
    options:
      ua_token: <your token>
```

For the `anbox-cloud-core` bundle, the `ua.yaml` file should look like this:

```yaml
applications:
  ams:
    options:
      ua_token: <your token>
  ams-node-controller:
    options:
      ua_token: <your token>
  lxd:
    options:
      ua_token: <your token>
```

You will use the overlay file during the deployment.

(sec-deploy-anbox-cloud-juju)=
## Deploy Anbox Cloud

```{note}
This section explains how to start the Anbox Cloud deployment without any customization. However, in most cases you will want to include a custom configuration when you start the deployment.

Therefore, make sure to check the following sections before you run the deploy command.
```

To install Anbox Cloud, deploy the suitable Anbox Cloud bundle to the Juju model. This will add instances to the model and deploy the required applications.

Choose between the available {ref}`sec-juju-bundles`:

* For a minimized version of Anbox Cloud without the streaming stack, run the following command to deploy the `anbox-cloud-core` bundle:

        juju deploy anbox-cloud-core --overlay ua.yaml

* For the full version of Anbox Cloud, run the following command to deploy the `anbox-cloud` bundle:

        juju deploy anbox-cloud --overlay ua.yaml

## Customize the hardware configuration

To customize the machine configuration Juju will use for the deployment, create another overlay file. Here you can, for example, specify AWS instance types, change the size or source of the root disk or other things. See the [complete list of constraints](https://juju.is/docs/juju/constraint#heading--list-of-constraints) in the Juju documentation for details.


```{note}
Anbox Cloud charms supports deployment on both Ubuntu noble 24.04 and Ubuntu jammy 22.04. The examples below use **noble**. If you prefer to deploy on Ubuntu jammy 22.04, simply modify the `series` configuration accordingly.
```

For the `anbox-cloud-core` bundle, such an `overlay.yaml` file looks like this:

```
machines:
  '0':
    series: noble
    constraints: "instance-type=m4.xlarge root-disk=40G"
  '1':
    series: noble
    constraints: "instance-type=m4.xlarge root-disk=40G"
```

For the `anbox-cloud` bundle, the `overlay.yaml` file includes one more machine in the default configuration:

```
machines:
  '0':
    series: focal
    constraints: "instance-type=m4.xlarge root-disk=40G"
  '1':
    series: noble
    constraints: "instance-type=m4.xlarge root-disk=40G"
  '2':
    series: noble
    constraints: "instance-type=m4.xlarge root-disk=40G"
  '3':
    series: noble
    constraints: "instance-type=m4.2xlarge root-disk=50G"
```

To deploy, add `--overlay overlay.yaml` to your deploy command. For example:

    juju deploy anbox-cloud --overlay ua.yaml --overlay overlay.yaml

(sec-customize-storage-juju)=
### Customize storage

By default, Anbox Cloud uses a loop file with an automatically calculated size for LXD storage. For optimal performance, however, you should use a dedicated block storage device. See {ref}`sec-lxd-storage` for more information.

The easiest way to do this is to use a storage device defined by Juju:

1. Decide which Juju storage pool you want to use.

   See [View the available storage pools](https://juju.is/docs/juju/manage-storage-pools#heading--view-the-available-storage-pools) in the Juju documentation for instructions on how to display existing storage pools. If you are running on AWS, for example, you can use the existing `ebs-ssd` pool.

   If you want to use a new pool, see [Create a storage pool](https://juju.is/docs/juju/manage-storage-pools#heading--create-a-storage-pool) in the Juju documentation for instructions. It can also be useful to create a Juju storage pool if you want to use a specific volume type that is optimized for your setup. For example, AWS provides [EBS volume types](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ebs-volume-types.html) that are optimized for different purposes.

   If you decide to create a pool, make sure to do so before you start the deployment.
1. Configure the `ams-lxd` charm to use the Juju storage pool.

   The `ams-lxd` charm defines an optional storage pool (see the `metadata.yaml` file in the `ams-lxd` charm). To make the LXD charm use this storage pool, you must configure a [storage constraint](https://juju.is/docs/olm/storage-constraint) for it.

   For example, to use the AWS `ebs-ssd` Juju storage pool for LXD storage, use an overlay file with the following storage constraint:

   ```
   applications:
     lxd:
       storage:
         pool: ebs-ssd,100GB,1
   ```

   ```{note}
   You can add only one storage pool.
   ```

When you deploy Anbox Cloud with this configuration, Juju allocates the requested storage and attaches it to LXD. During initialization, AMS then configures LXD to create a ZFS storage pool on the configured storage.

### Add GPU support

On most clouds, adding GPU support is done by picking a specific instance type. The following example uses the `g4dn.xlarge` instance type on AWS, which includes an NVIDIA Tesla T4 GPU.

The `overlay.yaml` file for the `anbox-cloud` bundle looks like this:

```
machines:
  '0':
    series: focal
    constraints: "instance-type=m4.xlarge root-disk=40G"
  '1':
    series: noble
    constraints: "instance-type=m4.xlarge root-disk=40G"
  '2':
    series: noble
    constraints: "instance-type=m4.xlarge root-disk=40G"
  '3':
    series: noble
    constraints: "instance-type=g4dn.2xlarge root-disk=50G"
```

To deploy, add `--overlay overlay.yaml` to your deploy command. For example:

    juju deploy anbox-cloud --overlay ua.yaml --overlay overlay.yaml

### Use Arm instances

Some clouds, like AWS with their Graviton instances, provide support for Arm instance types. These can be used with Anbox Cloud by specifying the correct instance type in the `overlay.yaml`:

```
applications:
  lxd:
    # With Juju >= 2.9.0 we must specify the architecture of the underlying machine
    # in the constraints of the application
    constraints: "arch=arm64"
machines:
  ...
  '3':
    series: noble
    constraints: "instance-type=m6g.2xlarge root-disk=50G"
```

The default bundles for `anbox-cloud` and `anbox-cloud-core` available on Charmhub are suitable only for pure AMD64/X86 based deployments.
Applying the overlay given above, to the bundle directly does not properly deploy the correct architecture for the charms.
You need to download the bundle using,

    juju download anbox-cloud --channel <bundle_channel>

Unzip the bundle to extract the `bundle.yaml` file and remove the revisions for all Anbox Cloud charms from the bundle.
Now use this `bundle.yaml` file to deploy `anbox-cloud` using your own overlay as follows,

    juju deploy ./bundle.yaml --overlay ua.yaml --overlay overlay.yaml

## Monitor the deployment

After starting the deployment, Juju will create instances, install software and connect the different parts of the cluster together. This can take several minutes. You can monitor what's going on by running the following command:

    watch -c juju status --color

## Perform necessary reboots

In some cases, a reboot of the LXD machines is necessary.

Check the output of the `juju status` command to see whether you need to reboot:

```sh
...
Unit       Workload  Agent  Machine  Public address  Ports      Message
lxd/0*     active    idle   3        10.75.96.23     8443/tcp   Actions: Reboot Required, Role: Database-leader
...
```
To reboot the machine hosting LXD, run the following command:

    juju ssh lxd/0 -- sudo reboot

Once done, the reboot operation is finished.

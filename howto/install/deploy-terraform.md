(howto-deploy-anbox-terraform)=
# How to deploy Anbox Cloud with Terraform

To deploy Anbox Cloud using Terraform, you need the Juju provider for it.

```{note}
The terraform plan is a work in progress and makes use of [terraform-provider-juju](https://github.com/juju/terraform-provider-juju)
which is also in active development. There may be breaking changes in the future for the terraform plan.
```

## Prerequisites

* A machine running a {ref}`supported Ubuntu version <ref-requirements>`.
* Your Ubuntu Pro token for an Ubuntu Pro subscription. If you don't have one yet, [speak to your Canonical representative](https://anbox-cloud.io/contact-us). If you already have a valid Ubuntu Pro token, log in to [Ubuntu Pro website](https://ubuntu.com/pro) to retrieve it.
  ```{caution}
  The *Ubuntu Pro (Infra-only)* token does **NOT** work and will result in a failed deployment. You need an Ubuntu Pro subscription.
  ```
* A Juju Controller bootstrapped and connected to your Juju Client (CLI). See {ref}`sec-setup-juju-controller` for information on how to setup a Juju Controller.

## Install Terraform

[Terraform](https://developer.hashicorp.com/terraform) is an infrastructure as code (IaC) tool that helps you build, change, and version infrastructure safely and efficiently.

To install Terraform, enter the following command:

    sudo snap install --classic --channel=latest/stable terraform

## Initialize Terraform

Clone the [reference terraform plan](https://github.com/canonical/anbox-cloud-terraform) and initialize terraform:

    git clone https://github.com/canonical/anbox-cloud-terraform
    cd anbox-cloud-terraform
    terraform init

The required providers for the terraform plan with their correct versions, including the Juju provider for terraform, are downloaded.

## Deploy Anbox Cloud

```{note}
The current reference terraform plan maps a basic Anbox Cloud deployment with a limited amount of configuration options. If you want to customize the deployment based on your current infrastructure requirements, remember to modify the cloned plan as required.
```

Create a `deploy.tfvars` file and provide necessary configuration values to the terraform plan. Your `deploy.tfvars` file could look like this:

    ubuntu_pro_token = "<your_ubuntu_pro_token>"
    constraints      = ["arch=amd64"]
    anbox_channel    = "1.26/stable" // Channel to use for deploying Anbox Cloud
    subclusters = [
      {
        name           = "a" // Suffix for the Juju model designated to an Anbox Subcluster
        lxd_node_count = 1  // Number of LXD nodes to deploy in the Anbox Subcluster
      }
    ]

To preview what will be deployed by the terraform plan, run the following command:

    terraform plan -out=tfplan -var-file=deploy.tfvars

If everything looks fine, apply the plan:

    terraform apply tfplan -parallelism=1

You should use the terraform option `-parallelism=1` to increase the reliability for the plan to successfully apply.

```{note}
Throughout this guide, you will learn about the different configuration parameters you can set in the `deploy.tfvars` file for customizing your deployment. Every time you modify this file, remember to preview the changes and apply the plan.
```

Now, if you run `juju models`, you will see two Juju models created, namely `anbox-controller` and `anbox-subcluster-a`.

```sh
Model                Cloud/Region  Type  Status     Machines  Units  Access  Last connection
anbox-controller     juju/default  lxd   available         4      4  admin   1 minute ago
anbox-subcluster-a*  juju/default  lxd   available         6      6  admin   1 minute ago
```

After deployment is finished, Juju will continue to install software and connect the different parts of the cluster together. This can take several minutes. You can monitor the status by running the following commands:

    juju status -m anbox-controller --color
    juju status -m anbox-subcluster-a --color

## Scale the number of Anbox Subclusters

One of the advantages of using Terraform is the ability to manage infrastructure with a persistent state. Terraform remembers and synchronizes the current state of the infrastructure with the expectations of the plan.
Terraform generates a diff of the current state and the expected state in the defined plan when you run `terraform plan`. Use this to scale your Anbox Cloud deployments.

To add another subcluster, modify the `deploy.tfvars` file:

    ubuntu_pro_token = "<your_ubuntu_pro_token>"
    constraints      = ["arch=amd64"]
    anbox_channel    = "1.26/stable" // Channel to use for deploying Anbox Cloud
    subclusters = [
      {
        name           = "a" // Suffix for the Juju model designated to an Anbox Subcluster
        lxd_node_count = 1  // Number of LXD nodes to deploy in the Anbox Subcluster
      },
      { // Add a new subcluster
        name           = "b"
        lxd_node_count = 1
      }
    ]

Review and apply the plan.

Similarly, to scale down your deployment, remove the subcluster from the configuration and apply the plan.

## Scale the number of LXD nodes per Anbox Subcluster

Similar to the scaling operation for subclusters, we can also scale the number of LXD nodes per subcluster.
To add or remove LXD nodes, modify the value of the `lxd_node_count` variable.

## Enable HA Configuration

The terraform plan comes with a recommended high availability (HA) configuration for Anbox Cloud deployments. Enable it by setting `enable_ha` to `true`.

## Deploy AAR (Anbox Application Registry)

To deploy the AAR alongside Anbox Cloud, set the `registry_config` and `deploy_registry` parameters:

    ubuntu_pro_token = "<your_ubuntu_pro_token>"
    constraints      = ["arch=amd64"]
    anbox_channel    = "1.26/stable" // Channel to use for deploying Anbox Cloud
    subclusters = [
      {
        name           = "a"
        lxd_node_count = 5
        registry_config = { // registry configuration for the subcluster
            mode = "client"
        }
      }
    ]
    deploy_registry = true

This deploys a new Juju model dedicated to the Anbox Application Registry.

## Enable observability using COS (Canonical Observability Stack)

Set the `enable_cos` configuration to `true` to deploy the required resources/charms to integrate Anbox Cloud components with COS.

```{note}
The plan only deploys the `grafana-agent` charm internally in the models and creates the required relations with other anbox charms. The plan does NOT create Juju relations for integrating with a COS model deployed externally.
If you want to use an external COS model, follow the instructions as described in the [COS tutorial](https://charmhub.io/topics/canonical-observability-stack/tutorials/instrumenting-machine-charms#step-4-relate-grafana-agent-to-cos-lite-prometheus-loki-and-grafana) to create those relations manually.
```


---
myst:
  html_meta:
    "description": "How to perform common tasks in Anbox Cloud, covering installation, application management, instance operations, and troubleshooting."
---

(how-to-guides)=
# How-to guides

These how-to guides help you install, configure, manage, and use Anbox Cloud.

## Installation and configuration

Deploy Anbox Cloud on a single machine with the Appliance or at scale with a charmed deployment managed by Juju.

- {ref}`howto-install-anbox-cloud`
- {ref}`howto-install-appliance`
- {ref}`howto-upgrade`
- {ref}`howto-set-up-idp`

## Using Anbox Cloud

Manage Android workloads by working with images, applications, instances and more.

- {ref}`howto-manage-images`
- {ref}`howto-manage-applications`
- {ref}`howto-instance`
- {ref}`howto-addons`
- {ref}`howto-streaming`
- {ref}`howto-port-android-apps`
- {ref}`howto-use-web-dashboard`
- {ref}`howto-Android`
- {ref}`howto-gpu`

## Managing Anbox Cloud

Distribute the load of Anbox Cloud over several machines in a cluster, share applications via AAR and work with Anbox runtime.

- {ref}`howto-manage-anbox`
- {ref}`howto-manage-cluster`
- {ref}`howto-aar`
- {ref}`howto-anbox-runtime`

## Monitoring Anbox Cloud

Anbox Cloud exposes metrics through API endpoints for integration with external observability tools.

- {ref}`howto-monitor-anbox`

## Troubleshooting Anbox Cloud

When something goes wrong, these guides help you diagnose the issue and collect the information needed for a bug report.

- {ref}`howto-ts-anbox-cloud`


If you are new to Anbox Cloud, start with the {ref}`tutorials` for step-by-step instructions. 
For technical details, see the {ref}`reference`. 
For background information and concepts, refer to {ref}`explanation`.

```{toctree}
:hidden:

Install the appliance <install-appliance/index>
Install Anbox Cloud <install/index>
Set up a custom IdP <setup-custom-idp/index>
Manage AAR <aar/index>
Manage Addons <addons/index>
Manage Anbox Cloud <anbox/index>
Manage Images <images/index>
Manage Applications <application/index>
Manage cluster nodes <cluster/index>
Manage Instances <instance/index>
Monitor Anbox Cloud <monitor/index>
Port Android apps <port/index>
Stream <stream/index>
Troubleshoot Anbox Cloud <troubleshoot/index>
Upgrade Anbox Cloud <upgrade/index>
Use web dashboard <dashboard/index>
Work with Anbox runtime <anbox-runtime/index>
Work with Android <android/index>
Tuning GPU Configuration <gpu/index>
```

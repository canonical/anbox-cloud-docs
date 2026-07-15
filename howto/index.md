---
myst:
  html_meta:
    "description": "How to perform common tasks in Anbox Cloud, covering installation, application management, instance operations, and troubleshooting."
---

(how-to-guides)=
# How-to guides

These how-to guides help you perform key operational tasks when configuring, managing or using Anbox Cloud.

## Installation and deployment

Anbox Cloud can be installed as a single-machine appliance or as a charmed deployment using Juju.

- {ref}`howto-install-anbox-cloud`
- {ref}`howto-install-appliance`
- {ref}`howto-upgrade`

## Using Anbox Cloud

Images provide the Android base for instances, which run packaged applications. The streaming stack can deliver the visual output to end users.

- {ref}`howto-manage-images`
- {ref}`howto-manage-applications`
- {ref}`howto-instance`
- {ref}`howto-addons`
- {ref}`howto-streaming`
- {ref}`howto-port-android-apps`
- {ref}`howto-use-web-dashboard`
- {ref}`howto-Android`

## Managing Anbox Cloud

Both deployment variants can be managed remotely. Charmed deployments can additionally distribute load across a cluster and share applications via AAR.

- {ref}`howto-manage-anbox`
- {ref}`howto-manage-cluster`
- {ref}`howto-aar`
- {ref}`howto-anbox-runtime`

## Monitoring Anbox Cloud

Anbox Cloud exposes metrics through API endpoints for integration with external observability tools.

- {ref}`howto-monitor-anbox`

## Troubleshooting Anbox Cloud

Resolutions for common issues with Anbox Cloud and how to collect useful debugging information before reporting an issue.

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

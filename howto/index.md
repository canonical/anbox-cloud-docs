---
myst:
  html_meta:
    "description": "How-to guides for installing Anbox Cloud, managing workloads, customizing Android, configuring streaming and maintaining deployments."
---

(how-to-guides)=
# How-to guides

These how-to guides help you install, configure, manage, and use Anbox Cloud.

## Install and upgrade

Install the Anbox Cloud Appliance on a single machine, deploy Anbox Cloud with Juju or upgrade an existing deployment.

- {ref}`howto-install-appliance`
- {ref}`howto-install-anbox-cloud`
- {ref}`howto-upgrade`

## Manage workloads

Manage images and applications, create instances in projects and use the Anbox Cloud dashboard.

- {ref}`howto-manage-images`
- {ref}`howto-manage-applications`
- {ref}`howto-instance`
- {ref}`howto-projects`
- {ref}`howto-use-web-dashboard`

## Customize Android and the runtime

Port applications, debug Android environments, integrate automotive features and extend instance behavior through addons and runtime plugins.

- {ref}`howto-port-android-apps`
- {ref}`howto-Android`
- {ref}`howto-addons`
- {ref}`howto-anbox-runtime`

## Configure streaming and graphics

Set up streaming, integrate client features and tune GPU usage to improve instance density.

- {ref}`howto-streaming`
- {ref}`howto-gpu`

## Manage your deployment

Control access, harden your deployment, resize storage, manage cluster nodes and distribute applications through the Anbox Application Registry (AAR).

- {ref}`Manage authentication and authorization <howto-manage-auth>`
- {ref}`howto-manage-anbox`
- {ref}`howto-manage-cluster`
- {ref}`howto-aar`

## Monitor and troubleshoot

Connect your observability stack, investigate failures and collect logs to diagnose problems.

- {ref}`howto-monitor-anbox`
- {ref}`howto-ts-anbox-cloud`

If you are new to Anbox Cloud, start with the {ref}`tutorials`.
For configuration options, commands and APIs, see {ref}`reference`.
For background information and concepts, see {ref}`explanation`.

```{toctree}
:hidden:

Install the appliance <install-appliance/index>
Install Anbox Cloud <install/index>
Manage AAR <aar/index>
Manage Addons <addons/index>
Manage authentication and authorization <authentication-authorization/index>
Manage Anbox Cloud <anbox/index>
Manage Images <images/index>
Manage Applications <application/index>
Manage cluster nodes <cluster/index>
Manage Instances <instance/index>
Manage projects <projects/index>
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

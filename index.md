---
myst:
  html_meta:
    "description": "Run Android at scale in the cloud. Anbox Cloud delivers high-density streaming using LXD containers or VMs on public or private infrastructure."
---

(home)=
# Anbox Cloud documentation

**Anbox Cloud runs Android in the cloud using lightweight LXD system containers or full virtual machines.**

**Built on Ubuntu, it provides a scalable platform to deploy, manage, and stream Android workloads across public and private infrastructure with consistent performance and low latency.** It can run up to 100 Android instances per server while maintaining security and isolation.

Anbox Cloud is available as a single-machine {ref}`appliance <sec-variants>` for small-scale deployments or as a {ref}`charmed deployment <sec-variants>` using Juju for production environments and multi-cluster scaling.

**You should consider Anbox Cloud for the wide range of Android workloads it supports.** Cloud gaming providers can deliver high-performance streaming at scale, automotive OEMs can test infotainment systems without physical hardware, Android developers can preview UI changes instantly, and enterprises can provide remote Android workspaces as a service.

## In this documentation

### Lifecycle

- **Installation:** {ref}`ref-requirements` • {ref}`tut-installing-appliance` • {ref}`howto-deploy-anbox-baremetal`
- **Authentication and authorization:** {ref}`howto-set-up-idp` • {ref}`howto-configure-oidc` • {ref}`howto-auth` • {ref}`exp-auth` • {ref}`ref-auth`
- **Configuration:** {ref}`ref-appliance-preseed-config` • {ref}`ref-addon-manifest` • {ref}`ref-application-manifest` • {ref}`ref-ams-configuration` • {ref}`ref-ams-instance-configuration`
- **Deployment:** {ref}`howto-validate-deployment` • {ref}`howto-use-ceph-storage` • {ref}`howto-customize-installation`
- **Scaling:** {ref}`exp-nodes` • {ref}`exp-clustering` • {ref}`howto-configure-cluster-nodes` • {ref}`howto-scale-up-cluster` • {ref}`howto-scale-down-cluster`
- **Upgrading:** {ref}`howto-upgrade-appliance` • {ref}`howto-upgrade-anbox-cloud`

### Artifacts and interfaces

- **Appliance:** {ref}`sec-variants` • {doc}`CLI </reference/cmd-ref/appliance/anbox-cloud-appliance>` • {ref}`exp-web-dashboard`
- **Anbox Management Service:** {ref}`exp-ams` • {ref}`howto-access-ams-remote` • {doc}`CLI </reference/cmd-ref/amc/ams.amc>`
- **Anbox Application Registry:** {ref}`exp-aar` • {ref}`howto-configure-aar` • {ref}`howto-deploy-aar` • {ref}`howto-revoke-aar`
- **Images:** {ref}`exp-images` • {ref}`howto-configure-image-server` • {ref}`howto-add-image` • {ref}`howto-delete-image` • {ref}`howto-use-specific-release`
- **Instances:** {ref}`exp-instances` • {ref}`exp-resources-presets` • {ref}`howto-create-instance` • {ref}`howto-configure-instance` • {ref}`howto-start-instance` • {ref}`howto-stop-instance` • {ref}`howto-delete-instance` • {ref}`howto-expose-services` • {ref}`howto-view-instance-logs` • {ref}`howto-backup-restore-application-data` • {ref}`ref-hooks`
- **Applications:** {ref}`howto-create-application` • {ref}`howto-delete-application` • {ref}`howto-update-application` • {ref}`howto-pass-custom-data-application` • {ref}`howto-extend-application` • {ref}`howto-stream-applications`
- **Addons:** {ref}`howto-create-addon` • {ref}`howto-enable-addons-globally` • {ref}`howto-migrate-addons` • {ref}`howto-update-addons` • {ref}`exp-addons`
- **SDKs:** {ref}`ref-sdks` • [Platform SDK API](https://canonical.github.io/anbox-cloud.github.com/latest/anbox-platform-sdk/)

### Features

- **Streaming:** {ref}`exp-application-streaming` • {ref}`tut-set-up-stream-client` • {doc}`Stream Gateway API </reference/api-reference/gateway-api>` • {ref}`ref-webrtc` • {ref}`exp-platforms` • {ref}`howto-share-session`
- **Rendering:** {ref}`exp-rendering-architecture` • {ref}`exp-rendering-graphics`
- **Images:** {ref}`exp-custom-images` • {ref}`exp-aaos`
- **Supported features:** {ref}`ref-android-features` • {ref}`ref-aosp-aaos` • {ref}`ref-rendering-resources` • {ref}`ref-codecs` • {ref}`ref-feature-flags`

### Quality

- **Security:** {ref}`ref-security-policy` • {ref}`howto-harden` • {ref}`howto-set-up-tls` • {ref}`exp-security`
- **Performance:** {ref}`howto-run-benchmarks` • {ref}`ref-performance-benchmarks` • {ref}`ref-prometheus-metrics`
- **Plan a deployment:** {ref}`exp-capacity-planning` • {ref}`exp-production-planning` • {ref}`howto-enable-ha` • {ref}`howto-monitor-anbox`

## How this documentation is organised

This documentation uses the [Diátaxis documentation structure](https://diataxis.fr/).

- The {ref}`tutorials` take you step-by-step through installing Anbox Cloud Appliance, creating your first virtual Android device,  and setting up a stream client.
- {ref}`how-to-guides` assume you have basic familiarity with Anbox Cloud. They cover key operations such as managing applications, instances, and clusters.
- {ref}`reference` provides technical details on configuration options, APIs, CLI commands, and system requirements.
- {ref}`explanation` offers topic overviews and context on architecture, working with Anbox Cloud, deploying, and security.

## Project and community

Anbox Cloud is a product developed by [Canonical](https://canonical.com/). While it was initially based on the open-source Anbox project (archived in [GitHub](https://github.com/anbox)), its codebase has since become entirely independent.

We welcome community involvement through suggestions, fixes and constructive feedback both on the product and its documentation.

### Get involved

- [Discourse forum](https://discourse.ubuntu.com/c/project/anbox-user/148?_gl=1*1q03mla*_ga*Mjg0ODIyOTM5LjE3NzY3MDY4ODQ.*_ga_892F83CXG5*czE3Nzk4NjkzMzEkbzcyJGcxJHQxNzc5ODc0MTQzJGo2MCRsMCRoMA..)
- [Matrix channel](https://matrix.to/#/#anbox-cloud:ubuntu.com)
- {ref}`contribute`
- [Issue tracker](https://bugs.launchpad.net/anbox-cloud/+bugs)
- [Support](https://ubuntu.com/support?_gl=1*1396238*_ga*Mjg0ODIyOTM5LjE3NzY3MDY4ODQ.*_ga_892F83CXG5*czE3Nzk4NzY2NjUkbzczJGcxJHQxNzc5ODc2OTE0JGo1OSRsMCRoMA..)

### Releases

- {ref}`ref-release-notes`
- {ref}`ref-component-versions`
- {ref}`ref-deprecation-notes`
- {ref}`ref-provided-images`

### Governance and policies

- {ref}`ref-license-information`
- {ref}`ref-charm-configuration`
- [Code of conduct](https://ubuntu.com/community/code-of-conduct)

### Commercial support

Thinking about using Anbox Cloud for your next project? [Get in touch\!](https://canonical.com/anbox-cloud?_gl=1*1hm0lj*_ga*Mjg0ODIyOTM5LjE3NzY3MDY4ODQ.*_ga_892F83CXG5*czE3Nzk4NzY2NjUkbzczJGcxJHQxNzc5ODc3NzAwJGo1OSRsMCRoMA..*_gcl_au*NTcyOTk1ODc5LjE3NzYyNjY3MjQ.*_ga_5LTL1CNEJM*czE3Nzk4NzY2NjQkbzYyJGcxJHQxNzc5ODc3NzAwJGo1OSRsMCRoMA..#get-in-touch)

```{toctree}
:hidden:
tutorial/index
howto/index
explanation/index
reference/index
Contribute <contribute/index>
reference/release-notes/release-notes
```

---
myst:
  html_meta:
    "description": "Run Android at scale in the cloud. Anbox Cloud delivers high-density streaming using LXD containers or VMs on public or private infrastructure."
---

(home)=
# Anbox Cloud documentation

**Anbox Cloud runs Android workloads at scale** across public cloud, private cloud, and bare-metal infrastructure.

It supports high-density, fast-starting **containerized Android** in LXD system containers and **virtualized Android** in [Cuttlefish](https://source.android.com/docs/devices/cuttlefish) virtual machines for a standard, unmodified Android environment with stronger isolation.

Teams can launch **reproducible Android environments on demand** without the overhead of maintaining and scaling physical device fleets.

Anbox Cloud serves cloud gaming and application streaming providers, Android developers and CI teams, automotive and embedded developers, OEMs, and enterprises building managed Android services.
[Get in touch with the Anbox Cloud team](https://canonical.com/anbox-cloud#get-in-touch) to talk through your Android workload, deployment, or evaluation.

## In this documentation

### Getting started

- **Anbox Cloud:** {ref}`Overview <exp-anbox-cloud>` • {ref}`Deployment variants <sec-variants>` • {ref}`Android execution models <exp-android-execution-models>`
- **Tutorials:** {ref}`Install the appliance <tut-installing-appliance>` • {ref}`Create a virtual device <tut-create-virtual-device>` • {ref}`Get started with virtualized Android <tut-getting-started-virtualized-android>` • {ref}`Set up a stream client <tut-set-up-stream-client>`

### Workloads

- **Images:** {ref}`Overview <exp-images>` • {ref}`Manage images <howto-manage-images>` • {ref}`Provided images <ref-provided-images>` • {ref}`Feature support by image type <ref-feature-support-by-image-type>`
- **Instances:** {ref}`Overview <exp-instances>` • {ref}`Manage instances <howto-instance>` • {ref}`Resource presets <exp-resources-presets>`
- **Applications:** {ref}`Overview <exp-applications>` • {ref}`Manage applications <howto-manage-applications>` • {ref}`Application manifest <ref-application-manifest>`
- **Addons:** {ref}`Overview <exp-addons>` • {ref}`Manage addons <howto-addons>` • {ref}`Migrate from addon hooks to system units <howto-migrate-from-addon-and-app-hooks>`

### Streaming and rendering

- **Streaming:** {ref}`Overview <exp-application-streaming>` • {ref}`Access the gateway <howto-access-stream-gateway>` • {ref}`Share a session <howto-share-session>` • {ref}`Supported codecs <ref-codecs>`
- **Rendering:** {ref}`Rendering architecture <exp-rendering-architecture>` • {ref}`Configure rendering <exp-rendering-graphics>` • {ref}`Supported GPUs <ref-rendering-resources>`

### Use cases

- **Testing and automation:** {ref}`Test your application <howto-test-application>` • {ref}`Debug Android test environments <howto-access-android-instance>` • {ref}`Port Android apps <howto-port-android-apps>` • {ref}`Compatibility considerations <ref-compatibility-considerations>`
- **Android automotive:** {ref}`Work with AAOS <exp-aaos>` • {ref}`Set vehicle properties <howto-set-automotive-properties>` • {ref}`Integrate a custom VHAL <howto-replace-anbox-vhal>`
- **Custom Android and platform development:** {ref}`Custom images <exp-custom-images>` • {ref}`Package a custom Android build <howto-package-custom-android-build>` • {ref}`Develop a platform plugin <howto-develop-platform-plugin>`

### Interfaces

- **Dashboard:** {ref}`Overview <exp-web-dashboard>` • {ref}`Use the dashboard <howto-use-web-dashboard>`
- **CLI:** {doc}`AMC </reference/cmd-ref/amc/ams.amc>` • {doc}`Anbox Cloud Appliance </reference/cmd-ref/appliance/anbox-cloud-appliance>` • {doc}`AAR </reference/cmd-ref/aar/aar>`
- **APIs:** {doc}`AMS HTTP API </reference/api-reference/ams-api>` • {doc}`Stream Gateway API </reference/api-reference/gateway-api>` • {doc}`Anbox HTTPS API </reference/api-reference/anbox-https-api>`
- **SDKs:** {ref}`SDK overview <ref-sdks>` • [Platform SDK](https://canonical.github.io/anbox-cloud.github.com/latest/anbox-platform-sdk/)

### Deployment lifecycle

- **Deploy:** {ref}`Requirements <ref-requirements>` • {ref}`Anbox Cloud Appliance <howto-install-appliance>` • {ref}`Charmed deployment <howto-install-anbox-cloud>`
- **Configure:** {ref}`AMS configuration <ref-ams-configuration>` • {ref}`Appliance configuration <ref-appliance-configuration>` • {ref}`Charm configuration <ref-charm-configuration>`
- **Scale:** {ref}`Clustering <exp-clustering>` • {ref}`Nodes <exp-nodes>` • {ref}`Manage a cluster <howto-manage-cluster>` • {ref}`Enable high availability <howto-enable-ha>`
- **Plan:** {ref}`Capacity planning <exp-capacity-planning>` • {ref}`Production planning <exp-production-planning>`
- **Monitor and troubleshoot:** {ref}`Monitor Anbox Cloud <howto-monitor-anbox>` • {ref}`View logs <howto-ts-view-logs>` • {ref}`Prometheus metrics <ref-prometheus-metrics>` • {ref}`Troubleshooting guides <howto-ts-anbox-cloud>`
- **Upgrade:** {ref}`Upgrade the appliance <howto-upgrade-appliance>` • {ref}`Upgrade a charmed deployment <howto-upgrade-anbox-cloud>`

### Security and performance

- **Security:** {ref}`Overview <exp-security>` • {ref}`Harden your deployment <howto-harden>` • {ref}`Set up TLS <howto-set-up-tls>` • {ref}`Security policy <ref-security-policy>`
- **Access control:** {ref}`Authentication and authorization <exp-auth>` • {ref}`Configure OIDC for the appliance <howto-configure-oidc>` • {ref}`Configure user permissions <howto-auth>`
- **Performance:** {ref}`Overview <exp-performance>` • {ref}`Performance benchmarks <ref-performance-benchmarks>` • {ref}`Run benchmarks <howto-run-benchmarks>` • {ref}`GPU instance density <howto-increase-instance-density>`

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
reference/index
explanation/index
```

```{toctree}
:hidden:
reference/release-notes/release-notes
Contribute <contribute/index>
```

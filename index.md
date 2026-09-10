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

```{eval-rst}
..  domain::

    ..  slice:: Anbox Cloud

        :doc:`Overview </explanation/anbox-cloud>` slice
        :doc:`Deployment variants </explanation/anbox-cloud>`
        :doc:`Android execution models </explanation/android-execution-models>`

    ..  slice:: Tutorials

        :doc:`Install the appliance </tutorial/installing-appliance>`
        :doc:`Create a virtual device </tutorial/create-test-virtual-device>`
        :doc:`Get started with virtualized Android </tutorial/getting-started-with-virtualized-android>`
        :doc:`Set up a stream client </tutorial/stream-client>`
```

### Workloads

```{eval-rst}
..  domain::

    ..  slice:: Images

        :doc:`Overview </explanation/images>` slice
        :doc:`Manage images </howto/images/index>`
        :doc:`Provided images </reference/provided-images>`
        :doc:`Feature support by image type </reference/feature-support-by-image-type>`

    ..  slice:: Instances

        :doc:`Overview </explanation/instances>` slice
        :doc:`Manage instances </howto/instance/index>`
        :doc:`Resource presets </explanation/resources>`

    ..  slice:: Applications

        :doc:`Overview </explanation/applications>` slice
        :doc:`Manage applications </howto/application/index>`
        :doc:`Application manifest </reference/application-manifest>`

    ..  slice:: Addons

        :doc:`Overview </explanation/addons>` slice
        :doc:`Manage addons </howto/addons/index>`
        :doc:`Migrate from addon hooks to system units </howto/instance/migrate-from-addon-and-app-hooks>`
```

### Streaming and rendering

```{eval-rst}
..  domain::

    ..  slice:: Streaming

        :doc:`Overview </explanation/application-streaming>` slice
        :doc:`Access the gateway </howto/stream/access-stream-gateway>`
        :doc:`Share a session </howto/instance/share-session>`
        :doc:`Supported codecs </reference/supported-codecs>`

    ..  slice:: Rendering

        :doc:`Rendering architecture </explanation/rendering-architecture>`
        :doc:`Configure rendering </explanation/rendering-graphics>`
        :doc:`Supported GPUs </reference/supported-rendering-resources>`
```

### Use cases

```{eval-rst}
..  domain::

    ..  slice:: Testing and automation

        :doc:`Test your application </howto/application/test-application>`
        :doc:`Debug Android test environments </howto/android/access-android-instance>`
        :doc:`Port Android apps </howto/port/index>`
        :doc:`Compatibility considerations </reference/compatibility-considerations>`

    ..  slice:: Android automotive

        :doc:`Work with AAOS </explanation/aaos>`
        :doc:`Set vehicle properties </howto/android/set-automotive-properties>`
        :doc:`Integrate a custom VHAL </howto/android/custom-vhal>`

    ..  slice:: Custom Android and platform development

        :doc:`Custom images </explanation/custom-images>`
        :doc:`Package a custom Android build </howto/images/package-custom-android-build>`
        :doc:`Develop a platform plugin </howto/anbox-runtime/develop-platform-plugin>`
```

### Interfaces

```{eval-rst}
..  domain::

    ..  slice:: Dashboard

        :doc:`Overview </explanation/web-dashboard>`
        :doc:`Use the dashboard </howto/dashboard/index>`

    ..  slice:: CLI

        :doc:`AMC </reference/cmd-ref/amc/ams.amc>`
        :doc:`Anbox Cloud Appliance </reference/cmd-ref/appliance/anbox-cloud-appliance>` slice
        :doc:`AAR </reference/cmd-ref/aar/aar>`

    ..  slice:: APIs

        :doc:`AMS HTTP API </reference/api-reference/ams-api>`
        :doc:`Stream Gateway API </reference/api-reference/gateway-api>`
        :doc:`Anbox HTTPS API </reference/api-reference/anbox-https-api>`

    ..  slice:: SDKs

        :doc:`SDK overview </reference/sdks>`
```

### Deployment lifecycle

```{eval-rst}
..  domain::

    ..  slice:: Deploy

        :doc:`Requirements </reference/requirements>`
        :doc:`Anbox Cloud Appliance </howto/install-appliance/index>` slice
        :doc:`Charmed deployment </howto/install/index>`

    ..  slice:: Configure

        :doc:`AMS configuration </reference/ams-configuration>`
        :doc:`Appliance configuration </reference/appliance-configuration>`
        :doc:`Charm configuration </reference/charm-configuration>`

    ..  slice:: Scale

        :doc:`Clustering </explanation/clustering>`
        :doc:`Nodes </explanation/nodes>`
        :doc:`Manage a cluster </howto/cluster/index>`
        :doc:`Enable high availability </howto/install/enable-high-availability>`

    ..  slice:: Plan

        :doc:`Capacity planning </explanation/capacity-planning>`
        :doc:`Production planning </explanation/production-planning>`

    ..  slice:: Monitor and troubleshoot

        :doc:`Monitor Anbox Cloud </howto/monitor/index>`
        :doc:`View logs </howto/troubleshoot/view-logs>`
        :doc:`Prometheus metrics </reference/prometheus>`
        :doc:`Troubleshooting guides </howto/troubleshoot/index>`

    ..  slice:: Upgrade

        :doc:`Upgrade the appliance </howto/upgrade/upgrade-appliance>`
        :doc:`Upgrade a charmed deployment </howto/upgrade/upgrade-anbox>`
```

### Security and performance

```{eval-rst}
..  domain::

    ..  slice:: Security

        :doc:`Overview </explanation/security/index>` slice
        :doc:`Harden your deployment </howto/anbox/harden>`
        :doc:`Set up TLS </howto/anbox/tls-for-appliance>`
        :doc:`Security policy </reference/security-policy>`

    ..  slice:: Access control

        :doc:`Authentication and authorization </explanation/auth>`
        :doc:`Configure OIDC for the appliance </howto/setup-custom-idp/configure-oidc>`
        :doc:`Configure user permissions </howto/anbox/auth>`

    ..  slice:: Performance

        :doc:`Overview </explanation/performance>` slice
        :doc:`Performance benchmarks </reference/perf-benchmarks>`
        :doc:`Run benchmarks </howto/anbox/benchmarks>`
        :doc:`GPU instance density </howto/gpu/increase-instance-density>`
```

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

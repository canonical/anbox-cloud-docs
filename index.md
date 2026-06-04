---
myst:
  html_meta:
    "description": "Run Android at scale in the cloud. Anbox Cloud delivers high-density streaming using LXD containers or VMs on public or private infrastructure."
---

# Anbox Cloud documentation

Anbox Cloud is a scalable platform for running Android in the cloud using lightweight LXD system containers or full virtual machines. Built on Ubuntu, it enables you to deploy, manage, and stream Android workloads across public or private infrastructure with consistent performance and low latency.

Compared to other Android emulation solutions, Anbox Cloud delivers at least twice the density and can run up to **100 Android instances per server** while maintaining security and isolation for each instance.

This makes it well suited for a wide range of Android workloads. **Cloud gaming service providers** can deliver high-performance streaming experiences at scale, **automotive OEMs** can test infotainment systems without relying on physical hardware, **Android developers** can preview UI changes instantly, and **enterprises** can provide remote Android workspaces as a service.

Anbox Cloud is available as a single-machine [appliance](https://documentation.ubuntu.com/anbox-cloud/explanation/anbox-cloud/#anbox-cloud-appliance) for development and small-scale deployments, or as a [charmed deployment](https://documentation.ubuntu.com/anbox-cloud/explanation/anbox-cloud/#id1) using Juju for production environments and multi-cluster scaling.

## In this documentation

### Lifecycle

- **Installation:** [Requirements](https://documentation.ubuntu.com/anbox-cloud/reference/requirements/) • [Install using appliance](https://documentation.ubuntu.com/anbox-cloud/tutorial/installing-appliance/) • [Install using charms](https://documentation.ubuntu.com/anbox-cloud/howto/install/deploy-bare-metal/)
- **Authentication and authorization:** [Custom IdP](https://documentation.ubuntu.com/anbox-cloud/howto/setup-custom-idp/#) • [OIDC](https://documentation.ubuntu.com/anbox-cloud/howto/setup-custom-idp/configure-oidc/) • [User permissions](https://documentation.ubuntu.com/anbox-cloud/howto/anbox/auth/#) • [Authorization entities in Anbox Cloud](https://documentation.ubuntu.com/anbox-cloud/explanation/auth/) • [Entitlements](https://documentation.ubuntu.com/anbox-cloud/reference/auth/)
- **Configuration:** [Non-interactive configuration](https://documentation.ubuntu.com/anbox-cloud/reference/appliance-preseed/) • [Addon manifest](https://documentation.ubuntu.com/anbox-cloud/reference/addon-manifest/#) • [Application manifest](https://documentation.ubuntu.com/anbox-cloud/reference/application-manifest/) • [AMS parameters](https://documentation.ubuntu.com/anbox-cloud/reference/ams-configuration/) • [Instance parameters](https://documentation.ubuntu.com/anbox-cloud/reference/ams-instance-configuration/#)
- **Deployment:** [Validate](https://documentation.ubuntu.com/anbox-cloud/howto/install/validate-deployment/) • [Use shared storage](https://documentation.ubuntu.com/anbox-cloud/howto/install/use-ceph-storage/)  • [Customize](https://documentation.ubuntu.com/anbox-cloud/howto/install/customize-installation/#)
- **Scaling:** [Nodes](https://documentation.ubuntu.com/anbox-cloud/explanation/nodes/) • [Clustering](https://documentation.ubuntu.com/anbox-cloud/explanation/clustering/#) • [Configure clusters](https://documentation.ubuntu.com/anbox-cloud/howto/cluster/configure-nodes/) • [Scale up](https://documentation.ubuntu.com/anbox-cloud/howto/cluster/scale-up/) • [Scale down](https://documentation.ubuntu.com/anbox-cloud/howto/cluster/scale-down/)
- **Upgrading:** [Appliance](https://documentation.ubuntu.com/anbox-cloud/howto/upgrade/upgrade-appliance/#) • [Charmed Anbox](https://documentation.ubuntu.com/anbox-cloud/howto/upgrade/upgrade-anbox/)


### Artifacts and interfaces

- **Appliance:** [Introduction](https://documentation.ubuntu.com/anbox-cloud/explanation/anbox-cloud/#variants) • [CLI](https://documentation.ubuntu.com/anbox-cloud/reference/cmd-ref/appliance/anbox-cloud-appliance/) • [Web dashboard](https://documentation.ubuntu.com/anbox-cloud/explanation/web-dashboard/#)
- **Anbox Management Service:** [Introduction](https://documentation.ubuntu.com/anbox-cloud/explanation/web-dashboard/#) • [Remote access](https://documentation.ubuntu.com/anbox-cloud/howto/anbox/control-ams-remotely/#) • [CLI](https://documentation.ubuntu.com/anbox-cloud/reference/cmd-ref/amc/ams.amc/)
- **Anbox Application Registry:** [Introduction](https://documentation.ubuntu.com/anbox-cloud/explanation/web-dashboard/#) • [Configure](https://documentation.ubuntu.com/anbox-cloud/howto/aar/configure/#) • [Deploy](https://documentation.ubuntu.com/anbox-cloud/howto/aar/deploy/) • [Revoke a client](https://documentation.ubuntu.com/anbox-cloud/howto/aar/deploy/)
- **Images:** [Overview](https://documentation.ubuntu.com/anbox-cloud/explanation/images/) • [Image server](https://documentation.ubuntu.com/anbox-cloud/howto/images/configure-image-server/#) • [Add](https://documentation.ubuntu.com/anbox-cloud/howto/images/add-image/) • [Delete](https://documentation.ubuntu.com/anbox-cloud/howto/images/delete-image/) • [Choose](https://documentation.ubuntu.com/anbox-cloud/howto/images/use-specific-release/)
- **Instances:** [Overview](https://documentation.ubuntu.com/anbox-cloud/explanation/instances/) • [Resource presets](https://documentation.ubuntu.com/anbox-cloud/explanation/resources/) • [Create](https://documentation.ubuntu.com/anbox-cloud/howto/instance/create-instance/) • [Configure](https://documentation.ubuntu.com/anbox-cloud/howto/instance/configure-instance/) • [Start](https://documentation.ubuntu.com/anbox-cloud/howto/instance/start-instance/) • [Stop](https://documentation.ubuntu.com/anbox-cloud/howto/instance/stop-instance/) • [Delete](https://documentation.ubuntu.com/anbox-cloud/howto/instance/delete-instance/) • [Expose services](https://documentation.ubuntu.com/anbox-cloud/howto/instance/expose-services/) • [Logs](https://documentation.ubuntu.com/anbox-cloud/howto/instance/view-instance-logs/) • [Backup](https://documentation.ubuntu.com/anbox-cloud/howto/instance/backup-restore-application-data/) • [Hooks](https://documentation.ubuntu.com/anbox-cloud/reference/hooks/)
- **Applications:** [Create](https://documentation.ubuntu.com/anbox-cloud/howto/application/create-application/) • [Delete](https://documentation.ubuntu.com/anbox-cloud/howto/application/delete-application/) • [Update](https://documentation.ubuntu.com/anbox-cloud/howto/application/update-application/) • [Custom data](https://documentation.ubuntu.com/anbox-cloud/howto/application/pass-custom-data/) • [Extend](https://documentation.ubuntu.com/anbox-cloud/howto/application/extend-application/) • [Stream](https://documentation.ubuntu.com/anbox-cloud/howto/application/stream-application/)
- **Addons:** [Create](https://documentation.ubuntu.com/anbox-cloud/howto/addons/create-addon/) • [Enable globally](https://documentation.ubuntu.com/anbox-cloud/howto/addons/create-addon/) • [Migrate from an older version](https://documentation.ubuntu.com/anbox-cloud/howto/addons/create-addon/) • [Update](https://documentation.ubuntu.com/anbox-cloud/howto/addons/create-addon/) • [Best practices](https://documentation.ubuntu.com/anbox-cloud/explanation/addons/)
- **SDKs:** [Available SDKs](https://documentation.ubuntu.com/anbox-cloud/reference/sdks/) • [Platform SDK API](https://canonical.github.io/anbox-cloud.github.com/latest/anbox-platform-sdk/)


### Features

- **Streaming:** [Streaming Stack](https://documentation.ubuntu.com/anbox-cloud/explanation/application-streaming/#) • [Set up a stream client](https://documentation.ubuntu.com/anbox-cloud/tutorial/stream-client/) • [Stream Gateway API](https://documentation.ubuntu.com/anbox-cloud/reference/api-reference/gateway-api/) • [WebRTC streamer](https://documentation.ubuntu.com/anbox-cloud/reference/webrtc-streamer/) • [Platforms](https://documentation.ubuntu.com/anbox-cloud/explanation/platforms/) • [Share a stream session](https://documentation.ubuntu.com/anbox-cloud/howto/instance/share-session/)
- **Rendering:** [Architecture](https://documentation.ubuntu.com/anbox-cloud/explanation/rendering-architecture/#) • [Graphical output](https://documentation.ubuntu.com/anbox-cloud/explanation/rendering-graphics/)
- **Images:** [Custom images](https://documentation.ubuntu.com/anbox-cloud/explanation/custom-images/) • [AAOS images](https://documentation.ubuntu.com/anbox-cloud/explanation/aaos/#)
- **Supported features:** [Android features](https://documentation.ubuntu.com/anbox-cloud/reference/android-features/) • [Anbox features](https://documentation.ubuntu.com/anbox-cloud/reference/anbox-features/) • [Rendering resources](https://documentation.ubuntu.com/anbox-cloud/reference/supported-rendering-resources/) • [Video codecs](https://documentation.ubuntu.com/anbox-cloud/reference/supported-codecs/) **•** [Feature flags](https://documentation.ubuntu.com/anbox-cloud/reference/feature-flags/)

### Quality

- **Security:** [Security policy](https://documentation.ubuntu.com/anbox-cloud/reference/security-policy/) • [Harden your deployment](https://documentation.ubuntu.com/anbox-cloud/howto/anbox/harden/) • [Set up TLS](https://documentation.ubuntu.com/anbox-cloud/howto/anbox/tls-for-appliance/) • [Component level security](https://documentation.ubuntu.com/anbox-cloud/explanation/security/)
- **Performance:** [Run benchmarks](https://documentation.ubuntu.com/anbox-cloud/howto/anbox/benchmarks/) • [Reference benchmarks](https://documentation.ubuntu.com/anbox-cloud/reference/perf-benchmarks/) • [Prometheus metrics](https://documentation.ubuntu.com/anbox-cloud/reference/prometheus/)
- **Plan a deployment:** [Resource planning](https://documentation.ubuntu.com/anbox-cloud/explanation/capacity-planning/) • [Production](https://documentation.ubuntu.com/anbox-cloud/explanation/production-planning/) • [High availability](https://documentation.ubuntu.com/anbox-cloud/howto/install/enable-high-availability/) • [Monitoring](https://documentation.ubuntu.com/anbox-cloud/howto/monitor/)

## How this documentation is organised

This documentation uses the [Diátaxis documentation structure](https://diataxis.fr/).

- The [Tutorial](https://documentation.ubuntu.com/anbox-cloud/tutorial/) takes you step-by-step through installing Anbox Cloud Appliance and creating your first virtual Android device.
- [How to guides](https://documentation.ubuntu.com/anbox-cloud/howto/) assume you have basic familiarity with Anbox Cloud. They cover key operations such as managing applications, instances, and clusters.
- [Reference](https://documentation.ubuntu.com/anbox-cloud/reference/) provides technical details on configuration options, APIs, CLI commands, and system requirements.
- [Explanation](https://documentation.ubuntu.com/anbox-cloud/explanation/#explanation) offers topic overviews and context on architecture, working with Anbox Cloud, deploying, and security.

## Project and community

Anbox Cloud is a product developed by [Canonical](https://canonical.com/). While it was initially based on the open-source Anbox project (archived in [GitHub](https://github.com/anbox)), its codebase has since become entirely independent.

We welcome community involvement through suggestions, fixes and constructive feedback both on the product and its documentation.

### Get involved

- [Join the Discourse forum](https://discourse.ubuntu.com/c/project/anbox-user/148?_gl=1*1q03mla*_ga*Mjg0ODIyOTM5LjE3NzY3MDY4ODQ.*_ga_892F83CXG5*czE3Nzk4NjkzMzEkbzcyJGcxJHQxNzc5ODc0MTQzJGo2MCRsMCRoMA..)
- [Chat to us on Matrix](https://matrix.to/#/#anbox-cloud:ubuntu.com)
- [Contribute to this documentation](https://documentation.ubuntu.com/anbox-cloud/contribute/)
- [Report a bug](https://bugs.launchpad.net/anbox-cloud/+bugs)
- [Get support](https://ubuntu.com/support?_gl=1*1396238*_ga*Mjg0ODIyOTM5LjE3NzY3MDY4ODQ.*_ga_892F83CXG5*czE3Nzk4NzY2NjUkbzczJGcxJHQxNzc5ODc2OTE0JGo1OSRsMCRoMA..)

### Releases

- [Release notes & roadmap](https://documentation.ubuntu.com/anbox-cloud/reference/release-notes/release-notes/)
- [Component versions](https://documentation.ubuntu.com/anbox-cloud/reference/component-versions/)
- [Deprecation notices](https://documentation.ubuntu.com/anbox-cloud/reference/deprecation-notices/)
- [Available images](https://documentation.ubuntu.com/anbox-cloud/reference/provided-images/)

### Governance and policies

- [License](https://documentation.ubuntu.com/anbox-cloud/reference/license-information/)
- [Charm configuration](https://documentation.ubuntu.com/anbox-cloud/reference/charm-configuration/)
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

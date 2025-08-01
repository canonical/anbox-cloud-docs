# Anbox Cloud documentation

Anbox Cloud enables running Android apps on any cloud platform at scale. It uses system containers or virtual machines to run the nested Android containers and [Juju](https://juju.is/) for deployment in a cloud environment.

Anbox Cloud supports x86 and ARM64 hardware, providing the same set of features for both architectures.

By using system containers or virtual machines to emulate Android systems, Anbox Cloud achieves the isolation and security levels of a virtual machine without the associated overhead. Compared to other Android emulation solutions, Anbox Cloud can provide at least twice the density and can serve up to 100 Android instances per server.

Due to its highly scalable nature and performance optimization, delivering device-agnostic mobile applications is very easy. Popular use cases of Anbox Cloud include mobile game streaming services, corporate application streaming, application automation and testing.

## In this documentation


````{grid} 1 1 2 2
```{grid-item-card} [Tutorial](/tutorial/index.md)
**Start here** - a hands-on introduction to Anbox Cloud
- [Install Anbox Cloud Appliance](/tutorial/installing-appliance.md)
- [Create a virtual device](/tutorial/create-test-virtual-device.md)
```

```{grid-item-card} [How-to guides](/howto/index.md)
**Key operations and common tasks**
- Install: [appliance](/howto/install-appliance/index.md) | [charmed Anbox Cloud](/howto/install/index.md)
- Work with [applications](/howto/application/index.md) and [instances](/howto/instance/index.md)
- [Harden your deployment](/howto/anbox/harden.md)
- [Upgrade](/howto/upgrade/index.md)
- [Troubleshoot](/howto/troubleshoot/index.md) | [View logs](/howto/troubleshoot/view-logs.md)
```
````
````{grid} 1 1 2 2
:reverse:
```{grid-item-card} [Reference](/reference/index.md)
**Technical information**
- [AMS configuration](/reference/ams-configuration.md)
- [Application manifest](/reference/application-manifest.md) | [Addon manifest](/reference/addon-manifest.md)
- [CLI help](/reference/cmd-ref/index.md) | [API help](/reference/api-reference/index.md)
- [Release notes](/reference/release-notes/release-notes.md)
```

```{grid-item-card} [Explanation](/explanation/index.md)
**To understand how Anbox Cloud works**
- [Architecture](/explanation/anbox-cloud.md)
- [Security](/explanation/security/index.md)
- [Resource and capacity estimation](/explanation/capacity-planning.md)
- [Preparing to deploy in production](/explanation/production-planning.md)
```
````

## Project and community

Anbox Cloud is a product developed by Canonical. While it was initially based on the open-source Anbox project (archived in [GitHub](https://github.com/anbox)), its codebase has since become entirely independent.

We welcome community involvement through suggestions, fixes and constructive feedback both on the product and its documentation. You can engage with the Anbox Cloud team and the community using the following channels:


````{grid}
:reverse:
```{grid-item-card} Get help
[File a bug](https://bugs.launchpad.net/anbox-cloud/+bugs) | [Get support](https://ubuntu.com/support)

```

```{grid-item-card} Contribute
[Contribution guide](/contribute/index.md) | [Style guide](/contribute/anbox-style-guide.md)

```
```{grid-item-card} Engage
[Discourse](https://discourse.ubuntu.com/c/anbox-cloud/users/148) | [Matrix](https://matrix.to/#/#anbox-cloud:ubuntu.com) |
[Contact us](https://anbox-cloud.io/contact-us)

```
````

```{toctree}
:hidden:
tutorial/index
howto/index
explanation/index
reference/index
Contribute <contribute/index>
reference/release-notes/release-notes
```

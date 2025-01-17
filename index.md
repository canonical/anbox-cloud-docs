# Anbox Cloud documentation

Anbox Cloud enables running Android apps on any cloud platform at scale. It uses system containers or virtual machines to run the nested Android containers and [Juju](https://juju.is/) for deployment in a cloud environment.

Anbox Cloud supports x86 and Arm64 hardware, providing the same set of features for both architectures.

Since Anbox Cloud uses system containers or virtual machines to emulate Android systems, you can achieve the isolation and security level of a virtual machine without the associated overhead. Therefore, compared to other Android emulation solutions, Anbox Cloud can provide at least twice the density and can serve up to 100 Android instances per server.

Due to its highly scalable nature and performance optimization, delivering device-agnostic mobile applications is very easy. Popular use cases of Anbox Cloud include mobile game streaming services, corporate application streaming, application automation and testing.

## In this documentation

| | |
|--|--|
|  [Tutorials](/tutorial/landing.md)</br>  Get started - a hands-on introduction to Anbox Cloud for new users </br> |  [How-to guides](/howto/landing.md) </br> Step-by-step guides covering key operations and common tasks |
|  [Explanation](/explanation/landing.md) </br> Concepts - discussion and clarification of key topics, architecture  | [Reference](/reference/landing.md) </br> Technical information - specifications, APIs |

## Project and community

Anbox Cloud is a Canonical product. It originally grew out of the [Anbox open-source project](https://github.com/anbox), but its code base is now completely independent.

We welcome community involvement through suggestions, fixes and constructive feedback both on the product and its documentation. You can engage with the Anbox Cloud team and the community using the following channels:

- Engage with the Anbox Cloud team and community:
  - [Discourse](https://discourse.ubuntu.com/c/anbox-cloud/users/148)
  - [Matrix](https://matrix.to/#/#anbox-cloud:ubuntu.com)
- {ref}`Troubleshoot Anbox Cloud <howto-ts-anbox-cloud>`
- [Report a bug](https://bugs.launchpad.net/anbox-cloud/+bugs) with the product or documentation
- {ref}`contribute`

The {ref}`ref-release-notes` helps you get familiar with Anbox Cloud, its releases and roadmap.

For official support requirements, you can get support through [Ubuntu Pro](https://ubuntu.com/support).


Thinking about using Anbox Cloud for your next project? [Get in touch!](https://anbox-cloud.io/contact-us)

```{toctree}
:hidden:
tutorial/landing
howto/landing
explanation/landing
reference/landing
Contribute <contribute/landing>
reference/release-notes/release-notes
```

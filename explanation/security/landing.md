(exp-security)=
# Security

Anbox Cloud is designed using secure development practices - its architecture, components and all communication between components are designed to be fundamentally secure.

Anbox Cloud uses [LXD](https://ubuntu.com/lxd) for container and virtual machine management. To ensure security and isolation of each Android system, Anbox Cloud runs a single Android system per LXD instance.

The following security guides provide you information about each component's security and the cryptographic technology that they use:

```{toctree}
:maxdepth: 1

ams
anbox-runtime
android
charms
dashboard
instance
streaming-stack
```

## Communication among components

The architecture of Anbox Cloud has been designed in a way that ensures secure communication among all components.

All communication among services uses TLS encryption and authentication. Access is controlled through secure authentication tokens or temporary passwords. There are no insecure HTTP endpoints - all HTTP communication is secured by TLS and happens over HTTPS.

Secure communication is achieved using TLS and public-key encryption with a chain of trust, up to a shared root Certificate Authority (CA). However, when the cluster is being brought up or a new unit is being added, the chain of trust and certificates required must be bootstrapped into the machines.

The following table shows the authentication methods that are in place for the different components.

| Component             | Authentication method        |
|-----------------------|------------------------------|
| AMS                   | TLS client certificates      |
| LXD                   | TLS client certificates      |
| etcd                  | TLS client certificates      |
| Stream gateway        | Token authentication         |
| Stream agent <-> AMS  | TLS client certificates      |
| Stream agent <-> NATS | TLS and token authentication |
| Coturn with STUN      | No authentication needed     |
| Coturn with TURN      | Temporary user and password  |

## Security updates

Anbox Cloud provides images that are frequently updated with the latest security patches. When an image is updated, all Anbox Cloud applications that use the image are automatically updated as well (unless disabled with `application.auto_update`,See {ref}`ref-ams-configuration`).

In addition, to ensure that the latest Ubuntu security patches are applied outside of image updates as well, Anbox Cloud checks for and installs available security updates every time an application is bootstrapped. So when you create an application, its underlying image is updated with the latest Ubuntu security patches. You can also create a new application version without other changes to bootstrap the application again, and thus install the latest security patches.

It is possible to turn off this update mechanism by setting `container.security_updates` to `false`, but it is not recommended to do so. See {ref}`ref-ams-configuration`.

For security reasons, always keep your systems up-to-date at all times. To ensure this, snaps update automatically, and the snap daemon is by default configured to check for updates four times a day.

## Snap confinement

Since Anbox Cloud uses [snaps](https://snapcraft.io/), [Snap confinement](https://snapcraft.io/docs/snap-confinement) restricts the amount of access the applications have to system resources and provides an additional layer of security when creating applications and addons.

## Data security

The following table helps you understand how data related to you or provided by you is used within Anbox Cloud by various components.

| Component | Databases | Data stored|
|-----------|-----------|------------|
| LXD instances | Dqlite and SQLite | Information about instances, their management, authentication and certificates |
| AMS | etcd | Information about instance management and configuration, {ref}`custom user data <howto-pass-custom-data-application>` when explicitly provided |
| Anbox Stream Gateway | Dqlite | Session and management metadata, service account IDs that identify the web client |
| Anbox Cloud dashboard | SQLite | User emails that are used for authentication |

Services used by Anbox Cloud have configuration files that contain secrets. The secrets are automatically generated and managed by the respective charms or the appliance. The authentication methods used are further defined in {ref}`sec-cryptography` for managing secrets.

A charmed Anbox Cloud deployment contains the following configuration files that contain secrets:

`/var/snap/ams/common/server/settings.yaml`

`/var/snap/aar/common/conf/main.yaml`

`/var/snap/anbox-cloud-dashboard/common/service/config.yaml`

`/var/snap/anbox-stream-agent/common/agent/config.yaml`

`/var/snap/anbox-stream-gateway/common/service/config.yaml`

`/etc/turnserver.conf`

`/etc/coturn/auth_secret`

`/var/snap/nats/common/server/nats.cfg`

An Anbox Cloud Appliance deployment contains the following configuration files that contain secrets:

`/var/snap/anbox-cloud-appliance/common/daemon/config.yaml`

`/var/snap/anbox-cloud-appliance/common/telegraf/main.conf`

`/var/snap/anbox-cloud-appliance/common/agent/config.yaml`

`/var/snap/anbox-cloud-appliance/common/coturn/turnserver.conf`

`/var/snap/anbox-cloud-appliance/common/ams/server/settings.yaml`

`/var/snap/anbox-cloud-appliance/common/dashboard/config.yaml`

`/var/snap/anbox-cloud-appliance/common/nats/nats.cfg`

`/var/snap/anbox-cloud-appliance/common/gateway/config.yaml`

`/var/snap/anbox-cloud-appliance/common/config.yaml`

For the Anbox Stream Gateway, the secrets are stored in Juju relation data.

The data that you provide to your applications in Android is stored within the instance, for the duration of the instance.

## Related topics

- {ref}`howto-harden`

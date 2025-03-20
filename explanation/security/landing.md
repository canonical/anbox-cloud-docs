(exp-security)=
# Security

Anbox Cloud is designed using secure development practices - its architecture, components and all communication between components are designed to be fundamentally secure.

Anbox Cloud uses [LXD](https://ubuntu.com/lxd) for container and virtual machine management. To ensure security and isolation of each Android system, Anbox Cloud runs a single Android system per LXD instance.

This security guide gives more insight into how security is ensured through different aspects of Anbox Cloud.

## Secure communication between components

The architecture of Anbox Cloud has been designed in a way that ensures secure communication between all components.

All communication between services uses TLS encryption and authentication. Access is controlled through secure authentication tokens or temporary passwords. There are no insecure HTTP endpoints, but all HTTP communication is secured by TLS and happens over HTTPS.

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

(sec-cryptography)=
## Cryptography

This section provides details about the cryptographic technology used by Anbox Cloud and why they are used.

This information is currently available for the following components:

```{toctree}
:titlesonly:

crypto_ams
crypto_anbox_runtime
crypto_charms
crypto_dashboard
crypto_stream_agent
crypto_stream_gateway
```

## Instance security

Anbox Cloud uses secure and isolated system instances supplied by [LXD](https://ubuntu.com/lxd). LXD provides a high degree of flexibility when setting up instances, allowing you to run in a fully secure or less secure way, depending on your requirements. See [Security](https://documentation.ubuntu.com/lxd/en/latest/security/) in the LXD documentation for more information about how a LXD setup can be secured.

Using virtual machines to host Android containers provides better workload isolation. Thus, Anbox Cloud uses LXD in a way that enforces the highest security level.

### Unprivileged instances

```{note}
This section is particularly applicable for container based instances because a virtual machine is unprivileged by nature.
```

Many instance managers use privileged instances, which means that the instances have root privileges on the host system, including access to all devices. This is a security risk, because attackers could gain control over the host system.

Anbox Cloud uses unprivileged LXD instances only, which fully isolates the instances and ensures that they cannot gain root privileges. In addition, the Android container that runs inside the LXD instance also runs as an unprivileged instance. This method isolates the Android container twice, with the result that if the encapsulation of either the LXD instance or the Android container should fail, the system would still be protected.

```{caution}
While instances are fully isolated, all instances currently use the same GPU resources. As a result, any instance that is launched with GPU support could take all GPU resources in a DDoS-like attack, which would prevent other instances from starting.

Monitoring how the GPU resources are used for different applications and ensuring that you are running trusted workloads can provide insulation against DDoS-like attacks.

See {ref}`sec-gpu-slots` for more information.
```

### Secure communication with the Juju controller

All communication between Juju units and the Juju controller happens over TLS-encrypted websockets. The certificate for the TLS connection to the controller is added as explicitly trusted to each machine as part of the bootstrap process using a combination of cloud-init and SSH.

With this secure channel, Juju charms can communicate with each other using relation data. The data published by one unit is sent to the controller, which then makes it available for all other units on the same relation. The data for each relation is scoped by ID and is only visible to units participating in the specific relation on which it is set.

See [Security with Juju](https://canonical-juju.readthedocs-hosted.com/en/latest/user/explanation/juju-security/) for more information.

### Security updates

Anbox Cloud provides images that are frequently updated with the latest security patches. When an image is updated, all Anbox Cloud applications that use the image are automatically updated as well (unless disabled with `application.auto_update`,See {ref}`ref-ams-configuration`).

In addition, to ensure that the latest Ubuntu security patches are applied outside of image updates as well, Anbox Cloud checks for and installs available security updates every time an application is bootstrapped. So when you create an application, its underlying image is updated with the latest Ubuntu security patches. You can also create a new application version without other changes to bootstrap the application again, and thus install the latest security patches.

It is possible to turn off this update mechanism by setting `container.security_updates` to `false`, but it is not recommended to do so. See {ref}`ref-ams-configuration`.

For security reasons, always keep your systems up-to-date at all times. To ensure this, snaps update automatically, and the snap daemon is by default configured to check for updates four times a day.

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

## Android security

The images that Anbox Cloud provides are based on different Android versions. They are updated with security patches monthly, based on the upstream security tags. You can find detailed information on the security patches that have been included (or considered to be included but found unrelated) in the [Android Security Bulletins](https://source.android.com/docs/security/bulletin). The relevant security bulletin for each Anbox Cloud release is linked in the {ref}`ref-release-notes`.

See [Android Security Features](https://source.android.com/docs/security/features) in the Android documentation for an overview of security-related features that Android provides. Anbox Cloud supports some of these features, but not all of them. Some of the features rely on hardware that is not available in a virtual system, and others interfere with the Ubuntu security features.

The following table shows which Android security features are supported in Anbox Cloud.

| Security feature                           | Supported in Anbox Cloud |
|--------------------------------------------|:------------------------:|
| App sandbox                                | ✓                        |
| App signing                                | ✓                        |
| Authentication                             | -                        |
| Biometrics                                 | -                        |
| Encryption                                 | -                        |
| Keystore                                   | ✓                        |
| Security-Enhanced Linux (SELinux)          | -                        |
| Trusty Trusted Execution Environment (TEE) | -                        |
| Verified Boot                              | -                        |

### Security-Enhanced Linux (SELinux)

Currently, Anbox Cloud disables SELinux in Android. The reason for this is that SELinux conflicts with AppArmor, which is by default enabled in LXD. Anbox Cloud utilizes the security features provided by LXD and therefore relies on AppArmor instead of SELinux.

In future releases, it might be possible to run AppArmor and SELinux in parallel. In this case, the decision to disable SELinux will be reconsidered.

## Snap confinement

Since Anbox Cloud uses [snaps](https://snapcraft.io/), [Snap confinement](https://snapcraft.io/docs/snap-confinement) restricts the amount of access the applications have to system resources and provides an additional layer of security when creating applications and addons.

## Streaming security

The Anbox Cloud Streaming Stack is based on [WebRTC](https://webrtc.org/). WebRTC forbids unencrypted communication, which enforces a certain security level.

For communication with the Anbox stream gateway, token-based authentication is used. This allows components that need to communicate with the stream gateway to verify their identity, and in return receive a unique access token. During the life of the token, it acts as a means to verify the identity of the services that handle communication between the applications and the gateway.

Of course, the overall streaming security relies on a secure client implementation. This is ensured by Anbox Cloud's web dashboard, but other client implementations might have weaknesses. However, since encryption is a mandatory feature of WebRTC, developers are forced to consider security aspects when implementing a client application.

See [A Study of WebRTC Security](https://webrtc-security.github.io/) for a detailed discussion of security features in WebRTC.


## Related topics

- {ref}`howto-harden`

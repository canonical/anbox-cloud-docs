Anbox Cloud is secure by design, which means that its architecture, its components and all communication between components are designed to be fundamentally secure.

Anbox Cloud uses the secure [LXD](https://ubuntu.com/lxd) for container and virtual machine management. To ensure security and isolation of each Android system, Anbox Cloud runs a single Android system per LXD instance.

This security guide gives more insight into how security is ensured through different aspects of Anbox Cloud.

To report a security issue, contact the [Ubuntu security team](https://wiki.ubuntu.com/SecurityTeam/FAQ#Contact).

## Architecture

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

## Instance security

Anbox Cloud uses secure and isolated system instances supplied by [LXD](https://ubuntu.com/lxd). LXD provides a high degree of flexibility when setting up instances, allowing you to run in a fully secure or less secure way, depending on your requirements. See [Security](https://documentation.ubuntu.com/lxd/en/latest/security/) in the LXD documentation for more information about how a LXD setup can be secured.

Using virtual machines to host Android containers provides provides better workload isolation.

Anbox Cloud uses LXD in a way that enforces the highest security level.

### Unprivileged instances

[note type="information" status="Note"]This section is particularly applicable for container based instances because a virtual machine is unprivileged by nature.[/note]

Many instance managers use privileged instances, which means that the instances have root privileges on the host system, including access to all devices. This is a security risk, because attackers could gain control over the host system.

Anbox Cloud uses unprivileged LXD instances only, which fully isolates the instances and ensures that they cannot gain root privileges. In addition, the Android container that runs inside the LXD instance also runs as an unprivileged instance. This method isolates the Android container twice, with the result that if the encapsulation of either the LXD instance or the Android container should fail, the system would still be protected.

[note type="caution" status="Warning"]
While instances are fully isolated, all instances currently use the same GPU resources. As a result, any instance that is launched with GPU support could take all GPU resources in a DDoS-like attack, which would prevent other instances from starting.

See [GPU slots](https://discourse.ubuntu.com/t/about-capacity-planning/28717#gpu-slots) for more information.
[/note]

### Secure communication with the Juju controller

All communication between Juju units and the Juju controller happens over TLS-encrypted websockets. The certificate for the TLS connection to the controller is added as explicitly trusted to each machine as part of the bootstrap process using a combination of cloud-init and SSH.

With this secure channel, Juju charms can communicate with each other using relation data. The data published by one unit is sent to the controller, which then makes it available for all other units on the same relation. The data for each relation is scoped by ID and is only visible to units participating in the specific relation on which it is set.


### Security updates

Anbox Cloud provides images that are frequently updated with the latest security patches. When an image is updated, all Anbox Cloud applications that use the image are automatically updated as well (unless disabled with [`application.auto_update`](https://discourse.ubuntu.com/t/ams-configuration/20872)).

In addition, to ensure that the latest Ubuntu security patches are applied outside of image updates as well, Anbox Cloud checks for and installs available security updates every time an application is bootstrapped. So when you create an application, its underlying image is updated with the latest Ubuntu security patches. You can also create a new application version without other changes to bootstrap the application again, and thus install the latest security patches.

It is possible to turn off this update mechanism by setting [`container.security_updates`](https://discourse.ubuntu.com/t/ams-configuration/20872) to `false`, but it is not recommended to do so.

## Android security

The images that Anbox Cloud provides are based on different Android versions. They are updated with security patches monthly, based on the upstream security tags. You can find detailed information on the security patches that have been included (or considered to be included but found unrelated) in the [Android Security Bulletins](https://source.android.com/docs/security/bulletin). The relevant security bulletin for each Anbox Cloud release is linked in the [Release notes](https://discourse.ubuntu.com/t/release-notes/17842).

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

Currently, Anbox Cloud disables SELinux in Android. The reason for this is that SELinux conflicts with AppArmor, which is by default enabled in LXD. Anbox Cloud utilises the security features provided by LXD and therefore relies on AppArmor instead of SELinux.

In future releases, it might be possible to run AppArmor and SELinux in parallel. In this case, the decision to disable SELinux will be reconsidered.

## Streaming security

The Anbox Cloud Streaming Stack is based on [WebRTC](https://webrtc.org/). WebRTC forbids unencrypted communication, which enforces a certain security level.

Of course, the overall streaming security relies on a secure client implementation. This is ensured by Anbox Cloud's web dashboard, but other client implementations might have weaknesses. However, since encryption is a mandatory feature of WebRTC, developers are forced to consider security aspects when implementing a client application.

See [A Study of WebRTC Security](https://webrtc-security.github.io/) for a detailed discussion of security features in WebRTC.

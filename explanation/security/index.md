---
myst:
  html_meta:
    "description": "Explanation of security in Anbox Cloud, covering secure-by-default principles across AMS, the Anbox runtime, and streaming."
---

(exp-security)=
# Security

Anbox Cloud is built on secure development practices. Security principles are incorporated throughout the design of its architecture and components and the communication between them.

Anbox Cloud uses [LXD](https://canonical.com/lxd) for container and virtual machine management. To provide isolation between Android systems, Anbox Cloud runs a single Android system per LXD instance.

The following guides describe the security model and cryptographic technology used by each component:

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

Communication among Anbox Cloud services is secured with TLS for encryption and authentication. Access is controlled through mechanisms including TLS client certificates, authentication tokens, and temporary passwords. All HTTP communication takes place over HTTPS; Anbox Cloud does not expose insecure HTTP endpoints.

TLS and public-key encryption establish a chain of trust anchored to a shared root Certificate Authority (CA). When a cluster is being brought up or a new unit is added, the required certificates and chain of trust must be bootstrapped into the machines.

The following table shows the authentication methods used by each component.


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

## Cryptography

Anbox Cloud uses TLS and public-key cryptography to secure inter-component communication. For details about the cryptographic algorithms and key lengths used by each component, see the per-component security guides. For user-facing cryptographic controls such as TLS certificate replacement, external CA integration, and OIDC configuration, see {ref}`howto-set-up-tls`, {ref}`exp-security-charms`, and {ref}`exp-auth`.

## Security lifecycle

Anbox Cloud supports only the most recent release. Upgrades are supported from the immediately previous minor version (n-1) to the current version (n). See the {ref}`release and support policy <release-and-support-policy>` for the release cadence and roadmap.

To ensure you receive the latest security fixes, upgrade to each new release shortly after it is published.

### How security updates are delivered

Anbox Cloud delivers security updates through:

- **Anbox Cloud images**: Within a minor version, Anbox Cloud images are regularly updated with the latest security patches. When an image is updated, all Anbox Cloud applications using that image are automatically updated as well (unless disabled with `application.auto_update`, see {ref}`ref-ams-configuration`). Receiving patches for a new minor version requires an explicit upgrade of the deployment.
- **Instance bootstrap**: Anbox Cloud checks for and installs available Ubuntu security updates every time an application is bootstrapped. This means that when you create an application, its underlying image is updated with the latest Ubuntu security patches. You can also create a new application version without other changes to trigger a fresh bootstrap and install the latest patches. This mechanism can be disabled by setting `instance.security_updates` to `false`, but doing so is not recommended. See {ref}`ref-ams-configuration`.
- **Snap packages**: Snap updates are managed differently depending on the deployment type. In a charmed deployment, snaps are held at the installed version and upgraded only during a charm upgrade. In an appliance deployment, snaps update automatically; the snapd daemon checks for updates four times a day by default. See [Managing updates](https://snapcraft.io/docs/managing-updates).

For instructions on upgrading Anbox Cloud, see {ref}`howto-upgrade-appliance` and {ref}`howto-upgrade-anbox-cloud` depending on your deployment.

## Snap confinement

Since Anbox Cloud is packaged and distributed as [snaps](https://snapcraft.io/), [Snap confinement](https://snapcraft.io/docs/snap-confinement) restricts the access Anbox Cloud components have to host system resources, providing an additional layer of security.

## Data security

The following table helps you understand how data related to you or provided by you is used within Anbox Cloud by various components.

| Component | Databases | Data stored|
|-----------|-----------|------------|
| LXD instances | Dqlite and SQLite | Information about instances, their management, authentication and certificates |
| AMS | etcd | Information about instance management and configuration, {ref}`custom user data <howto-pass-custom-data-application>` when explicitly provided |
| Anbox Stream Gateway | Dqlite | Session and management metadata, service account IDs that identify the web client |
| Anbox Cloud dashboard | SQLite | User emails that are used for authentication |

Services used by Anbox Cloud have configuration files that contain secrets. The secrets are automatically generated and managed by the respective charms or the appliance. The authentication methods used for managing secrets are explained in the security topics.

The data that you provide to your applications in Android is stored within the instance, for the duration of the instance.

```{dropdown} Configuration files that contain secrets

**Charmed Anbox Cloud deployment:**

- `/var/snap/ams/common/server/settings.yaml`
- `/var/snap/aar/common/conf/main.yaml`
- `/var/snap/anbox-cloud-dashboard/common/service/config.yaml`
- `/var/snap/anbox-stream-agent/common/agent/config.yaml`
- `/var/snap/anbox-stream-gateway/common/service/config.yaml`
- `/etc/turnserver.conf`
- `/etc/coturn/auth_secret`
- `/var/snap/nats/common/server/nats.cfg`

**Anbox Cloud Appliance deployment:**

- `/var/snap/anbox-cloud-appliance/common/daemon/config.yaml`
- `/var/snap/anbox-cloud-appliance/common/telegraf/main.conf`
- `/var/snap/anbox-cloud-appliance/common/agent/config.yaml`
- `/var/snap/anbox-cloud-appliance/common/coturn/turnserver.conf`
- `/var/snap/anbox-cloud-appliance/common/ams/server/settings.yaml`
- `/var/snap/anbox-cloud-appliance/common/dashboard/config.yaml`
- `/var/snap/anbox-cloud-appliance/common/nats/nats.cfg`
- `/var/snap/anbox-cloud-appliance/common/gateway/config.yaml`
- `/var/snap/anbox-cloud-appliance/common/config.yaml`

For the Anbox Stream Gateway, the secrets are stored in Juju relation data.

```

## See also

How-to guide: 
- {ref}`howto-harden`
- {ref}`howto-decommission`

Reference: 
- {ref}`ref-security-policy`
- {ref}`ref-security-notices`
- {ref}`ref-release-notes`

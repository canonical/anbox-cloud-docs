---
myst:
  html_meta:
    "description": "Explanation of security in Anbox Cloud, covering secure-by-default principles across AMS, the Anbox runtime, and streaming."
---

(exp-security)=
# Security

Anbox Cloud is built on secure development practices. Its architecture, components, and all inter-component communication are designed to be fundamentally secure.

Anbox Cloud uses [LXD](https://canonical.com/lxd) for container and virtual machine management. To ensure security and isolation of each Android system, Anbox Cloud runs a single Android system per LXD instance.

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

The architecture of Anbox Cloud is designed to ensure secure communication among all components.

All communication among services uses TLS for encryption and authentication. Access is controlled through secure authentication mechanisms, including TLS client certificates, authentication tokens, and temporary passwords. There are no insecure HTTP endpoints; all HTTP communication is secured with TLS and takes place over HTTPS.

Secure communication relies on TLS and public-key encryption, with a chain of trust anchored to a shared root Certificate Authority (CA). When a cluster is being brought up or a new unit is added, the required certificates and chain of trust must be bootstrapped into the machines.

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

Anbox Cloud enforces TLS 1.2 or later for all inter-component communication, with most components enforcing TLS 1.3. Components use RSA 4096-bit keys, and users cannot reduce the minimum TLS version or weaken the cryptographic algorithms.

For details on the algorithms, key lengths, and cryptographic packages used by each component, see the per-component security guides linked above. For user-facing cryptographic controls such as TLS certificate replacement, external CA integration, and OIDC configuration, see {ref}`howto-set-up-tls`, {ref}`exp-security-charms`, and {ref}`exp-auth`.

## Security lifecycle

Anbox Cloud supports only the most recent release. Once a new minor release is published, the previous release receives only limited support for a short transition period. Upgrades are supported from the immediately previous minor version (n-1) to the current version (n). See the {ref}`release and support policy <release-and-support-policy>` for the release cadence and roadmap.

To ensure you receive the latest security fixes, upgrade to each new release shortly after it is published.

### How security updates are delivered

Anbox Cloud delivers security updates through:

- **Anbox Cloud images**: Updated with the latest security patches. When an image is updated, all Anbox Cloud applications using that image are automatically updated as well (unless disabled with `application.auto_update`, see {ref}`ref-ams-configuration`).
- **Instance bootstrap**: Anbox Cloud checks for and installs available Ubuntu security updates every time an application is bootstrapped. This means that when you create an application, its underlying image is updated with the latest Ubuntu security patches. You can also create a new application version without other changes to trigger a fresh bootstrap and install the latest patches. This mechanism can be disabled by setting `container.security_updates` to `false`, but doing so is not recommended. See {ref}`ref-ams-configuration`.
- **Snap packages**: Snaps update automatically. The snap daemon checks for updates four times a day by default.

### How to manually trigger updates

To manually trigger an update:

- **Appliance:** `sudo snap refresh anbox-cloud-appliance`. See {ref}`howto-upgrade-appliance`.
- **Charmed deployment:** `juju refresh` for each charm. See {ref}`howto-upgrade-anbox-cloud`.

### How to verify an update was applied

To check the currently installed version:

- **Appliance:** Run `anbox-cloud-appliance status` and check the version in the output.
- **Charmed deployment:** Run `juju status` and check the charm revision and workload version for each unit.
- **Images:** Run `amc image ls` and check the image version column.

## Snap confinement

Since Anbox Cloud uses [snaps](https://snapcraft.io/), [Snap confinement](https://snapcraft.io/docs/snap-confinement) restricts application access to system resources and provides an additional layer of security when creating applications and addons.

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

For the Anbox Stream Gateway, the secrets are stored in Juju relation data.

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
```

## Reporting vulnerabilities

If you discover a security vulnerability with Anbox Cloud, report it following the process described in the {ref}`ref-security-policy`. At a minimum, report a bug at <https://bugs.launchpad.net/anbox-cloud> and set the information type to *Private Security*.

The [Ubuntu Security disclosure and embargo policy](https://ubuntu.com/security/disclosure-policy) details what you can expect when you contact us and what we expect from you.

For information about known vulnerabilities and fixes, see {ref}`ref-security-notices`. Each Anbox Cloud release also includes a summary of security fixes in the {ref}`ref-release-notes`.

To stay informed about new releases and security updates, subscribe to the [Anbox Cloud category](https://discourse.ubuntu.com/c/anbox-cloud/49) on Ubuntu Discourse.

## See also

How-to guide: 
- {ref}`howto-harden`

Reference: 
- {ref}`ref-security-policy`
- {ref}`ref-security-notices`
- {ref}`ref-release-notes`

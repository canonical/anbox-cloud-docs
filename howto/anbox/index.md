---
myst:
  html_meta:
    "description": "How to manage an Anbox Cloud deployment, including authentication, remote AMS access, benchmarks, and security hardening."
---

(howto-manage-anbox)=
# Manage Anbox Cloud

The guides apply to both Anbox Cloud and Anbox Cloud Appliance installation.

## Access and permissions

AMS supports remote management over HTTPS with OpenFGA-based access control.

- {ref}`howto-access-ams-remote`
- {ref}`howto-auth`

## Security

Harden your deployment by restricting network exposure and replacing the appliance's default TLS certificate.

- {ref}`howto-harden`
- {ref}`howto-set-up-tls`

## Storage and performance

Resize storage pools, measure performance with benchmarks, or try alternative userspace schedulers.

- {ref}`howto-resize-lxd-storage`
- {ref}`howto-run-benchmarks`
- {ref}`howto-scx`


```{toctree}
:hidden:

control-ams-remotely
auth
harden
resize-storage
benchmarks
tls-for-appliance
scx
```

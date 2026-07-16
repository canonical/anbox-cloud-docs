---
myst:
  html_meta:
    "description": "How to manage Anbox Cloud instances, including creating, configuring, starting, stopping, accessing, and viewing logs."
---

(howto-instance)=
# Manage instances

Instances are the running workloads in Anbox Cloud. These guides walk you through creating, accessing and managing instances throughout their lifecycle.

## Create and manage instances

Instances can be created from applications or images, configured, copied, or removed as needed.

- {ref}`howto-create-instance`
- {ref}`howto-configure-instance`
- {ref}`howto-configure-geographic-location`
- {ref}`howto-list-instances`
- {ref}`howto-copy-instance`
- {ref}`howto-delete-instance`

## Control instance state

Start, stop, and restart instances, or wait for them to reach a ready state before proceeding.

- {ref}`howto-start-instance`
- {ref}`howto-wait-for-instance`
- {ref}`howto-stop-instance`
- {ref}`howto-restart-instance`

## Access and share instances

Access a running instance through a shell, inspect its logs, or share an active streaming session with other users.

- {ref}`howto-access-instance`
- {ref}`howto-view-instance-logs`
- {ref}`howto-share-session`

## Back up data and expose services

Back up application data across restarts and expose instance services to the external network.

- {ref}`howto-backup-restore-application-data`
- {ref}`howto-expose-services`

## See also

- Explanation: {ref}`exp-instances`

```{toctree}
:hidden:

create-instance
list-instances
configure-instance
access-instance
start-instance
wait-for-instance
share-session
stop-instance
restart-instance
copy-instance
view-instance-logs
delete-instance
backup-restore-application-data
configure-geographic-location
expose-services
```

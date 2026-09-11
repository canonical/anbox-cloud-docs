---
myst:
  html_meta:
    "description": "Managing Control Plane Members for elastic LXD cluster scaling"
---

(howto-manage-control-plane-members)=
# Manage control plane members

This guide shows how to assign, remove and check the `control-plane` role on LXD cluster members via Juju actions. See {ref}`sec-lxd-auto-scaling` for an explanation of control plane members and how they work.

## Assign or remove the control-plane role

Use the `set-control-plane` action on the `lxd` charm unit you want to designate (or remove) as a
control-plane member:

    juju run lxd/2 set-control-plane

This assigns the `control-plane` role to the LXD cluster member corresponding to unit `lxd/2`. To
remove the role instead:

    juju run lxd/2 set-control-plane enabled=false

The action reports whether control plane mode is currently active as part of its result, for example:

```
result: The 'control-plane' role was successfully assigned to lxd2. Control plane mode is not yet
  active: at least 3 members must be assigned the 'control-plane' role for it to take effect.
roles: '["control-plane", "database-leader"]'
```

Repeat the action against additional units until at least 3 members have been assigned the role for control plane mode to activate.

## List current control-plane assignments

To check the roles currently assigned to all cluster members, and whether control plane mode is active, run the `list-control-plane` action against any `lxd` unit:

    juju run lxd/0 list-control-plane

This returns the full list of cluster members together with their roles (for example `control-plane`, `database-leader`, `database-voter`, `database-standby`) and status, plus a
`control-plane-mode-active` flag, for example:

    control-plane-mode-active: "True"
    members:
      lxd2:
          roles: control-plane, database-leader
          status: Online
      lxd3:
          roles: control-plane, database-voter
          status: Online
      lxd4:
          roles: ""
          status: Online
      lxd5:
          roles: control-plane, database-voter
          status: Online


## Check the role via `juju status`

Units that are currently assigned the `control-plane` role also show this in their status line in `juju status lxd`:

    App  Version      Status  Scale  Charm  Channel  Rev  Exposed  Message
    lxd  6.9-ab8fad2  active      4  lxd               2  no       Cluster role: control-plane

    Unit    Workload  Agent  Machine  Public address  Ports     Message
    lxd/2   active    idle   5        10.165.203.149  8443/tcp  Cluster role: control-plane
    lxd/3   active    idle   6        10.165.203.250  8443/tcp  Cluster role: control-plane
    lxd/4*  active    idle   7        10.165.203.122  8443/tcp
    lxd/5   active    idle   8        10.165.203.244  8443/tcp  Cluster role: control-plane

    Machine  State    Address         Inst id        Base          AZ         Message
    5        started  10.165.203.149  juju-a27a2a-5  ubuntu@24.04  charm-env  Running
    6        started  10.165.203.250  juju-a27a2a-6  ubuntu@24.04  charm-env  Running
    7        started  10.165.203.122  juju-a27a2a-7  ubuntu@24.04  charm-env  Running
    8        started  10.165.203.244  juju-a27a2a-8  ubuntu@24.04  charm-env  Running

This message is only shown when the unit has no other higher-priority status to report (for example, it is hidden while `Actions: Reboot Required` is shown for the unit) and updates immediately after running `set-control-plane` `update-status` hook.

## Using control-plane members with autoscaling

When planning an autoscaling setup (see {ref}`howto-scale-up-cluster` and {ref}`howto-scale-down-cluster`), assign the `control-plane` role to your fixed set of "always on" members before scaling the rest of the cluster elastically. Never remove a unit that has the `control-plane` role assigned without first reassigning the role to a different member, to avoid unexpectedly deactivating control plane mode.

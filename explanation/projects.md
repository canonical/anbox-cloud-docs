---
myst:
  html_meta:
    "description": "Explanation of projects in Anbox Cloud, covering tenant boundaries, the default project, project authorization and network isolation."
---

(exp-projects)=
# Projects

Projects introduce a native mechanism to group instances by tenant boundaries within an Anbox Cloud deployment. A project is a scope that provides access control for its instances through entitlements and entitlement sets and hypervisor-level network isolation from the instances in other projects.

## Why projects exist

Before projects, all instances shared a common network bridge (`amsbr0`) and a global permission scope. This made multi-tenant isolation difficult to enforce.

Projects allow users to group workloads according to their intended purposes and establish separate access and network boundaries for those workloads.

A project in Anbox Cloud acts as a scope with two boundaries:

1. Clear object ownership and access: Every instance belongs to one project. The project defines the scope for managing access to its instances. A user must belong to a group with access to the project it is in before the group's direct instance entitlements can apply.
1. Network isolation: Each project uses a LXD-managed network. Instances connect to their project's network, which is isolated from other project networks by default.

## The default project

AMS comes with a pre-defined, immutable `default` project that users cannot edit or delete. If no project is specified when launching an instance, AMS places it in the `default` project. Instances that existed before projects were introduced are assigned to the `default` project during upgrade.

The `default` project preserves the networking that existed before projects. It uses a fixed address `192.168.100.1/20` that maps to a special network bridge `amsbr0` on LXD. Its bridge mapping cannot be changed.

## Authorization model

Project access is granted to groups through entitlements and entitlement sets. Newly created groups have no project access until an administrator grants it.

Access to an instance depends on the access to the project it is in. A group must have the `can_view` entitlement on that project before it can use any entitlements granted directly on the instance.

A project provides two entitlement sets:

- `viewer` grants read-only access. It allows users to view the project details, list and view its instances.
- `editor` grants read-write access. It includes `viewer` access and allows users to create, update and delete instances, run commands and view instance logs.

The `editor` entitlement set does not grant access to edit or delete the project itself. These operations require the `can_edit` and `can_delete` entitlements, respectively, on that project. Administrator access also allows these operations, except on the `default` project.

On a new deployment, only the `admin` group initially has access to `default`. An administrator can grant other groups access.

When you upgrade from a release that predates projects, AMS grants existing groups `can_view` on `default` so their existing instance entitlements continue to work. Groups that previously had permission to create instances across the deployment receive `can_create_instances` on `default`.

To create projects, users need administrator access or the global `can_create_projects` entitlement. Refer to the {ref}`global entitlements list <ref-auth>`.

## Network traffic

Since a project forces stronger network isolation, a project has the following network properties:

- Within a project: network traffic between instances within a project is unrestricted. In 1.31.0, communication is supported only between instances running on the same node.
- Between projects: traffic between projects is denied by default. The `default` project is an exception: it can be reached from any other project in the system.
- Outbound to the internet: traffic from any instance within a project to the internet is allowed.
- Inbound traffic: for non-default projects, traffic from the internet to instances is denied by default.

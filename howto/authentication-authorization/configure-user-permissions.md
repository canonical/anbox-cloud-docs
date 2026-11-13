---
myst:
  html_meta:
    "description": "How to configure user permissions in Anbox Cloud with OpenFGA, including identities, groups, and entitlements."
---

(howto-auth)=
# Configure user permissions

Configure which resources users can access and which operations they can perform using the CLI or the dashboard.

To give a user access, assign the required entitlements to a group and add the user's identity to that group.

For an overview, see {ref}`exp-auth`. For the available entitlements, see {ref}`Reference: Authentication and authorization <ref-auth>`.

OpenFGA must be configured before assigning permissions.

## Configure OpenFGA

```{important}
In the Anbox Cloud Appliance, OpenFGA is preconfigured and the steps in this section can be skipped.
```

Anbox Management Service (AMS) requires a store ID in OpenFGA to manage authorization data. To generate a store ID in OpenFGA, follow the steps in the [OpenFGA documentation](https://openfga.dev/docs/getting-started/create-store) and create a store.

When you have a store ID, run these commands to configure AMS:

```
amc config set openfga.api.url '<URL of your OpenFGA instance>'
amc config set openfga.store.id '<store id of the user created store>'
```

Optionally, you can also configure the API token if your deployment setup will require authentication for API access to OpenFGA:

    amc config set openfga.api.token '\<api token generated from OpenFGA\>'

When the API URL and store ID are set, AMS starts synchronizing the data with OpenFGA. You might see some authorization failures initially till the synchronization completes.

```{important}
For fine-grained permissions to work in Anbox Cloud Dashboard, OpenFGA must be used in conjunction with a configured OIDC provider. Follow the instructions in {ref}`howto-set-up-idp` to configure Auth0, Keycloak, or Ory Hydra.
```

## Configure access

Follow the workflow for your chosen interface.

::::{tab-set}
:::{tab-item} CLI
:sync: cli

(sec-create-identity)=
### Create identities

To create an OIDC identity, run:

    amc auth identity create oidc/test@example.com

To create a TLS identity, provide its client certificate:

    cat client.crt | amc auth identity create tls/test-user

{ref}`The security explanation on AMS <exp-security-ams>` provides information about TLS-based and token-based authentication methods. See {ref}`howto-access-ams-remote` for instructions on connecting to AMS remotely.

You can view the identities you created by using:

    amc auth identity ls

The output will look similar to this:

```{terminal}
:user: user
:host: host

amc auth identity ls

+--------------------+---------------------+----------------------+----------------------+--------------+
|    ID                | AUTHENTICATION TYPE |      NAME          |     IDENTIFIER       |    GROUPS    |
+----------------------+---------------------+------------------+------------------------+--------------+
| d3kb9pvriueuguose410 | oidc                | test@example.com   | test@example.com     | image_viewer |
+----------------------+---------------------+-------------------------+----------------------+---------+
| d3o2u7vriuenvvlfcae0 | tls                 | test-user          | 9cbb1aced3fb587405c7abaa7c83ec59b4bb9bd567843703884632e77e0aa455 |   |
+----------------------+---------------------+-----------------------+--------------------+-------------+
```

Use the identity ID in the group-membership commands below.

### Create authorization groups with identities

Create a group and add the identities that should receive its access.

#### Create groups

Create a new authorization group:

    amc auth group create developer

To verify details of the created group, use the `show` command:

```{terminal}
:user: user
:host: host

amc auth group show developer

name: developer
created-at: 2025-10-17 12:06:33 +0530 IST
updated-at: 2025-10-17 12:06:33 +0530 IST
identities: []
permissions: []
immutable: false
```

#### Add identities to the group

Add an identity using its ID from `amc auth identity ls`:

    amc auth identity group add d3o2u7vriuenvvlfcae0 --groups 'developer'

Replace the example ID with the identity that needs access.

Use the `show` command to verify that the identity was added.

```{note}
A newly created group has no project access until the required entitlements are assigned. Assign them in the following section.
```

### Assign permissions

Choose the grants required for the group's tasks. The examples below are alternatives. You do not need to run all of them.

#### Grant global permissions

Global entitlements are assigned on the `server` resource. To grant global administrative access, run:

    amc auth group permission add developer server --permissions admin

To allow the group to create projects, run:

    amc auth group permission add developer server --permissions can_create_projects

#### Grant resource-level permissions

Specify the group, resource type, resource identifier and required entitlements:

    amc auth group permission add <group_name> <resource_type> <resource_id> --permissions <entitlements>

For example, to provide read and edit access to a particular LXD node (`lxd0`) to the developer group, run:

    amc auth group permission add developer node lxd0 --permissions "can_view,can_edit"

Use this command structure for other resource types.

```{important}
For entitlements granted directly on an instance, the same group must also have `can_view` on the project it is in. Grant that project access first (see {ref}`sec-grant-project-access`), then assign the required instance entitlements.
```

(sec-grant-project-access)=
#### Grant access to a project and its instances

To grant read-only access to a project and its instances, run:

    amc auth group permission add developer project <project_name> --permissions viewer

Use `editor` for additional instance operations. For details, see {ref}`Authorization model <sec-project-authorization>`.

#### View permissions

As the administrator, check the group's membership and assigned permissions:

    amc auth group show developer

Then authenticate using an identity in the group. Users can view their current permissions with:

    amc auth permission ls

### Revoke access

Revoke access by removing permissions from a group or removing an identity from the group.

#### Remove permissions

To revoke the global admin entitlement, run:

    amc auth group permission delete developer server --permissions admin

To revoke an entitlement on a resource, run:

    amc auth group permission delete <group_name> <resource_type> <resource_id> --permissions <entitlement>

#### Remove an identity from the group

To remove an identity from an authorization group, run:

    amc auth identity group delete <identity_id> --groups developer

Check access again after removing a grant or group membership. Other grants or group memberships may still provide access.
:::

:::{tab-item} Dashboard
:sync: dashboard

### Create an identity

The **Permissions > Identities** page displays the identities that the currently logged-in user is authorized to view.

To create an identity from this page:

1. Click *Create identity*.
2. Select the *Authentication method*:
   - OIDC: Enter the identity name and email address.
   - TLS: Enter the identity name and provide the client certificate.
3. Click *Create* to confirm.

To manage an identity’s group memberships, click *Groups count* or *Manage groups* ( ![manage groups icon](/images/icons/manage-groups-icon.png) ). This opens the *Change groups* panel, which lists all groups that the logged-in user is authorized to view. Select or deselect groups as needed, then confirm with *Save changes*.

Authorized users can delete other identities. However, logged-in users cannot delete their own identity.

### Create a group

On the **Permissions > Groups** page, follow these steps to create a group:

1. Click *Create group* to open the *Create group* panel.
2. Enter a group name and, optionally, a description.
3. (Optional) Add identities:
   - Click *Add identities*. The *Add identities* panel displays all identities that the logged-in user is authorized to view. Identities that the user is not authorized to edit are disabled.
   - Select from the available identities to add them to the group.
4. (Optional) Add permissions:
   - Click *Add permissions*.
   - Select a *Resource type*.
   - Select a *Resource* (only resources you are authorized to view are listed).
   - Select the *Entitlement* for that resource type.
   - Click *Add* to add the permission.
   - Added permissions are listed in the table and are not applied to the group yet. You can remove them or add more permissions as needed.
5. When you are finished configuring the group, confirm with *Create group*.

```{note}
The *Server* resource type does not have an associated resource. When creating permissions for the *Server* resource type, no resource selection is required and the field remains disabled.
```

To grant a group access to a project and its instances, select the *Project* resource type, the target project and the `viewer` or `editor` entitlement set. The entitlement set applies to all existing and future instances in the project, so you do not need to grant access to each instance separately.

Access to an individual instance depends on access to the project it is in. If you grant a group entitlements directly on an instance, the group must also have at least `can_view` on the project that contains the instance. The group does not need to have the same entitlement on both resources.

For more information, see {ref}`Authorization model <sec-project-authorization>`.

To manage group membership, click *Identities count* or *Edit* to add or remove identities from the group.

To manage group permissions, click *Permissions count* or *Edit* to add or remove permissions assigned to the group.

Authorized users can also delete groups. The admin group is immutable and cannot be deleted or have its permissions changed. However, the identities of the admin group can be edited.

```{important}
Permission changes to groups the logged-in user belongs to take effect immediately in the dashboard.
```

:::
::::

## Related topics 

- {ref}`Explanation: Authentication and authorization <exp-auth>`
- {ref}`Reference: Authentication and authorization <ref-auth>`
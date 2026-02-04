(howto-auth)=
# Configure user permissions

To be able to configure user permissions in Anbox Cloud, you need to first configure OpenFGA.

::::{tab-set}
:::{tab-item} CLI
:sync: cli

## Configure OpenFGA

```{important}
In the Anbox Cloud Appliance, OpenFGA is pre-configured and the steps in this section can be skipped.
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
(sec-create-identity)=
## Create identities

To create an OIDC identity, run:

    amc auth identity create oidc/test@example.com

To create a TLS identity, run:

    cat client.crt | amc auth identity create tls/test-user

{ref}`The security explanation on AMS <exp-security-ams>` provides information about TLS based and token based authentication methods. See {ref}`howto-access-ams-remote` for understanding how to connect to AMS remotely.

You can view the identities you created by using:  

    amc auth identity ls

The output will look similar to this:
```{terminal}
   :input: amc auth identity ls
   :user: user
   :host: host
`+--------------------+---------------------+----------------------+----------------------+--------------+`
`|    ID                | AUTHENTICATION TYPE |      NAME          |     IDENTIFIER       |    GROUPS    |`
`+----------------------+---------------------+------------------+------------------------+--------------+`
`| d3kb9pvriueuguose410 | oidc                | test@example.com   | test@example.com     | image_viewer |`
`+----------------------+---------------------+-------------------------+----------------------+---------+`
`| d3o2u7vriuenvvlfcae0 | tls                 | test-user          | 9cbb1aced3fb587405c7abaa7c83ec59b4bb9bd567843703884632e77e0aa455 |   |`
`+----------------------+---------------------+-----------------------+--------------------+-------------+`
```

## Create authorization groups with identities

### Create groups

Create a new authorization group:

    amc auth group create developer

To verify details of the created group, use the `show` command:

```{terminal}
   :input: amc auth group show developer
   :user: user
   :host: host
name: developer
created-at: 2025-10-17 12:06:33 +0530 IST
updated-at: 2025-10-17 12:06:33 +0530 IST
identities: []
permissions: []
immutable: false
```

### Add identities

Notice that there are currently no identities added to the group yet. The next step is to add an identity to the authorization group:

    amc auth identity group add d3o2u7vriuenvvlfcae0 --groups 'developer'

Use the `show` command and verify if the identity was added.

### Remove identity from a group

If you want to remove a particular identity from an authorization group, run:

    amc auth identity group delete d3o2u7vriuenvvlfcae0 --groups 'developer'

## Assign permissions

### Grant permissions

To assign server administrative permissions to the developer group you created, run:

    amc auth group permissions add developer server --permissions admin

To verify the access of the developer group, run:

    amc auth group show developer

The developer group should have `admin` permissions now. If your identity does not have access to the `developer` group, the command will notify you that you are unauthorized to do this operation.

You can set permissions at the object level too. For example, to provide read and edit access to a particular LXD node (`lxd0`) to the developer group, run:

    amc auth group permissions add developer node lxd0 --permissions "can_view,can_edit"

### Remove permissions

To revoke the global admin permission, run:

    amc auth group permissions delete developer server --permissions admin
:::

:::{tab-item} Dashboard
:sync: dashboard

Anbox Cloud Dashboard allows you to manage identities and their access through groups and permissions.

## Identities

The dashboard does not support creating identities. Instead, it displays the identities that the currently logged-in user is authorized to view on the **Permissions > Identities** page.

To manage an identity’s group memberships, click *Groups count* or *Manage groups* ( ![manage groups icon](/images/icons/manage-groups-icon.png) ). This opens the *Change groups* panel, which lists all groups that the logged-in user is authorized to view. Select or deselect groups as needed, then confirm with *Save changes*.

Authorized users can delete other identities. However, logged-in users cannot delete their own identity.

## Groups

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

To manage group membership, click *Identities count* or *Edit* to add or remove identities from the group.

To manage group permissions, click *Permissions count* or *Edit* to add or remove permissions assigned to the group.

Authorized users can also delete groups. The admin group is immutable and cannot be deleted or have its permissions changed. However, the identities of the admin group can be edited.

```{important}
Permission changes to groups the logged-in user belongs to take effect immediately in the dashboard.
```
:::
::::

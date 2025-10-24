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
Anbox Management Service(AMS) requires a store ID in OpenFGA to manage authorization data. To generate a store ID in OpenFGA, follow the steps in the [OpenFGA documentation](https://openfga.dev/docs/getting-started/create-store) and create a store. 

When you have a store ID, run these commands to configure AMS:

```
amc config set openfga.api.url '<URL of your OpenFGA instance>'
amc config set openfga.store.id '<store id of the user created store>'
```

Optionally, you can also configure the API token if your deployment setup will require authentication for API access to OpenFGA:

    amc config set openfga.api.token '\<api token generated from OpenFGA\>'

When the API URL and store ID are set, AMS starts synchronizing the data with OpenFGA. You might see some authorization failures initially till the synchronization completes.

## Create identities

To create an OIDC identity, run:

    amc auth identity create oidc/test@example.com

To create a TLS identity, run:

    cat client.crt | amc auth identity create tls/test-user

See {ref}`howto-access-ams-remote` for understanding how to connect to AMS remotely.

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

    amc config show  

The developer group should have `admin` listed in the permissions.

To provide read and edit access to a particular LXD node (`lxd0`) to the developer group, run:

    amc auth group permissions delete developer node lxd0 --permissions "can_view,can_edit"

### Remove permissions

To revoke the global admin permission, run:

    amc auth group permissions delete developer server --permissions admin
:::

:::{tab-item} Dashboard
:sync: dashboard

If you are using the web dashboard, the *Permissions* section help you to view and manage your identities, groups and their associated permissions.

Note that the authorization actions that can be performed through the dashboard are currently limited as compared to that of the CLI. Subsequent releases will bring feature parity between dashboard and the CLI.

:::
::::

The `cluster` command allows management of cluster members for the Anbox Cloud Appliance. Using this command, you can join additional nodes to an existing installation or to remove existing nodes from a cluster.

See [How to join a machine to the Anbox Cloud Appliance](https://discourse.ubuntu.com/t/29054) for more information.

    anbox-cloud-appliance cluster <subcommand>

## Subcommands

### `add`

Adds a new member to the cluster

    anbox-cloud-appliance cluster add <member-name>

### `remove`

Removes a member from the cluster

    `anbox-cloud-appliance cluster remove <member-name> <options>`

#### Options

 `--force` to force remove members on non interactive terminals

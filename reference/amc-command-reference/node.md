The `node` command manage LXD nodes of the deployment that run instances with Anbox Cloud and are managed by the Anbox Management Service (AMS). See https://discourse.ubuntu.com/t/17765 for more information.

    amc node <subcommand>

## Subcommands

The following subcommands are available:

### `add`

Add a node to AMS. You can also use the alias `new`.

    amc node add <node_name> <node_ip_address> [options]

There are a few prerequisites for the adding a node:

* The new node must have an accessible IP address.
* LXD must be installed on the node before adding it but not initialised because AMS takes care of the initialisation and configuration of the node.

The following options are available:

| Option | Input type | Description |
|--------|------------|-------------|
|`-h`, `--help` |  | Displays help information for the command |
| `--network`| String | Name of the network device to create on the LXD cluster. The default value is `amsbr0` |
| `--network-bridge-mtu` | Integer | Maximum Transmission Unit of the network bridge that is configured for LXD |
| `--network-subnet` | String | Network subnet for the network device on the node (default '192.168.100.1/20') |
| `--storage-device` | String | Storage device that the LXD node should use |
| `--storage-pool` | String | Existing LXD storage pool to use |
| `--tags` | String | Comma-separated list of tags to set for the node |
| `--trust-password` | String | Trust password for the remote LXD node |
| `--unmanaged` | | Indicates that the node is already clustered |


### `list`

List available nodes. You can also use `ls` as an alias.

    amc node list [options]

The following options are available:

| Options | Description |
|---------|-------------|
|`-f`, `--filter`| Filters the output based on specified conditions |
| `--format` | Controls output formatting. The output format can be `table`, `json` or `csv` and the default value is `table` |
| `-h`, `--help` | Displays help information for the command |

Usage for `--filter`:

        amc node list --filter attribute=value

where `attribute` can be one of the following:

|     Name      |       Argument type           |
|---------------|-------------------------------|
|<!-- wokeignore:rule=master --> master        | Boolean (true/false)          |
| status        | string (online, offline etc.) |


### `remove`

Removes a node from the Anbox Cloud cluster thereby making it unable to host instances.

[note type="information" status="Note]You cannot delete a node with running instances unless you use the `--force` flag.[/note]

    amc node remove <node_name> [options]

The following options are available:

| Options | Description |
|---------|-------------|
| `-f`, `--force` | Forcibly removes the node |
| `-h`, `--help`  | Displays help information for the command |
| `--keep-in-cluster` | Removes the LXD node from the AMS database but keeps it as part of the cluster |
| `-y`, `--yes` | Run non interactively by assuming 'yes' for all prompts |


### `set`

Set specific configuration for a node. See [AMS configuration](https://discourse.ubuntu.com/t/20872) for a list of available configuration items.

    amc node set <node_name> <config_item_name> <config_item_value> [options] --timeout=10m

where `-t` or --`timeout` is a string value to indicate the maximum wait time for the operation to complete. The default value is `5m`.

### `show`

Display information about a node.

    amc node show <node_name> [options]

The following options are available:

| Option | Description |
|--------|-------------|
| `--allocations` | Shows resource allocations |
|`-f`, `--format` | Controls output formatting with values `json` or `yaml`. The default value is `yaml`. |
| `-h`, `--help` | Displays help information for the command |

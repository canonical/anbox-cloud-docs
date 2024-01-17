The `addon` command allows you to manage addons that are necessary for customising images.

    amc addon <subcommand>

## Subcommands

### `add`
Create an addon from the contents of the provided directory, tarball or zip archive. See how to [create an addon](https://discourse.ubuntu.com/t/40632) or [create an addon tutorial](https://discourse.ubuntu.com/t/create-an-addon/25284) for more information.

    amc addon add <addon_name> (<directory> | <tarball> | <zip archive>) --timeout=3m

where `-t` or --`timeout` is a string value to denote the maximum wait time for the operation to complete. The default is `5m`.

### `delete`
Delete the specified addon.

    amc addon delete <addon_name> [options]

The following options are available:

|Option|Description|
|------|-----------|
|`-h`, `--help`| Display help information for the command. |
|`-t`, `--timeout`| String value to denote the maximum wait time for the operation to complete. The default is `5m`. |
|`-v`, `--version`| Indicates the version of the application for which the addon needs to be deleted. If a version is not mentioned, the addon is deleted for all versions of an application. |
|`-y`, `--yes`| Option for non interactive deletion, assuming 'yes' as an answer to all prompt. |

### `list`
List available addons along with its application details.

    amc addon list --format=(table | json |csv)

where `--format` option controls the output format which can be in the form of a table, JSON or CSV. The default value is `table`.

### `show`
Display information about a specific addon, including its size and created timestamp.

    amc addon show <addon_name> --format=(json | yaml)

where `--format` option controls the output format which can be either JSON or YAML. The default value is `yaml`.

### `update`
Update an existing addon

    amc addon update <addon_name> <addon_path> --timeout=3m

where `-t` or `--timeout` is a string value to denote the maximum wait time for the operation to complete. The default is `5m`.

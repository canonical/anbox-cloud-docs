---
orphan: true
---
# `application`

The `application` command allows you to manage applications using the Anbox Management Client (AMC).

    amc application <subcommand>

You can also use the alias `app` instead of `application`.

## Subcommands

The following subcommands are available:

### `create`

Create an application from the contents of the directory, tarball or zip archive.

    amc application create <app_name> (<directory> | <tarball> | <zip archive>) [options]

The following options are available:

|Option|Description|
|------|-----------|
|`-h`, `--help`| Display help information for the command. |
|`-t`, `--timeout`| String value to denote the maximum wait time for the operation to complete. The default is `5m`. |
|`--vm`| Create an application using virtual machines instead of containers. |

### `delete`

Delete the specified application.

    amc application delete <app_name> [options]

The following options are available:

|Option|Description|
|------|-----------|
|`-a`, `--all`| Delete all existing applications. |
|`-f`, `--force`| Force deletes of the application even if it is immutable. Applications downloaded from the registry cannot be deleted unless this flag is used. |
|`-h`, `--help`| Displays help information for the `delete` command. |
|`--no-wait`| Indicates not to wait for the delete operation to finish. |
| `-t`, `--timeout`| String value that denotes the maximum wait time for the operation to complete. The default is `5m`. |
| `-v`, `--version`| Displays the version of the application that needs to be deleted. If a version is not mentioned, the addon is deleted for all versions of an application. |
|`-y`, `--yes`| Option for non interactive deletion, assuming 'yes' as an answer to all prompt. |

### `list`

List all available applications. You can apply filters to see a specific list of applications.

    amc application list [options]

You can use the alias `ls` instead of `list`.

The following options are available:

|Option|Description|
|------|-----------|
|`-f`, `--filter` | Filters the output based on specified attributes. The attributes can be one of these: <br/>* `instance-type=(comma-separated list)` <br/>* `addons=(comma-separated list)` <br/>* `tags=(comma-separated list)` <br/>* `published=(true/false)` <br/>* `immutable=(true/false)` <br/>* `status=(string)` <br/>* `vm=(true/false)`|
|`--format`| String value that controls the output format which can either be in a table form, JSON, YAML or CSV. The default value is `table`. |
|`-h`, `--help`| Displays help information for the `list` command. |

### `publish`

Publish a version of the application. When an application is launched, AMS always uses the published version of the application unless otherwise mentioned.

    amc application publish <app_name> <version> --timeout=3m

where `-t` or --`timeout` is a string value to denote the maximum wait time for the operation to complete. The default is `5m`.

### `revoke`

Revoke a published application version.

    amc application revoke <app_name> <version> --timeout=3m

where `-t` or --`timeout` is a string value to denote the maximum wait time for the operation to complete. The default is `5m`.

### `set`

Update specific attributes of an application's manifest without creating a new version of the application.

    amc application set <app_name> <field> <field_value>

You can update the following fields:

* `image`
* `addons`
* `tags`
* `inhibit-auto-updates`
* `resources.cpus`
* `resources.memory`
* `resources.disk-size`
* `resources.gpu-slots`
* `resources.vpu-slots`
* `boot-activity`
* `features`
* `hooks.timeout`
* `bootstrap.keep`
* `node-selector`
* `watchdog.disabled`
* `watchdog.allowed-packages`

### `show`

Display information about an application and its versions.

    amc application show <app_name> --format=json

where `--format` controls the output formatting. The values for `--format` can be `json` or `yaml`. The output displays in YAML format by default if a format is not specified.

### `unset`

Reset an attribute of an application's manifest to its default value.

    amc application unset <app_name> <field>

You can reset the following attributes:

* `tags`
* `addons`
* `features`

For resetting any other attribute, use the `amc application set` command and specify the attribute value.

### `update`

Update an existing application. Updating an application creates a new version.

    amc application update <app_name> <package_path> --timeout=10m

where `-t` or --`timeout` is a string value to denote the maximum wait time for the operation to complete. The default is `5m`.

If you don't provide a package for the update, AMS checks all possible updates by verifying the application against newer images and addons and applies pending changes as necessary.

If you prefer specific updates to your application, use the `amc application set` command instead as it allows you to update specific fields of the application without updating the application.

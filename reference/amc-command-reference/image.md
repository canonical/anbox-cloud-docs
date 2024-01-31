The `image` command manages images that contain everything necessary to properly run an Android application in an instance.

Images can be provided manually or via an image server. You can add, update or
delete them from AMS. See https://discourse.ubuntu.com/t/24185 and
https://discourse.ubuntu.com/t/17758 for more information.

    amc image <subcommand>

## Subcommands

The following subcommands are available:

### `add`

Add an image. The first image that you add is marked as the default image. This default image is used when creating an application or launching a raw container without specifying an image. To set any image added after the first image as the default, add the '--default' flag.

    amc image add <image_name> <image_path> [options]

The following options are available:

|Option|Description|
|------|-----------|
| `-d`, `--default` | Marks the specified image as the default image |
| `-h`, `--help` | Displays help information for the command |
| `-t`, `--timeout` | String value that indicates the maximum time to wait for the operation to complete. The default value is `5m`. |
| `--type` | String value that denotes the type of image to import. Use only when a remote image is added. Valid values for this option are `any`, `container`, `vm`. `any` is the default value. |

### `delete`

Delete an image. When an image is deleted, all of its versions are removed unless otherwise specified.

    amc image delete <image_name> [options]

The following options are available:

|Option|Description|
|------|-----------|
| `-f`, `--force` |  Forcibly deletes immutable images |
| `-h`, `--help` | Displays help information for the command |
| `-t`, `--timeout` |  String value that indicates the maximum time to wait for the operation to complete. The default value is `5m`. |
| `-v`, `--version` | Integer that indicates the version of the image to delete |
| `-y`, `--yes` | Runs non interactively assuming `yes` for all prompts |

### `list`

List all available images.

    amc image list --format=json

where `--format` controls the output formatting. Valid values are `table`, `json` or `csv` and the default value is `table`.

You can use the alias `ls` instead of `list`.

### `show`

Display information about an image

    amc image show <image_name> --format=json

where `--format` controls the output formatting. The values for `--format` can be `json` or `yaml`. The output displays in YAML format by default if a format is not specified.

### `switch`

Set the default image. The default image is used when creating an application that does not have an image specified in the application manifest, or when launching a raw instance.

    amc image switch <image_name>

### `sync`

Synchronises the image with the remote image server. If the image is used from a remote image server, this command triggers explicit sync with the remote server and the image is downloaded to the cluster from the remote server.

    amc image sync <image_name>

### `update`

Update an existing image. This command replaces the specified image with the new image and bumps its version number.

    amc image update <image_name> <image_path>

The following options are available:

|Option|Description|
|------|-----------|
|`-d`, `--default` | Marks the image as the default image |
| `-h`, `--help` | Displays help information for the command |
|`-t`, `--timeout` |  String value that indicates the maximum time to wait for the operation to complete. The default value is `5m`. |

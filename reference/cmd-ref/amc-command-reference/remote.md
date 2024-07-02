---
orphan: true
---
# `remote`

The `remote` command allows interacting with remote Anbox Management Service (AMS) daemons. See {ref}`howto-access-ams-remote` for more information.

    amc remote <subcommand>

## Subcommands

The following subcommands are available:

### `add`

Add a remote AMS daemon. Note that if you set up a trust password on the daemon, provide the password when running the command.

    amc remote add <remote_name> <remote_url> [trust_password] --accept-certificate

where `--accept-certificate` is to implicitly accept the remote server certificate.

### `list`

List registered remotes. You can also use the alias `ls`.

    amc remote list --format=json

where `--format` is to control output formatting. The valid values are `table`, `json` and `csv`. The default format is `table`.

### `remove`

Remove a registered remote.

    amc remote remove <remote_name>

### `set-default`

Set the default remote which is the primary remote used for requests.

    amc remote set-default <remote_name>

### `set-url`

Set the URL of an existing remote.

    amc remote set-url <remote_name> <remote_url>

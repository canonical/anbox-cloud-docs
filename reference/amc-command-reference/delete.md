The `delete` command deletes an instance.

    amc delete <instance_id> [options]

The following options are available:

| Option | Description |
|--------|-------------|
|`-a`, `-all`| Deletes all existing instances |
|`-f`, `--force` | Forcibly removes an instance |
|`-h`, `--help` | Displays help information for the command |
|`--no-wait` | Indicates not to wait for the delete operation to finish |
|`-n`, `--node` | This option only works when used in combination with `--all` and can be used to select only instances for the specified node. Input type: String |
|`-t`, `--timeout` | Indicates the maximum time to wait for the operation to complete. The default value is `5m` |
|`-y`, `--yes` | Runs non interactively assuming `yes` for all prompts |

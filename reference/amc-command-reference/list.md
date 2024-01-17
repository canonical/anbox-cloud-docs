The `list` command lists all the instances.

    amc list [options]

You can also use `ls` as an alias.

The following options are available:

| Options | Description |
|---------|-------------|
|`-f`, `--filter`| Filters the output based on specified conditions |
| `--format` | Controls output formatting. The output format can be `table`, `json` or `csv` and the default value is `table` |
| `-h`, `--help` | Displays help information for the command |

Usage for `--filter`:

        amc list --filter attribute=value

where `attribute` can be one of the following:

|  Name  |             Argument type              |
|--------|----------------------------------------|
| `app`    | string (application name)              |
| `status` | string (prepared, started, error, etc) |
| `node`   | string                                 |
| `type`   | string (regular/base)                  |
| `tags`   | comma-separated list                   |
| `vm`     | boolean (true/false)                   |

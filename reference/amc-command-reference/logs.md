The `logs` command shows runtime logs of an instance. You can display system-level logs of the instance or the nested Android container.

    amc logs <instance_id> [options]

The following options are available:

| Option | Description |
|--------|-------------|
|`-f`, `--follow` | Shows only the most recent log entries and continuously prints new entries as they are appended to the log |
| `-h`, `--help` | Displays help information for the command |
| `-t`, `--type` | Type of logs to show: `anbox` or `android`. The default is `anbox`. |

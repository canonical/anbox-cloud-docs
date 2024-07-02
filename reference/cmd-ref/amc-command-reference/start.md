---
orphan: true
---
# `start`

The `start` command starts an existing instance that is in a prepared or a stopped status. This command can be used to start an instance when:
* An instance is just initialised with the `amc init` command and not started.
* An instance is in an error status.

        amc start <instance_id> [options]

The following options are available:

| Option | Description | Default value |
|--------|-------------|---------------|
| `-h`, `--help` | Displays help information for the command |
| `--no-wait` | Indicates not to wait for the instance to start | Disabled |
| `-t`, `--timeout` | Indicates the maximum time to wait for the operation to complete | 5m |
| `-y`, `--yes` | Force start the instance from error state | |

---
orphan: true
---
# `wait`

The `wait` command waits for an instance to reach a specific condition.

    amc wait (<app_id> | <instance_id>) --condition <key=value> [options]

The following options are available:

| Option | Description | Default value |
|--------|-------------|---------------|
| `-c`, `--condition` | Condition in the form of a `key=value` where `key` is a supported attribute and `value` defines what to wait on. <br/>Valid attributes for applications and their versions are `published` and `status` and for instances `status`. | |
| `-h`, `--help` | Displays help information for the command | |
| `-s`, `--selector` | Selector to filter the application or instance. <br/>Use `--selector version=<version number>` to wait on an application version. | |
| `-t`, `--timeout` | Indicates the maximum time to wait for the operation to complete | 5m |

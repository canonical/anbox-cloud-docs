---
orphan: true
---
# `exec`

The `exec` command executes commands directly inside an instance without a shell environment.

    amc exec <instance_id> -- <command> [options]

To use flags in your command, you must isolate the command with the '--' separator. Use `-T`, `--force-noninteractive` to disable pseudo-terminal allocation.

Remember that shell patterns will not be recognised. If you need a shell environment, execute the shell command and pass the command as an argument. For example: `amc exec <instance_id> -- sh -c "cd /tmp && pwd`.

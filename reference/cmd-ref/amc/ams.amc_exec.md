## ams.amc exec

Execute a command inside an instance

### Synopsis

Execute a command inside an instance.

To use flags in your command, you must isolate the command with
the '--' separator.

The command is executed directly using exec, so there is no shell.
Shell patterns (variables, file redirects ...) won't be understood.
If you need a shell environment, execute the shell command and
pass the actual command as an argument (see the example below).


```
ams.amc exec <instance_id> [--] <command> [flags]
```

### Examples

```
$ amc exec <instance_id> -- sh -c "cd /tmp && pwd"
```

### Options

```
  -T, --force-noninteractive   Disable pseudo-terminal allocation
  -h, --help                   help for exec
```

### SEE ALSO

* [ams.amc](ams.amc.md)	 - Anbox Management Client


# ams.amc show-log

Show an instance log file

## Synopsis

Show an instance log file.

This command is used to get logs from an instance in 'stopped' or 'error' state.
There are different log files that you can display. Use the following
command to get the names of the available log files:
	amc show <instance_id>


```
ams.amc show-log <instance_id> <log_name> [flags]
```

## Examples

```
$ amc show-log bknj0n9hpuo01q954fq0 system.log
```

## Options

```
  -h, --help   help for show-log
```

## SEE ALSO

* [ams.amc](ams.amc.md)	 - Anbox Management Client


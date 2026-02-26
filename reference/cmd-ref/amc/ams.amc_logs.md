# ams.amc logs

Show runtime logs of a running instance

## Synopsis

Show runtime logs of a running instance.

Anbox instances run a regular Ubuntu system with a nested Android container.
You can display system-level logs of the Anbox instance or the nested Android
instance.

NOTE: The specified instance must be in the 'started' or 'running' state for this command to show output.

```
ams.amc logs <instance_id> [flags]
```

## Examples

```
Show the runtime logs of the Ubuntu instance:

$ amc logs burp70p3p7j1icvtebig

Show the logs of the Android container:

$ amc logs -t android burp70p3p7j1icvtebig

Follow the logs for new entries:

$ amc logs -f burp70p3p7j1icvtebig

```

## Options

```
  -f, --follow        Show only the most recent log entries and continuously print new entries as they are appended to the log
  -h, --help          help for logs
  -t, --type string   Type of logs to show: anbox, android, console, container (default "anbox")
```

## SEE ALSO

* [ams.amc](ams.amc.md)	 - Anbox Management Client


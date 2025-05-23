## ams.amc start

Start an existing instance

### Synopsis

Start an existing instance that has an status 'prepared', 'stopped'.

When an Anbox instance is initialised with the 'amc init' command, it is not started automatically.
You must start it explicitly with the 'amc start' command.

When an Anbox instance ends up with the 'error' status, you can start it again with 'amc start' command.


```
ams.amc start <instance_id> [flags]
```

### Examples

```
  Initialise an instance:
  $ amc init <image_id|app_id>
  ceg2ukbhc8ic3ftkc990

  Start the instance:
  $ amc start ceg2ukbhc8ic3ftkc990
```

### Options

```
  -h, --help             help for start
      --no-wait          Don't wait for the instance to start before returning (default disabled)
  -t, --timeout string   Maximum time to wait for the operation to complete (default "5m")
  -y, --yes error        Force start the instance from error state
```

### SEE ALSO

* [ams.amc](ams.amc.md)	 - Anbox Management Client


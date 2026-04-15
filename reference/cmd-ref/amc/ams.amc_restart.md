# ams.amc restart

Restart a running instance

## Synopsis

Restart a running instance.

Stop a running instance and start it again. If the instance is already
stopped, it will not be started.


```
ams.amc restart <instance_id> [flags]
```

## Examples

```
  Restart a running instance:
  $ amc restart ceg2ukbhc8ic3ftkc990
```

## Options

```
  -h, --help             help for restart
  -t, --timeout string   Maximum time to wait for each operation to complete (default "5m")
```

## SEE ALSO

* [ams.amc](ams.amc.md)	 - Anbox Management Client


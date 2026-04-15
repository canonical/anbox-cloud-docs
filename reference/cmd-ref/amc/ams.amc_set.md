# ams.amc set

Set a configuration value for an existing instance

## Synopsis

Set a configuration value for an existing instance.

This command allows you to change the configuration of an existing instance.

The following configs can be set:
  security.delete_protected

```
ams.amc set <instance_id> <name> <value> [flags]
```

## Examples

```
  Set a configuration value for an existing instance:
  $ amc set ceg2ukbhc8ic3ftkc990 security.delete_protected true
```

## Options

```
  -h, --help             help for set
  -t, --timeout string   Maximum time to wait for each operation to complete (default "5m")
```

## SEE ALSO

* [ams.amc](ams.amc.md)	 - Anbox Management Client


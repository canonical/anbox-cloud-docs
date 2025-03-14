## ams.amc node set

Set a configuration item for a node

### Synopsis

Set a configuration item for a node.

See https://documentation.ubuntu.com/anbox-cloud/en/latest/reference/ams-configuration/ for a list of
available configuration items.

```
ams.amc node set <name> <key> <value> [flags]
```

### Examples

```
$ amc node set lxd0 cpus 8
```

### Options

```
  -h, --help             help for set
  -t, --timeout string   Maximum time to wait for the operation to complete (default "5m")
```

### SEE ALSO

* [ams.amc node](ams.amc_node.md)	 - Manage nodes


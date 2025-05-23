## ams.amc node remove

Remove a node

### Synopsis

Remove a node.

Removing a node excludes it from the Anbox Cloud cluster and makes it unable to host containers.

You cannot delete a node with running containers unless you specify the '--force'|'-f' flag.


```
ams.amc node remove <name> [flags]
```

### Examples

```
$ amc node remove lxd2
```

### Options

```
  -f, --force             Force the removal of the node
  -h, --help              help for remove
      --keep-in-cluster   Keep the LXD node as part of the cluster and just remove it from the AMS database
  -t, --timeout string    DEPRECATED: Maximum time to wait for the operation to complete (default "5m")
  -y, --yes               Assume 'yes' as answer to all prompts and run non-interactively
```

### SEE ALSO

* [ams.amc node](ams.amc_node.md)	 - Manage nodes


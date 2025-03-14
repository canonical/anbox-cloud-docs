## ams.amc delete

Delete an instance

```
ams.amc delete <instance_id> [flags]
```

### Examples

```
$ amc delete bkm6mj1hpuo01q954fl0
The following instance will be REMOVED:
  - bkm6mj1hpuo01q954fl0
Do you want to continue? [Y/n]:

```

### Options

```
  -a, --all              Delete all existing instances
  -f, --force            Force the removal of the instance
  -h, --help             help for delete
      --no-wait          Don't wait for the delete operation to finish
  -n, --node string      Select only instances for the specified node (this flag only works in combination with '--all')
  -t, --timeout string   Maximum time to wait for the operation to complete (default "5m")
  -y, --yes              Assume 'yes' as answer to all prompts and run non-interactively
```

### SEE ALSO

* [ams.amc](ams.amc.md)	 - Anbox Management Client


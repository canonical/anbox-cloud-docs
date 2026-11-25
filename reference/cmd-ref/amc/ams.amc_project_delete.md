# ams.amc project delete

Delete a project

## Synopsis

Deletes a project from AMS.


```
ams.amc project delete <name> [flags]
```

## Examples

```
$ amc project delete team-a
```

## Options

```
  -f, --force            Force deletion of the project, deleting any contained instances first
  -h, --help             help for delete
      --no-wait          Don't wait for the delete operation to finish
  -t, --timeout string   Maximum time to wait for the operation to complete (default "5m")
  -y, --yes              Assume 'yes' as answer to all prompts and run non-interactively
```

## SEE ALSO

* [ams.amc project](ams.amc_project.md)	 - Manage projects


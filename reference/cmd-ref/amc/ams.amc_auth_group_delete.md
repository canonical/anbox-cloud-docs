# ams.amc auth group delete

Delete an authorization group

## Synopsis

Deletes an authorization group from AMS.

An authorization group can be deleted regularly only if the group is empty with no identities as members.
To delete a group having identities, you need to delete the group forcefully with a --force
flag. This will remove the memberships of all the identities from the group before removal.


```
ams.amc auth group delete <group_name> [flags]
```

## Examples

```
$ amc auth group delete test-group
```

## Options

```
  -f, --force            Force deletion of groups
  -h, --help             help for delete
      --no-wait          Don't wait for the delete operation to finish
  -t, --timeout string   Maximum time to wait for the operation to complete (default "5m")
  -y, --yes              Assume 'yes' as answer to all prompts and run non-interactively
```

## SEE ALSO

* [ams.amc auth group](ams.amc_auth_group.md)	 - Manage authorization groups in AMS


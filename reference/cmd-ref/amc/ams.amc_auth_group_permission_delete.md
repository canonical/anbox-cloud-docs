## ams.amc auth group permission delete

Revoke a permission from an authorization group

### Synopsis

Revoke a permission to an authorization group.

Use this command to revoke a permission from an authorization group to remove their access
to manage the given resource in AMS.
		

```
ams.amc auth group permission delete <group_name> <resource_type> <resource_id> [flags]
```

### Examples

```
$ amc auth group permission delete test-group-1 application foo --permissions can_view
```

### Options

```
  -h, --help                  help for delete
  -p, --permissions strings   Comma separated list of permissions to add to the group.
```

### SEE ALSO

* [ams.amc auth group permission](ams.amc_auth_group_permission.md)	 - Manage permissions for an authorization group


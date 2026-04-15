# ams.amc auth group permission add

Assign a permission to an authorization group

## Synopsis

Assign a permission to an authorization group.

Use this command to assing a permission to an authorization group to give them access
to manage the given resource in AMS.
		

```
ams.amc auth group permission add <group_name> <resource_type> [<resource_id_or_name>] [flags]
```

## Examples

```
$ amc auth group permission add test-group-1 application foo --permissions can_view,can_edit
```

## Options

```
  -h, --help                  help for add
  -p, --permissions strings   Comma separated list of permissions to add to the group.
```

## SEE ALSO

* [ams.amc auth group permission](ams.amc_auth_group_permission.md)	 - Manage permissions for an authorization group


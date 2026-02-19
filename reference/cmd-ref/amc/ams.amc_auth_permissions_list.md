## ams.amc auth permissions list

List permissions for the current identity

### Synopsis

List permissions for the current identity.

Shows all permissions the current identity has in AMS.
Permissions are grouped by resource and sorted alphabetically.

Formatting can be controlled with the '--format' flag.
Valid formats are 'table' (default), 'json' and 'csv'.

```
ams.amc auth permissions list [flags]
```

### Examples

```
$ amc auth permissions list

+------------------+---------------------------+---------------------------+
|  RESOURCE TYPE   |       RESOURCE ID         |      ENTITLEMENTS         |
+------------------+---------------------------+---------------------------+
| server           | server                    | admin                     |
|                  |                           | can_create_applications   |
+------------------+---------------------------+---------------------------+

$ amc auth permissions list --format json
$ amc auth permissions list --format csv
```

### Options

```
      --format string   Output format - 'table', 'json' or 'csv' (default "table")
  -h, --help            help for list
```

### SEE ALSO

* [ams.amc auth permissions](ams.amc_auth_permissions.md)	 - Manage permissions


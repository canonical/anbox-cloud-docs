## ams.amc auth group set

Update fields for an authorization group

### Synopsis

Update fields for an authorization group.

Update specific fields for an existing auth group.
The following fields can be updated: description

```
ams.amc auth group set <name> <field> <value> [flags]
```

### Examples

```
$ amc auth group set test-group description 'this is an auth group'
```

### Options

```
  -h, --help   help for set
```

### SEE ALSO

* [ams.amc auth group](ams.amc_auth_group.md)	 - Manage authorization groups in AMS


## ams.amc application unset

Reset an application field

### Synopsis

Reset an application field.

The field is set to its default value.

The following fields can be unset: tags, addons, features

For resetting other fields, use the 'application set' command and specify a
value.


```
ams.amc application unset <id> <field> [flags]
```

### Examples

```
$ amc application unset foo tags
```

### Options

```
  -h, --help   help for unset
```

### SEE ALSO

* [ams.amc application](ams.amc_application.md)	 - Manage applications


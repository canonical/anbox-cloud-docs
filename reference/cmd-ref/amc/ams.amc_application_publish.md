## ams.amc application publish

Mark an application version as published

### Synopsis

Mark an application version as published.

Publishing a version marks it as the latest available version for that application.
When you launch an application, AMS picks the latest published version unless specified otherwise.

By default, application versions are unpublished.

If you publish a wrong version, you can revert it with the 'application revoke' command.


```
ams.amc application publish <id> <version> [flags]
```

### Examples

```
$ amc application publish foo 0
```

### Options

```
  -h, --help             help for publish
  -t, --timeout string   Maximum time to wait for the operation to complete (default "5m")
```

### SEE ALSO

* [ams.amc application](ams.amc_application.md)	 - Manage applications


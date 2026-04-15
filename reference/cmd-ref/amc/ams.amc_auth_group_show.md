# ams.amc auth group show

Show information about an authorization group in AMS.

## Synopsis

Show information about an authorization group in AMS.

Formatting can be controlled with the '--format' flag.
Valid formats are 'json' and 'yaml'.

```
ams.amc auth group show <group_name> [flags]
```

## Examples

```
$ amc auth group show test
name: test
description: this is a test group
identities: []
created-at: 1970-01-01 00:00:00 +0000 UTC
updated-at: 1970-01-01 00:00:00 +0000 UTC
immutable: false

```

## Options

```
      --format string   Output format - 'json' or 'yaml' (default "yaml")
  -h, --help            help for show
```

## SEE ALSO

* [ams.amc auth group](ams.amc_auth_group.md)	 - Manage authorization groups in AMS


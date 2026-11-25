# ams.amc project show

Show information about a project in AMS

## Synopsis

Show information about a project in AMS.

Formatting can be controlled with the '--format' flag.
Valid formats are 'json' and 'yaml'.

```
ams.amc project show <name> [flags]
```

## Examples

```
$ amc project show team-a
name: team-a
description: Project for team A
subnet: 100.64.0.0/28
status: ready
created-at: 1970-01-01 00:00:00 +0000 UTC

```

## Options

```
      --format string   Output format - 'json' or 'yaml' (default "yaml")
  -h, --help            help for show
```

## SEE ALSO

* [ams.amc project](ams.amc_project.md)	 - Manage projects


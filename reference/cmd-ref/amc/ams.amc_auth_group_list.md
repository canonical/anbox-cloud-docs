# ams.amc auth group list

List authorization groups in AMS

## Synopsis

List authorization groups in AMS.

Formatting can be controlled with the '--format' flag.
Valid formats are 'table' (see example), 'json' and 'csv'.

You can apply filters to narrow down the list of instances.
They are of the following form:

	--filter attribute=value

'attribute' can be one of the following:

+--------+------------------------+
|  Name  |      Argument type     |
+--------+------------------------+
|  name  |        string          |
+--------+------------------------+ 

```
ams.amc auth group list [flags]
```

## Examples

```
$ amc auth group ls

+----------------------+-----------------------------------------------+-------------------------------+-------------------------------+
|          NAME        |                  Identities 	               |          CREATED AT           |          UPDATED AT           |
+----------------------+-----------------------------------------------+-------------------------------+-------------------------------+
|  test-group-1        |  bknj0n9hpuo01q954fq0,bknj0n9hpuo01q954fq0    | 2025-08-11 09:11:28 +0000 UTC | 2025-08-11 09:11:28 +0000 UTC |
+----------------------+-----------------------------------------------+-------------------------------+-------------------------------+

$ amc auth group list --filter name=test-group
```

## Options

```
  -f, --filter stringArray   Filter the output based on conditions (for example, 'name=test-group')
      --format string        Output format -'table', 'json' or 'csv' (default "table")
  -h, --help                 help for list
```

## SEE ALSO

* [ams.amc auth group](ams.amc_auth_group.md)	 - Manage authorization groups in AMS


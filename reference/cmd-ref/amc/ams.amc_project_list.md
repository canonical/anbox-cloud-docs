# ams.amc project list

List projects in AMS

## Synopsis

List projects in AMS.

Formatting can be controlled with the '--format' flag.
Valid formats are 'table' (see example), 'json' and 'csv'.

You can apply filters to narrow down the list of projects.
They are of the following form:

    --filter attribute=value

'attribute' can be one of the following:

    name    string (fuzzy match)
    status  string (unknown, created, ready, deleted, error)


```
ams.amc project list [flags]
```

## Examples

```
$ amc project list
+---------+----------------------+----------------+--------+
|  NAME   |     DESCRIPTION      |     SUBNET     | STATUS |
+---------+----------------------+----------------+--------+
| default |                      |                | ready  |
+---------+----------------------+----------------+--------+
| team-a  | Project for team A     | 100.64.0.0/28  | ready  |
+---------+----------------------+----------------+--------+

$ amc project list --filter status=ready
```

## Options

```
  -f, --filter stringArray   Filter the output based on conditions (for example, 'status=ready')
      --format string        Output format - 'table', 'json' or 'csv' (default "table")
  -h, --help                 help for list
```

## SEE ALSO

* [ams.amc project](ams.amc_project.md)	 - Manage projects


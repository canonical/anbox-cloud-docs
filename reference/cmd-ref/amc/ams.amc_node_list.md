## ams.amc node list

List available nodes

### Synopsis

List available nodes.

Formatting can be controlled with the '--format' flag.
Valid formats are 'table' (see example), 'json' and 'csv'.

You can apply filters to narrow down the list of nodes.
They are of the following form:

	--filter attribute=value

'attribute' can be one of the following:

	+---------------+-------------------------------+
	|     Name      |       Argument type           |
	+---------------+-------------------------------+
	| master        | Boolean (true/false)          |
	| status        | string (online, offline etc.) |
	+---------------+-------------------------------+



```
ams.amc node list [flags]
```

### Examples

```
$ amc node list
+------+--------------+----------------+--------+--------------+
| NAME |   ADDRESS    | PUBLIC ADDRESS | STATUS | ARCHITECTURE |
+------+--------------+----------------+--------+--------------+
| lxd0 | 10.247.64.32 | 10.247.64.32   | online | aarch64      |
+------+--------------+----------------+--------+--------------+

$ amc node list --filter status=online
```

### Options

```
  -f, --filter stringArray   Filter the output based on conditions (for example, 'master=true')
      --format string        Output format - 'table', 'json' or 'csv' (default "table")
  -h, --help                 help for list
```

### SEE ALSO

* [ams.amc node](ams.amc_node.md)	 - Manage nodes


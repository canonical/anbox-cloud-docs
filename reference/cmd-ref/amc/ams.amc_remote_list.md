## ams.amc remote list

List registered remotes

### Synopsis

List registered remotes.

Formatting can be controlled with the '--format' flag.
Valid formats are 'table' (see example), 'json' and 'csv'.

```
ams.amc remote list [flags]
```

### Examples

```
$ amc remote list
+--------+---------+---------+
|  NAME  |   URL   | DEFAULT |
+--------+---------+---------+
| local  | unix:// | true    |
+--------+---------+---------+

```

### Options

```
      --format string   Output format - 'table', 'json' or 'csv' (default "table")
  -h, --help            help for list
```

### SEE ALSO

* [ams.amc remote](ams.amc_remote.md)	 - Interact with remote AMS daemons


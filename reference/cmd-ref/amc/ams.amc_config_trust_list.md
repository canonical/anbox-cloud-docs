## ams.amc config trust list

List trusted client certificates

### Synopsis

List trusted client certificates.

Formatting can be controlled with the '--format' flag.
Valid formats are 'table' (see example), 'json' and 'csv'.

```
ams.amc config trust list [flags]
```

### Examples

```
$ amc config trust list
+--------------+--------------------+------------------------------+------------------------------+
| FINGERPRINT  |    COMMON NAME     |          ISSUE DATE          |         EXPIRY DATE          |
+--------------+--------------------+------------------------------+------------------------------+
| a1c88ffec38d | ubuntu@vm0         | May 27, 2022 at 3:09pm (UTC) | May 24, 2032 at 3:09pm (UTC) |
+--------------+--------------------+------------------------------+------------------------------+
| a31c1ab256f3 | root@juju-3bdb58-1 | May 27, 2022 at 3:06pm (UTC) | May 24, 2032 at 3:06pm (UTC) |
+--------------+--------------------+------------------------------+------------------------------+

```

### Options

```
      --format string   Output format - 'table', 'json' or 'yaml' (default "table")
  -h, --help            help for list
```

### SEE ALSO

* [ams.amc config trust](ams.amc_config_trust.md)	 - Manage trusted clients


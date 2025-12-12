## ams.amc auth identity list

List identities

### Synopsis

List identities.

Formatting can be controlled with the '--format' flag.
Valid formats are 'table' (see example), 'json' and 'csv'.

You can apply filters to narrow down the list of identities.
They are of the following form:

	--filter attribute=value

'attribute' can be one of the following:

	+-----------+-------------------------------+
	|  Name     |      Argument type            |
	+-----------+-------------------------------+
	| id        | string (identity id)          |
	| auth_type | string (tls or oidc)          |
	+-----------+-------------------------------+

```
ams.amc auth identity list [flags]
```

### Examples

```
$ amc auth identity ls

	+----------------------+---------------------+----------------------+------------------------------------------------------------------+--------+
	|          ID          | AUTHENTICATION TYPE |    NAME              |                            IDENTIFIER                            | GROUPS |
	+----------------------+---------------------+----------------------+------------------------------------------------------------------+--------+
	| d3nfvd3c209uuurlgidg | tls                 | test-user            | 1588dd9a244a3e78d7f3572b0bc5a7b6c08658c9e3129793b4eb8f215962190a | tests  |
	+----------------------+---------------------+----------------------+------------------------------------------------------------------+--------+
	| bknj0n9hpuo01q954fq0 | oidc                | user@example.com     | 6c06937b6bb8e1ee02e8d379d17bf68aac0f91558d9bf61e040eee0b2aa09067 | admins |
	+----------------------+---------------------+----------------------+------------------------------------------------------------------+--------+


$ amc auth identity list --filter auth_type=oidc
```

### Options

```
  -f, --filter stringArray   Filter the output based on conditions (for example, 'auth_type=oidc')
      --format string        Output format - 'table', 'json' or 'csv' (default "table")
  -h, --help                 help for list
```

### SEE ALSO

* [ams.amc auth identity](ams.amc_auth_identity.md)	 - Manage authentiation & authorization


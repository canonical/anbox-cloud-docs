# ams.amc auth identity show

Show information about an identity

## Synopsis

Show information about an identity.

Formatting can be controlled with the '--format' flag.
Valid formats are 'json' and 'yaml'.

```
ams.amc auth identity show <identity_id> [flags]
```

## Examples

```
$ amc auth identity show bknj0n9hpuo01q954fq0
id: bknj0n9hpuo01q954fq0
authentication-method: oidc
groups: []
email: test-user@anbox-cloud.io
created-at: 1970-01-01 00:00:00 +0000 UTC
updated-at: 1970-01-01 00:00:00 +0000 UTC
name: test-user

```

## Options

```
      --format string   Output format - 'json' or 'yaml' (default "yaml")
  -h, --help            help for show
```

## SEE ALSO

* [ams.amc auth identity](ams.amc_auth_identity.md)	 - Manage authentiation & authorization


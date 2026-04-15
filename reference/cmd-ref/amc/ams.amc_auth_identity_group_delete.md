# ams.amc auth identity group delete

Remove an identity from authorization groups.

## Synopsis

Remove an identity from authorization groups.

This command can be used to remove an identity from a specific AMS group.
The assigned permissions to groups are then revoked from the identities and can
be used to manage access for the identities in AMS.
		

```
ams.amc auth identity group delete <identity_id> [flags]
```

## Examples

```
$ amc auth identity groups delete bknj0n9hpuo01q954fq0 --groups test,test-1
```

## Options

```
  -g, --groups strings   Comma separated list of groups
  -h, --help             help for delete
```

## SEE ALSO

* [ams.amc auth identity group](ams.amc_auth_identity_group.md)	 - Manage groups for an identity


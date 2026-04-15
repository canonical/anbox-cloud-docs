# ams.amc auth identity group add

Add an identity to authorization groups.

## Synopsis

Add an identity to authorization groups.

This command can be used to make an identity a member of a specific AMS group.
The assigned permissions to groups are then inherited by the identities and can
be used to manage access for the identities in AMS.
		

```
ams.amc auth identity group add <identity_id> [flags]
```

## Examples

```
$ amc auth identity group add bknj0n9hpuo01q954fq0 --groups test,test-1
```

## Options

```
  -g, --groups strings   Comma separated list of groups
  -h, --help             help for add
```

## SEE ALSO

* [ams.amc auth identity group](ams.amc_auth_identity_group.md)	 - Manage groups for an identity


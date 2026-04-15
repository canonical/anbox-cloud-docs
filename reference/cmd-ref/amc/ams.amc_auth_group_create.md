# ams.amc auth group create

Create a new group in AMS

## Synopsis

Create a new group to manage access in AMS.

Use this command to create a group to manage authorization permissions
for a collection of identities in AMS.
		

```
ams.amc auth group create <group_name> [flags]
```

## Examples

```
$ amc auth group create test --description 'this is a new group'
```

## Options

```
  -d, --description string   A description for the authorization group
  -h, --help                 help for create
```

## SEE ALSO

* [ams.amc auth group](ams.amc_auth_group.md)	 - Manage authorization groups in AMS


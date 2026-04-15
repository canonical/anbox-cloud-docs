# ams.amc auth identity delete

Delete an identity

## Synopsis

Deletes an identity from AMS.

This can be used to revoke access from an identity in AMS. The identity
can be re-registered to provide access to AMS again.
		

```
ams.amc auth identity delete <identity_id> [flags]
```

## Examples

```
$ amc auth identity delete bknj0n9hpuo01q954fq0
```

## Options

```
  -f, --force            force deletion of identity
  -h, --help             help for delete
      --no-wait          Don't wait for the delete operation to finish
  -t, --timeout string   Maximum time to wait for the operation to complete (default "5m")
  -y, --yes              Assume 'yes' as answer to all prompts and run non-interactively
```

## SEE ALSO

* [ams.amc auth identity](ams.amc_auth_identity.md)	 - Manage authentiation & authorization


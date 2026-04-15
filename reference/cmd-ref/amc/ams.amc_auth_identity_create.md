# ams.amc auth identity create

Create a new identity in AMS

## Synopsis

Create a new identity to allow access to AMS.

The identity can be created using different authentication methods. Currently "oidc" and "tls" are supported.
		

```
ams.amc auth identity create <authentication_method>/<name> [Path to PEM encoded certificate or - to read from stdin] [flags]
```

## Examples

```
$ amc auth identity create oidc/john.doe@example.com\n$amc auth identity create tls/test-user - < client-cert.pem
```

## Options

```
  -h, --help   help for create
```

## SEE ALSO

* [ams.amc auth identity](ams.amc_auth_identity.md)	 - Manage authentiation & authorization


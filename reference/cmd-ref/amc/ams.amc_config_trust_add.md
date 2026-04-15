# ams.amc config trust add

Add a trusted client

## Synopsis

Add a trusted client.

Trust a new client to communicate with AMS by providing its certificate.
Use '-' as certificate_path to read from stdin.


```
ams.amc config trust add <certificate_path> [flags]
```

## Examples

```
$ amc config trust add client.crt
$ cat client.crt | amc config trust add -
```

## Options

```
  -h, --help   help for add
```

## SEE ALSO

* [ams.amc config trust](ams.amc_config_trust.md)	 - Manage trusted clients


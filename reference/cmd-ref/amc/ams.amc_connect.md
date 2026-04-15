# ams.amc connect

Connect to an instance via ADB

## Synopsis

Connect to a running instance using an Android Debug Bridge (ADB) connection.

If an instance ID is provided, a temporary share URL will be created to connect to the instance.
If a share URL is provided, it will be used directly to establish the connection.

The instance must be running and have an active session to be connected to.

```
ams.amc connect <instance-id or URL> [flags]
```

## Options

```
  -k, --accept-remote-cert   Accept remote certificate when running in non-interactive mode
  -h, --help                 help for connect
```

## SEE ALSO

* [ams.amc](ams.amc.md)	 - Anbox Management Client


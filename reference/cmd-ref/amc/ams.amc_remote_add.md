## ams.amc remote add

Add a remote

### Synopsis

Add a remote.

Set a connection to a remote AMS daemon.

If you set up a trust password on the daemon, you must provide it when running the command.


```
ams.amc remote add <name> <url> [trust_password] [flags]
```

### Examples

```
$ amc remote add local unix://
```

### Options

```
      --accept-certificate   Implicitly accept remote server certificate
  -h, --help                 help for add
```

### SEE ALSO

* [ams.amc remote](ams.amc_remote.md)	 - Interact with remote AMS daemons


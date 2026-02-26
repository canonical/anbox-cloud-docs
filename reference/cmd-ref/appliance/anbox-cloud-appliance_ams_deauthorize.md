# anbox-cloud-appliance ams deauthorize

Deauthorize a user on the system from accessing the AMS service.

## Synopsis

Deauthorize a user on the system from accessing the AMS service.

AMS implements local authorization by verifying the UID of the user connecting
over the local UNIX domain socket. For the user to be authorized, their
UID must be specified in the AMS configuration. The root user always has access
to the AMS service and can remove registered UIDs to remove their access
rights.

The command will automatically restart AMS after applying the change unless
explicitly disabled.

To deauthorize a user's UID, run:

    sudo anbox-cloud-appliance ams deauthorize 1000

This will remove the UID 1000 from the list of authorized UIDs and the user
will no longer have access to the AMS service over its UNIX domain socket.


```
anbox-cloud-appliance ams deauthorize [<uid>] [flags]
```

## Examples

```
$ sudo anbox-cloud-appliance ams deauthorize 1000
```

## Options

```
      --force        Force deauthorizing specified UID
  -h, --help         help for deauthorize
      --no-restart   Do not restart AMS after applying the change
```

## SEE ALSO

* [anbox-cloud-appliance ams](anbox-cloud-appliance_ams.md)	 - Manage the AMS service of the Anbox Cloud Appliance


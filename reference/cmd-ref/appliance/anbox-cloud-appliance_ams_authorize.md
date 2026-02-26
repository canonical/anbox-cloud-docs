# anbox-cloud-appliance ams authorize

Authorize a new user on the system to access the AMS service.

## Synopsis

Authorize a new user on the system to access the AMS service.

AMS implements local authorization by verifying the UID of the user connecting
over the local UNIX domain socket. For the user to be authorized, their
UID must be specified in the AMS configuration. The root user always has access
to the AMS service and can register additional UIDs for access.

The command will automatically restart AMS after applying the change unless
explicitly disabled.

To register their UID, a user with `sudo` privileges must run:

    sudo anbox-cloud-appliance ams authorize

The command will determine the UID to authorized from the SUDO_UID environment
variable that `sudo` sets for the invoking user.

To register another user, a `sudo` user must specify the UID that they want to register:

    sudo anbox-cloud-appliance ams authorize 1001

This will allow the user on the system with the UID 1001 to access the AMS
service.


```
anbox-cloud-appliance ams authorize [<uid>] [flags]
```

## Examples

```
$ sudo anbox-cloud-appliance ams authorize
```

## Options

```
      --force        Force deauthorizing specified UID
  -h, --help         help for authorize
      --no-restart   Do not restart AMS after applying the change
```

## SEE ALSO

* [anbox-cloud-appliance ams](anbox-cloud-appliance_ams.md)	 - Manage the AMS service of the Anbox Cloud Appliance


## ams.amc image sync

Synchronizes the image with the remote image server

### Synopsis

Synchronizes the image with the remote image server.

If the image is coming from a remote image server this will trigger explicit
synchronization with the remote server. This results in the image being
downloaded to the cluster from the remote server.


```
ams.amc image sync <id> [flags]
```

### Examples

```
$ amc image sync foo
```

### Options

```
  -h, --help   help for sync
```

### SEE ALSO

* [ams.amc image](ams.amc_image.md)	 - Manage images


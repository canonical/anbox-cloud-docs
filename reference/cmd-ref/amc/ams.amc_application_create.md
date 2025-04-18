## ams.amc application create

Create an application

### Synopsis

Create an application.

Applications can be created from plain directories, tarballs or zip archives.
A valid application must contain an APK and a manifest that defines various
application properties.


```
ams.amc application create (<directory> | <.tar.bz2 tarball> | <.zip archive>) [flags]
```

### Examples

```
$ tree my-app
my-app/
├── app.apk
└── manifest.yaml

$ amc application create my-app

```

### Options

```
  -h, --help             help for create
  -t, --timeout string   Maximum time to wait for the operation to complete (default "5m")
      --vm               Create an application using VMs instead of containers
```

### SEE ALSO

* [ams.amc application](ams.amc_application.md)	 - Manage applications


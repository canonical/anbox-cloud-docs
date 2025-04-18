## ams.amc image add

Add an image

### Synopsis

Add an image.

The first image you add will be marked as the default image, which means it is used
when creating an application or launching a raw container without specifying an image.
After that, you can mark a new image as the default by adding the '--default' flag.


```
ams.amc image add <name> <image_path> [flags]
```

### Examples

```
$ amc image add base path/to/image
```

### Options

```
  -d, --default          Mark image as the default image
  -h, --help             help for add
  -t, --timeout string   Maximum time to wait for the operation to complete (default "5m")
      --type string      Type of image to import. Only used when a remote image is added. Valid values are: any, container, vm (default "any")
```

### SEE ALSO

* [ams.amc image](ams.amc_image.md)	 - Manage images


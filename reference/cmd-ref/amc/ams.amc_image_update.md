## ams.amc image update

Update an existing image

### Synopsis

Update an existing image.

This command replaces the specified image with the new image and bumps its version number.


```
ams.amc image update ( <id> | <name> ) <image_path> [flags]
```

### Examples

```
$ amc image update foo foo-v2.tar.xz
```

### Options

```
  -d, --default          Mark image as the default image
  -h, --help             help for update
  -t, --timeout string   Maximum time to wait for the operation to complete (default "5m")
```

### SEE ALSO

* [ams.amc image](ams.amc_image.md)	 - Manage images


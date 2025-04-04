## ams.amc image delete

Delete an image

### Synopsis

Delete an image.

Deleting an image removes all of its versions. If you want to remove only a
specific version, use the '--version' flag.

Images synchronised from the image server cannot be deleted unless you specify
the '--force'|'-f' flag.


```
ams.amc image delete ( <id> | <name> ) [flags]
```

### Examples

```
$ amc image delete foo
The following image will be REMOVED:
  - foo
Do you want to continue? [Y/n]:

```

### Options

```
  -f, --force            Force the deletion of immutable images
  -h, --help             help for delete
  -t, --timeout string   Maximum time to wait for the operation to complete (default "5m")
  -v, --version int      Version of the image to delete. If not specified, all versions are deleted.
      --vm               Delete the virtual machine variant of the image
  -y, --yes              Assume 'yes' as answer to all prompts and run non-interactively
```

### SEE ALSO

* [ams.amc image](ams.amc_image.md)	 - Manage images


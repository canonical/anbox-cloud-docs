## ams.amc publish

Publish an instance as an image

### Synopsis

Publish an instance as an image.

This command creates an image from an existing instance. The instance must be stopped
unless the --force flag is used to stop it automatically. The resulting image can be
used to launch new instances.

If the --name flag is not provided, the image will only have an ID and can be referenced
by that ID in subsequent commands.


```
ams.amc publish <instance_id> [flags]
```

### Examples

```
  Publish a stopped instance:
  $ amc publish bcnh5b2j1q001q954e70

  Publish with a custom name:
  $ amc publish bcnh5b2j1q001q954e70 --name my-custom-image

  Force stop and publish:
  $ amc publish my-instance --force --name my-image

  Publish and set as default:
  $ amc publish bcnh5b2j1q001q954e70 --name my-base-image --default
```

### Options

```
      --default          Make the new image the default image
      --force            Force stop the instance if it is running
  -h, --help             help for publish
  -n, --name string      Name for the new image (optional)
  -t, --timeout string   Maximum time to wait for the operation to complete (default "5m")
```

### SEE ALSO

* [ams.amc](ams.amc.md)	 - Anbox Management Client


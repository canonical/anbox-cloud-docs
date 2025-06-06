## ams.amc application set

Update fields for an application

### Synopsis

Update fields for an application.

Update specific fields for an existing application without creating
a new version of the application.

The following fields can be updated: image, instance-type, addons, tags, inhibit-auto-updates, resources.cpus, resources.memory, resources.disk-size, resources.gpu-slots, resources.vpu-slots, boot-activity, features, hooks.timeout, bootstrap.keep, node-selector, watchdog.disabled, watchdog.allowed-packages

```
ams.amc application set <id> <field> <value> [flags]
```

### Examples

```
$ amc application set foo instance-type a4.3
```

### Options

```
  -h, --help   help for set
```

### SEE ALSO

* [ams.amc application](ams.amc_application.md)	 - Manage applications


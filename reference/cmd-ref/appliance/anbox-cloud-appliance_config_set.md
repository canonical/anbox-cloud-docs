## anbox-cloud-appliance config set

Set specific configuration items for the Anbox Cloud Appliance

### Synopsis

Set configuration items for the Anbox Cloud Appliance

This command allows changing the following configuration items:

* network.public_address (IP address)
* network.location (DNS name)
* core.https_allowed_origin (HTTP origin, see https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Origin)
* core.https_allowed_headers (comma seprated list of allowed HTTP headers)
* core.https_allowed_methods (comma separate list of allowed HTTP methods)

Multiple configuration items can be set in a single call, e.g.

  $ sudo anbox-cloud-appliance config set \
      network.public_address=5.6.7.8 network.location=foo.bar

Changes made are immediately effective and will require a restart
of all services the Anbox Cloud Appliance includes. Once the
configuration has been updated the command will restart all services
unless the --no-restart option is set.


```
anbox-cloud-appliance config set [flags]
```

### Examples

```
$ sudo anbox-cloud-appliance config set network.public_address=1.2.3.4
```

### Options

```
  -h, --help         help for set
      --no-restart   Do not restart the Anbox Cloud Appliance
```

### SEE ALSO

* [anbox-cloud-appliance config](anbox-cloud-appliance_config.md)	 - Managed the Anbox Cloud Appliance configuration


## ams.amc show

Show information about an instance

### Synopsis

Show information about an instance.

Formatting can be controlled with the '--format' flag.
Valid formats are 'json' and 'yaml'.

```
ams.amc show <instance_id> [flags]
```

### Examples

```
$ amc show bknj0n9hpuo01q954fq0
id: bknj0n9hpuo01q954fq0
name: ams-bknj0n9hpuo01q954fq0
status: running
node: lxd0
created_at: 2019-07-17T14:27:41Z
image:
  id: bkkbiaphpuo3mh78ain0
network:
  address: 192.168.100.2
  public_address: 10.48.61.89
  services: []
stored_logs: []
error_message: ""

```

### Options

```
      --format string   Output format - 'json' or 'yaml' (default "yaml")
  -h, --help            help for show
```

### SEE ALSO

* [ams.amc](ams.amc.md)	 - Anbox Management Client


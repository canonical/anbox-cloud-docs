## ams.amc node show

Show information about a node

### Synopsis

Show information about a node.

Formatting can be controlled with the '--format' flag.
Valid formats are 'json' and 'yaml'.

```
ams.amc node show <name> [flags]
```

### Examples

```
$ amc node show node1
name: node1
managed: true
status: online
unschedulable: false
architecture: x86_64
disk:
  pool: ams0
  size: 13GB
network:
  address: 10.48.61.89
  bridge-mtu: 1500
gpus:
  0:
    pci-address: 00:08.0
config:
  public-address: 10.48.61.89
  cpus: 0
  cpu-allocation-rate: 4
  memory: 0B
  memory-allocation-rate: 2
  gpu-slots: 0
  gpu-encoder-slots: 0
  tags: []

```

### Options

```
      --allocations       Show resource allocations
  -f, --format string     Output format - 'json' or 'yaml' (default "yaml")
      --gpu-allocations   Show GPU allocations
  -h, --help              help for show
```

### SEE ALSO

* [ams.amc node](ams.amc_node.md)	 - Manage nodes


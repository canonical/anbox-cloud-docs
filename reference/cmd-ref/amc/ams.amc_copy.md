## ams.amc copy

Copy an instance

### Synopsis

Copy an existing instance to a new one.

This command creates a full clone of an existing instance. If the source instance is running,
the --force flag must be used to force stop it before the copy proceeds. The --force flag
is also required when copying an instance in an 'error' state.

Note: when copying an instance in an 'error' state, the new instance will be a fresh copy
and will not include the logs from the source instance.


```
ams.amc copy <instance_id_or_name> [flags]
```

### Examples

```

  Create a copy of an existing instance:
  $ amc copy bcnh5b2j1q001q954e70

  Specify a name for the new instance:
  $ amc copy bcnh5b2j1q001q954e70 --name my-clone

  Force stop a running instance and copy:
  $ amc copy bcnh5b2j1q001q954e70 --force

  Copy to a specific node:
  $ amc copy bcnh5b2j1q001q954e70 --name my-clone --node lxd2
```

### Options

```
      --config stringArray      Instance configuration, e.g., security.delete_protected=true (can be used multiple times)
  -c, --cpus int                Number of CPU cores to be assigned for the instance (for example, 2). If not specified, the number of CPU cores specified by the instance type will be used. (default 2)
      --devmode                 Enable developer mode for the instance (default disabled)
      --disable-watchdog        Disable watchdog for the instance (regular instances only)
      --display-density int     Pixel density of the virtual display of the instance (default 240)
      --display-size string     Size of the virtual display of the instance in the format <width>x<height> (default "1280x720")
      --enable-graphics         Enable graphics for the instance (default: disabled)
      --enable-streaming        Enable streaming for the instance (default: disabled)
  -f, --features string         Comma-separated list of features to enable for the Anbox runtime inside the instance
      --force                   Force copy even if the source instance is running or in error state
      --fps int                 Frame rate the virtual display of the instance (default 60)
  -g, --gpu-slots int           Number of GPU slots to be assigned for the instance (for example, 1). If not specified, the number of GPU slots specified by the instance type will be used. (default -1)
      --gpu-type string         Type of the GPU to select for the instance. If not given the GPU with the minimum usage is assigned to the instance on the node it is scheduled on. Possible values are: amd, intel, nvidia
  -h, --help                    help for copy
      --launch                  Launch the instance immediately after copying
  -m, --memory string           Memory to be assigned for the instance (for example, 3GB). If not specified, the memory specified by the instance type will be used.
      --metrics-server string   Metrics server to which the instance sends its data
      --name string             Name of the instance. Must be unique, 3–63 characters, alphanumeric or hyphens, cannot start or end with a hyphen.
      --no-disk-reserve         Create the instance with a non-reserved disk space (default: disabled)
      --no-wait                 Don't wait for the instance to start before returning (default: disabled)
  -n, --node string             LXD node to use for creating the instance
  -p, --platform string         Anbox platform to use
  -r, --raw                     If specified, create a raw instance for the specified image instead of an application instance
  -s, --service stringArray     Services to expose on the instance IP endpoint for external access (public or private)
      --tags string             Comma-separated list of tags to set for the instance
  -t, --timeout string          Maximum time to wait for the operation to complete (default "5m")
      --userdata string         String with additional user data to be pushed into the created instance
      --userdata-path string    Path to a file with additional user data to be pushed into the created instance
      --vm                      Create a virtual machine instead of a container (default: disabled)
  -v, --vpu-slots int           Number of VPU slots to be assigned for the instance (for example, 1). If not specified, the number of VPU slots specified by the instance type will be used. (default -1)
```

### SEE ALSO

* [ams.amc](ams.amc.md)	 - Anbox Management Client


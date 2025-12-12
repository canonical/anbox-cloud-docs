## ams.amc init

Create an instance but do not start it immediately

### Synopsis

Create an instance but do not start it immediately. To start such an instance, run 'amc start <instance_id>'.

```
ams.amc init ( <app_id> | <image_id> ) [flags]
```

### Examples

```
$ amc init foo
```

### Options

```
  -a, --addons string             Comma-separated list of addons to install in the instance (raw instances only)
      --application-version int   Specific version of an application to use when creating an instance
      --config stringArray        Instance configuration, e.g., security.delete_protected=true (can be used multiple times)
  -c, --cpus int                  Number of CPU cores to be assigned for the instance (for example, 2). If not specified, the number of CPU cores specified by the instance type will be used. (default 2)
      --devmode                   Enable developer mode for the instance (default disabled)
      --disable-watchdog          Disable watchdog for the instance (regular instances only)
  -d, --disk-size string          Disk size of the instance (for example, 5GB). If not specified, the disk size specified by the instance type will be used.
      --display-density int       Pixel density of the virtual display of the instance (default 240)
      --display-size string       Size of the virtual display of the instance in the format <width>x<height> (default "1280x720")
      --enable-graphics           Enable graphics for the instance (default: disabled)
      --enable-streaming          Enable streaming for the instance (default: disabled)
  -f, --features string           Comma-separated list of features to enable for the Anbox runtime inside the instance
      --fps int                   Frame rate the virtual display of the instance (default 60)
  -g, --gpu-slots int             Number of GPU slots to be assigned for the instance (for example, 1). If not specified, the number of GPU slots specified by the instance type will be used. (default -1)
      --gpu-type string           Type of the GPU to select for the instance. If not given the GPU with the minimum usage is assigned to the instance on the node it is scheduled on. Possible values are: amd, intel, nvidia
  -h, --help                      help for init
  -i, --instance-type string      Instance type to use for the instance when creating a raw instance
  -m, --memory string             Memory to be assigned for the instance (for example, 3GB). If not specified, the memory specified by the instance type will be used.
      --metrics-server string     Metrics server to which the instance sends its data
      --name string               Name of the instance. Must be unique, 3–63 characters, alphanumeric or hyphens, cannot start or end with a hyphen.
      --no-wait                   Don't wait for the instance to start before returning (default: disabled)
  -n, --node string               LXD node to use for creating the instance
  -p, --platform string           Anbox platform to use
  -r, --raw                       If specified, create a raw instance for the specified image instead of an application instance
  -s, --service stringArray       Services to expose on the instance IP endpoint for external access (public or private)
      --tags string               Comma-separated list of tags to set for the instance
  -t, --timeout string            Maximum time to wait for the operation to complete (default "5m")
      --userdata string           String with additional user data to be pushed into the created instance
      --userdata-path string      Path to a file with additional user data to be pushed into the created instance
      --version int               Specific version of an application or image to use when creating an instance (default -1)
      --vm                        Create a virtual machine instead of a container (default: disabled)
  -v, --vpu-slots int             Number of VPU slots to be assigned for the instance (for example, 1). If not specified, the number of VPU slots specified by the instance type will be used. (default -1)
```

### SEE ALSO

* [ams.amc](ams.amc.md)	 - Anbox Management Client


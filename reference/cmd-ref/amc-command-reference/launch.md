---
orphan: true
---
# `launch`

The `launch` command launches an instance.

    amc launch <app_id | image_id> [options]

The following options are available:

| Option | Input type | Description | Default value |
|------|--------------|-------------|---------------|
| `-a`, `--addons` | String | Comma-separated list of addons to install in the instance. Applicable for raw instances only. | |
| `-c`, `--cpus` | Integer | Number of CPU cores to be assigned for the instance. | 2 |
| `--devmode` |    | Enables developer mode for the instance. | Disabled |
| `--disable-watchdog` | | Disables watchdog for the instance. Applicable for regular instances only. | |
| `-d`, `--disk-size` | String | Disk size of the instance. | 3 GB for a container instance;<br/> 15 GB for a virtual machine instance |
| `--enable-graphics` | | Enables graphics for the instance | Disabled |
| `-f`, `--features` | String | Comma-separated list of features to enable for the Anbox runtime inside the instance | |
| `-g`, `--gpu-slots` |  Integer | Number of GPU slots to be assigned for the instance. | -1 |
| `-h`, `--help` |  | Displays help information for the command | |
| `-m`, `--memory` | String | Memory to be assigned for the instance | 3GB |
| `--metrics-server` | String | Metrics server to which the instance sends its data |
| `--no-wait` | | Indicates not to wait for the instance to start | Disabled |
| `-n`, `--node` | String | Indicates the LXD node to use for creating the instance | |
| `-p`, `--platform` | String | Indicates the Anbox platform to use | `null` platform |
| `-r`, `--raw` | | Creates a raw instance for the specified image instead of an application instance | |
|  `-s`, `--service` | String array | Services to expose on the instance's IP endpoint for external access (public or private) | |
|  `--tags` | String | Comma-separated list of tags to set for the instance | |
| `-t`, `--timeout` | | String value that indicates the maximum time to wait for the operation to complete. The default value is `5m`. |
| `--userdata` | String | Additional user data to be sent to the created instance | |
| `--userdata-path` | String | Path to a file with additional user data to be sent to the created instance |
| `--version` | Integer | Indicates the specific version of an application or image to use when creating an instance | -1 |
| `--vm` | | Creates a virtual machine instead of a container | Disabled |
| `-v`, `--vpu-slots` | Integer | Indicates the number of VPU slots to be assigned for the instance. | -1 |

---
orphan: true
---
# `benchmark`

The `benchmark` command allows you to benchmark your Anbox Cloud deployment. Benchmarking your deployment helps in evaluating the performance of Anbox Cloud for a well-defined workload.

    amc benchmark (<app_id> | <image_id>) [options]

Define the workload with the following options:

|Option|Input type|Description| Default value|
|------|-----------|-----------|-------------|
|`-d`, `--dump-data` | | Dump data collected during the benchmark, the file name containing the data is printed | |
| `-c`, `--force` | | Force remove instances | |
| `-f`, `--fps`  | | Measure Frames Per Second (FPS) for all instances | |
| `--fps-threshold` | Integer | FPS threshold below which an instance will be considered slow | 30 |
| `-h`, `--help` | | Displays help information for `amc benchmark` command| |
| `-s`, `--instances-per-second` | Float | Number of instances to launch per second | 0.1 |
| `--measure-time` | String | Time spent measuring instance statistics| 1 minute |
| `--network-address` | String | Outbound network address on which the instances can reach the benchmark executor. For example: 127.0.0.1 | |
| `-n`, `--num-instances` | Integer | Number of instances to launch  | 1 |
| `-p`, `--platform` | String | Anbox platform to use for the instances | `null` |
| `-r`, `--raw` | | If specified, the instance is created for the specified image instead of an application | |
|`--settle-time` | String | Settling time allowed for the instance performance measurement starts | 30 seconds |                 
| `--userdata` | String | Additional user data to be sent to the created instance | |


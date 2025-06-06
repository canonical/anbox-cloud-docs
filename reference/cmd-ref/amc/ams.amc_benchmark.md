## ams.amc benchmark

Benchmark your Anbox Cloud deployment

### Synopsis

Benchmark your Anbox Cloud deployment.

The results can be used to evaluate the performance of Anbox Cloud for a well-defined workload.


```
ams.amc benchmark ( <app_id> | <image_id> ) [flags]
```

### Examples

```
 $ amc benchmark --fps --network-address=172.31.4.11 --num-instances=15 --instances-per-second=0.1 bh2q90vo3v1lt1ft4mlg

2019/01/21 11:11:49 Test environment:
2019/01/21 11:11:49   AMS version: 1.2.1
2019/01/21 11:11:49   Available nodes:
2019/01/21 11:11:49     lxd0 (CPU: 48, Memory: 185GB)
2019/01/21 11:11:49
2019/01/21 11:11:49 Launching 15 instances for application bh2q90vo3v1lt1ft4mlg with 0.1 instances per second
[...]
2019/01/21 11:15:39 Instances boot time measurement:
2019/01/21 11:15:39   Launching all 15 instances took 2m36.560310342s
2019/01/21 11:15:39   Out of 15 instances 0 failed to launch
2019/01/21 11:15:39   Average instance launch time: 6.149119411s
2019/01/21 11:15:39   Max instance launch time: 6.576302043s
2019/01/21 11:15:39   Min instance launch time: 5.911184959s
2019/01/21 11:15:39   Android system failed to boot in the following instances:
2019/01/21 11:15:39     None
2019/01/21 11:15:39 Instances statistics:
2019/01/21 11:15:39   FPS avg 58 min 52 max 64 for 15 instances
2019/01/21 11:15:39   Instances below run at low FPS(<30):
2019/01/21 11:15:39     None

```

### Options

```
      --containers-per-second float   Number of containers to launch per second (default 0.1)
  -d, --dump-data                     Dump data collecting during the benchmark; the file name will be printed
      --features string               Feature flags to set for launched instances
  -c, --force                         Force the removal of the instances
  -f, --fps                           Measure FPS of all instances
      --fps-threshold int             FPS threshold below which an instance will be seen as slow (default 30)
  -h, --help                          help for benchmark
  -i, --instance-type string          Instance type to use for the instance when launching a raw instance (default "a2.3")
  -s, --instances-per-second float    Number of instances to launch per second (default 0.1)
      --keep-instances                Keep all instances after finishing the benchmark itself and don't attempt to delete them
      --measure-time string           Time spent measuring instance statistics (default "1m")
      --network-address string        Outbound network address on which the instances can reach the benchmark executor (for example, 127.0.0.1)
      --num-containers int            Number of containers to launch (default 1)
  -n, --num-instances int             Number of instances to launch (default 1)
  -p, --platform string               Anbox platform to use for the instances (default "null")
  -r, --raw                           If specified, the instance is created for the specified image instead of an application
      --settle-time string            Time the benchmark allows the instance to settle before it starts to measure performance (default "30s")
      --userdata string               Additional user data to be pushed into the created instance
```

### SEE ALSO

* [ams.amc](ams.amc.md)	 - Anbox Management Client


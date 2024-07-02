(howto-list-instances)=
# How to list instances

To get an overview of the running status of instances on an Anbox Cloud deployment, run the `amc ls` command:

```bash
+----------------------+----------------+---------+---------+------+---------------+------------------------+
|          ID          |  APPLICATION   |  TYPE   | STATUS  | NODE |    ADDRESS    |       ENDPOINTS        |
+----------------------+----------------+---------+---------+------+---------------+------------------------+
| bdpaqaqhmss611ruq6kg |     candy      | regular | running | lxd0 | 192.168.100.2 | 192.168.100.2:22/tcp   |
|                      |                |         |         |      |               | 10.103.46.41:10000/tcp |
+----------------------+----------------+---------+---------+------+---------------+------------------------+
```

This will list all instances with their status and additional information, for example, the LXD node in the cluster on which the instances are running.

## Filter instances

`amc ls` accepts a `--filter` flag to filter and group instances.

The filter flag accepts a key-value pair as the filtering value. The following attributes are valid keys:

Name            |  Value
----------------|------------
`app`           |  Application name or ID
`type`          |  Type of the instance, possible values: "base", "regular"
`node`          |  Node on which the instance runs
`status`        |  Instance status, possible values: "created", "prepared", "started", "stopped", "running", "error", "deleted", "unknown"


To list all regular instances:

    amc ls --filter type=regular

If you need to apply multiple filters, pass multiple flags:

    amc ls --filter type=regular --filter node=lxd0

This will query all regular instances that are placed on the node with the name `lxd0`.

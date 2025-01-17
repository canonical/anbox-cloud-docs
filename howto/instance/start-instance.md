(howto-start-instance)=
# How to start an instance

When an instance is either initialized with the `amc init` command or stopped with the `amc stop` command, you must start it explicitly with the `amc start` command:

    amc start <instance_id>

`<instance_id>` is the ID of the instance that you want to start.

```{important}
Do not use the `lxc` command to manage an instance. Always use the `amc` command instead. In Anbox Cloud, instances have their own life cycle and using the `lxc` command to manage an instance can cause the instance to be out of sync.
```

By default, the `amc start` command waits 5 minutes for an instance to run before the operation times out. When starting an instance, you can specify a custom wait time with the `--timeout` option.

    amc start <instance_id> --timeout 10m

When the `--no-wait` option is specified, the `amc start` command exits immediately after the instance starts and will not wait till it is running.

    amc start <instance_id> --no-wait

```{important}
Starting an instance that has stopped with an error status is is not allowed. Doing so would cause the `amc start` command to fail.
```

## Related topics
* {ref}`howto-create-instance`
* {ref}`howto-stop-instance`

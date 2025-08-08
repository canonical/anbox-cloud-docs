(howto-restart-instance)=
# Restart an instance

A running instance can be restarted using the `amc restart` command:

    amc restart <instance_id>

`<instance_id>` is the ID of the instance that you want to restart.

```{important}
Do not use the `lxc` command to manage an instance. Always use the `amc` command instead. In Anbox Cloud, instances have their own life cycle and using the `lxc` command to manage an instance can cause the instance to be out of sync.
```

By default, the `amc restart` command waits 5 minutes for both stopping and starting the instance before the command times out. If you want to specify a custom wait time, you can do so by using the `--timeout` option in the `amc stop` command.

    amc restart <instance_id> --timeout 10m

## Related topics
* {ref}`howto-create-instance`
* {ref}`howto-start-instance`
* {ref}`howto-stop-instance`

(howto-ts-lxd-clustering)=
# Troubleshoot issues with LXD clustering

The following issues might occur if you use clustering.

## AMS hook failed: `lxd-relation-changed`

*Applies to: Anbox Cloud*

> I see an error message like the following in the output of `juju debug-log --include ams`:
>
> ```
> unit-ams-0: 13:30:51 INFO unit.ams/0.juju-log Error adding LXD node lxd5 to AMS: 1 - Flag --timeout has been deprecated, Using the timeout argument has no longer an effect as cancelling cluster operations is not supported
> Error: Get "https://10.25.83.151:8443": Unable to connect to: 10.25.83.151:8443
> unit-ams-0: 13:30:51 ERROR unit.ams/0.juju-log Hook error:
> Traceback (most recent call last):
>   File "/var/lib/juju/agents/unit-ams-0/.venv/lib/python3.8/site-packages/charms/reactive/__init__.py", line 74, in main
>     bus.dispatch(restricted=restricted_mode)
>   File "/var/lib/juju/agents/unit-ams-0/.venv/lib/python3.8/site-packages/charms/reactive/bus.py", line 390, in dispatch
>     _invoke(other_handlers)
>   File "/var/lib/juju/agents/unit-ams-0/.venv/lib/python3.8/site-packages/charms/reactive/bus.py", line 359, in _invoke
>     handler.invoke()
>   File "/var/lib/juju/agents/unit-ams-0/.venv/lib/python3.8/site-packages/charms/reactive/bus.py", line 181, in invoke
>     self._action(*args)
>  File "/var/lib/juju/agents/unit-ams-0/charm/reactive/ams.py", line 356, in endpoint_lxd_changed
>     process_cluster_changes(lxd)
>   File "/var/lib/juju/agents/unit-ams-0/charm/reactive/ams.py", line 333, in process_cluster_changes
>     update_lxd_nodes_in_service(nodes, use_node_state=True)
>   File "/var/lib/juju/agents/unit-ams-0/charm/reactive/ams.py", line 966, in update_lxd_nodes_in_service
>     if add_lxd_node_to_service(n) and use_node_state:
>   File "/var/lib/juju/agents/unit-ams-0/charm/reactive/ams.py", line 1061, in add_lxd_node_to_service
>     raise ex
>   File "/var/lib/juju/agents/unit-ams-0/charm/reactive/ams.py", line 1050, in add_lxd_node_to_service
>     check_output(cmd, stderr=STDOUT)
>   File "/usr/lib/python3.8/subprocess.py", line 415, in check_output
>     return run(*popenargs, stdout=PIPE, timeout=timeout, check=True,
>   File "/usr/lib/python3.8/subprocess.py", line 516, in run
>     raise CalledProcessError(retcode, process.args,
> subprocess.CalledProcessError: Command '['amc', 'node', 'add', 'lxd5', '10.25.83.151', '--storage-device', 'dir', '--network-bridge-mtu', '1500', '--timeout', '5m']' returned non-zero exit status 1.
> ```
> What is the problem, and how can I fix it?

This error indicates a faulty LXD node. Most likely, something went wrong when AMS tried adding a new LXD node to the cluster, either because the LXD node was not available on the network or the node failed to join the cluster for unknown reasons.

The easiest way to make the AMS unit work again is to remove the faulty LXD node (`lxd/5` in this example) by running the following command:

    juju remove-unit --force lxd/5

```{note}
Add `--destroy-storage` to the command if you allocated dedicated storage for LXD.
```

After the LXD unit is successfully removed, resolve the failed hook of the AMS unit. To do that, first disable automatic retries to prevent Juju from re-running the failed hook:

    juju model-config automatically-retry-hooks=false

Wait for any pending hook execution to finish. Check `juju status` to monitor the status.

Once the model has settled, resolve the failed hook by running the following command:

    juju resolve ams/0 --no-retry

Check the `juju status` output. The status of the `ams/0` unit should switch back to `active`.

To verify that the LXD cluster is still correctly in place, compare the output of `juju ssh ams/0 -- amc node ls` and `juju ssh lxd/0 -- lxc cluster ls`. Both commands should list the same LXD nodes.

Finally, enable automatic retries again:

    juju model-config automatically-retry-hooks=true
(ref-hooks)=
# Hooks

Hooks are scripts that automatically trigger actions based on an event performed in the life cycle of an instance. A hook can be any executable file that is placed in the `hooks` directory of an addon or an application folder.

The hook name **must** be one of the following:

| Name                 | Description      |
|----------------------|---------------------|
| pre-start            | Executed **before** Android is started. If the hook fails to execute, the instance fails to start and has an error status.  |
| post-start           | Executed **after** Android is started. If the hook fails to execute, the instance stops with an error.              |
| post-stop            | Executed **after** Android is stopped. If the instance fails to start, this hook will not be invoked. If the hook fails to execute, the instance stops with an error.  |
| install (deprecated) | DEPRECATED: Use `pre-start` instead. Executed during the application bootstrap when the addon is installed.          |
| prepare (deprecated) | DEPRECATED: Use `post-start` instead. Executed during the application bootstrap when Android is running.             |
| restore (deprecated) | DEPRECATED: Use `pre-start` instead. Executed before Android starts.                                                 |
| backup (deprecated)  | DEPRECATED: Use `post-stop` instead. Executed after Android shuts down.                                              |

A failed hook will cause the instance to stop immediately and end up in an error state. In such cases, see {ref}`howto-view-instance-logs` to further investigate the causes of failure.

The following figure shows when the different hooks are executed in the life cycle of a base or a regular instance.

![Hooks execution in the life cycle of an instance |471x601](https://assets.ubuntu.com/v1/8441e690-addons-reference-hook-order.png)

(sec-env-variables)=
## Environment variables

When hooks are invoked, several environment variables are set to provide context to the addon.

The following variables are available:

| Name             | Description         | Possible values         |
|------------------|----------------------|------------------------|
| `ADDON_DIR`      | Directory of the addon whose hook is currently running. |                         |
| `APP_DIR`        | Path to the Anbox application directory.                | `/var/lib/anbox/app`    |
| `ANBOX_DIR`      | Path to the Anbox directory.                            | `/var/lib/anbox`        |
| `ANDROID_ROOTFS` | Path to the Android RootFS.                             | `/var/lib/anbox/rootfs` |
| `BOOT_PACKAGE`   | Boot package of the APK.                                |                         |
| `CONTAINER_TYPE` | Type of container being run. This variable is now deprecated. Use `INSTANCE_TYPE` instead.                   | `regular` (container running an application or a raw image)<br/>`base` (container bootstrapping, thus creating or updating, an application)|
| `INSTANCE_TYPE`  | Type of instance being run      | `regular` (instance running an application or a raw image)<br/>`base` (instance bootstrapping, thus creating or updating, an application)|
| `ANBOX_EXIT_CODE`| *`post-stop` hook only:* Exit code of the Anbox process.| `0` if no error occurred, otherwise set to the actual return code.|

## Hook timeouts

By default, all hooks are subject to a 5 minute timeout to avoid blocking an instance for too long. The timeout can be configured through the `hooks.timeout` key in the addon or application manifest. For example:

```yaml
...
hooks:
  timeout: 15m
...
```

A hook that runs into a timeout exits with an error. Timeout values longer than 15 minutes are considered invalid.

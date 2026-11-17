---
myst:
  html_meta:
    "description": "Explanation of instances in Anbox Cloud, covering lifecycle states, types, resource handling, and how each runs a full Android system."
---

(exp-instances)=
# Instances

Instances are the center piece of the Anbox Cloud stack. You can create an instance from an image or copy an existing instance. Every instance provides a full Android system managed by Anbox Management Service (AMS) and belongs to exactly one {ref}`project`<exp-projects>, which defines its network and access scope.


Anbox Cloud **DOES NOT** back up any data from the Android or the outer Ubuntu instance. Backup and restore of data must be implemented separately through addons. See {ref}`howto-backup-restore-example` for information on how to do this.

(sec-instances-and-projects)=
## Instances and projects

Every instance belongs to exactly one {ref}`project <exp-projects>`. A project gives its instances a shared network and access scope:

- Network:  An instance connects to its project's LXD-managed network, which is isolated from other project networks by default.
- Access: a group can act on an instance only if it has access to the instance's project, in addition to any instance-level permissions. See {ref}`configure user permission page <howto-auth>`.

You choose the project when you create the instance. If you do not specify one, the instance is placed in the default project. An instance cannot be moved to another project after it is created.

(sec-instances-from-images)=
## Instances created from images

You create an instance from an {ref}`image <ref-provided-images>`. The instance runs the full Android system, without any additional apps installed. The image determines the {ref}`Android execution model <exp-android-execution-models>` of the instance: containerized Android or virtualized Android.

Instances created from images are called *raw instances*.

(sec-application-instances)=
## Instances created from applications (deprecated)

```{important}
Applications are deprecated and are available only for instances with containerized Android. See {ref}`ref-deprecation-notes`.
```

If you use {ref}`applications <exp-applications>`, AMS works with two additional kinds of instances:

- **Application instances** are created when you launch an application and run the full Android system. If the application is based on an Android app (an APK package), the app is launched after the system boots and is monitored by the {ref}`sec-application-manifest-watchdog`. With the default configuration, you see only the app and not the Android launcher.
- **Base instances** are temporary instances that AMS uses to bootstrap an application. They are deleted automatically when the bootstrap completes. See {ref}`sec-application-bootstrap` for more information on the bootstrapping process.

The `TYPE` column in the `amc ls` output shows `base` for base instances and `regular` for all other instances. Instances created from images are always regular instances.

## Life cycle of an instance

This section describes the life cycle of instances with {ref}`containerized Android <exp-android-execution-models>`.

```{important}
Applications, addons, and hooks are deprecated. See {ref}`ref-deprecation-notes`. To replace hooks, see {ref}`howto-migrate-from-addon-and-app-hooks`.
```

### Creating an instance

When you create an instance, AMS schedules it on a LXD node. The instance then executes the following steps in order:

1. Configure the network interface and gateway.
2. (Only for raw instances) Install addons that are specified with `--addons`.
3. Expose services that are specified with `--service` or through the application manifest.
4. Execute the `pre-start` hook provided by the installed addons.
5. Launch the Android container.
6. Execute the `post-start` hook provided by the installed addons.

![Instance start|584x646](/images/instance_start.png)

Launching an instance is successful only if all of the above steps succeed. If there are issues during the process, the status of the instance changes to `error`. You can view the available logs from the instance for further troubleshooting. See {ref}`howto-view-instance-logs`.

### Stopping an instance

Instances can be stopped because of the following scenarios:

- You stopped it.
- You deleted it.
- An error occurred.

When an instance is stopped, it executes the following steps in order:

1. Stop the Android container.
2. Execute the `post-stop` hook provided by the installed addons.
3. Shut down the instance.

Beyond that, an instance is removed from AMS only when you delete it. An instance in the `error` status remains in AMS until you delete it.

![Instance stop|575x521](/images/instance_stop.png)

## Possible instance statuses

An instance moves through different stages and correspondingly can have the following statuses depending on its current state.

| Status            |  Description |
|-------------------|--------------|
| `created`         | AMS has created an internal database object for the instance and will next schedule the instance onto a suitable LXD node. |
| `prepared`        | AMS has decided the LXD node on which it will schedule the instance. |
| `started`         | The instance is started and Android is booting. The instance switches to `running` when the boot completes. |
| `running`         | The instance is fully up and running. |
| `stopped`         | The instance has been stopped and can be restarted when required.|
| `deleted`         | The instance has been deleted and will be removed from the AMS database soon. |
| `error`           | An error occurred while processing the instance. The instance is stopped. |
| `unknown`         | A possible error occurred and the real state of the instance cannot be determined. |

If you encounter the `error` or the `unknown` status, use [`amc show <instance_id>`](/reference/cmd-ref/amc/ams.amc_show.md) or [`amc show-log`](/reference/cmd-ref/amc/ams.amc_show-log.md) to troubleshoot. If you are still unable to figure out the issue, [file a bug](https://bugs.launchpad.net/anbox-cloud) with the {ref}`relevant instance logs <sec-view-stored-logs>`.

(sec-dev-mode)=
## Development mode

AMS allows starting an instance in development mode. This mode turns off some features that are usually active in an instance. It is mainly useful when developing addons inside an instance.

When development mode is enabled, the instance sends status updates to AMS when the Anbox runtime is terminated, however, AMS allows the instance to continue running. This allows you to restart the Anbox runtime inside the instance, providing an easy way to test addons or develop a platform plugin.

To check whether development mode is enabled, run `amc show <instance_ID>`. If the `devmode` field in the configuration file is set to `true`, development mode is active.

## Related topics

- {ref}`exp-android-execution-models`
- {ref}`howto-instance`
- {ref}`howto-create-instance`
- {ref}`howto-migrate-from-addon-and-app-hooks`

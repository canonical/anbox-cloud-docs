---
myst:
  html_meta:
    "description": "How to migrate from addon or application hooks (pre-start, post-start, post-stop) to a systemd service built into an Anbox image."
---

(howto-migrate-from-addon-and-app-hooks)=
# Migrate from app/addon hooks to system units

```{important}
Addons and application hooks are deprecated and will be removed from Anbox Cloud. See {ref}`ref-deprecation-notes` for the exact release in which support ends.
```

Addon and application hooks (`pre-start`, `post-start`, `post-stop`) are available only for instances with containerized Android (`jammy:*` images) and are not supported for virtualized Android (see {ref}`exp-android-execution-models`).

This guide shows how to replace addon and application hook behavior with a `systemd` unit baked into a custom Anbox image. This approach works for both containerized and virtualized Android and does not depend on the addon subsystem.

## Identify what your hook depends on

Before rewriting your hook as a systemd unit, identify its dependencies. Hook scripts had access to environment variables injected by the Anbox runtime that are not available in systemd. Review your existing hook scripts for the variables below and replace each one with its systemd equivalent.

| Hook variable | Migration |
| --- | --- |
| `APP_DIR` | Use `/var/lib/anbox/app` directly. |
| `ANBOX_DIR` | Use `/var/lib/anbox` directly. |
| `ANDROID_ROOTFS` | Use `/var/lib/anbox/rootfs` directly. |
| `BOOT_PACKAGE` | Use the `boot-package` attribute from the application manifest file directly in the script instead of `BOOT_PACKAGE`. |
| `INSTANCE_TYPE` |  Check whether `/var/lib/anbox/bootstrap.yaml` exists. Its presence indicates a `regular` instance; its absence indicates a `base` instance. |
| `CONTAINER_TYPE` |This variable is deprecated. Use the same `/var/lib/anbox/bootstrap.yaml `check described for `INSTANCE_TYPE`. |
| `ANBOX_EXIT_CODE` | Query `anbox.service` directly for the exit code: `systemctl show anbox.service --property=ExecMainStatus`. |

## General workflow

To run a script before or after Android starts, or after Android stops, follow this workflow:

1. Launch an instance from a container image.
2. Inside that instance, write a `systemd` unit that runs your script at the desired point in the Android life cycle, relative to the `anbox.service` unit, which represents the Anbox runtime.
3. Enable the unit to automatically activate upon the initial startup or every startup of an instance created from this image.
4. Publish the modified instance as a new image.
5. Launch future instances from this custom image instead of relying on an addon or application.

The following sections show concrete examples for each of the three hooks that addons or applications used to provide.

## Launch and access a source instance

Launch an instance to use as the base for your custom image:

    amc launch --name source-inst jammy:android15:amd64
    amc shell source-inst

All steps below run inside this instance.

### Replace a `pre-start` hook

If you need a script to run on every start before Android starts, create a one-shot unit that starts before `anbox.service` is up and running:

1. Inside the instance, create the unit file, for example `/etc/systemd/system/app-pre-start.service`:

      ```systemd
      [Unit]
      Description=Run a script before Android starts
      Before=anbox.service

      [Service]
      Type=oneshot
      ExecStart=/usr/local/bin/pre-start.sh
      TimeoutStartSec=10min

      [Install]
      WantedBy=anbox.service
      ```
1. Verify the unit file for any syntax or spelling errors:

      sudo systemd-analyze verify /etc/systemd/system/app-pre-start.service

1. Add your script (`/usr/local/bin/pre-start.sh` in this example), make it executable, then enable the unit.

      sudo chmod +x /usr/local/bin/pre-start.sh
      sudo systemctl daemon-reload
      sudo systemctl enable app-pre-start.service

```{note}
AMS waits for an instance to become fully up and running with a maximum timeout of 15 minutes. Consequently, all scripts should be as lightweight as possible and avoid long-running operations. We recommend setting an appropriate `TimeoutStartSec` in the unit file to prevent instance launches from failing due to long-running operations in the pre-start unit.
```

### Replace a `post-start` hook

If you need a script to run every time after Android starts, create a one-shot unit that starts after anbox.service is up and running.

1. Inside the instance, create the unit file, for example `/etc/systemd/system/app-post-start.service`:

      ```systemd
      [Unit]
      Description=Run a script after Android has started
      After=anbox.service
      Requires=anbox.service

      [Service]
      Type=oneshot
      ExecStart=/usr/local/bin/post-start.sh

      [Install]
      WantedBy=multi-user.target
      ```

1. Add your script (`/usr/local/bin/post-start.sh` in this example), make it executable, and enable it the same way as in the previous section.

### Replace a `post-stop` hook

If you need a script to run after Android was stopped, bind a unit to the life cycle of `anbox.service` and run your cleanup or data backup logic in `ExecStop`, so it executes whenever `anbox.service` stops:

1. Inside the instance, create the unit file, for example `/etc/systemd/system/app-post-stop.service`:

      ```systemd
      [Unit]
      Description=Run a script after Android has stopped
      Before=anbox.service
      BindsTo=anbox.service

      [Service]
      Type=oneshot
      ExecStop=/usr/local/bin/post-stop.sh
      RemainAfterExit=yes

      [Install]
      WantedBy=anbox.service
      ```

1. Add your script (`/usr/local/bin/post-stop.sh` in this example), make it executable, and enable it the same way as in the previous section.

## Publish and use custom image

Once your units and scripts are in place inside the instance, publish it as a new image(see {ref}`howto-publish-instance-as-image`) and use it for future instances:

    amc publish source-inst --name custom-image --force
    amc launch --name new-instance custom-image

Verify that your system units ran as expected by checking the instance logs(see {ref}`howto-view-instance-logs`),

    amc logs new-instance

Or check the logs of a specific system unit,

    amc exec new-instance -- journalctl -u app-pre-start.service

## Related topics

- {ref}`ref-hooks`
- {ref}`ref-deprecation-notes`
- {ref}`howto-publish-instance-as-image`
- {ref}`howto-create-instance`
- {ref}`howto-view-instance-logs`

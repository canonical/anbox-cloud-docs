---
myst:
  html_meta:
    "description": "How to work with Anbox Cloud addons, including creating hooks, enabling addons globally, updating, and migrating from deprecated hooks."
---

(howto-addons)=
# Addons

```{important}
These guides apply to images with containerized Android (`jammy:*`). Addons are not supported for images with virtualized Android. See {ref}`exp-android-execution-environments` for details.
```

Addons customize the images used for instances. You can use addons to:

- Enable SSH access for automation tools ({ref}`howto-create-addon`)
- Install additional tools in the instance ({ref}`howto-install-tools-example`)
- Set up user-specific data when starting an application ({ref}`howto-backup-restore-example`)
- Back up data when the instance is stopping ({ref}`howto-backup-restore-example`)
- Configure the Android system before running the application ({ref}`howto-customize-android-example`)
- Provide support for other platforms ({ref}`howto-emulate-platforms-example`)

To manage existing addons:

- {ref}`howto-enable-addons-globally`
- {ref}`howto-update-addons`

If you used addons before Anbox Cloud 1.12, refer to {ref}`howto-migrate-addons` to update your addons to use the new hooks.

## See also

- Explanation: {ref}`exp-addons`
- Reference: {ref}`ref-addon-manifest`

```{toctree}
:hidden:


create-addon
enable-addons-globally
migrate-addon
update-addon
examples
```

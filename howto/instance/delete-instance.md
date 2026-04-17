---
html_meta:
  description: 'Delete an instance. An instance can be deleted, which will cause any
    connected user to be disconnected immediately. CLI :sync: cli Provide the ID of
    the.'
---
(howto-delete-instance)=
# Delete an instance

An instance can be deleted, which will cause any connected user to be disconnected immediately.

::::{tab-set}
:::{tab-item} CLI
:sync: cli

Run:

    amc delete <instance_id>

Provide the ID of the instance that you want to delete.

In some cases, it is helpful to delete all instances currently available.
The `amc` command provides a `--all` flag for this, but be careful while performing a deletion of all instances.

    amc delete --all
:::

:::{tab-item} Dashboard
:sync: dashboard

On the *Instances* page, click *Delete* ( ![delete application icon](/images/icons/delete-icon.png) ) and confirm the deletion.

:::
::::

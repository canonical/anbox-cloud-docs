---
myst:
  html_meta:
    "description": "How to delete a project in Anbox Cloud with amc project delete or the dashboard, including force deletion and instance deletion protection."
---

(howto-delete-project)=
# Delete a project

This guide walks you through deleting a project using the CLI or the dashboard.

You need administrator access or the `can_delete` entitlement on the project.

The `default` project cannot be deleted.

## Delete the project

A project must be empty before you delete it. If it contains instances, delete them first using {ref}`howto-delete-instance` or use force deletion to remove the project and its instances together.

If any instances have deletion protection enabled, see {ref}`sec-disable-instance-delete-protection` first.

```{important}
Force deletion permanently deletes the project, its instances and their data. This cannot be undone.
```

::::{tab-set}
:::{tab-item} CLI
:sync: cli

To delete an empty project, run:

    amc project delete <project_name>

To delete the project and any instances it contains, run:

    amc project delete <project_name> --force

Check that the project no longer appears in the list:

    amc project list
:::

:::{tab-item} Dashboard
:sync: dashboard

1. Open the project selector and select **Manage projects**.
1. On the *Projects* page, click anywhere in the project's row except the project name to open the *Project details* side panel. Clicking the project name opens the project's *Instances* page.
1. In the side panel, select **Delete**.
1. If the project contains instances, select the *Force delete* checkbox.
1. Confirm the deletion.
1. Check that the project no longer appears on the *Projects* page.
:::
::::

(sec-disable-instance-delete-protection)=
## Disable instance deletion protection

Instances with deletion protection enabled block deletion of their project, including force deletion.

Identify the protected instances and disable `security.delete_protected` only on those you intend to delete. Then retry the project deletion.

For instructions, see {ref}`howto-configure-instance` and {ref}`ref-ams-instance-configuration`.

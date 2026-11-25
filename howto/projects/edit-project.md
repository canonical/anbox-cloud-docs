---
myst:
  html_meta:
    "description": "How to edit a project description in Anbox Cloud with amc project set or the dashboard."
---

(howto-edit-project)=
# Edit a project

This guide walks you through updating a project's description using the CLI or the dashboard.

You need administrator access or the `can_edit` entitlement on the project. The `editor` entitlement set alone does not allow editing the project itself.

You cannot change the name of a project after creation. The `default` project cannot be edited.

::::{tab-set}
:::{tab-item} CLI
:sync: cli

View the project's current settings:

    amc project show <project_name>

Update the description:

    amc project set <project_name> description <value>

Check the updated description:

    amc project show <project_name>
:::

:::{tab-item} Dashboard
:sync: dashboard

1. Open the project selector and select **Manage projects**.
1. On the *Projects* page, click anywhere in the project's row except the project name to open the *Project details* side panel. The project name links to the project's *Instances* page.
1. In the side panel, select **Edit**.
1. Update the *Description*.
1. Save your changes.
1. Check that the updated description appears on the *Projects* page.
:::
::::

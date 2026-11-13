---
myst:
  html_meta:
    "description": "How to create a project in Anbox Cloud with amc project create or the dashboard to group instances."
---

(howto-create-project)=
# Create a project

This guide walks you through creating a project using the CLI or the dashboard. For an overview of projects, see {ref}`exp-projects`.

You need administrator access or the global `can_create_projects` entitlement.

::::{tab-set}
:::{tab-item} CLI
:sync: cli

To create a project, run:

    amc project create <project_name>

Replace `<project_name>` with the name you want to assign to the project.

To include a description, run:

    amc project create <project_name> --description "<project_description>"

Check that the project appears in the list of projects:

    amc project list
:::

:::{tab-item} Dashboard
:sync: dashboard

1. Open the project selector and select **Manage projects**.
1. On the *Projects* page, select **Create project**.
1. Enter a *Name*.
1. Optionally, enter a *Description*.
1. Select **Create**.
1. Check that the project appears on the *Projects* page.
:::
::::

To create instances in the project, see {ref}`howto-create-instance`.

## Related topics

- Explanation: {ref}`exp-projects`
- How-to guide: {ref}`howto-auth`
- How-to guide: {ref}`howto-create-instance`

---
myst:
  html_meta:
    "description": "How to list and view projects in Anbox Cloud with amc project list and amc project show or the dashboard."
---

(howto-list-projects)=
# List projects

This guide walks you through listing projects and viewing their status, subnet and instance count using the CLI or the dashboard.

::::{tab-set}
:::{tab-item} CLI
:sync: cli

List the projects available to your identity:

    amc project list

To view a project's details, run:

    amc project show <project_name>

Check its status, description and subnet.
:::

:::{tab-item} Dashboard
:sync: dashboard

1. Open the project selector.
1. Select **Manage projects**.

The *Projects* page lists projects with their status, description, subnet and instance count.

To work with a project's instances, open the project selector and select that project.
:::
::::

If no projects are listed, check that your group has project access. See {ref}`howto-auth`.

To list instances in a project, see {ref}`howto-list-instances`.

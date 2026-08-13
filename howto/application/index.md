---
myst:
  html_meta:
    "description": "How to manage Anbox Cloud applications, including creating, updating, deleting, extending with addons, and streaming."
---

(howto-manage-applications)=
# Manage applications

```{important}
These guides apply to images with containerized Android (`jammy:*`). The application model is not supported for images with virtualized Android. See {ref}`exp-android-execution-models` for details.
```

## Create and manage

Applications are packaged from Android APKs, extended with addons or hooks, and updated as needed.

- {ref}`howto-create-application`
- {ref}`howto-update-application`
- {ref}`howto-extend-application`
- {ref}`howto-pass-custom-data-application`
- {ref}`howto-wait-for-application`

## Stream and test

Once ready, applications can be streamed to users or tested with automated UI frameworks.

- {ref}`howto-stream-applications`
- {ref}`howto-test-application`

## List and delete

View all registered applications or permanently remove ones you no longer need.

- {ref}`howto-list-applications`
- {ref}`howto-delete-application`

## See also

- Explanation: {ref}`exp-applications`
- Reference: {ref}`ref-application-manifest`

```{toctree}
:hidden:

create-application
delete-application
extend-application
list-applications
stream-application
test-application
update-application
Pass custom data <pass-custom-data>
wait-for-application
```

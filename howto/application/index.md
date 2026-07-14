---
myst:
  html_meta:
    "description": "How to manage Anbox Cloud applications, including creating, updating, deleting, extending with addons, and streaming."
---

(howto-manage-applications)=
# Manage applications

The guides in this section describe how to manage your applications.

```{important}
These guides apply to images with containerized Android (`jammy:*`). The application model is not supported for images with virtualized Android. See {ref}`exp-android-execution-environments` for details.
```

See {ref}`exp-applications` for an introduction to how applications are used in Anbox Cloud. To check which configuration options are available for applications, see {ref}`ref-application-manifest`.

## Create and configure

- {ref}`howto-create-application`
- {ref}`howto-update-application`
- {ref}`howto-pass-custom-data-application`
- {ref}`howto-extend-application`

## Run and stream

- {ref}`howto-wait-for-application`
- {ref}`howto-stream-applications`
- {ref}`howto-test-application`

## List and remove

- {ref}`howto-list-applications`
- {ref}`howto-delete-application`

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

---
myst:
  html_meta:
    "description": "How to work with the Anbox runtime, including addon development in developer mode and building custom platform plugins."
---

(howto-anbox-runtime)=
# Work with the Anbox runtime

```{important}
These guides apply to images with containerized Android (`jammy:*`). For virtualized Android, see {ref}`tut-getting-started-virtualized-android` and {ref}`howto-package-custom-android-build`.
```

The Anbox runtime runs the Android container, provides access to hardware, and integrates with streaming protocols. To work with Anbox runtime:

- {ref}`howto-develop-addons-devmode`
- {ref}`howto-develop-platform-plugin`

```{toctree}
:hidden:

develop-addon-devmode
develop-platform-plugin
```

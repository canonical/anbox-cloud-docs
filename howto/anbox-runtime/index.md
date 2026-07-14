---
myst:
  html_meta:
    "description": "How to work with the Anbox runtime, including addon development in developer mode and building custom platform plugins."
---

(howto-anbox-runtime)=
# Work with the Anbox runtime

The Anbox runtime is responsible for running the Android container, providing access to hardware, and integrating with streaming protocols. These guides apply to images with containerized Android (`jammy:*`).

For virtualized Android (`resolute:*-cf:*`), see {ref}`tut-getting-started-virtualized-android` and {ref}`howto-package-custom-android-build`.
- {ref}`howto-develop-addons-devmode`
- {ref}`howto-develop-platform-plugin`

```{toctree}
:hidden:

develop-addon-devmode
develop-platform-plugin
```

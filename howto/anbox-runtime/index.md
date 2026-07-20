---
myst:
  html_meta:
    "description": "How to work with the Anbox runtime, including addon development in developer mode and building custom platform plugins."
---

(howto-anbox-runtime)=
# Work with the Anbox runtime

The guides in this section describe how to work with the Anbox runtime, which is responsible for running the Android container, providing access to any hardware and integrating with streaming protocols. They apply to images with containerized Android (`jammy:*`).

For images with virtualized Android (`resolute:*-cf:*`), see {ref}`tut-getting-started-virtualized-android` and {ref}`howto-package-custom-android-build`. For a comparison of the two execution models, see {ref}`exp-android-execution-models`.

The following guides are available:

```{toctree}
:titlesonly:

develop-addon-devmode
develop-platform-plugin
```

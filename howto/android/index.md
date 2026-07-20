---
myst:
  html_meta:
    "description": "How to work with Android in Anbox Cloud, including ADB access, custom VHAL configuration, graphics debugging, and SMS simulation."
---

(howto-Android)=
# Work with Android

These guides cover Android-specific tasks, including debugging instances with ADB and integrating custom VHAL implementations for automotive use cases.

## Access and debug

- {ref}`howto-access-android-instance`
- {ref}`howto-debug-graphics-renderdoc`
- {ref}`howto-simulate-incoming-sms`

## Integrate with Android Automotive

- {ref}`howto-integrate-hidl`
- {ref}`howto-replace-anbox-vhal`
- {ref}`howto-set-automotive-properties`

```{toctree}
:hidden:

access-android-instance
debug-graphics-renderdoc
integrate-hidl
custom-vhal
set-automotive-properties
simulate-incoming-sms

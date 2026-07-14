---
myst:
  html_meta:
    "description": "How to work with Android in Anbox Cloud, including ADB access, custom VHAL configuration, graphics debugging, and SMS simulation."
---

(howto-Android)=
# Work with Android

These guides cover Android-specific tasks such as debugging and automotive integration.

To access and debug Android instances:

- {ref}`howto-access-android-instance`
- {ref}`howto-debug-graphics-renderdoc`

To integrate with Android Automotive (AAOS):

- {ref}`howto-integrate-hidl`
- {ref}`howto-replace-anbox-vhal`
- {ref}`howto-set-automotive-properties`

To simulate Android system behavior:

- {ref}`howto-simulate-incoming-sms`

```{toctree}
:hidden:

access-android-instance
debug-graphics-renderdoc
integrate-hidl
custom-vhal
set-automotive-properties
simulate-incoming-sms

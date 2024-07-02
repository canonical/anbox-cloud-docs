(howto-customise-android-example)=
# Example: Customise Android

To do any customisation to the Android system that runs your application, use the `anbox-shell` tool within a hook. This tool is useful to interact with the Android system directly.

In this example, we create a hook that configures the Android system to use an HTTP proxy:

```bash
#!/bin/sh -ex

# The settings we change are persistent, so we only need to set them once
if [ "$INSTANCE_TYPE" = "regular" ]; then
  exit 0
fi

anbox-shell settings put global http_proxy myproxy:8080
```

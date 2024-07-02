(howto-install-tools-example)=
# Example: Install tools

Application images are designed to be as lightweight as possible, and as such, common tools you might expect to see in a regular cloud image might not be available.

You can use hooks to install packages that you require for your application. In this example, we'll install `curl` and `python3`.

To do so, create a new addon with the following `pre-start` hook:

```bash
#!/bin/bash -e

# We only need to install things once when the image is being created, so we
# don't need to execute the hook when users are running the application.
if  [ "$INSTANCE_TYPE" = "regular" ]; then
  exit 0
fi

apt update -q
apt install -y curl python3
```

When an application is created or updated with this addon, both `curl` and `python3` will be installed and made available for other hooks to use.

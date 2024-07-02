(tut-create-addon)=
# Create an addon

This tutorial guides you through the creation of a simple addon. The addon that we create in this tutorial is an example for enabling SSH access on a container.

## Write the addon metadata

In a new `ssh-addon` directory, create a `manifest.yaml` file with the following content:
```yaml
name: ssh
description: |
  Enable SSH access when starting a container
```

## Add a hook

Next to your `manifest.yaml` file in the `ssh-addon` directory, create a `hooks` directory. This is where we'll put the hooks we want to implement.

Hooks can be implemented in any language, but we are using a bash script here.

In the `hooks` directory, create a `pre-start` file with the following content:

```bash
#!/bin/bash

if [ "$INSTANCE_TYPE" = "regular" ]; then
  exit 0
fi

mkdir -p ~/.ssh
cat "$ADDON_DIR"/ssh-addon-key.pub >> ~/.ssh/authorized_keys
```

Make the file executable. To do so, enter the following command (in the `ssh-addon` directory):
```bash
chmod +x hooks/pre-start
```

```{tip}
- Supported hooks are `pre-start`, `post-start` and `post-stop`.
- Use the `INSTANCE_TYPE` variable to distinguish between regular and base instances.

See {ref}`ref-hooks` for more information.
```
Create an SSH key in your addon directory and move the private key to a location outside of the addon directory (for example, your home directory):
```bash
ssh-keygen -f ssh-addon-key -t ecdsa -b 521
mv ssh-addon-key ~/
```
Alternatively, you can use an existing key and move the public key into the addon directory.

## Create the addon

Your addon structure currently looks like this:
```bash
ssh-addon
├── hooks
│   └── pre-start
├── manifest.yaml
└── ssh-addon-key.pub
```

Create the addon with `amc` by entering the following command (in the directory that contains the `ssh-addon` directory):
```bash
amc addon add ssh ./ssh-addon
```

When your addon is created, you can view it with:
```bash
amc addon list
```

## Use the addon in an application

Create an application manifest file (`my-application/manifest.yaml`) and include the addon name under `addons`:

```yaml
name: my-application
resources:
  cpus: 4
  memory: 3GB
  disk-size: 3GB
addons:
  - ssh
```

Then create your application:
```bash
application_id=$(amc application create ./my-application)
amc wait "$application_id" -c status=ready
```

The `amc wait` command returns when your application is ready to launch. You can now launch an instance of your application:
```bash
amc launch my-application --service +ssh
```

```{note}
The SSH port 22 is closed by default. In the above command, we open it by exposing its service by using `--service`. See {ref}`howto-expose-services` for more information.
```

You can now access your container via SSH:
```bash
ssh -i ~/ssh-addon-key root@<container_ip> -p <exposed port>
```

```{note}
The exposed port can be found be running `amc ls`, under the `ENDPOINTS` column. Exposed ports usually start around port 10000.
```

## Related topics

* {ref}`exp-addons`
* {ref}`howto-update-addons`
* {ref}`howto-extend-application`
* {ref}`ref-addon-manifest`

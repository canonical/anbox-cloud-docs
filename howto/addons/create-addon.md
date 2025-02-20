(howto-create-addon)=
# How to create an addon

Addons help you extend and customize your applications in Anbox Cloud. To create or update an addon, you need a specific file structure for the directory containing your addon files.

This how-to guide helps you create an addon and use it in an application.

The directory containing the addon files must also contain the following:

- The addon manifest file named `manifest.yaml`. See {ref}`ref-addon-manifest` to learn about valid keys in an addon manifest file.
- A directory named `hooks`. This directory must contain at least one executable file with a valid hook name.

Any other files in the addon directory are bundled with the addon. They can be accessed in a hook by using the `$ADDON_DIR` environment variable. See {ref}`sec-env-variables` for more information.

For example:

```bash
cat "$ADDON_DIR"/public_key.pem >> ~/.ssh/authorized_keys
```

To create an addon, you must provide the Anbox Management Client (AMC) with either of the following:
* The addon directory
* A tarball containing the required addon file structure
* A zip archive containing the required addon file structure

Let's look at an example for of an addon for enabling SSH access on a container.

## Write the addon metadata

In a new `ssh-addon` directory, create a `manifest.yaml` file with the following content:
```yaml
name: ssh
description: |
  Enable SSH access when starting a container
```

## Add a hook

In the `ssh-addon` directory, create a `hooks` directory. Hooks can be implemented in any language, this example uses a bash script.

In the `hooks` directory, create a `pre-start` file with the following content:

```bash
#!/bin/bash

if [ "$INSTANCE_TYPE" = "regular" ]; then
  exit 0
fi

mkdir -p ~/.ssh
cat "$ADDON_DIR"/ssh-addon-key.pub >> ~/.ssh/authorized_keys
```

To make the `pre-start` file executable, run the following command in the `ssh-addon` directory:

        chmod +x hooks/pre-start

```{tip}
- Supported hooks are `pre-start`, `post-start` and `post-stop`.
- Use the `INSTANCE_TYPE` variable to distinguish between regular and base instances.

See {ref}`ref-hooks` for more information.
```
Create an SSH key in your addon directory and move the private key to a location outside of the addon directory:

        ssh-keygen -f ssh-addon-key -t ecdsa -b 521
        mv ssh-addon-key ~/

Alternatively, you can use an existing key and move the public key into the addon directory.

## Create the addon

Your addon structure currently looks like this:

```terminal
ssh-addon
├── hooks
│   └── pre-start
├── manifest.yaml
└── ssh-addon-key.pub
```

In the parent directory of the `ssh-addon` directory, run the following command to create the addon:

        amc addon add ssh ./ssh-addon

When your addon is created, you can view it with:

        amc addon list


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

        application_id=$(amc application create ./my-application)
        amc wait "$application_id" -c status=ready

The `amc wait` command returns when your application is ready to launch. You can now launch an instance of your application:

        amc launch my-application --service +ssh

```{note}
The SSH port 22 is closed by default. In the above command, we open it by exposing its service by using `--service`. See {ref}`howto-expose-services` for more information.
```

You can now access your container via SSH:

        ssh -i ~/ssh-addon-key root@<container_ip> -p <exposed port>


```{note}
Exposed ports usually start around port 10000. `amc ls` displays the export port under the `ENDPOINTS` column.
```

## Related topics

* {ref}`exp-addons`
* {ref}`howto-update-addons`
* {ref}`howto-extend-application`
* {ref}`ref-addon-manifest`

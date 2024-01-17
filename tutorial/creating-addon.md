This tutorial guides you through the creation of a simple [addon](https://discourse.ubuntu.com/t/managing-addons/17759). The addon that we create in this tutorial is an example for enabling SSH access on a container.

### 1. Write the addon metadata
In a new `ssh-addon` directory, create a `manifest.yaml` file with the following content:
```yaml
name: ssh
description: |
  Enable SSH access when starting a container
```

### 2. Add a hook
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

[note type="information" status="Tip"]

- Supported hooks are `pre-start`, `post-start` and `post-stop`.
- Use the `INSTANCE_TYPE` variable to distinguish between regular and base instances.

See [Hooks](https://discourse.ubuntu.com/t/hooks/28555) for more information.
[/note]

Create an SSH key in your addon directory and move the private key to a location outside of the addon directory (for example, your home directory):
```bash
ssh-keygen -f ssh-addon-key -t ecdsa -b 521
mv ssh-addon-key ~/
```
Alternatively, you can use an existing key and move the public key into the addon directory.

### 3. Create the addon
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

### 4. Use the addon in an application
Create an application manifest file (`my-application/manifest.yaml`) and include the addon name under `addons`:

```yaml
name: my-application
instance-type: a4.3
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

The SSH port 22 is closed by default. In the above command, we open it by [exposing its service](https://discourse.ubuntu.com/t/24326) by using `--service`.[/note]

You can now access your container via SSH:
```bash
ssh -i ~/ssh-addon-key root@<container_ip> -p <exposed port>
```

[note type="information" status="Note"] The exposed port can be found be running `amc ls`, under the `ENDPOINTS` column. Exposed ports usually start around port 10000.[/note]

## More information

* [Addon reference](https://discourse.ubuntu.com/t/addons/25293)
* [How to update addons](https://discourse.ubuntu.com/t/update-addons/25286)
* [Extend an application](https://discourse.ubuntu.com/t/extand-an-application/28554)

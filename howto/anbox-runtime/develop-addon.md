(howto-develop-addons-devmode)=
# How to develop addons in `--devmode`

Developing and testing addons using the Anbox Management Service (AMS) may be time-consuming. Instead, an instance with `--devmode` enabled can provide a safe environment to develop and test addons and their hooks without having to upload the addon to the AMS.

This guide explains how to use an instance in development mode to develop and test an addon using Anbox runtime. See {ref}`sec-dev-mode` to learn more about development mode enabled instances.

## Launch an instance in development mode

Start a raw instance with `--devmode` enabled:

```
amc launch --devmode --raw
```
or

```
amc launch --vm --devmode --raw
```
The command prints out the ID of the instance. Note down the instance ID for next steps.

Use the `amc shell <instance_id>` command to open a shell inside the instance. `instance_id` is the instance ID from the previous step.

Alternatively, you can use `amc exec <instance_id> <command_options>` to directly execute commands inside the instance.

## Create an addon within the instance

Use the instance as a remote environment to develop your addon. To make your addon source available within the instance, either copy the addon manifest and hooks using the [`lxc file push`](https://documentation.ubuntu.com/lxd/en/latest/howto/instances_access_files/#push-files-from-the-local-machine-to-the-instance) command or clone a git repository using SSH.

You can test your addon hooks by running it inside the instance shell. For example, `ADDON_DIR=$PWD ./hooks/install` can help test if the install hook of the addon works. See {ref}`sec-env-variables` for a list of available variables.

To troubleshoot issues within the instance, try either of the following options:
* Run `amc logs <instance_id>` on the host to see the Anbox runtime logs.
* Run `journalctl --no-pager` within the instance to view instance logs.
* Restart the instance using `amc stop <instance_id>` and then `amc start <instance_id>`.

## Example: Launch an SSH-enabled container for remote development

This example uses a container for demonstration, you can create an SSH-enabled VM using the same procedure by using the `--vm` option when launching the instance.

```bash
# Launch and obtain the container id
id="$(amc launch --devmode -s ssh --raw)"
# Install the ssh-import-id package
amc exec $id -- apt install -y ssh-import-id
# Import SSH keys from GitHub; Use lp:<username> for Launchpad
amc exec $id -- ssh-import-id gh:<username>
# Get the container's public IP address
# Run `sudo apt install jq` if `jq` is not already installed
container_address="$(amc show $id --format=json | jq -r '.network.public_address')"
# Get the SSH port
node_port="$(amc show $id --format=json | jq -r '.network.services[0].node_port')"
# Connect to the container using SSH
ssh -p "$node_port" root@"$container_address"
```
Once you are logged in to the instance, you can remotely develop and test your addon within the instance. For example, see how to [set up VS Code for remote development using SSH](https://code.visualstudio.com/docs/remote/ssh).

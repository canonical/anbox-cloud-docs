(howto-copy-instance)=

# Copy an instance

Copying an instance allows you to create a copy of an existing instance. This is particularly good for scaling environments, replicating same instance state, creating backups before risky operations, or debugging instances that have encountered errors without affecting the original.

Important considerations before copying instances:

* Resource availability: Ensure the cluster has enough capacity (CPU, GPU, RAM) to host the new copy.
* State awareness: Understand that a copied instance will inherit the file system state of the source.
* Log isolation: When copying an instance in an error state, the new instance is a fresh clone and will not include logs from the source instance.

## Copy an instance

To copy an instance, follow these steps:

::::{tab-set}

:::{tab-item} CLI
:sync: cli

### Modify the source instance

Make any modifications you want to include in the copied instance. For example, you can access the source instance and modify files:

    amc shell <instance_id_or_name>

Inside the instance, you can install additional software, modify configuration files, add custom files or data and make any other changes you want to be carried to the copied instance.

For example, install additional APT packages

    sudo apt install -y adb

Exit the instance shell when you're done.

### Check the source instance status

Before initializing a copy, verify the status of the source instance. A copy operation is permitted only if the instance is in one of the following states:

* `Stopped`
* `Running` (requires --force or interactive confirmation to stop the instance)
* `Error` (requires --force or interactive confirmation to acknowledge logs will not be copied)

Check the instance status with:

    amc show <instance_id_or_name>

### Copy the instance

Use the `amc copy` command to create a new instance based on the source:

    amc copy <instance_id_or_name>

AMS will generate and return a unique ID for the new instance. By default, the copied instance remains in the `stopped` status once the operation succeeds. To start the instance afterward:

    amc start <new_instance_id>

Alternatively, use the `--launch` flag to start the instance immediately after the copy process completes:

    amc copy <instance_id_or_name> --launch

#### Specify a name

If you want to assign a specific name to the new instance, use the `--name` flag:

    amc copy <instance_id_or_name> --name instance-copy

#### Manual node selection

By default, AMS scheduler automatically selects the most suitable node for the new instance. You can manually target a specific node using the `--node` flag:

    amc copy <instance_id_or_name> --name instance-copy --node node1

This is especially useful for ensuring high availability by manually distributing instance copies across the cluster.

### Test the copied instance

Start the copied instance:

    amc start instance-copy

Once the instance is running, verify that your modifications are present:

    amc shell instance-copy

List Android devices within Anbox instance with adb:

    adb devices
    List of devices attached
    emulator-5558   device

:::

:::{tab-item} Dashboard
:sync: dashboard

Navigate to the *Instances* page. Create and start an instance from an existing image or application.
Alternatively, you can also navigate either to the *Images* or *Applications* page, find the image or application you want to use as a base, and create an instance ( ![create instance icon](/images/icons/create-instance-icon.png) ).

Wait until the instance starts *running*, then click on the instance name. In *Instance details* > *Terminal*, make any modifications you want to include in the copied instance (e.g. install a package, create a file).

When you're done, stop the instance ( ![stop instance icon](/images/icons/stop-instance-icon.png) ) and then copy it ( ![copy instance icon](/images/icons/copy-instance-icon.png) ) from the *Instances* page.

Verify the instance you want to copy is pre-selected in the *Source* section of the instance creation form, make the necessary customizations, then create and start the instance.

Once the instance is running, visit the *Terminal* tab from its *Instance details* page to confirm that your modifications are present.


## Related topics

* {ref}`howto-create-instance`
* {ref}`howto-start-instance`
* {ref}`howto-stop-instance`
* {ref}`howto-publish-instance-as-image`

To launch an application or an image, Anbox Cloud creates an instance for it. To create and launch an instance, you can use the Anbox Cloud dashboard or the CLI.

## Using the dashboard

Select *Create Instance* on the *Instances* view to launch an instance. The information required for launching an instance depends on whether you are creating the instance from an application or an image.

When you create the instance from an application, the attributes you define for the application decide most of the properties of the instance.

When you create the instance from an image, you can define the properties of the instance during its creation.

Once you *Create and Start* an instance by providing the necessary attributes, you can view the instance and its status on the *Instances* view.

There may be more advanced scenarios while creating an instance that cannot be performed using the dashboard and may require using the `amc` CLI.

## Using the CLI

Depending on what you need, you can use the either of the following commands to create an instance for a registered application or an image.

* `amc launch` creates and starts the instance.
* `amc init` only creates the instance.

By default, the instance will run headless.

The following examples demonstrate different ways of launching instances using `amc launch`, but you can use `amc init` in the same way.

### Launch application instances

Before launching an instance for an application, get the ID of the application that for which you want to launch an instance. To do this, run:

    amc application ls

This command lists the available applications along their IDs and their published status.

```bash
+----------------------+----------------+---------------+--------+-----------+--------+---------------------+
|          ID          |      NAME      | INSTANCE TYPE | ADDONS | PUBLISHED | STATUS |    LAST UPDATED     |
+----------------------+----------------+---------------+--------+-----------+--------+---------------------+
| bdp7kmahmss3p9i8huu0 |      candy     | a4.3          | ssh    | false     | ready  | 2018-08-14 08:44:41 |
+----------------------+----------------+---------------+--------+-----------+--------+---------------------+
```

To launch an instance for a [published](https://discourse.ubuntu.com/t/how-to-update-an-application/24201#publish-application-versions-1) application, run:

    amc launch <application_id>

[note type="information" Status="Tip"]The `--vm` flag is not required when you specify an application id. The application has the information about whether a container or a virtual machine is to be created.[/note]

The `amc launch` command fails if you provide the ID of an application that is not yet published. However, if you have a specific version of an application that has been published, you can specify it to launch the instance successfully:

    amc launch --application-version=0 bcmap7u5nof07arqa2ag

### Launch a raw instance

You can launch a [raw instance](https://discourse.ubuntu.com/t/instances/17763#application-instances-vs-raw-instances-2) from an image. To do so, get the ID of the image by running:

    amc image ls

This command lists the available images along with their IDs and status:

```bash
+----------------------+---------+--------+----------+----------------------+
|          ID          |  NAME   | STATUS | VERSIONS |       USED BY        |
+----------------------+---------+--------+----------+----------------------+
| bh01n90j1qm6416q0ul0 | default | active | 1        |                      |
+----------------------+---------+--------+----------+----------------------+
```

Launch a raw instance by providing the image ID in the following command:

    amc launch --raw <image_id>

See [Provided images](https://discourse.ubuntu.com/t/provided-images/24185) for a list of images that are available in Anbox Cloud.

### Launch an instance on a specific node

By default, every instance is scheduled by AMS onto a LXD node. Alternatively, you can launch an instance directly on a specific node:

    amc launch --node=lxd0 <application_id>

[note type="information" status="Note"]AMS will still verify that the selected node has enough resources to host the instance. If not, the instance will fail to launch.[/note]

### Launch an instance with a different Anbox platform

By default, instances start with the `webrtc` platform if `--enable-graphics` is specified. Otherwise, they start with the `null` platform. To select a different platform, specify it with the `-p` flag. The platform cannot be changed at runtime and must be selected when the instance is created. For example, you can launch an instance with the `webrtc` platform with the following command:

    amc launch -p webrtc <application_id>

If you have built your own platform named `foo` and you built it via an addon into the instance images, you can launch an instance with the platform the same way:

    amc launch -p foo <application_id>

For more information, see [supported platforms](https://discourse.ubuntu.com/t/supported-rendering-resources/37322#supported-platforms-3) and [configuration for supported platforms](https://discourse.ubuntu.com/t/configuration-for-supported-platforms/18733).

### Launch an instance with development mode enabled

You can launch instances with additional development features turned on. This development mode must be enabled when an instance is launched, and it cannot be turned off afterwards. You should never enable development mode for instances used in a production environment.

To launch an instance with development mode enabled, add the `--devmode` flag to the launch command:

    amc launch --devmode <application_id>

## Related information

* [Instances](https://discourse.ubuntu.com/t/instances/17763)
* [How to access an instance](https://discourse.ubuntu.com/t/17772)
* [Application streaming](https://discourse.ubuntu.com/t/streaming-android-applications/17769)

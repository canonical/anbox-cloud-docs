(howto-create-instance)=
# How to create an instance
To launch an application or an image, Anbox Cloud creates an instance for it. To create and launch an instance, you can use the Anbox Cloud dashboard or the CLI.

`````{tabs}
````{group-tab} CLI

Depending on what you need, you can use the either of the following commands to create an instance for a registered application or an image.

* `amc launch` creates and starts the instance.
* `amc init` only creates the instance.

By default, the instance will run headless.

The following examples demonstrate different ways of launching instances using `amc launch`, but you can use `amc init` in the same way.

(sec-launch-application-instances)=
## Launch application instances

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

To launch an instance for a published application, run:

    amc launch <application_id>

```{tip}
- To know about published applications, see {ref}`sec-publish-app-versions`.
- The `--vm` flag is not required when you specify an application id. The application has the information about whether a container or a virtual machine is to be created.
```

The `amc launch` command fails if you provide the ID of an application that is not yet published. However, if you have a specific version of an application that has been published, you can specify it to launch the instance successfully:

    amc launch --application-version=0 bcmap7u5nof07arqa2ag

## Launch a raw instance

You can launch a raw instance from an image. To do so, get the ID of the image by running:

```{tip}
If you don't know what a raw instance is, see {ref}`sec-application-raw-instances`.
```
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

See {ref}`ref-provided-images` for a list of images that are available in Anbox Cloud.

## Launch an instance with streaming enabled

*since 1.22.0*

If you want to stream the visual output from an instance, specify it at the time of instance creation. Otherwise, the instance cannot be streamed. In previous versions of Anbox Cloud, it was only possible to create an instance that has streaming enabled via the [Stream Gateway API](https://canonical.github.io/anbox-cloud.github.com/latest/anbox-stream-gateway/). The same can now be achieved through the [AMS API](https://canonical.github.io/anbox-cloud.github.com/latest/ams/) or the `amc` CLI.

To enable streaming for a new instance, simply run:

    amc launch --enable-streaming ...

AMS will automatically create a streaming session for the instance. You can find the id of the session as a tag on the instance in the format `session=<id>`.

If you want to to further customize the streaming configuration such as display settings or frame rate, use the corresponding arguments: `--display-size`, `--display-density` and `--fps`. For example, to create an instance with a 1080p resolution, a frame rate of 60 and a DPI of 120, run:

    amc launch --enable-streaming --display-size=1920x1080 --display-density=120 --fps=60 ...

## Launch an instance with a specific name

*since 1.22.0*

To allow identifying and referencing instances easier you can give them a name at creation time. Names must be unique and can be used with all CLI commands.

To create an instance with a name, run:

    amc launch --name=foo ...

This will create an instance with the name "foo" which can then be used in other CLI commands. For example, when opening a shell for interacting with the instance, the following command can be used:

    amc shell foo

## Launch an instance on a specific node

By default, every instance is scheduled by AMS onto a LXD node. Alternatively, you can launch an instance directly on a specific node:

    amc launch --node=lxd0 <application_id>

```{note}
AMS will still verify that the selected node has enough resources to host the instance. If not, the instance will fail to launch.
```

## Launch an instance with a different Anbox platform

By default, instances start with the `webrtc` platform if `--enable-graphics` is specified. Otherwise, they start with the `null` platform. To select a different platform, specify it with the `-p` flag. The platform cannot be changed at runtime and must be selected when the instance is created. For example, you can launch an instance with the `webrtc` platform with the following command:

    amc launch -p webrtc <application_id>

If you have built your own platform named `foo` and you built it via an addon into the instance images, you can launch an instance with the platform the same way:

    amc launch -p foo <application_id>

For more information, see {ref}`exp-platforms` and {ref}`sec-supported-platforms`.

## Launch an instance with development mode enabled

You can launch instances with additional development features turned on. This development mode must be enabled when an instance is launched, and it cannot be turned off afterwards. You should never enable development mode for instances used in a production environment.

To launch an instance with development mode enabled, add the `--devmode` flag to the launch command:

    amc launch --devmode <application_id>

````

```{group-tab} Dashboard

You can create instances from the *Images* and *Applications* pages using the *Create an Instance* button ( ![create instance icon](/images/icons/create-instance-icon.png) ). You can also create instances from the details page of an image and an application.

The information required for creating an instance depends on whether you are creating it from an application or an image.

When you create the instance from an application, the attributes you define for the application decide most of the properties of the instance. When you create an instance from a selected image, you will find that several fields are already set based on the image base and type.

```{note}
There may be more advanced scenarios while creating an instance that cannot be performed using the dashboard and may require using the `amc` CLI.
```

Once you create an instance by providing the necessary attributes, you can view the instance and its status on the *Instances* page.

You can view details about a particular instance when you click on the instance name in the *Instances* list page. The instance details page offers three types of information: *Overview*, *Terminal*, and *Logs*.

The *Overview* tab provides detailed information about the instance, including sections for the instance details, associated image or application, streaming configurations, network settings, and tags.

The *Terminal* tab features a terminal interface for the Anbox instance, helping you to monitor system processes in real-time, check memory usage, view android and system logs, and much more.

The *Logs* tab helps you debug issues with the instances as it provides  downloadable logs for instances in an error state.

The instance details page also contains all the available actions including streaming, setting up sharing, connecting ADB, starting or stopping the instance, and deleting the instance.

```

`````

## Related topics

* {ref}`exp-application-streaming`
* {ref}`exp-instances`
* {ref}`howto-access-instance`

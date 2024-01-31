You can either launch an instance with `amc launch` or initialise an instance with the `amc init` command for a registered application or image (see [Application instances vs. raw instances](https://discourse.ubuntu.com/t/17763#application-vs-raw)), by using the `amc` tool or through another service over the REST API that the AMS service provides. The `amc init` command only creates the instance, while the `amc launch` command creates and starts it.

By default, the instance will run headless. See [How to access a instance](https://discourse.ubuntu.com/t/17772) for instructions on how to access it for debugging purposes, and [About application streaming](https://discourse.ubuntu.com/t/streaming-android-applications/17769) for information about the streaming stack.

[note type="information" status="Note"] The following examples use `amc launch`, but you can use `amc init` in the same way.[/note]

## Launch application instances

Launching an instance for a registered application can be achieved with the following command:

    amc launch <application_id>

The `--vm` flag is not required when you specify an application id. The application has the information about whether a container or a virtual machine is to be created.

As argument, provide the ID of the application that you want to launch.

You can list all available applications with the `amc application ls` command:

```bash
+----------------------+----------------+---------------+--------+-----------+--------+---------------------+
|          ID          |      NAME      | INSTANCE TYPE | ADDONS | PUBLISHED | STATUS |    LAST UPDATED     |
+----------------------+----------------+---------------+--------+-----------+--------+---------------------+
| bdp7kmahmss3p9i8huu0 |      candy     | a4.3          | ssh    | false     | ready  | 2018-08-14 08:44:41 |
+----------------------+----------------+---------------+--------+-----------+--------+---------------------+
```
If the application for which you want to launch an instance is not yet published (see [Update an application](https://discourse.ubuntu.com/t/update-an-application/24201) for more details), the launch command will fail as it only allows launching an instance for a published application. However, you can work around this by specifying a specific version of an application:

    amc launch --application-version=0 bcmap7u5nof07arqa2ag

## Launch raw instance

The command for launching a raw instance from an image is:

    amc launch --raw <image_id>

As argument, provide the ID or name of the image for which you want to launch an instance. See [Provided images](https://discourse.ubuntu.com/t/provided-images/24185) for a list of images that are available in Anbox Cloud.

You can also list all available images with the `amc image ls` command:

```bash
+----------------------+---------+--------+----------+----------------------+
|          ID          |  NAME   | STATUS | VERSIONS |       USED BY        |
+----------------------+---------+--------+----------+----------------------+
| bh01n90j1qm6416q0ul0 | default | active | 1        |                      |
+----------------------+---------+--------+----------+----------------------+
```

## Launch an instance on a specific node

By default, every instance is scheduled by AMS onto a LXD node. Alternatively, you can launch an instance directly on a specific node:

    amc launch --node=lxd0 bcmap7u5nof07arqa2ag

[note type="information" status="Note"]AMS will still verify that the selected node has enough resources to host the instance. If not, the instance will fail to launch.[/note]

## Launch an instance with a different Anbox platform

By default, instances start with the `webrtc` platform if `--enable-graphics` is specified and with the `null` platform otherwise (see [Anbox platforms](https://discourse.ubuntu.com/t/anbox-platforms/18733)). To select a different platform, specify it with the `-p` flag. The selected platform cannot be changed at runtime and must be selected when the instance is created. For example, you can launch an instance with the `webrtc` platform like this:

    amc launch -p webrtc <application-id>

If you have built your own platform named `foo` and you built it via an addon into the instance images, you can launch an instance with the platform the same way:

    amc launch -p foo <application-id>

## Launch an instance with development mode enabled

You can launch instances with additional development features turned on. This development mode must be enabled when an instance is launched, and it cannot be turned off afterwards. You should never enable development mode for instances used in a production environment.

To launch an instance with development mode enabled, add the `--devmode` flag to the launch command:

    amc launch --devmode <application-id>

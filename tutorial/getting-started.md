This tutorial guides you through the first steps of managing Anbox Cloud from the command line. You will learn how to communicate with [AMS](https://discourse.ubuntu.com/t/about-ams/24321) and how to create and access a virtual Android device or an application.

The tutorial focuses on using the command line to work with Anbox Cloud, which gives you access to all features of Anbox Cloud. Alternatively, you can use the [web dashboard](https://discourse.ubuntu.com/t/web-dashboard/20871), which provides a simpler user interface but does not support all functionality. See the [Get started with Anbox Cloud (web dashboard)](https://discourse.ubuntu.com/t/getting-started-with-anbox-cloud-web-dashboard/24958) tutorial for an introduction on how to use the web dashboard.

## Preparation
If you haven't installed Anbox Cloud or the Anbox Cloud Appliance yet, you must do so before you can continue with this tutorial. See the following documentation for installation instructions:

* [How to install the Anbox Cloud Appliance](https://discourse.ubuntu.com/t/how-to-install-the-anbox-cloud-appliance/29702)
* [How to install Anbox Cloud](https://discourse.ubuntu.com/t/install-anbox-cloud/24336)

## 1. Run AMC

The Anbox Management Client `amc` communicates with the [Anbox Management Service (AMS)](https://discourse.ubuntu.com/t/about-ams/24321). You will use `amc` to manage all aspects of Anbox Cloud that are related to AMS.

How and where to run `amc` depends on your use case:

- If you are running the Anbox Cloud Appliance on AWS, `amc` is already installed on the machine that runs the appliance. Log on to that machine to run `amc`.

  Note that you must use the user name `ubuntu` and provide the path to your private key file when connecting. See [Connect to your Linux instance using SSH](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/AccessingInstancesLinux.html) for instructions on how to connect.
- If you are running the Anbox Cloud Appliance on a physical or virtual machine, log on to that machine and ensure that you have [enabled the `anbox-cloud` service using the Ubuntu Pro client](https://discourse.ubuntu.com/t/22681#enable-anbox-service).
- If you are running a full Anbox Cloud deployment, access the `ams/0` machine to run `amc`. You can do this by opening an SSH session with the `juju` command:

        juju ssh ams/0

- If you want to run `amc` on your local Ubuntu-based development machine against a remote Anbox Cloud installation, follow the instructions in [How to control AMS remotely](https://discourse.ubuntu.com/t/managing-ams-access/17774).

To ensure that `amc` is available, run the following command:

    amc help

To check if `amc` is set up to access the correct AMS, run the following command:

    amc remote list

## 2. Ensure images are available

Next, check whether AMS has synchronised all images from the Canonical hosted image server. You can list all synchronised images with the `amc image ls` command:

```bash
+----------------------+------------------------+--------+----------+--------------+---------+
|          ID          |          NAME          | STATUS | VERSIONS | ARCHITECTURE | DEFAULT |
+----------------------+------------------------+--------+----------+--------------+---------+
| cgrqjd6k9eqlsruefcng | jammy:android13:arm64  | active | 1        | aarch64      | true    |
+----------------------+------------------------+--------+----------+--------------+---------+
| cgrqjnmk9eqlsruefco0 | jammy:android12:arm64  | active | 1        | aarch64      | false   |
+----------------------+------------------------+--------+----------+--------------+---------+
| cgrqk2uk9eqlsruefcog | jammy:android11:arm64  | active | 1        | aarch64      | false   |
+----------------------+------------------------+--------+----------+--------------+---------+
```

See [Provided images](https://discourse.ubuntu.com/t/provided-images/24185) for more information.

If the images are not yet available, wait a few minutes, then try again.

## 3. Create a virtual device

Let's start exploring what Anbox Cloud can do by launching a virtual device that runs a specific Android version.

[note type="information" status="Note"]With "virtual device" we mean a simulated device that runs a plain Android operating system without any special apps installed. Technically speaking, Anbox Cloud treats such a virtual device as an "empty" application, thus an application that is not running a specific APK.[/note]

Complete the following steps to create a virtual device:

1. Create a simple `manifest.yaml` file that contains the name and resource preset for the virtual device. For example, the file could look like this:

   ```yaml
   name: virtual-device-cli
   resources:
     cpus: 4
     memory: 4GB
     disk-size: 3GB
   ```

2. Enter the following command to create the virtual device, replacing */path/to/manifest/directory/* with the path to the directory where you created the manifest file:

        amc application create /path/to/manifest/directory/

3. The application is now being [bootstrapped](https://discourse.ubuntu.com/t/managing-applications/17760#bootstrap). Enter the following command to monitor the progress:

        watch -n 1 amc application ls

   Wait until the status of the application changes to `ready`.

   ```
   +----------------------+--------------------+---------------+--------+------+-----------+--------+---------------------+
   |          ID          |        NAME        | INSTANCE TYPE | ADDONS | TAGS | PUBLISHED | STATUS |    LAST UPDATED     |
   +----------------------+--------------------+---------------+--------+------+-----------+--------+---------------------+
   | c5mnh3oehn3g26pv4jlg | virtual-device-cli | a4.3          |        |      | true      | ready  | 2021-10-18 13:37:19 |
   +----------------------+--------------------+---------------+--------+------+-----------+--------+---------------------+
   ```


<a name="logon"></a>
## 4. Log on to the virtual device

When the application for the virtual device is ready, you can launch it and log on to it:

1. Start a container for the virtual device by launching the application:

        amc launch virtual-device-cli

2. Enter the following command to monitor the progress:

        watch -n 1 amc ls

   Wait until the status of the container changes to `running`.

   ```
   +----------------------+--------------------+---------+---------+------+---------------+-----------+
   |          ID          |    APPLICATION     |  TYPE   | STATUS  | NODE |    ADDRESS    | ENDPOINTS |
   +----------------------+--------------------+---------+---------+------+---------------+-----------+
   | c5mnkvoehn3g26pv4jn0 | virtual-device-cli | regular | running | lxd0 | 192.168.100.3 |           |
   +----------------------+--------------------+---------+---------+------+---------------+-----------+
   ```

3. Enter the following command to get a shell inside the container that runs the virtual device:

        amc shell <container ID>

   You can find the container ID of the virtual device in the list of containers.

   [note type="information" status="Tip"]You can use tab completion when entering the container ID.[/note]
4. You are now inside the Linux container that runs the Android container. To access the nested Android container, enter the following command:

        anbox-shell

5. Enter some commands. For example, enter `ls` to display the files inside the Android container, or `logcat` to display the logs.
6. Enter `exit` or press `Ctrl`+`D` once to exit the Android shell, and then again to exit the Linux container.

<a name="scrcpy"></a>
## 5. Test the virtual device

You can test the virtual device by connecting to it from your local machine and mirroring its screen. To do so, use the `scrcpy` tool. See [How to access a container with scrcpy](https://discourse.ubuntu.com/t/container-access/17772#scrcpy) for more detailed instructions.

If you do not have `scrcpy` installed on your local machine, enter the following command to install it:

    sudo apt install scrcpy

See the [`scrcpy` documentation](https://github.com/Genymobile/scrcpy) for installation instructions for other operating systems.

To connect to your virtual device with `scrcpy`, complete the following steps:

1. Launch a container based on the virtual device application, with the ADB service exposed and graphics enabled:

        amc launch virtual-device-cli --service +adb --enable-graphics

2. Enter the following command to monitor the progress:

        watch -n 1 amc ls

   Wait until the status of the container changes to `running`.
3. Find the public network endpoint of the ADB service for the container. For example, with the following output, the public network endpoint of the ADB service is `10.229.100.38:10001`:

   ```bash
   +----------------------+--------------------+---------+---------+------+---------------+--------------------------------------------------------+
   |          ID          |    APPLICATION     |  TYPE   | STATUS  | NODE |    ADDRESS    |                       ENDPOINTS                        |
   +----------------------+--------------------+---------+---------+------+---------------+--------------------------------------------------------+
   | c5mnur0ehn3g26pv4jp0 | virtual-device-cli | regular | running | lxd0 | 192.168.100.4 | adb:192.168.100.4:5559/tcp adb:10.229.100.38:10001/tcp |
   +----------------------+--------------------+---------+---------+------+---------------+--------------------------------------------------------+
   ```

4. On your local machine, enter the following command to establish a connection between your machine and the container:

        adb connect 10.229.100.38:10001

5. Confirm that the connection has been established and the endpoint is listed in the list of devices:

        adb devices

6. Run `scrcpy` to access the device:

        scrcpy

## 6. Create an application from an APK

Creating an application for a specific Android app is very similar to creating a virtual device, except that you provide an APK of the Android app when creating the Anbox Cloud application.

[note type="information" status="Important"]Not all Android apps are compatible with Anbox Cloud. See [How to port Android apps](https://discourse.ubuntu.com/t/port-android-apps/17776) for more information.[/note]

Complete the following steps to create an application from an APK:

1. Create a folder for your application (for example, `my-application`) and place your APK inside this folder.

2. Create a `manifest.yaml` file in that folder. This manifest contains the application name and if necessary, define resources for the application. If your instance is equipped with a GPU and your application requires the use of the GPU for rendering and video encoding, make sure to mention the GPU requirement using the `resources` attribute. Otherwise, the container will use a GPU if available or software encoding.

If no specific resources are mentioned, the [default resource preset](https://discourse.ubuntu.com/t/24960) is used.

   For example, the file could look like this:

   ```yaml
   name: my-application
   resources:
     cpus: 6
     memory: 4GB
     disk-size: 8GB
   ```

   [note type="information" status="Tip"]The manifest can also contain more advanced configuration like [Addons](https://discourse.ubuntu.com/t/managing-addons/17759), permissions and others. For more information about the manifest format, see [Application manifest](https://discourse.ubuntu.com/t/application-manifest/24197) documentation.[/note]
2. Enter the following command to create the application, replacing */path/to/manifest/directory/* with the path to the directory where you created the manifest file:

        amc application create /path/to/manifest/directory/

3. The application is now being [bootstrapped](https://discourse.ubuntu.com/t/managing-applications/17760#bootstrap). Enter the following command to monitor the progress:

        watch -n 1 amc application ls

   Wait until the status of the application changes to `ready`.

When the application is ready, you can launch it and then test it in the same way as the virtual device by either [logging on to it](#logon) or [connecting to it with `scrcpy`](#scrcpy).

## 7. Update an application

You can have several versions of an application. See [How to update an application](https://discourse.ubuntu.com/t/update-an-application/24201) for detailed information.

Complete the following steps to add a new version to your application:

1. Update either the APK or the manifest for your application. For example, update the manifest to automatically expose the ADB service (so that you don't need to do this when launching the application):

   ```yaml
   name: my-application
   instance-type: a4.3
   services:
    - name: adb
      port: 5559
      protocols: [tcp]
      expose: true
   ```

2. Update the existing application, replacing *\<application ID>* with the ID of the application (from `amc application ls`) and */path/to/manifest/directory/* with the path to the directory where you created the manifest file:

        amc application update <application ID> /path/to/manifest/directory/

3. Check and monitor the different versions of the application:

        watch -n 1 amc application show <application ID>

   Note the `status` and the `published` fields. Once the status changes to `active`, the new version of the application is automatically published.

When you launch an application without explicitly specifying a version, AMS uses the latest published version of the application. Therefore, when you now launch the application again, the new version of your application is selected and the ADB service is exposed automatically.

## 8. List and delete applications and containers

While following this tutorial, you created several applications and containers. Let's check them out and delete the ones that aren't needed anymore:

1. Enter the following command to list all containers:

        amc ls

   You created a container every time you launched an application. For example, the output could look like this:

   ```
   +----------------------+--------------------+---------+---------+------+---------------+--------------------------------------------------------+
   |          ID          |    APPLICATION     |  TYPE   | STATUS  | NODE |    ADDRESS    |                       ENDPOINTS                        |
   +----------------------+--------------------+---------+---------+------+---------------+--------------------------------------------------------+
   | c5mnkvoehn3g26pv4jn0 | virtual-device-cli | regular | running | lxd0 | 192.168.100.3 |                                                        |
   +----------------------+--------------------+---------+---------+------+---------------+--------------------------------------------------------+
   | c5moua0ehn3g26pv4k0g | virtual-device-cli | regular | running | lxd0 | 192.168.100.4 | adb:192.168.100.4:5559/tcp adb:10.229.100.38:10001/tcp |
   +----------------------+--------------------+---------+---------+------+---------------+--------------------------------------------------------+
   | c5mo75gehn3g26pv4jrg | my-application     | regular | running | lxd0 | 192.168.100.5 | adb:192.168.100.5:5559/tcp adb:10.229.100.38:10002/tcp |
   +----------------------+--------------------+---------+---------+------+---------------+--------------------------------------------------------+
   | c5moufoehn3g26pv4k1g | my-application     | regular | running | lxd0 | 192.168.100.6 | adb:192.168.100.6:5559/tcp adb:10.229.100.38:10003/tcp |
   +----------------------+--------------------+---------+---------+------+---------------+--------------------------------------------------------+
   ```

   For each container, you can enter `amc show <container ID>` to display more information.
2. Delete the containers that you don't need anymore:

        amc delete <container ID>

   You can find the container ID in the list of containers. Alternatively, you can delete all containers with `amc delete --all`.
3. Enter the following command to list all applications:

        amc application ls

   For example, the output could look like this:

   ```
   +----------------------+--------------------+---------------+--------+------+-----------+--------+---------------------+
   |          ID          |        NAME        | INSTANCE TYPE | ADDONS | TAGS | PUBLISHED | STATUS |    LAST UPDATED     |
   +----------------------+--------------------+---------------+--------+------+-----------+--------+---------------------+
   | c5mnh3oehn3g26pv4jlg | virtual-device-cli | a4.3          |        |      | true      | ready  | 2021-10-18 13:37:19 |
   +----------------------+--------------------+---------------+--------+------+-----------+--------+---------------------+
   | c5mo3eoehn3g26pv4jq0 | my-application     | a4.3          |        |      | true      | ready  | 2021-10-18 14:45:02 |
   +----------------------+--------------------+---------------+--------+------+-----------+--------+---------------------+
   ```

   For each application, you can enter `amc application show <application ID>` to display more information.
4. Delete the applications that you don't need anymore:

        amc application delete <application ID>

   You can find the application ID in the list of applications.

## Done!

You now know how to use the command line to create, launch and test applications in Anbox Cloud.

This tutorial used a container to illustrate how to create and work with applications using Anbox Cloud. Alternatively, you can also use a virtual machine instead of a container by using the `--vm` option with the `amc` commands.

If you are interested in a more easy-to-use interface, check out the [Get started with Anbox Cloud (web dashboard)](https://discourse.ubuntu.com/t/getting-started-with-anbox-cloud-web-dashboard/24958) tutorial to learn how to manage Anbox Cloud using the [web dashboard](https://discourse.ubuntu.com/t/web-dashboard/20871).

Also see the documentation about [How to manage applications](https://discourse.ubuntu.com/t/manage-applications/24333) and [How to work with instances](https://discourse.ubuntu.com/t/24335) for more in-depth information.

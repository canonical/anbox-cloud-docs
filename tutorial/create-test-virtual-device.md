(tut-create-virtual-device)=
# Create and test a virtual device

> Before you start, complete: {ref}`tut-installing-appliance` but when initializing, remember to answer *Yes* to the question: *Do you want to setup access to the AMS API for your current user (ubuntu, uid=1000)?*

In this tutorial, we will go through the first steps of using Anbox Cloud to create a virtual Android device. By *virtual device*, we mean a simulated device that runs a plain Android operating system without any special apps installed. Anbox Cloud treats such a virtual device as an *empty* application, meaning an application that is not running a specific APK.

By the end of this tutorial, we will be familiar with an {term}`Application` and an {term}`Instance` in Anbox Cloud that are used to create and stream the virtual Android device.

This tutorial has two paths - you can use the CLI or the dashboard, depending on your learning goals. The CLI is more powerful and gives you access to all features of Anbox Cloud, while the dashboard is a simpler user interface. For this tutorial, it does not matter which path you choose.

`````{tabs}
````{group-tab} CLI

We will use the {term}`Anbox Management Client (AMC)` in this tutorial to work with applications and instances. AMC communicates with the {term}`Anbox Management Service (AMS)`, the instance management module of Anbox Cloud.

## Create the device

The first step is to create a `yaml` file that can be used as the application manifest. It is important that this file is created in your `home` directory.

In the home directory, let's first create a directory for the application content:

      mkdir my-app

This directory is the location where the application manifest file and any relevant application artifacts must reside.

For this tutorial, we are going to create a device with a basic application without an APK that will start directly with the Android system launcher.

Let's first create the `manifest.yaml` inside the `my-app` directory with the following contents:

```yaml
name: my-first-app
resources:
   cpus: 4
   memory: 4GB
   disk-size: 3GB
```
This example will use the default image as we haven't mentioned a specific image.

Now, let's create the application:

      amc application create my-app/

This command will return the application ID.

```{terminal}
      :input: amc application create my-app/
      :user: ubuntu
      :host: vm
      :dir: ~

cv3a7ofg2e7td2g9smt0
```

`my-app/` is the application directory where the manifest and any other application related artifacts are available. The command should return the application ID.

The application is created and bootstrapped. Now, to see the application details and its status, run:

      amc application list

The output of this command should look similar to the following. Watch this output till the application becomes *ready*. The time taken for the application to become ready could depend on your network speed but with a good network connection, it shouldn't take more than 10 minutes.

```{terminal}
      :input: amc application list
      :user: ubuntu
      :host: vm
      :dir: ~
      :scroll:

+----------------------+--------------+---------------+--------+------+-----------+--------------+---------------------+-------+
|          ID          |     NAME     | INSTANCE TYPE | ADDONS | TAGS | PUBLISHED |    STATUS    |    LAST UPDATED     |  VM   |
+----------------------+--------------+---------------+--------+------+-----------+--------------+---------------------+-------+
| cv3a7ofg2e7td2g9smt0 | my-first-app | a2.3          |        |      | false     | initializing | 2025-03-04 12:25:29 | false |
+----------------------+--------------+---------------+--------+------+-----------+--------------+---------------------+-------+
```

## Test the virtual device

**Launch an instance**

When the application is *ready*, let's launch an instance:

      amc launch my-first-app --enable-streaming

```{terminal}
      :input: amc launch my-first-app --enable-streaming
      :user: ubuntu
      :host: vm
      :dir: ~

cv3ct202cdutj02fttsg
```

This command creates and starts an instance for the application.

`my-first-app` is the application name, you can also use the application ID to launch an instance for it.

The `--enable-streaming` flag indicates that we want to stream this instance.

To see the instance details and its status, run:

      amc ls

You will see an output similar to the following:

```{terminal}
   :input: amc ls
   :user: ubuntu
   :host: vm
   :dir: ~
   :scroll:

+----------------------+------+--------------+------+---------+------+------+---------+-----------+-------+----------------+
|          ID          | NAME | APPLICATION  | TYPE | STATUS  | TAGS | NODE | ADDRESS | ENDPOINTS |  VM   | STATUS MESSAGE |
+----------------------+------+--------------+------+---------+------+------+---------+-----------+-------+----------------+
| cv3ct202cdutj02fttsg |      | my-first-app | base | created |      |      |         |           | false |                |
+----------------------+------+--------------+------+---------+------+------+---------+-----------+-------+----------------+
```

When the instance reaches the *running* status, the output for `amc ls` should look like:

```{terminal}
:input: amc ls
   :user: ubuntu
   :host: vm
   :dir: ~
   :scroll:

+----------------------+------+--------------+---------+---------+------------------------------+------+--------------+-----------+-------+----------------+
|          ID          | NAME | APPLICATION  |  TYPE   | STATUS  |             TAGS             | NODE |   ADDRESS    | ENDPOINTS |  VM   | STATUS MESSAGE |
+----------------------+------+--------------+---------+---------+------------------------------+------+--------------+-----------+-------+----------------+
| cv3ct202cdutj02fttsg |      | my-first-app | regular | running | session=cv3ct202cduikviuu6rg | lxd0 | 192.168.96.1 |           | false |                |
+----------------------+------+--------------+---------+---------+------------------------------+------+--------------+-----------+-------+----------------+

```

Now, let's try to access the instance. We will need to copy the instance ID from the previous command's output.

      amc shell instance_id

This takes us into the Linux instance that runs the Android container. Next, let's try accessing the nested Android container:

      anbox-shell

Now, we are inside the Android container. Play around by running some of the following commands:

      ls
      logcat
      exit

`exit` or pressing Control+D takes us back to the Linux container.

**Update an application**

We can have several versions of an application. Let's try and update the application:

Go to the application directory and update the manifest file. This manifest introduces a change to the disk-size.

```yaml
name: my-first-app
resources:
   cpus: 4
   memory: 4GB
   disk-size: 8GB
```

Now, run the following commands and observe the output:

      amc application update my-first-app my-app/
      amc application list
      amc application show my-first-app

The `list` command displays the list of applications available. As an application becomes *active*, it is automatically published and a new version of the `my-first-app` is created.

The `show` command displays the application information along with its versions:

```{terminal}
:input: amc application show my-first-app
   :user: ubuntu
   :host: vm
   :dir: ~
   :scroll:

id: cv3a7ofg2e7td2g9smt0
name: my-first-app
created-at: 2025-03-04 15:19:32 +0530 IST
status: ready
published: true
immutable: false
inhibit-auto-updates: false
tags: []
node-selector: []
parent-image: jammy:android14:amd64
parent-image-variant: android
abi: x86_64
vm: false
config:
  instance-type: a2.3
versions:
  0:
    image: jammy:android14:amd64 (version 0)
    published: true
    status: active
    extra-data: {}
    video-encoder: gpu-preferred
    watchdog:
      disabled: false
      allowed-packages: []
  1:
    image: jammy:android14:amd64 (version 0)
    published: true
    status: active
    extra-data: {}
    video-encoder: gpu-preferred
    watchdog:
      disabled: false
      allowed-packages: []
resources:
  cpus: 4
  memory: 4GB
  disk-size: 8GB
```

Now if we launch our application without explicitly specifying a version, our latest published version will be considered:

```{terminal}
:input: amc launch my-first-app
   :user: ubuntu
   :host: vm
   :dir: ~
   :scroll:

cv3d5ag2cdutj02fttvg

:input: amc ls

+----------------------+------+--------------+---------+---------+------------------------------+------+--------------+-----------+-------+----------------+
|          ID          | NAME | APPLICATION  |  TYPE   | STATUS  |             TAGS             | NODE |   ADDRESS    | ENDPOINTS |  VM   | STATUS MESSAGE |
+----------------------+------+--------------+---------+---------+------------------------------+------+--------------+-----------+-------+----------------+
| cv3ct202cdutj02fttsg |      | my-first-app | regular | running | session=cv3ct202cduikviuu6rg | lxd0 | 192.168.96.1 |           | false |                |
+----------------------+------+--------------+---------+---------+------------------------------+------+--------------+-----------+-------+----------------+
| cv3d5ag2cdutj02fttvg |      | my-first-app | regular | running |                              | lxd0 | 192.168.96.2 |           | false |                |
+----------------------+------+--------------+---------+---------+------------------------------+------+--------------+-----------+-------+----------------+

```

Notice how the second instance launched without the `--enable-streaming` flag does not have a session ID. This instance cannot be streamed while the earlier one we created can be streamed.

**Streaming the application**

To look at a visual output of the stream-enabled instance that we created, we need a stream client.You can set up your own stream client by following the {ref}`tut-set-up-stream-client` later. For this tutorial, you can use the default client, the Anbox Cloud dashboard.

Go to `https://machine-address` using a browser and go to the *Instances* page where we can see the instance we created. See the *Dashboard* tab for details on using the dashboard to test the virtual device.

## Success!
You now know how to use the command line to create and test an Android virtual device in Anbox Cloud. 

````

````{group-tab} Dashboard

## Create the device

The first step is to create an application. Let's go to the dashboard and then *Applications* > *Create Application*.

The next step is to give our application, a name: *my-application*.

We can select whether we want to create the application in a container or a virtual machine. For this tutorial, let's select *Container*.

Then, we can select the Android image. Observe that the image can be identified if it is an Android (AOSP) or an Android automotive (AAOS) image by looking at the image names. Let's select `jammy:android14:amd64` which is an Ubuntu 22.04 based Android 14 image for AMD64 architecture.

Next, let's select the resource type. We can leave it to the default value for this tutorial.

Finally, we have a choice to upload an Android APK. It is not mandatory to have an APK because we can still create and interact with the plain Android operating system. For this tutorial, we are not uploading an APK. However, if you wish to test your Android application, this is where you upload its APK.

The dashboard allows for more configuration through the *Configuration* options. Some attributes that can be configured include the boot package, boot activity, enabling the watchdog, stopping auto-updates and more. These options are also dependent on whether we uploaded an APK. For this tutorial, we can safely ignore these options.

There is a `Customize manifest.yaml` option to configure the attributes of the application. You can learn about the different attributes that are available at {ref}`ref-application-manifest` later but for now, the default manifest file will work.

Click *Create* and watch the *Applications* page as our application gets initialized. While waiting for the application to be ready, you can click on the application name and explore the application details.

## Test the device

**Launch an instance**

Now, we need an instance that can be streamed to test our Android virtual device. 

The *Create instance* button becomes available when the application is *ready*. Let's click *Create instance*.

While creating the instance, we can observe some interesting behaviors:

- It is possible to create an instance from an image instead of an application. If you want to learn more about the different types of instances, you can later refer to {ref}`sec-application-raw-instances`.
- Some of the details are pre-populated based on the context of our application.
- There can be multiple versions of an application and an instance can be based on any of the active versions.

To test our virtual device quickly, all we have to do for now, is to provide a name to the instance and click *Create and start*.

Watch the *Instances* page as the instance is quickly created and started.

**Stream the application**

You will notice that even after the instance is started, we cannot stream it yet - the stream icon(![stream icon](/images/icons/stream-icon.png)) is not enabled yet. This is because the instance needs to reach a *running* status before it can be streamed.

Once the status turns to *running*, click the stream icon.

Before the stream starts, there may be a warning from your browser to accept the certificates manually. This is because the dashboard uses self-signed certificates. Accept the certificate and reload the page.

 Now, you should be able to interact with the Android virtual device. If we had used an APK, the application interface would be visible directly.

On the stream page, we can see options for:

- Sharing the stream with others
- Setting up an authenticated connection using the Android Debug Bridge (ADB)
- Viewing the network, audio and video statistics for the stream
- Setting the location for a maps application
- A *Developer tools* toggle that offers access to the Ubuntu and Android instances. For example, if you are performing an resource intensive operation in your Android stream, you can monitor its impact using this terminal.

Let's try a simple operation of sharing our stream: Click *Set up sharing*, give your share a title and an expiry date.

When we click *Set up*, we are provided with a URL to our Android stream that can be shared.

**Troubleshoot instance failures**

If we click on our instance name, we can explore the instance details, interact with it using a terminal and view logs for debugging.

This terminal is the shell for the Linux instance that runs the Android container. You can run commands in the Linux instance, or you can type `anbox-shell` and to gain access to the nested Android container. 

The `exit` command takes you back from the Android container shell to the Linux instance shell.

If you have an instance with an *error* status, you can explore the different types of logs available for the instance.

## Success!

You now know how to use the Anbox Cloud dashboard to create and test an Android virtual device. 

````
`````

> Next: You can check out the following how-to sections to try out other applications with applications and instances:

- {ref}`howto-manage-applications`
- {ref}`howto-instance`

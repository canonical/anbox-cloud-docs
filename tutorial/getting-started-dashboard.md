(tut-getting-started-dashboard)=
# Getting started with Anbox Cloud (web dashboard)

This tutorial guides you through the first steps of using Anbox Cloud. You will learn how to create and access a virtual Android device or an application using the web dashboard.

The web dashboard provides an easy-to use interface to Anbox Cloud. However, it currently supports a limited set of functionality, which means that it might not be sufficient for all use cases. If you want to learn how to manage Anbox Cloud from the command line, see the {ref}`tut-getting-started-cli` tutorial.

## Preparation

If you haven't installed Anbox Cloud or the Anbox Cloud Appliance yet, you must do so before you can continue with this tutorial. See the following documentation for installation instructions:

- {ref}`howto-install-appliance`
- {ref}`howto-install-anbox-cloud`

(sec-create-virtual-device)=
## Create a virtual device

Let's start exploring what Anbox Cloud can do by launching a virtual device that runs a specific Android version.

```{note}
With "virtual device" we mean a simulated device that runs a plain Android operating system without any special apps installed. Technically speaking, Anbox Cloud treats such a virtual device as an "empty" application, thus an application that is not running a specific APK.
```

Complete the following steps to create a virtual device:

1. Open `https://<your-machine-address>/applications` in your browser. By default, the Anbox Cloud Appliance uses self-signed certificates, which might cause a security warning in your browser. Use the mechanism provided by your browser to proceed to the web page.
2. Click **Add Application**.
3. Enter a name for the application, for example, `virtual-device-web`.
4. Keep the preselected resource type.
5. Select the Android image that you want to use, for example, `jammy:android13:arm64`.
6. Do not upload an APK file.
7. Click **Add Application**.

   ![Add application](https://assets.ubuntu.com/v1/7cb08440-add-application.png)
8. You are redirected to the application view. Wait until the application status changes to `ready`.

## Launch and test the virtual device

When the application has been initialised and its status changes to `ready`, complete the following steps to launch and test the virtual device:

1. In the list of applications, click the play button in the **Actions** column for the application to start a new session.

   ![Start a new session](https://assets.ubuntu.com/v1/7f1553f5-start-new-session.png)
2. Accept the default settings and click **Create Session**.

   ![Create session](https://assets.ubuntu.com/v1/11ee7ef4-create-session.png)
3. When the stream has loaded, you can interact with your virtual device.

   ![Stream the virtual device](https://assets.ubuntu.com/v1/9d9ba326-interact-virtual-device.png)

## Create an application from an APK

To create an application for a specific Android app, follow the steps in {ref}`sec-create-virtual-device`, but upload the APK of the Android app.

```{important}
Not all Android apps are compatible with Anbox Cloud. See {ref}`howto-port-android-apps` for more information.
```

Choose a {ref}`resource preset <sec-application-manifest-resources>` suitable for your application. If your instance is equipped with a GPU and your application requires the use of the GPU for rendering and video encoding, make sure to mention the GPU requirement using the `resources` attribute. Otherwise, the container will use a GPU if available or software encoding.

You can launch and test the application in the same way as you did for the virtual device.

## Update an application

You can have several versions of an application. See {ref}`howto-update-application` for detailed information.

Complete the following steps to add a new version to your application:

1. Open `https://<your-machine-address>/applications` in your browser.
2. Click the **Edit application** button  in the **Actions** column next to the application for which you want to add a new version.
3. Upload a new APK, or do other changes to the configuration.
4. Click **Update application**.

## Delete an application

While following this tutorial, you created several applications. You can see them in the application view at `https://<your-machine-address>/applications`.

To delete an application, click the **Delete application** button in the **Actions** column and confirm the deletion.

```{tip}
To skip the confirmation window, hold **Shift** when clicking the **Delete application** button.
```

## Inspect instances

Every time you start a session for an application, Anbox Cloud creates an instance. The instance keeps running even if you exit the stream, until you either stop the session by clicking **Stop session** or delete the instance.

You can see all instances in the instance list view at `https://<your-machine-address>/instances`.

![Instance list view](https://assets.ubuntu.com/v1/57063a40-instance_list.png)

Complete the following steps to inspect an instance:

1. Click on the ID of one of the running instances. The **Overview** tab displays detailed information for the instance.
1. Switch to the **Terminal** tab. You will see a terminal for the Linux instance that runs the Android container.

   You can run commands in the Linux instance, or you can enter `anbox-shell` to access the nested Android container (enter `exit` to go back to the Linux instance).

   ![Use the instance terminal](https://assets.ubuntu.com/v1/bc5ad728-instance_terminal.png)
1. Switch to the **Logs** tab. You will not see any logs, because log files are available only for instances that are in an error state, not for running instances.

   To simulate a failure for the instance, switch to the **Terminal** tab and enter the following command:

        amsctl notify-status error --message="My error message"

   Go back to the instance overview, and when the instance status changes to **error**, click on the instance ID and switch to the **Logs** tab. You can now see the error logs for the instance.

   ![Instance logs](https://assets.ubuntu.com/v1/7004a76a-instance_logs.png)

## Done!

You now know how to use the web dashboard to create, launch and test applications in Anbox Cloud.

If you are interested in more advanced use cases, check out the {ref}`tut-getting-started-cli` tutorial to learn how to use Anbox Cloud from the command line.

## Related topics

* {ref}`howto-use-web-dashboard`
* {ref}`howto-manage-applications`
* {ref}`howto-instance`

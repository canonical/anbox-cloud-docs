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

1. Open `https://<your-machine-address>/applications` in your browser. By default, the Anbox Cloud Appliance uses self-signed certificates, which might cause a security warning in your browser. Use the mechanism provided by your browser to proceed to the web page.
1. Click *Create application*.
   - Select the application type: Mobile or Automotive.
   - Enter a name for the application, for example, `virtual-device-web`.
   - Keep the preselected resource type.
   - Select if you want to create a container-based or a VM-based application
   - Select the Android image that you want to use, for example, `jammy:android13:arm64`.
   - Do not upload an APK file.

Click *Create application* again to complete the process. You are redirected to the *Applications* page. Wait until the application status changes to `ready`.

## Test the virtual device

When the application has been initialized and its status changes to `ready`, complete the following steps to launch and test the virtual device:

1. In the list of applications, Click *Create an instance* ( ![create an instance icon](/images/icons/create-instance-icon.png) ).

2. Create an instance for your application:

   - Provide a name for the instance. Your application details will be auto-filled.
   - Optionally, you can select the capabilities, virtual display specifications and other configuration options for your instance. For this tutorial, you can leave these options to the defaults.

   Click *Create and start*. You will be directed to the *Instances* page where you can monitor the status of your instance.

3. Once the instance status is *running*, you can stream it and interact with your virtual device.

## Create an application

To create an application for a specific Android app, follow the steps in {ref}`sec-create-virtual-device`, but upload the APK of the Android app.

```{important}
Not all Android apps are compatible with Anbox Cloud. See {ref}`howto-port-android-apps` for more information.
```

Choose a {ref}`resource preset <sec-application-manifest-resources>` suitable for your application. If your instance is equipped with a GPU and your application requires the use of the GPU for rendering and video encoding, make sure to mention the GPU requirement using the `resources` attribute. Otherwise, the container will use a GPU if available or software encoding.

You can launch and test the application in the same way as you did for the virtual device.

## Update an application

You can have several versions of an application. See {ref}`howto-update-application` for detailed information.

Complete the following steps to add a new version to your application:

1. Go to the *Applications* page of the dashboard.
2. Click *Edit application* (![edit application icon](/images/icons/edit-application-icon.png)) to add a new version to your application.
3. Upload a new APK, or do other changes to the configuration.
4. Click *Update application*.

## Delete an application

While following this tutorial, you created several applications. You can see them on the *Applications* page.

To delete an application, click *Delete* ( ![delete application icon](/images/icons/delete-icon.png) ) and confirm the deletion.

```{tip}
To skip the confirmation window, hold **Shift** when clicking *Delete*.
```

## View instances

You can see all instances on the *Instances* page at `https://<your-machine-address>/instances`.

To view an instance, click the name of the instance you wish to view. 

The *Overview* tab displays detailed information about the instance.

The *Terminal* tab displays the terminal for the Linux instance that runs the Android container.

   You can run commands in the Linux instance, or you can enter `anbox-shell` to access the nested Android container. 
   ```{tip}
   Enter `exit` to go back to the Linux instance.
   ```

The *Logs* tab shows logs for instances that are in an error state. You will not see any logs for running instances.

   To simulate a failure for the instance, switch to the *Terminal* tab and enter the following command:

      amsctl notify-status error --message="My error message"

   Go back to the instance overview, and when the instance status changes to *error*, click on the instance name and switch to the *Logs* tab. You can now see the error logs for the instance.

## Done!

You now know how to use the web dashboard to create, launch and test applications in Anbox Cloud.

If you are interested in more advanced use cases, check out the {ref}`tut-getting-started-cli` tutorial to learn how to use Anbox Cloud from the command line.

## Related topics

* {ref}`howto-use-web-dashboard`
* {ref}`howto-manage-applications`
* {ref}`howto-instance`

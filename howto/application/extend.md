You can extend an application either by adding [hooks](#application-hooks) directly to the application or by creating an [addon](#addon) that includes one or more hooks and adding it to the application.

* If you want to extend one application only, you should use application hooks. They are easy and quick to set up and do not require creating an addon.
* If your extension contains common functionality that you want to share among multiple applications, you should create an addon that includes one or more hooks. You can then add the addon to all applications that should use the functionality.

For both options, you must create one or more hooks first. The options differ in how you add these hooks to your application.

## Create a hook

A hook is a script file that runs a series of commands at a specific time in the application life cycle. See [Hooks](https://discourse.ubuntu.com/t/hooks/28555) for detailed information.

The general steps for creating a hook are as follows:

1. Create or download any files or applications that the hook needs. For example, this could be configuration files or Android applications that you want to run.
1. In a `hooks/` sub-directory, create a script file with the commands that you want to run. As the file name, use the name of the hook.

   [note type="information" status="Tip"]

   - Supported hooks are `pre-start`, `post-start` and `post-stop`.
   - Use the `INSTANCE_TYPE` variable to distinguish between regular and base instances.

   See [Hooks](https://discourse.ubuntu.com/t/hooks/28555) for more information.
   [/note]
1. Make the hook file executable.

You must then add the hook file to your application, either [as an application hook](#application-hooks) or [through an addon](#addon).

The following sections give some examples for hooks.

### Create a hook for changing the Android system locale

Complete the following steps to create a hook that changes the Android system locale to Korean:
<!-- wokeignore:rule=master -->
1. Build the [CustomLocale](https://android.googlesource.com/platform/development/+/master/apps/CustomLocale) application from the AOSP project and move the compiled APK to a folder of your choice.
1. In your folder, create a `hooks` sub-directory:

        mkdir -p hooks && cd hooks
1. In the `hooks` directory, create a `post-start` script file with the following content:

   ```
   #!/bin/sh -ex
   if  [ "$INSTANCE_TYPE" = "regular" ]; then
     exit 0
   fi
   cp "<working_dir>"/*.apk $ANBOX_DIR/data
   anbox-shell pm install -t -g /data/CustomLocale.apk && sleep 5
   # Start CustomLocale2 application after installation, this aims to
   # initialize all available locales in the app, otherwise the following
   # system language broadcast won't work
   anbox-shell am start -n com.android.customlocale2/.CustomLocaleActivity && sleep 5
   # Change the system language by sending the broadcast to CustomLocale2
   anbox-shell am broadcast \
     -a com.android.intent.action.SET_LOCALE \
     --es com.android.intent.extra.LOCALE "ko_KR" \
     com.android.customlocale2
   sleep 5
   ```

   [note type="information" status="Important"]
   In the file, replace `<working_dir>` with the [environment variable](https://discourse.ubuntu.com/t/hooks/28555#environment-variables-1) that points to the current working directory for the hook. If you plan to run the hook [as an application hook](#application-hooks), use `$APP_DIR`. If you plan to run the hook [through an addon](#addon), use `$ADDON_DIR`.
   [/note]
1. Make all files in the `hooks` directory executable:

        cd .. && chmod +x hooks/*

### Create a hook to replace the standard Android launcher

Complete the following steps to create a hook that replaces the standard Android launcher with the custom launcher [Lawnchair](https://lawnchair.app/):

1. Download Lawnchair to a folder of your choice:

        curl -o lawnchair.apk https://f-droid.org/repo/ch.deletescape.lawnchair.plah_2001.apk

1. In your folder, create a `hooks` sub-directory:

        mkdir -p hooks && cd hooks

1. In the `hooks` directory, create a `post-start` script file with the following content:

   ```
   #!/bin/sh -ex
   if  [ "$INSTANCE_TYPE" = "regular" ]; then
     exit 0
   fi
   cp "<working_dir>"/*.apk $ANBOX_DIR/data/
   anbox-shell pm install -g -t /data/lawnchair.apk
   #
   # We need to wait until the system has settled after the package installation
   sleep 10
   #
   # Setup lawnchair as our default launcher
   LAUNCHER_ACTIVITY="ch.deletescape.lawnchair.plah/ch.deletescape.lawnchair.Launcher"
   anbox-shell cmd package set-home-activity "$LAUNCHER_ACTIVITY"
   #
   # Once we applied all of our changes we give Android a moment. If we directly
   # return here the Android container will be immediately shutdown.
   sleep 20
   ```

   [note type="information" status="Important"]
   In the file, replace `<working_dir>` with the [environment variable](https://discourse.ubuntu.com/t/hooks/28555#environment-variables-1) that points to the current working directory for the hook. If you plan to run the hook [as an application hook](#application-hooks), use `$APP_DIR`. If you plan to run the hook [through an addon](#addon), use `$ADDON_DIR`.
   [/note]
1. Make all files in the `hooks` directory executable:

        cd .. && chmod +x hooks/*

<a name="application-hooks"></a>
## Use hooks in an application

You can add your hooks directly to an application. To do so, complete the following steps:

1. In a new `my-app` directory, create a `manifest.yaml` file for your application. For example, you could use the following content to create a virtual device:

   ```
   name: my-app
   instance-type: a4.3
   ```

1. Prepare one or more hooks as described in [Create a hook](#create-a-hook-1).

1. Move the `hooks` directory and any other files that are required by the hook into the `app` directory. The folder structure should look like this:

   ```
   app
   |__ manifest.yaml
   |__ <files required for the hooks>
   |__ hooks
       |__ <hook files>
   ```

1. Create the application in AMS:

        amc application create my-app

After the application is created, launch an instance. You should see that the hook is executed and that, for example, the system locale is changed or the standard Android launcher is replaced.

[note type="information" status="Important"]
By default, the files required for the hooks (for example, APK files) are removed automatically from the application image after the [application bootstrap](https://discourse.ubuntu.com/t/17760) is completed. According to your application requirements, consider using the [`bootstrap.keep`](https://discourse.ubuntu.com/t/application-manifest/24197#bootstrap-process-2) attribute in the application manifest file if you want to keep any content needed by the application running in a regular instance.
[/note]

<a name="addon"></a>
## Create an addon with hooks

If you want to use your hooks in multiple applications, you should include them in an addon. To do so, complete the following steps:

1. In a new `my-addon` directory, prepare one or more hooks as described in [Create a hook](#create-a-hook-1).
1. Create a `manifest.yaml` file in the `my-addon` directory with the following content:

   ```
   name: my-addon
   description: |
     <Description of your addon>
   ```
1. Ensure that the folder structure looks like this:

   ```
   my-addon
   |__ manifest.yaml
   |__ <files required for the hooks>
   |__ hooks
       |__ <hook files>
   ```
1. Add the addon:

        amc addon add my-addon .

Once the addon is uploaded to AMS, you can reference it from any application manifest:

```
name: my-app
instance-type: a4.3
addons: [my-addon]
```

The application will now execute the hook and you should see that, for example, the system locale is changed or the standard Android launcher is replaced.

For more information, see [Create an addon](https://discourse.ubuntu.com/t/creating-an-addon/25284) and the [addon reference guide](https://discourse.ubuntu.com/t/addons/25293).

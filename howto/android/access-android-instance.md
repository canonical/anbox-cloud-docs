---
myst:
  html_meta:
    "description": "How to connect to an Android instance running in Anbox Cloud via ADB over TCP for debugging."
---

(howto-access-android-instance)=
# Access an Android instance

As an Android application developer, you need access to the Android instance when developing and debugging applications. Depending on the kind of access you would like to the Android instance, you can use [amc](https://snapcraft.io/amc) to connect over the network from a remote machine or use {term}`anbox-shell` to connect from within the Anbox instance.

This guide uses the Anbox Cloud Appliance to demonstrate both ways of connecting to an Android instance. So if you don't have an existing Anbox Cloud deployment already, first {ref}`install the appliance <tut-installing-appliance>`.

## Private access: Connect to the Android instance using anbox-shell

On the machine where the appliance is installed, create an instance with streaming enabled:

    amc launch --name=demo --enable-streaming

This creates an instance using the default image available and also creates a session for the instance.

Wait until the instance is running. To check, run:

    amc ls

The output will list the instance ID, copy that and run:

    amc shell demo

Now, you should be inside the shell of the Anbox instance.

To gain access to the Android instance, run:

    anbox-shell

Running anbox-shell provides you root access to the Android instance.

## Public access: Connect to the Android instance using ADB

Using `amc connect` lets you securely connect to an Android instance via the Android Debug Bridge (ADB).

```{note}
If your dashboard still shows `anbox-connect`, replace it with `amc connect`. `anbox-connect` is {ref}`deprecated <sec-anbox-connect-deprecation>` as of 1.31.0.
```

If your host machine is not the one where the appliance is installed, install `amc` on it:

    snap install amc

[Install ADB](https://developer.android.com/tools/releases/platform-tools) on your host machine. You can [install Android Studio](https://developer.android.com/studio) which also installs the Android SDK (which includes ADB as part of the platform tools). You can choose to use another IDE of your choice and install ADB independently.

On the machine where appliance is installed, create an instance with streaming enabled:

    amc launch --name=demo --enable-streaming

This creates an instance using the default image available and also creates a session for the instance.

Wait until the instance is running. To check, run:

    amc ls

Once the instance is running and has a session ID, connect using either a share URL or its instance ID or name, then complete the ADB connection.

### Connect using a share URL

On the machine where the appliance is installed, share the session:

```{note}
If you are using the charmed deployment, use `anbox-stream-gateway` instead of `anbox-cloud-appliance.gateway` in the commands.
```

    sudo anbox-cloud-appliance.gateway session share <session_id> --description="remote access to demo instance"

```{tip}
Providing a description helps you identify a shared session when you are sharing a session multiple times with different people.
```

The output returns the command you need to run next from your host machine: `amc connect <connection_url>`

Copy this output. The `<connection_url>` is a presigned URL that establishes a single ADB connection — if multiple users attempt to use the same presigned URL, any existing ADB connection will be interrupted and only the last request succeeds.

> If you are using the dashboard, locate your running instance and click *Connect ADB > Authorize* to create your first ADB share. After that, you can use the show/hide toggle in the ADB share table to display and copy the command with the presigned URL.

Now, create the connection from the terminal of your host machine (where ADB is installed). Run:

    amc connect <connection_url>

### Connect using the instance ID or name

This works directly if you are running `amc` on the AMS host. From a remote machine, first {ref}`set up remote access to AMS <howto-access-ams-remote>`.

From the terminal of your host machine (where ADB is installed), run:

    amc connect <instance_id_or_name>

### Connect ADB to the instance

Accept the message to trust the connection. Once the ADB channel is established, the output returns guidance for the next step:

    Access to the remote Anbox Cloud instance over ADB is now possible. Please run:
        $ adb connect <ip_address>

Open a new tab in the terminal and run `adb connect <ip_address>` to connect to the Android instance. It is important to open another tab so that the established ADB connection is not aborted.

You are now connected to the Android instance and can interact with it using Android Studio. If you want a visual interface of your Android application while debugging, use the dashboard or your custom stream client to stream your instance.

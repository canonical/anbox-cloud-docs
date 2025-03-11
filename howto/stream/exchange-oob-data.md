
(howto-exchange-oob-data)=
# How to exchange out-of-band data

Enabling out-of-band (OOB) data transmission between an Android application and a WebRTC client makes it possible to exchange data and trigger actions between an Android application and a WebRTC client. Anbox Cloud provides a full-duplex bidirectional data transmission mode in which data can flow in both directions at the same time.

The following instructions will walk you through how to set up data channels and perform data transmission in both directions between an Android application and a WebRTC platform.

### Prepare your web application

This guide builds upon the [streaming client setup tutorial](https://documentation.ubuntu.com/anbox-cloud/en/latest/tutorial/stream-client/) for Anbox Cloud. Ensure you have completed the setup of a web-based streaming client as described in the tutorial till the [step where you set up stream client](https://documentation.ubuntu.com/anbox-cloud/en/latest/tutorial/stream-client/#implement-the-stream-client).

#### Extend `AnboxStream` Configuration

Now, to extend an `AnboxStream` object, add the `dataChannels` property to define a new data channel. For example:

```
  <body>
    <div id="anbox-stream"></div>
    <div id="controls" style="position: absolute; top: 20px; left: 20px; z-index: 10">
      <input type="text" id="textBox" placeholder="Send message">
      <button id="sendButton">Send</button>
    </div>

    <script>
      ...
      window.onload = () => {
        const stream = new AnboxStream({
          targetElement: "anbox-stream",
          ...
          dataChannels: {
            "foo": {
              callbacks: {
                close: () => {
                  console.log('data channel is closed')
                },
                open: () => {
                  console.log('data channel is open')
                },
                error: (err) => {
                  console.log(`error: ${err}`)
                },
                message: (data) => {
                  console.log(`data received: ${data}`)
                }
              }
            }
          }
        });
        stream.connect();

        const sendButton = document.getElementById("sendButton");
        const textBox = document.getElementById("textBox");
        sendButton.addEventListener("click", () => {
          const message = textBox.value;
          if (message) {
            stream.sendData('foo', message);
          }
        });
      };
    </script>
  </body>

```

1. This extends a `AnboxStream` object to create a data channel named `foo` and registers event handlers for data communication between the Anbox instance and web client.
2. It also adds a new section to the web page, containing an input field to type and send a message to Anbox runtime through the created data channel.

When joining an existing stream-enabled instance, the data channel can be created dynamically based on the specific configuration of the instance.

```{note}
An `AnboxStream` object can create a maximum of five data channels. If the number of data channels exceeds the allowed maximum, an exception is thrown when instantiating the `AnboxStream` object.
```

### Data exchange between Anbox runtime and web client

Launch a stream-enabled instance for web client to join

```
amc launch --name test-app \
  jammy:android13:arm64 \
  --enable-streaming
```

Once the instance is up and running, retrieve the session ID:

    amc ls --filter name=test-app --format=csv | awk -F',' '{split($6, r, "="); print r[2]}'

Next, launch the web client by opening `https://<appliance_private_ip>:8080/<session_id>` in your browser. Please replace <session_id> with the session ID retrieved. Once the web page is fully loaded, streaming will be established with the active session, after the streaming connection is successfully made, the `foo` data channel will be created on the Anbox runtime server side, in response to the client's request.

At the same time, a Unix domain socket is created under the `/run/user/1000/anbox/sockets` folder in the format of `webrtc_data_<channel_name>` (`webrtc_data_foo` in the example) within the Anbox instance and represent the established communication bridge between a web client and the Anbox runtime. This Unix domain socket can be used by a service or daemon to:

- Receive data sent from a web client over the data channel and forward it to an Android application.
- Receive data sent from an Android application and forward it to a web client over the data channel.

To simulate data transmission between the Anbox runtime and the web client, you can use the [`socat`](https://manpages.ubuntu.com/manpages/bionic/man1/socat.1.html) command to connect the Unix domain socket and perform bidirectional asynchronous data sending and receiving:

1. Install the `socat` package:

   ```
   sudo apt install socat
   ```

1. Connect the Unix domain socket:

   ```
   socat - UNIX-CONNECT:/run/user/1000/anbox/sockets/webrtc_data_foo
   ```

1. This command establishes a connection to the `webrtc_data_foo` Unix domain socket, allowing you to send and receive data directly through the established data channel between Anbox runtime and the web client. After the Unix domain socket is connected, type a message and hit the `Enter` key:

       hello world

   The data is now sent from the Anbox runtime over the data channel to the web client.
1. Observe that the message is displayed in the [console](https://developer.chrome.com/docs/devtools/console) of a web client, responding to the message event:

       data received: hello world

1. To test the other direction of the communication, in the web client, type a message and send the message over the `foo` data channel to the Anbox runtime.

1. Observe that the received data is printed out in the `socat` TCP session:

   ```
   socat - UNIX-CONNECT:/run/user/1000/anbox/sockets/webrtc_data_foo
   hello world
   anbox cloud
   ```

This enables data exchange between a service running on the Anbox instance and the web client. However, it does not yet facilitate data exchange between an Android application running inside the Android container and the web client.


### Data exchange between Android application and web client

In the [Anbox Streaming SDK](https://github.com/canonical/anbox-streaming-sdk), there is an [out_of_band_v2](https://github.com/canonical/anbox-streaming-sdk/tree/master/examples/android/out_of_band_v2) project. You can either:
- compile and modify the example application to meet your needs.
- use the pre-built out-of-band v2 APK from the [release tarball](https://github.com/canonical/anbox-streaming-sdk/releases) to get started and immediately try out this feature by [running end-to-end tests](https://documentation.ubuntu.com/anbox-cloud/en/latest/howto/stream/exchange-oob-data/#run-end-to-end-test).

To build up the communication bridge between an Android application and the web client, Anbox Cloud provides a system daemon named `anbox-webrtc-data-proxy`.  This daemon is responsible for:

 * Registering a system service named `org.anbox.webrtc.IDataProxyService` to the Android system
 * Accepting connection requests from an Android application
 * Connecting to a specific data channel via the Unix domain socket exposed by the Anbox runtime
 * Passing the connected socket as a file descriptor to the Android application

This allows developers to easily make use of the Android system service for data communication between an Android application and the Anbox runtime through a file descriptor, enabling further data exchange with the web client.

#### Get notified about the availability of data channels

To receive notifications about the availability of data channels, your Android application should register the following broadcast receiver in the `AndroidManifest.xml` file:

```
<receiver
    android:name=".DataChannelEventReceiver"
    android:enabled="true"
    android:exported="true">
    <intent-filter>
        <action android:name="com.canonical.anbox.BROADCAST_DATA_CHANNELS_STATUS"/>
    </intent-filter>
</receiver>
```

Whenever the availability of data channels changes, a broadcast is sent out to the Android application. The broadcast contains the following parameters:

| Parameters               | Type                                            | Description                                                                                                                                                                |
| ------------------------ | ----------------------------------------------- | -----------------------------------------------                                                                                                                            |
| `event`                  | string                                          | Can be `created` (which means the data channels are created and open for Android applications to use) or `destroyed` (which means that the data channels are closed and destroyed) |
| `data-channel-names`     | string array                                    | Comma-separated list of data channel names that identify the changed data channels

Your Android application is required to implement a subclass of the [`BroadcastReceiver`](https://developer.android.com/guide/components/broadcasts#effects-process-state), which responds to the above events that are sent by the Android system.

```
public class DataChannelEventReceiver extends BroadcastReceiver {
    private static final String TAG = "EventReceiver";

    @Override
    public void onReceive(Context context, Intent intent) {
        Bundle extras = intent.getExtras();
        String event = extras.getString("event");
        String[] names = extras.getStringArray("data-channel-names");
        Log.i(TAG, "channels: [" + TextUtils.join(",", names) + "] event type: " + event);
    }
}
```

```{note}
If an instance is running on Android 14 image, enabling the out-of-band v2 feature requires the Android app to be running in order to receive broadcasts. If the app is in the [cached state](https://developer.android.com/guide/components/activities/process-lifecycle), the system places [context-registered broadcasts in a queue]((https://developer.android.com/develop/background-work/background-tasks/broadcasts#android-14)),meaning the app may not receive broadcasts immediately, as it would when the app is actively running. Hence, your application, which integrates the out-of-band feature, must be in a running state to receive notifications about the availability of data channels.
```

#### Access the data proxy service

There are two ways to access the `org.anbox.webrtc.IDataProxyService` binder service from an Android application:

* If you develop the application with Android studio, you can access the service by using Android's reflection API.

    ```
    IBinder getDataProxyService() {
        IBinder service = null;
        try {
            Method method = Class.forName("android.os.ServiceManager").getMethod("getService", String.class);
            service = (IBinder) method.invoke(null, "org.anbox.webrtc.IDataProxyService");
        } catch (NoSuchMethodException e) {
            e.printStackTrace();
        } catch (IllegalAccessException e) {
            e.printStackTrace();
        } catch (InvocationTargetException e) {
            e.printStackTrace();
        } catch (ClassNotFoundException e) {
            e.printStackTrace();
        }
        return service;
    }
    ```

*  If you ship the Android application inside of the AOSP source tree and [build](https://source.android.com/docs/setup/build/building) it from there, you can use Android's hidden API to access the service.

    ```
    IBinder getDataProxyService() {
        return ServiceManager.getService("org.anbox.webrtc.IDataProxyService");
    }
    ```

#### Connect the data channel

To fetch the file descriptor that refers to one data channel, send a request to the data proxy service through a binder transaction:

```
ParcelFileDescriptor mFd = null;
String channel = "foo";   // denotes data channel name
Parcel data = Parcel.obtain();
Parcel reply = Parcel.obtain();
try {
    data.writeInterfaceToken("org.anbox.webrtc.IDataProxyService@1.0");
    data.writeString(channel);
    mService.transact(TRANSACTION_connect, data, reply, 0);
    mFd = reply.readFileDescriptor();
    if (mFd.getFd() < 0) {
        Log.e(TAG, "Invalid file descriptor");
        return;
    }
    ...
    ...
} catch (RemoteException ex) {
    Log.e(TAG, "Failed to connect data channel '" +  channel + "': " + ex.getMessage());
} finally {
    data.recycle();
    reply.recycle();
}
```

#### Receive data from the Anbox runtime

Once the valid file descriptor is returned, launch an asynchronous task to read data from the Anbox runtime:

```
public class DataReadTask extends AsyncTask<Void, Void, Void> {
    ...
    ...
    @Override
    protected Void doInBackground(Void... parameters) {
        try (InputStream in = new ParcelFileDescriptor.AutoCloseInputStream(mFd)) {
            byte[] data = new byte[1024];
            while (!isCancelled()) {
                int read_size = in.read(data);
                if (read_size < 0) {
                    Log.e(TAG, "Failed to read data");
                    break;
                } else if (read_size == 0) {
                    // EOF reached
                    break;
                }

                byte [] readBytes = Arrays.copyOfRange(data, 0, read_size);
                ...
                ...
            }
        } catch (IOException ex) {
            if (!isCancelled())
                Log.e(TAG, "Failed to read data: " + ex);
        }

        return null;
    }
}
```

#### Send data to the Anbox runtime

To send data to the Anbox runtime platform through the file descriptor:

```
try {
    OutputStream ostream = new FileOutputStream(mFd.getFileDescriptor());
    ostream.write(data.getBytes(), 0, data.length());
} catch (IOException ex) {
    Log.i(TAG, "Failed to write data: " + ex.getMessage());
    ex.printStackTrace();
}
```

#### Install the APK as system app

To connect the data channel to the Anbox WebRTC data proxy service within an Android container, the Android app must be installed and running as a system app. To do so, proceed with the following steps:
1. Add the attribute `android:sharedUserId="android.uid.system"` to the `<manifest>` tag in the `AndroidManifest.xml` file of your Android app, then build your application.
1. Create an Addon to install your APK as a system app
   - First, create a directory for your addon. Inside this directory, create a `manifest.yaml` file that defines your addon.

     ```
     name: install-system-app
     description: Install APK as a system app through the pre-start hook
     ```

   - Place your APK in the same directory, create a `pre-start` hook under the `hooks` folder with the following content:

     ```
     #!/bin/bash -ex

     # Only install the APK as a system app when bootstrapping an application.
     if  [ "$INSTANCE_TYPE" = "regular" ]; then
       exit 0
     fi

     aam install-system-app \
       --apk="${ADDON_DIR}"/<your_apk_file> \
       --permissions=<comma-separated list of permissions that the application requires> \
       --package-name=<package_name>
       --access-hidden-api
     ```

   - Make sure the `pre-start` hook is executable:

     ```
     chmod +x hooks/pre-start
     ```

   - Navigate to the addon root folder and add it to AMS:

     ```
     amc addon add install-system-app .
     ```

   See [How to install an APK as a system app](https://documentation.ubuntu.com/anbox-cloud/en/latest/howto/port/install-apk-system-app/#howto-install-apk-system-app) for details.

#### Run end-to-end test

  1. To launch a stream-enabled instance with the addon you created above, run:

      ```
      amc launch --name test-oobv2 \
        jammy:android13:arm64 \
        --enable-streaming \
        --features allow_custom_system_signatures \
        --addons install-out-of-band-app
      ```


     ```{note}
     Enabling the `allow_custom_system_signatures` feature is required to run the Android application as a system app in an Android container.
     ```

  1. Retrieve the session ID that associated to the `test-oobv2` instance once it's up and running

         amc ls --filter name=test-oobv2 --format=csv | awk -F',' '{split($6, r, "="); print r[2]}'

  1. Launch the stream client that extends to [create the `foo` data channel](https://documentation.ubuntu.com/anbox-cloud/en/latest/howto/stream/exchange-oob-data/#prepare-your-web-application) by opening `https://<appliance_private_ip>:8080/<session_id>` in your browser. Please replace `<session_id>` with the session ID retrieved above.
  1. Once the WebRTC connection is established, open the Out of Band v2 application in the Android container. enter 'foo' as the channel name in the line edit widget, then click the *CONNECT* button. Check if a toast message saying 'Channel "foo" is connected' appears.
  1. Next, in the edit text widget, enter 'hello' as the text and click *SEND*. In the web client console, verify if the message is printed.
  1. In the web client, type 'world' in the text box and click *Send*, Then, check the Android application to see if the message appears in the *Received Data* edit box.

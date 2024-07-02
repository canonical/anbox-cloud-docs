(howto-exchange-oob-data)=
# How to exchange out-of-band data

Enabling out-of-band (OOB) data transmission between an Android application and a WebRTC client makes it possible to exchange data and trigger actions between an Android application and a WebRTC client.

Anbox Cloud provides two versions of this OOB data exchange:

* [Version 2](#version-2) provides a full-duplex bidirectional data transmission mode in which data can flow in both directions at the same time.

  Use this version if you start your implementation now. If you already have an existing implementation, you should plan to update it to use version 2.
* [Version 1](#version-1) enables Android application developers to trigger an action from an Android application running in an instance and forward it to a WebRTC client through the Anbox WebRTC platform. When Anbox receives the action, as one peer of the WebRTC platform, the action is propagated from Anbox to the remote peer (the WebRTC client) through a WebRTC data channel. The client can then react to the action received from the remote peer and respond accordingly on the UI.

  This version supports only half-duplex data transmission. It allows sending data from an Android application to a WebRTC client through the Anbox WebRTC platform, but it is not possible to receive data from the WebRTC client to an Android application.

```{caution}
The support for [version 1](#version-1) of the out-of-band data exchange between an Android application and a WebRTC client has been removed in the Anbox Cloud 1.16 release. Therefore, you should migrate your integration of version 1 of the OOB data exchange to [version 2](#version-2) for full-duplex data transmission and better performance.
```

See the instructions for exchanging OOB data using a specific implementation version below:
* [Version 2](#version-2)
* [Version 1](#version-1)

(sec-oob-data-version-2)=
## Version 2

The following instructions will walk you through how to set up data channels and perform data transmission in both directions between an Android application and a WebRTC platform.

### Web application

In your web-based client application, import the {ref}`sec-streaming-sdk`.

Create a data channel (named `foo` in the following example) under the `dataChannels` property of an `AnboxStream` object and register event handlers that respond to the events sent from an Android application:

```
let stream = new AnboxStream({
  ...
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
```

```{note}
An `AnboxStream` object can create a maximum of five data channels. If the number of data channels exceeds the allowed maximum, an exception is thrown when instantiating the `AnboxStream` object.
```

To launch a new WebRTC session, the client must call `stream.connect()`. The `AnboxStream` object then builds up a WebRTC native data channel internally, based on the name declared under its `dataChannels` property for peer-to-peer communication (`foo` in the example).

To send data to an Android application through the channel, the client must use the member function `sendData` of the `AnboxStream` class:

```
stream.sendData('foo', 'hello world');
```


### Anbox WebRTC platform

When establishing a peer connection, a number of data channels are set up in the Anbox WebRTC platform on the server side, upon request by the client.

At the same time, a number of Unix domain sockets are created under the `/run/user/1000/anbox/sockets` folder. They use the format `webrtc_data_<channel_name>` and represent the established communication bridge between a WebRTC client and the Anbox WebRTC platform. Those Unix domain sockets can be used by a service or daemon to:

- Receive data sent from a WebRTC client over the data channel and forward it to an Android application.
- Receive data sent from an Android application and forward it to a WebRTC client over the data channel.

A trivial example to simulate the data transmission between an instance and a WebRTC client is using the [`socat`](https://manpages.ubuntu.com/manpages/bionic/man1/socat.1.html) command to connect the Unix domain socket and perform bidirectional asynchronous data sending and receiving:

1. Connect the Unix domain socket:

   ```
   socat - UNIX-CONNECT:/run/user/1000/anbox/sockets/webrtc_data_foo
   ```

1. After the Unix domain socket is connected, type a message and hit the `Enter` key:

       hello world

   The data is now sent from the Anbox WebRTC platform over the data channel to the WebRTC client.
1. Observe that the message is displayed in the console of a web browser, responding to the message event:

       data received: hello world

1. To test the other direction of the communication, send a message from a WebRTC client to the Anbox WebRTC platform through the data channel:

   ```
   session.sendData('foo', 'anbox cloud')
   ```

1. Observe that the received data is printed out in the `socat` TCP session:

   ```
   socat - UNIX-CONNECT:/run/user/1000/anbox/sockets/webrtc_data_foo
   hello world <--  the sent data
   anbox cloud <--  the received data
   ```

### Anbox WebRTC data proxy

To build up the communication bridge between an Android application and the Anbox WebRTC platform, Anbox Cloud provides a system daemon named `anbox-webrtc-data-proxy`. This daemon is responsible for:

 * Accepting connection requests from an Android application
 * Connecting to one specific data channel via the Unix domain socket exposed by the Anbox WebRTC platform
 * Passing the connected socket as a file descriptor to the Android application

The `anbox-webrtc-data-proxy` system daemon runs in the instance and registers an Android system service named `org.anbox.webrtc.IDataProxyService`. This service allows Android developers to easily make use of binder interprocess communication (IPC) for data communication between an Android application and the Anbox WebRTC platform through a file descriptor.

```{note}
To interact with the `org.anbox.webrtc.IDataProxyService` system service, the Android application must be installed as a system app. See {ref}`howto-install-apk-system-app` for instructions.
```

#### Get notified about the availability of data channels

To get notified about the availability of data channels, an Android application can register the following broadcast receiver in the `AndroidManifest.xml` file:

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

The Android application should implement a subclass of the [`BroadcastReceiver`](https://developer.android.com/guide/components/broadcasts#effects-process-state), which responds to the above events that are sent by the Android system.

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

#### Access the data proxy service

There are two ways to access the `org.anbox.webrtc.IDataProxyService` from an Android application:

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

#### Receive data from the Anbox WebRTC platform

Once the valid file descriptor is returned, launch an asynchronous task to read data from the Anbox WebRTC platform:

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

#### Send data to the Anbox WebRTC platform

To send data to the Anbox WebRTC platform through the file descriptor:

```
OutputStream ostream = new FileOutputStream(mFd.getFileDescriptor());
try {
    ostream.write(data.getBytes(), 0, data.length());
} catch (IOException ex) {
    Log.i(TAG, "Failed to write data: " + ex.getMessage());
    ex.printStackTrace();
}
```
<!-- wokeignore:rule=master -->
For a complete Android example, see the [out_of_band_v2](https://github.com/canonical/anbox-streaming-sdk/tree/master/examples/android/out_of_band_v2) project.

(sec-oob-data-version-1)=
## Version 1

```{caution}
The support for version 1 of the out-of-band data exchange between an Android application and a WebRTC client has been removed in the Anbox Cloud 1.16 release.
```

### Android application

The following instructions will walk you through how to send a message from an Android application
running in an instance to the client application developed with the Anbox Streaming
SDK.

#### Add required permissions

For the Android application running in the instance, add the
following required permission to the `AndroidManifest.xml` to allow the
application to send messages to the Anbox runtime:

```
<?xml version="1.0" encoding="utf-8"?>
<manifest xmlns:android="http://schemas.android.com/apk/res/android"
    package="<your_application>">

    …
    <uses-permission android:name="android.permission.ANBOX_SEND_MESSAGE" />
    …
</manifest>
```

Any attempt of an application that lacks the `android.permission.ANBOX_SEND_MESSAGE`
permission to invoke APIs that are provided by the Anbox platform library will
be disallowed, and a security exception will be raised.

#### Import Java library

Check out the [Anbox Streaming SDK](https://github.com/canonical/anbox-streaming-sdk) from GitHub:

    git clone https://github.com/canonical/anbox-streaming-sdk.git

To import the `com.canonical.anbox.platform_api_skeleton.jar` library into your
Android project, refer to the official [documentation](https://developer.android.com/studio/build/dependencies)
on how to import an external library into an Android application project.

Alternatively, you can follow the steps below:

1. Copy `com.canonical.anbox.platform_api_skeleton.jar` to the `project_root/app/libs`
   directory (if the folder doesn’t exist, just create it).

2. Edit `build.gradle` under the app folder by adding the following line
   under the dependencies scope.

   ```
   dependencies {
       implementation fileTree(dir: 'libs', include: ['*.jar'])
       …
       …
       implementation files('libs/com.canonical.anbox.platform_api_skeleton.jar')
   }
   ```

#### Send message from Android

The following example demonstrates how to send a message with the Anbox
Platform API to a remote client:

```java
import com.canonical.anbox.PlatformAPISkeleton;

public class FakeCameraActivity extends AppCompatActivity {
     ….
     ….
     public void onResume() {
        super.onResume();

        String type = "message-type"; //Size is limited to 256 KB
        String data = "message-data"; //Size is limited to 1 MB
        PlatformAPISkeleton api_skeleton = new PlatformAPISkeleton();
        if (!api_skeleton.sendMessage(type, data)) {
            Log.e(TAG, "Failed to send a message type " + type + " to Anbox session");
        }
    }
}
```

### Receive message on the client

A client application that receives a message from the Android application can be written
in JavaScript, C or C++ by using the Anbox Streaming SDK.

#### Web application

For a web-based application, you can use the JavaScript SDK which you can find under {ref}`sec-streaming-sdk`. To receive the data sent from the Android application running in the instance, implement the `messageReceived` callback
of the `AnboxStream` object:

```
    let stream = new AnboxStream({
      ...
      ...
      callbacks: {
        ….
        messageReceived: (type, data) => {
          console.log("type: ", type, "  data: ", data);
        }
      }
    });
```

(howto-access-instance)=
# How to access an instance

For certain scenarios, accessing an individual instance for debugging or development might be necessary. You can do this by:

- Running `anbox-connect` for secure Android Debug Bridge (ADB) connections.
- Exposing the ADB service upon Anbox instance creation.

## Access the Android instance using anbox-connect

Since the 1.23.0 release, Anbox Cloud allows users to create a secure ADB connection through the `anbox-connect` command without exposing the [ADB service](https://documentation.ubuntu.com/anbox-cloud/en/latest/howto/instance/expose-services/). This method is highly recommended for securely connecting to remote Android instances, offering a safe and efficient means of managing ADB connections.

```{tip}
If you are running the appliance, use `anbox-cloud-appliance.gateway` for all gateway commands instead of `anbox-stream-gateway`
```

### Install `anbox-connect` snap

First, install the `anbox-connect` snap from the snap store:

    snap install anbox-connect

### Identify the session

To identify a session that you would like to share with others, run:

    anbox-stream-gateway session list

Note down the `ID` of the session.

```{tip}
If you are using the dashboard, you can also find the session ID in the *Instance details* page.
```

### Create a share for the session

````{tabs}
```{group-tab} CLI

Using the session's ID, share it the session:

    anbox-stream-gateway session share <session_id> --description="Grant access to xxx"

Providing a description helps you identify a share later on, if you are sharing a session multiple times.

The output returns a presigned URL that you can use to connect to the remote Android instance.

```
```{group-tab} Dashboard

On the *Instances* page, locate a running instance and click *Connect ADB* ( ![Connect ADB|16x16](/images/icons/adb-connect-icon.png) ).

After you authorize the connection, copy the `anbox-connect <connection_url>` provided.

```
````

Each presigned URL can only be used to establish a single ADB connection. If multiple users attempt to use the same presigned URL, any existing ADB connection will be interrupted, to allow the new request to succeed.

### Connect to the instance

Open a terminal and use the `anbox-connect` command to establish a secure ADB connection to the remote Android instance:

    anbox-connect <connection_url>

After the ADB channel is established, the following output will be displayed:

    Access to the remote Anbox Cloud instance over ADB is now possible. Please run:

        $ adb connect 127.0.0.1:32985

Lastly, follow the prompt in the command line output and run the following command to set up the ADB connection:

    adb connect 127.0.0.1:32985

```{important}
The `anbox-connect` command sets up a secure ADB channel and routes traffic between your local machine and the remote Anbox instance. Therefore, it must be kept running to maintain the ADB connection. Do not abort the command once the connection is established.
```

### Update share details

At times, you may want to extend the expiration time of a particular share. If you have multiple shares of the same session, identify the ID of the share that you want to extend:

    anbox-stream-gateway share list --session-id=<session_id> --description="Grant access to xxx"

The description helps to identify the share from the list. Update the expiry of the share:

    anbox-stream-gateway share update <share_id> --expiry=24h

The `--expiry` flag accepts values in these formats:

* A relative duration such as `24h` or `30m`, calculated from the current time
* A date-only string in the format `YYYY-MM-DD`
* A date-time string in the format `YYYY-MM-DD HH:MM:SS`

You can also update the description of a share:

    anbox-stream-gateway share update <share_id> --description=new_description

### Revoke a share
 
To revoke a particular share, run:

    anbox-stream-gateway share delete -y <share_id>

(sec-expose-adb-service)=
## Expose ADB service upon Anbox instance creation

The AMS services allow for remote connections to instances over a network by exposing the [ADB service](https://documentation.ubuntu.com/anbox-cloud/en/latest/howto/instance/expose-services/).

```{caution}
Exposing the ADB service over the public internet brings security risks from having plain text data intercepted by third parties. It's always preferable to run anbox-connect to setup a secure ADB connection for the remote access to Android instance.
```

### Launch instance

First, launch an instance with graphics enabled:

    amc launch -s +adb --enable-graphics -r default

```{note}
Use the `--vm` flag to launch a virtual machine.
```

The above command will launch a container instance from the default image with the ADB service enabled by default. With the leading `+` symbol to the `adb` service, it exposes TCP port 5559 on the public address of the node.

Afterwards you can find the network endpoint of the instance in the output of the `amc ls` command:

```bash
+----------------------+---------------+---------+---------+------+---------------+-------------------------------------------------------+
|          ID          |  APPLICATION  |  TYPE   | STATUS  | NODE |    ADDRESS    |                       ENDPOINTS                       |
+----------------------+---------------+---------+---------+------+---------------+-------------------------------------------------------+
| bpg8298j1qm4og61p7q0 |    default    | regular | running | lxd0 | 192.168.100.2 | adb:192.168.100.2:5559/tcp adb:10.226.4.200:10000/tcp |
+----------------------+---------------+---------+---------+------+---------------+-------------------------------------------------------+
```

The endpoint of the ADB service exposed from the running instance is available at 10.226.4.200:10000 on the public network.

### Connect to the instance

Connect the running instance remotely, establish the connection between your host and the instance through the exposed ADB service via TCP/IP:

    adb connect 10.226.4.200:10000

After the connection is established, you can dump the Android system logs with:

    adb logcat

Or simply run [scrcpy](https://github.com/Genymobile/scrcpy) for the display mirror, which will return information similar to the following:

```bash
INFO: scrcpy 1.10 <https://github.com/Genymobile/scrcpy>
/usr/local/share/scrcpy/scrcpy-server.jar: 1 file pushed. 9.3 MB/s (22662 bytes in 0.002s)
INFO: Initial texture: 1280x720
```

Then you can interact with the running Android container locally.

### Through SSH tunnel

In the above example, the ADB service is exposed directly over the internet. This is a major security risk as the ADB connection is not secure. To overcome this security issue, you can use the machine where AMS is running as relay server to set up a secure and encrypted SSH tunnel by forwarding the exposed ADB TCP port from the LXD machine to your localhost through the AMS machine.

```{note}
Creating an ADB connection through an SSH tunnel is not straightforward and can be troublesome. It's strongly recommended to run anbox-connect to setup a secure ADB connection for the remote access to Android instance.
```

To set up a secure connection, launch the instance so that it doesn't expose the ADB service to the internet:

    amc launch -s adb --enable-graphics -r default

```{note}
Use the `--vm` flag to launch a virtual machine.
```

As the ADB service is enabled for the launched instance but without the leading `+`, the endpoint `10.226.4.168:10000/tcp` shown via `amc ls` is not exposed to the public network:

```bash
+----------------------+---------------+---------+---------+------+---------------+-------------------------------------------------------+
|          ID          |  APPLICATION  |  TYPE   | STATUS  | NODE |    ADDRESS    |                       ENDPOINTS                       |
+----------------------+---------------+---------+---------+------+---------------+-------------------------------------------------------+
| bpg8298j1qm4og61p7q0 |    default    | regular | running | lxd0 | 192.168.100.2 | adb:192.168.100.2:5559/tcp adb:10.226.4.168:10000/tcp |
+----------------------+---------------+---------+---------+------+---------------+-------------------------------------------------------+
```

Now forward any connection to port 10000 on your localhost to port 10000 on the remote LXD machine with the address 10.226.4.168 via the AMS machine with the address 10.180.45.183:

    ssh -NL 10000:10.226.4.168:10000 ubuntu@10.180.45.183

In another terminal, you can connect the running instance via ADB with the following command:

    adb connect localhost:10000

Then run the scrcpy to display and control the Android container:

    scrcpy

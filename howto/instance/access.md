(howto-access-instance)=
# How to access an instance

In some cases, it might be necessary to access an individual instance for debugging reasons.

You can do this on the command line with the `amc` command, or you can use [scrcpy](https://github.com/Genymobile/scrcpy) for graphical access.

## Access an instance with `amc`

The `amc` command provides simple shell access to any instance managed by AMS. To access a specific instance you only need its ID:

    amc shell <id>

This command opens a bash shell inside the instance. To access the nested Android container, use the `anbox-shell` command inside the new shell. If you combined the `anbox-shell` command with `amc exec`, you can get direct access to the Android container:

    amc exec <id> -- anbox-shell

If you only want to watch the Android log output, use the following command:

    amc exec <id> -- anbox-shell logcat

`amc shell` and `amc exec` open various possibilities for automation use cases. See the help output of the commands for further details.

(sec-access-instance-scrcpy)=
## Access an instance with scrcpy

The AMS services enable connecting remotely over a network to instance via [scrcpy](https://github.com/Genymobile/scrcpy).
Scrcpy provides a simple way to display and control instances running on Anbox Cloud remotely.

In the next sections, you will learn how to connect an instance running on Anbox Cloud via scrcpy.

### Install scrcpy

Install scrcpy in one of the following ways:
<!-- wokeignore:rule=master -->
* Build scrcpy from the source by following the official [guide](https://github.com/Genymobile/scrcpy/blob/master/doc/build.md)

* Install scrcpy from the Ubuntu repository

        apt install scrcpy

  ```{note}
  <!-- wokeignore:rule=master -->
  The packaged version from the Ubuntu repositories may not be the latest. It is recommended to follow the instructions mentioned in the [scrcpy documentation](https://github.com/Genymobile/scrcpy/blob/master/doc/linux.md#latest-version) to install the latest version of scrcpy.
  ```

* Install scrcpy from the [Ubuntu snap store](https://snapcraft.io):

        sudo snap install scrcpy

  ```{note}
  The scrcpy snap package that is published to snap store is a non-official package. You can use it, but it's at your own risk. Because of this, it's highly recommended to build scrcpy from source by yourself.
  ```

### Launch instance

First, launch an instance with graphics enabled:

    amc launch -s +adb --enable-graphics -r default

```{note}
Use the `--vm` flag to launch a virtual machine.
```

The above command will launch a container instance from the default image. Since scrcpy requires ADB to establish the connection between your host and the instance, the ADB service must be enabled by default. With the leading `+` symbol to the `adb` service, it exposes TCP port 5559 on the public address of the node.

Afterwards you can find the network endpoint of the instance in the output of the `amc ls` command:

```bash
+----------------------+---------------+---------+---------+------+---------------+-------------------------------------------------------+
|          ID          |  APPLICATION  |  TYPE   | STATUS  | NODE |    ADDRESS    |                       ENDPOINTS                       |
+----------------------+---------------+---------+---------+------+---------------+-------------------------------------------------------+
| bpg8298j1qm4og61p7q0 |    default    | regular | running | lxd0 | 192.168.100.2 | adb:192.168.100.2:5559/tcp adb:10.226.4.200:10000/tcp |
+----------------------+---------------+---------+---------+------+---------------+-------------------------------------------------------+
```

The endpoint of the ADB service exposed from the running instance is available at 10.226.4.200:10000 on the public network.

```{caution}
Exposing the ADB service over the public internet brings security risks from having plain text data intercepted by third parties. It's always preferable to run scrcpy [through an encrypted SSH tunnel](#through-ssh-tunnel) if possible.
```

### Run scrcpy

Before running scrcpy to connect the running instance remotely, establish the connection between your host and the instance through the exposed ADB service via TCP/IP:

    adb connect 10.226.4.200:10000

After the connection is established, simply run `scrcpy`, which will return information similar to the following:

```bash
INFO: scrcpy 1.10 <https://github.com/Genymobile/scrcpy>
/usr/local/share/scrcpy/scrcpy-server.jar: 1 file pushed. 9.3 MB/s (22662 bytes in 0.002s)
INFO: Initial texture: 1280x720
```

Then you can interact with the running Android container locally.

### Through SSH tunnel

In the above example, the ADB service is exposed directly over the internet. This is a major security risk as the ADB connection is not secure. To overcome this security issue, you can use the machine where AMS is running as relay server to set up a secure and encrypted SSH tunnel by forwarding the exposed ADB TCP port from the LXD machine to your localhost through the AMS machine.

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

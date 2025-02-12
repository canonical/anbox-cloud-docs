(howto-stream-applications)=
# How to stream applications

You can stream applications using the Anbox Cloud dashboard or your custom stream client. You can also stream applications by launching an instance with streaming enabled, using the `amc` CLI.

````{tabs}
```{group-tab} CLI

If you are using the `amc` CLI, you can use the `--enable-streaming` option at the time of launching the instance:

    amc launch --enable-streaming <application_id>

When the `--enable-streaming` option is specified, the Anbox Management Service (AMS) automatically creates a streaming session for the instance. You can find the id of the session as a tag on the instance in the format `session=<id>`.

To further customize the streaming configuration, use the following arguments:
* `--display-size`
* `--display-density`
* `--fps`

For example, to create an instance with a 1080p resolution, a frame rate of 60 and a DPI of 120, run:

    amc launch --enable-streaming --display-size=1920x1080 --display-density=120 --fps=60 <application_id>
```
```{group-tab} Dashboard

The dashboard has in-browser streaming capabilities through WebRTC. It uses the {ref}`sec-streaming-sdk`.

When creating an instance, make sure you select the *Enable Streaming* capability to be able to stream your application. You can also set the desired streaming attributes using the *Virtual display* options available for an instance.

You can start a streaming session for any of the successfully created applications. Once the associated instance is created and ready, click *Stream* ( ![stream icon](/images/icons/stream-icon.png) ) to start the stream.

To understand how the streaming stack of Anbox Cloud works, see {ref}`exp-application-streaming`.
```
````

## Streaming statistics

You can view the streaming statistics for your running sessions by selecting the **Statistics** button on the session. The statistics display on the right pane and also have a download option to download the statistics in a `.csv` format for further analysis.

The downloaded `.csv` file has the following statistics:

| Statistic | Description |
| --------- |------------ |
| `date` | Date and time in ISO 8601 format |
| `network-currentrtt` | Current round-trip time of the network |
| `video-bandwidth` | The amount of video data that the session can handle per second |
| `video-totalreceived` | Total video data received |
| `video-fps` | Video frames per second |
| `video-decodetime` | Time taken to extract video |
| `video-jitter` | Loss of transmitted video data during streaming |
| `video-averagejitterbufferdelay` | Average jitter buffer delay in video transmission  |
| `video-packetsreceived` | Number of video packets received |
| `video-packetslost` | Number of video packets lost |
| `audio-bandwidth` | The amount of audio data that the session can handle per second |
| `audio-totalreceived` | Total audio data received during streaming |
| `audio-totalsamplesreceived` | Total number of audio samples received |
| `audio-jitter` | Loss of transmitted audio data during streaming |
| `audio-averagejitterbufferdelay` | Average jitter buffer delay in audio transmission |
| `audio-packetsreceived` | Number of audio packets received |
| `audio-packetslost` | Number of audio packets lost |

### Sharing a streaming session


````{tabs}
```{group-tab} CLI
```{tip}
If you are running the appliance, use `anbox-cloud-appliance.gateway` for all gateway commands instead of `anbox-stream-gateway`
```

You can share an authenticated session with another user by running:

    anbox-stream-gateway share <session_id> --description="Grant access to xxx"

Running this command generates a presigned URL for the session, that is valid for a specified duration.

You can later update the expiration date and description of a shared session. See {ref}`howto-access-instance` for detailed steps.

```

```{group-tab} Dashboard

To share your stream with users without an account, click *Set up sharing* ( ![set up sharing icon](/images/icons/share-stream-icon.png) ) on the *Instances* page.

Set your stream title and expiration details and generate a link that can be shared with others.
```
````

### Developer Tools

Toggle the *Developer Tools* panel on the *Stream* page to interact with your Android stream and monitor its performance. It helps you to track resource usage, view logs, and perform various actions while interacting with your Android stream in real-time to enhance your workflow. This panel is resizable, allowing you to customize your layout as needed, and can also be undocked into a separate window.

The *Terminal* tab allows you to interact with the *Ubuntu* terminal and the *Android* terminal.

The *Ubuntu* terminal is a bash shell on the Ubuntu instance hosting Anbox Cloud, where you can run commands such as `top` to monitor system processes in real-time or `free -h` to check memory usage. Other starter commands are listed within the terminal for your reference.

The *Android* terminal provides shell access to the Android operating system, allowing you to perform actions equivalent to having ADB access. Commands such as `service list` to view running Android services or `pm list packages` to list packages can be executed here. Starter commands are also included for easy reference within the terminal.

The *Logs* tabs allows you to view logs as you interact with your Android stream in real-time. It supports two types of logs: *logcat*, which displays Android-specific logs, and *syslog*, which displays system-wide logs.

In the *Logs* tabs, you can toggle auto-scroll, pause and resume log messages, clear the logs, adjust the verbosity of the logs, search using free text search or regular expressions, and export the logs.

For a detailed demonstration of the *Developer Tools* and their full capabilities, refer to: [Developer Tools](https://youtu.be/M1N8pfIUjOI?t=257&si=DJsoziD0NRTrLPff).

```
````

## Related topics

* {ref}`tut-set-up-stream-client`
* {ref}`howto-access-stream-gateway`

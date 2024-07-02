(howto-stream-applications)=
# How to stream applications

You can stream applications using the Anbox Cloud dashboard or your custom stream client. You can also stream applications by launching an instance with streaming enabled, using the `amc` CLI.

## Using the CLI

If you are using the `amc` CLI, you can use the `--enable-streaming` option at the time of launching the instance:

    amc launch --enable-streaming <application_id>

When the `--enable-streaming` option is specified, the Anbox Management Service (AMS) automatically creates a streaming session for the instance. You can find the id of the session as a tag on the instance in the format `session=<id>`.

To further customise the streaming configuration, use the following arguments:
* `--display-size`
* `--display-density`
* `--fps`

For example, to create an instance with a 1080p resolution, a frame rate of 60 and a DPI of 120, run:

    amc launch --enable-streaming --display-size=1920x1080 --display-density=120 --fps=60 <application_id>

## Using the dashboard

The dashboard has in-browser streaming capabilities through WebRTC. It uses the {ref}`sec-streaming-sdk`.

You can start a streaming session for any of the successfully created applications. An application is ready to be streamed when its *Status* is *Ready*. When you select the *Start a new session* icon for an application, you can specify the desired streaming attributes such as the screen resolution, frame rate, screen orientation before launching the session.

To understand how the streaming stack of Anbox Cloud works, see {ref}`exp-application-streaming`.

### Streaming statistics

View the streaming statistics for your running sessions by selecting the **Statistics** button on the session. The statistics display on the right pane and also have a download option to download the statistics in a `.csv` format for further analysis.

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

Use the **Sharing** button on the session page to share a streaming session with users without an account. The button generates a link using which users without an account can join your session.

## Related topics

* {ref}`tut-set-up-stream-client`
* {ref}`howto-access-stream-gateway`

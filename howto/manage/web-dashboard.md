The Anbox Cloud Dashboard offers a web GUI that users can use to create, manage and stream applications from their web browser. You can use the pre-installed dashboard almost immediately after deploying Anbox Cloud.

## Prerequisites

Before you can log into the dashboard, you must register your Ubuntu One account with the dashboard to authenticate.

### Register an Ubuntu One account in Anbox Cloud

On a regular Anbox Cloud deployment, use the following Juju action to register an Ubuntu One account:

    juju run anbox-cloud-dashboard/0 --wait=5m register-account email=<Ubuntu One email address>

You will see output similar to the following:

```sh
unit-anbox-cloud-dashboard-0:
  UnitId: anbox-cloud-dashboard/0
  id: "157"
  results:
    Stdout: |
      Visit https://10.10.10.10/register?token=eyJ0...-Td7A to create the new user
  status: completed
  timing:
    completed: 2021-02-10 14:04:46 +0000 UTC
    enqueued: 2021-02-10 14:04:44 +0000 UTC
    started: 2021-02-10 14:04:44 +0000 UTC
```

### Register an Ubuntu One account in Anbox Cloud Appliance

If you followed the instructions in the [Install the Anbox Cloud Appliance on a dedicated machine](https://discourse.ubuntu.com/t/install-appliance/22681) tutorial or in [How to install the Anbox Cloud Appliance](https://discourse.ubuntu.com/t/how-to-install-the-anbox-cloud-appliance/29702), you already registered your Ubuntu One account.

To add more accounts, use the following command:

    anbox-cloud-appliance dashboard register <Ubuntu One email address>

Accessing the resulting link will create the account and ask you to login via Ubuntu One. You only need to do this step once per user for access to the dashboard.

The generated link is valid for one hour.

## Using the dashboard

To access the dashboard, go to `https://<your-machine-address>/`. The dashboard uses self-signed certificates. You might see a warning from your browser and have to accept the certificates manually.

### Creating applications

Before creating an application, you need the following:
* An application manifest. A default application manifest is available based on the *Resource type* you choose for your application. You can customise various attributes of your application including the resource requirements for your application.
* Optionally, an Android package with support for the target architecture.

To create an application using the dashboard, use the *Add application* button on the *Applications* list screen, enter the required and any optional details that you want to provide and select *Add application*. This screen also provides the option to customise your application manifest.

There may be more advanced scenarios while creating an application that cannot be performed using the dashboard and may require using the `amc` CLI. See [How to create an application](https://discourse.ubuntu.com/t/create-an-application/24198) for more information.

### Streaming applications

The dashboard has in-browser streaming capabilities through WebRTC. It uses the [Streaming SDK](https://discourse.ubuntu.com/t/anbox-cloud-sdks/17844#anbox-cloud-streaming-sdk-8).

You can start a streaming session for any of the successfully created applications. An application is ready to be streamed when its *Status* is *Ready*. When you select the *Start a new session* icon for an application, you can specify the desired streaming attributes such as the screen resolution, frame rate, screen orientation before launching the session.

To understand how the streaming stack of Anbox Cloud works, see [About application streaming](https://discourse.ubuntu.com/t/streaming-android-applications/17769).

#### Streaming statistics

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

#### Sharing a streaming session

Use the **Sharing** button on the session page to share a streaming session with users without an account. The button generates a link using which users without an account can join your session.

### Managing Applications and their versions

If you have configured the [Anbox Application Registry (AAR)](https://discourse.ubuntu.com/t/application-registry/17761), you can view and manage applications and their versions in the registry using the **Registry** button on the main menu. If you have configured AAR in manual mode, you can also manually push and delete apps from the registry.

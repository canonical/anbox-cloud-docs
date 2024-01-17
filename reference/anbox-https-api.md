Anbox Cloud provides an HTTP API endpoint through a Unix socket at `/run/users/1000/anbox/api.socket` inside every [instance](https://discourse.ubuntu.com/t/26204#instance). The API allows controlling certain aspects of the Anbox runtime and the Android container.

## Accessing the API endpoint

The API endpoint can be for example accessed via `curl` in the following way

    curl --unix-socket /run/user/1000/anbox/sockets/api.unix s/1.0

## API versioning
When the Android container gets up and running, all REST API endpoints are served under the base path `/1.0/` inside of the Android container.

The details of a version of the API can be retrieved using `GET s/1.0`.

The reason for a major API bump is if the API breaks backward compatibility.

Feature additions are done without breaking backward compatibility only result in addition to `api_extensions` which can be used by the client to check if a given feature is supported by the server.

## Return values
There are two standard return types:

 * Standard return value
 * Error

### Standard return value
For standard synchronous operation, the following dict is returned:

```json
{
    "type": "sync",        # Standard operation type ("sync" or "async")
    "status": "Success",   # Response status
    "status_code": 200,    # Response status code
    "metadata": {}         # Extra resource/action specific metadata
}
```

HTTP code must be 200.

### Error
There are various situations in which something may immediately go
wrong, in those cases, the following return value is used:

```json
{
    "type": "error",
    "error": "API endpoint does not exist",
    "error_code": 400,
}
```

HTTP code must be one of 400 or 500.


## API structure
 * [`/1.0`](#heading--10)
   * [`/1.0/location`](#heading--10location)
   * [`/1.0/camera`](#heading--10camera)
     * [`/1.0/camera/data`](#heading--10cameradata)
   * [`/1.0/sensors`](#heading--10sensors)
   * [`/1.0/tracing`](#heading--10tracing)
   * [`/1.0/platform`](#heading--10platform)

## API details
<a name="heading--10"></a>
### `/1.0/`
#### GET

 * Description: Server configuration
 * Operation: sync
 * Steps:
    - Fetch general information of the server
* Return: Dict representing server state

Return value for `curl -s -X GET --unix-socket /run/user/1000/anbox/sockets/api.unix s/1.0 | jq .`:

```bash
{
    "metadata": {
        "api_extensions": [           # List of API extensions added after the API was marked stable
          "camera_support",
          "camera_static_data",
          "camera_video_streaming",
          "sensor_support",
          "tracing_support"
        ],
        "api_status": "stable",       # API implementation status (one of, development, stable or deprecated)
        "api_version": "1.0"          # The API version as a string
    },
    "status": "Success",
    "status_code": 200,
    "type": "sync"
}
```

<a name="heading--10location"></a>
### `/1.0/location`
#### GET

 * Description: Get location status
 * Operation: sync
 * Return: Current location status

[note type="information" status="Note"]After enabling the location endpoint, any location updates provided via the [Anbox Platform API](https://anbox-cloud.github.io/latest/anbox-platform-sdk/) won't be processed by Anbox until the location endpoint is disabled again.[/note]

 Return value for `curl -s -X GET --unix-socket /run/user/1000/anbox/sockets/api.unix s/1.0/location | jq .`:

```bash
{
    "metadata": {
      "enabled": false,
    },
    "status": "Success",
    "status_code": 200,
    "type": "sync"
}
```

#### POST
 * Description: Activate or deactivate location updates
 * Operation: sync
 * Return: standard return value or standard error

[note type="information" status="Note"]Location updates must be activated before posting any location data to Anbox via the `PATCH` method.  If location updates are disabled, requests to provide updates to the Anbox HTTP API will fail.[/note]

Return value for `curl -s -X POST --unix-socket /run/user/1000/anbox/sockets/api.unix s/1.0/location --data '{"enable":true}' | jq .`:

```bash
{
    "status": "Success",
    "status_code": 200,
    "type": "sync"
}
```
<a name="location-patch"></a>
#### PATCH
 * Description: Provide location update to be forwarded to Android
 * Operation: sync
 * Return: standard return value or standard error

[note type="information" status="Note"]
The latitude or longitude of geographic coordinates can be expressed in [decimal degree](https://en.wikipedia.org/wiki/Decimal_degrees) form (WGS84 data format) as shown below in the example or in an NMEA-based data format as [`ddmm.mm`](https://en.wikipedia.org/wiki/Geographic_coordinate_conversion) (d refers to degrees, m refers to minutes). Specify the format by setting the `format` field to either `"wgs84"` or `"nmea"`. If the field is omitted, its value defaults to `"wgs84"`. No matter which format you use, northern latitudes or eastern longitudes are positive, southern latitudes or western longitudes are negative.

Both vertical and horizontal accuracy are measured in meters. The default value for GPS accuracy is 20 meters.
[/note]

Input:

```json
{
    "latitude": 52.4538982,          # Latitude of geographic coordinates
    "longitude": 13.3857982,         # Longitude of geographic coordinates
    "altitude": 10.0,                # Altitude in meters
    "time": 1597237057,              # Current time in millisecond since 1970-01-01 00:00:00 UTC
    "speed": 0.0,                    # Speed in meters per second
    "bearing": 0.0,                  # Magnetic heading in degrees
    "format": "wgs84",               # (optional) Location format
    "horizontal_accuracy": 20,       # (optional) Horizontal accuracy in meters
    "vertical_accuracy": 20          # (optional) Vertical accuracy in meters
}
```

Return value:

```json
{
    "status": "Success",
    "status_code": 200,
    "type": "sync"
}
```

<a name="heading--10camera"></a>
### `/1.0/camera`
#### GET

* Description: Get camera basic information
 * Operation: sync
 * Return: Current camera basic information

 Return value for `curl -s -X GET --unix-socket /run/user/1000/anbox/sockets/api.unix s/1.0/camera | jq .`:

```bash
{
  "metadata": {
    "data_available": false,  # The availability of camera data
    "enabled": false,         # Is the camera support enabled in Anbox
    "resolutions": [          # The supported camera resolutions
      {
        "height": 720,        # The height of the resolution dimension
        "width": 1280         # The width of the resolution dimension
      }
    ]
  },
  "status": "Success",
  "status_code": 200,
  "type": "sync"
}
```

#### POST
 * Description: Activate or deactivate camera data updates.
    Whenever uploading a static image or streaming video content to display it in Anbox,  you need to enable the camera support first in Anbox.
 * Operation: sync
 * Return: standard return value or standard error

 Return value for `curl -s -X POST --unix-socket /run/user/1000/anbox/sockets/api.unix s/1.0/camera --data '{"enable":true}' | jq .`:

```bash
{
  "metadata": {
    "video_stream_socket": "/run/user/1000/anbox/sockets/camera_video_stream_23a2a7e0cc"
  },
  "status": "Success",
  "status_code": 200,
  "type": "sync"
}
```
The `video_stream_socket` field is a socket path that is exposed by Anbox. It can be used to stream video content (`color-format=rgba`) to Anbox to display in camera preview mode.

To determine if the camera is enabled, run the following query:

    curl -s -X GET --unix-socket /run/user/1000/anbox/sockets/api.unix s/1.0/camera | jq .metadata.enabled

<a name="heading--10cameradata"></a>
### `/1.0/camera/data`
#### POST

* Description: Upload a static image to Anbox
 After a camera is enabled,  a static image (only JPEG format is supported by far) can be uploaded to Anbox as camera data.
 * Operation: sync
 * Return: standard return value or standard error

Return value for `curl -s --unix-socket /run/user/1000/anbox/sockets/api.unix -X POST s/1.0/camera/data --data-binary @/<jpeg image path> | jq .`:
```bash
{
  "status": "Created",
  "status_code": 201,
  "type": "sync"
}
```

After this, when opening a camera application, the uploaded image should be displayed in the preview.

If a static image already exists in Anbox Cloud, when you issue the above request next time, the existing image will be overridden.

[note type="information" status="Note"]Irrespective of whether the screen orientation is in landscape or portrait, the size of the uploaded JPEG image must match one of the resolutions you got from the response to the camera info request. Anbox Cloud will rotate the image automatically for you based on current screen orientation.[/note]

#### DELETE

* Description: Delete the uploaded static image
 * Operation: sync
 * Return: standard return value or standard error

Return value for `curl --unix-socket /run/user/1000/anbox/sockets/api.unix -X DELETE s/1.0/camera/data`:

```bash
{
  "status": "Success",
  "status_code": 200,
  "type": "sync"
}
```

Since a static image is deleted, the metadata that is recorded in camera information from the following query will indicate the camera data is unavailable anymore.

    curl -s -X GET --unix-socket /run/user/1000/anbox/sockets/api.unix s/1.0/camera | jq .metadata.data_available

#### STREAM VIDEO

Whenever you enable camera support in Anbox, you will get a video stream socket that can be eligible to receive raw colour format (RGBA) based video streaming and display in the camera preview.

For example, for `curl -s -X POST --unix-socket /run/user/1000/anbox/sockets/api.unix s/1.0/camera --data '{"enable":true}' | jq -r .metadata.video_stream_socket`:

```bash
/run/user/1000/anbox/sockets/camera_video_stream_f053368cc1
```

The returned socket path is not fixed. It varies when you toggle camera support in Anbox via the above API.

For example, you have an mp4 video file available in the instance, to stream video content to Anbox

```bash
ffmpeg -r 10 -i test.mp4 -vf format=rgba -f rawvideo -r 24 - | nc -N -U /run/user/1000/anbox/sockets/camera_video_stream_f053368cc1
```

The above command will yield out 24 frame rate raw video output and send them to Anbox via the exposed video stream socket.

Similar to uploading a static image to Anbox, the video frame size must match the one of the resolution you got from the camera information API. For example, if you get 1280(w) x 720(h) resolution from the response of the camera info API, and the size of the video frame encoded in the uploaded video file is 320x640, you have to scale the video frame to the required size in some manners, otherwise you may get artefacts.

With ffmpeg, you can do:

```bash
ffmpeg -r 10 -i test.mp4 -vf format=rgba -s 1280x720 -f rawvideo -r 25 - | nc -N -U /run/user/1000/anbox/sockets/camera_video_stream
```

<a name="heading--10sensors"></a>
### `/1.0/sensors`
#### GET

* Description: Get sensors’ status and supported sensors by Anbox
 * Operation: sync
 * Return: Current sensors’ status and supported sensors by Anbox

Return value for `curl -s -X GET --unix-socket /run/user/1000/anbox/sockets/api.unix s/1.0/sensors | jq .`:

```bash
{
  "metadata": {
    "active_sensors": [             # Active sensors in Android container
      {
        "delay": 66,
        "type": "proximity"
      },
      {
        "delay": 200,
        "type": "acceleration"
      }
    ],
   "enabled": false,
   "supported_sensors": [
     "acceleration",
     "gyroscope",
     "magnetic-field",
     "orientation",
     "temperature",
     "proximity",
     "light",
     "pressure",
     "humidity"
   ]
 },
  "status": "Success",
  "status_code": 200,
  "type": "sync"
}
```

#### POST
 * Description: Activate or deactivate sensor updates
 * Operation: sync
 * Return: standard return value or standard error

[note type="information" status="Note"]Sensor updates must be activated before posting any sensor data to Anbox via the `PATCH` method.  If sensor updates are disabled, requests to provide updates to the Anbox HTTP API will fail.[/note]

Return value for `curl -s -X POST --unix-socket /run/user/1000/anbox/sockets/api.unix s/1.0/sensors --data '{"enable":true}' | jq .`:

```bash
{
    "status": "Success",
    "status_code": 200,
    "type": "sync"
}
```

#### PATCH
 * Description: Update sensor data to be forwarded to Android.
    The API accepts a JSON array-based sensor data to be forwarded to Android
 * Operation: sync
 * Return: standard return value or standard error

Return value for `curl -s --unix-socket /run/user/1000/anbox/sockets/api.unix -X PATCH s/1.0/sensors --data '[{"type": "acceleration", "x": 0.3, "y":-0.1, "z": 0.1},{"type": "pressure", "value": 1.0}]' | jq .`:

```bash
{
 "status": "Success",
 "status_code": 200,
 "type": "sync"
}
```

The sensor data is in the form of the following JSON  data structure and all values in the data are represented as floating-point data.

Sensor Type       | JSON Data structure |
------------------|---------------------|
`acceleration`    | {"type": "acceleration", "x": \<data\>, "y": \<data\>, "z": \<data\>} |
`gyroscope`       | {"type": "gyroscope", "x": \<data\>, "y": \<data\>, "z": \<data\>} |
`magnetic-field`  | {"type": "magnetic-field", "x": \<data\>, "y": \<data\>, "z": \<data\>} |
`orientation`     | {"type": "orientation", "azimuth": \<data\>, "pitch": \<data\>, "roll": \<data\>} |
`humidity`        | {"type": "humidity", "value": \<data\>} |
`pressure`        | {"type": "pressure", "value": \<data\>} |
`light`           | {"type": "light", "value": \<data\>} |
`proximity`       | {"type": "proximity", "value": \<data\>}  |
`temperature`     | {"type": "temperature", "value": \<data\>}  |

Please check the following [link](https://developer.android.com/guide/topics/sensors/sensors_environment) for the units of measure for the environmental sensors.

[note type="information" status="Note"]If Android framework or applications are not requesting sensor data during its runtime, any attempt to send sensor data to Anbox via HTTP API endpoint will fail with the error `Sensor 'acceleration' is not active` even if the sensor updates are activated.
Issuing GET method to sensor endpoint can check the current active sensors in the Android container.
[/note]


<a name="heading--10tracing"></a>
### `/1.0/tracing`
#### GET

* Description: Get tracing status
 * Operation: sync
 * Return: Current tracing status

Return value for `curl -s -X GET --unix-socket /run/user/1000/anbox/sockets/api.unix s/1.0/tracing  | jq .`:

```bash
{
 "metadata": {
   "active": false
 },
 "status": "Success",
 "status_code": 200,
 "type": "sync"
}
```

#### POST
 * Description: Activate or deactivate tracing in Anbox
 * Operation: sync
 * Return: standard return value or standard error

Return value for `curl -s -X POST --unix-socket /run/user/1000/anbox/sockets/api.unix s/1.0/tracing --data '{"enable":true}' | jq .`:

```bash
{
  "status": "Success",
  "status_code": 200,
  "type": "sync"
}
```

With this, Perfetto will start to collect performance traces from the Anbox.

Issue the following request to stop tracing:

    curl -s -X POST --unix-socket /run/user/1000/anbox/sockets/api.unix s/1.0/tracing --data '{"enable":false}' | jq .

Return value:

```bash
{
 "metadata": {
   "path": "/var/lib/anbox/traces/anbox_468634.1"
 },
 "status": "Success",
 "status_code": 200,
 "type": "sync"
}
```

As a result, a trace file can be found from the given path recorded in the response.
You can pull that file from the instance and import it to [Perfetto Trace Viewer](https://ui.perfetto.dev/#!/viewer) for further analysis.

<a name="heading--10platform"></a>
### `/1.0/platform`
#### GET

* Description: Get information about the current platform that Anbox uses
* Operation: sync
* Return: Information about the current Anbox platform

Return value for `curl -s -X GET --unix-socket /run/user/1000/anbox/sockets/api.unix s/1.0/platform | jq .`:

```bash
{
  "metadata": {
    "name": "webrtc",
    "config": {
      ...
    }
 },
  "status": "Success",
  "status_code": 200,
  "type": "sync"
}
```

#### PATCH
 * Description: Update configuration of the platform currently used by Anbox
 * Operation: sync
 * Return: Standard return value or standard error

Return value for `curl -s --unix-socket /run/user/1000/anbox/sockets/api.unix -X PATCH s/1.0/platform --data '{"config":{"rtc_log":true}}' | jq .`:

```bash
{
 "status": "Success",
 "status_code": 200,
 "type": "sync"
}
```

The available configuration items depend on the platform being used by Anbox and are dynamically registered. The following table shows a list of items available with the platforms shipping with Anbox Cloud.

Platform | Field name       | Available since   | JSON type | Access | Description        |
---------|------------------|-------------------|-----------|--------|--------------------|
`webrtc` | `rtc_log`         | 1.15 | Boolean   | read/write | Enable/disable [RTC event logging](https://webrtc.googlesource.com/src/+/lkgr/logging/g3doc/rtc_event_log.md). Logs are written to `/var/lib/anbox/traces/rtc_log.*` inside the instance. |
`webrtc` | `stream_active`   | 1.15 | Boolean   | read | `true` if a client is actively streaming, `false` if no client is connected. |

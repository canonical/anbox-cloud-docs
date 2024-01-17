Usually you wouldn't need to adjust the default WebRTC streamer configuration because it is optimised to provide a good balance between low latency and high quality. However, you can still fine-tune it to provide better results in certain situations.

Place the WebRTC streamer configuration at `/var/lib/anbox/streamer.json` within the [instance](https://discourse.ubuntu.com/t/26204#instance) before the Anbox runtime starts. The configuration can be shipped as part of an [application](https://discourse.ubuntu.com/t/managing-applications/17760) or an [addon](https://discourse.ubuntu.com/t/managing-addons/17759).

The configuration file uses the JSON format. It has the following structure:

| Name | Value type | Default | Description |
|------|------------|---------|-------------|
| `video.bitrate_limits` | array of objects | `[]` | [Bitrate limits](#video-bitrate-limits) to apply to the video encoder. |
| `nvidia_h264.multipass` | bool | `false` | If set to true, multi-pass encoding is enabled. |
| `nvidia_h264.multipass_quarter_resolution` | bool | `false` | If set to true, multi-pass encoding will be run only for a quarter of a frame's resolution. |
| `nvidia_h264.aq` | bool | `false` | If set to true, adaptive quantisation is enabled. |
| `nvidia_h264.aq_strength` | integer | `0` | Strength of adaptive quantisation: a value from `1` (least aggressive) to `15` (most aggressive). `0` means the encoder will automatically decide. |
| `nvidia_h264.preset` | integer | `0` | Preset to use (a value from `1` to `7`). `0` means Anbox will automatically decide. |

See the [NVENC Video Encoder API](https://docs.nvidia.com/video-technologies/video-codec-sdk/11.0/nvenc-video-encoder-api-prog-guide/) documentation for more details on the `nvidia_h264` options.

<a name="video-bitrate-limits"/></a>
## Video bitrate limits

Bitrate limits allow to fine-tune which minimum and maximum bitrate the WebRTC streamer will use to dynamically decide the target bitrate for the encoded video stream. As network conditions are constantly changing, WebRTC automatically tries to adapt the video bitrate to find a configuration with best throughput, quality and latency. The bitrate limits allow changing the default values that WebRTC will use as the lower and upper bound for its decision.

As different resolutions require different bitrates, the bitrate limits allow defining a minimum and maximum bitrate for frames having up to the specified number of pixels. This puts aside the actual geometry of the frame and solely concentrates on the amount of pixels the frame has.

The WebRTC streamer will pick the closest limit for the configured resolution by comparing the number of pixels and frame rate. The following rules apply:

* If more than one limit is specified, the WebRTC streamer selects the nearest limit with a number of pixels higher than the number of pixels that a frame of the given resolution has.
* If multiple limits have the same number of pixels, the streamer will sort limits descending by frame rate and apply the nearest.

The JSON object defining a bitrate limit has the following possible fields:

| Name | Value type | Default | Description |
|------|------------|---------|-------------|
| `num_pixels` | integer | `0` | Number of pixels up to which the limit is considered. |
| `fps` | integer | `0` | Frame rate the limit applies for. |
| `min_kbps` | integer | `0` | Minimum bitrate in kb/s. |
| `max_kbps` | integer | `0` | Maximum bitrate in kb/s. |

If no limits are specified, the default limits from the following table will be used:

| Resolution | Number of pixels | Frame rate | Minimum bitrate | Maximum bitrate |
|------------|------------------|------------|-----------------|-----------------|
| 720p       | `921600`         | `30`       | 1000 kb/s       | 3000 kb/s       |
| 720p       | `921600`         | `60`       | 2500 kb/s       | 5000 kb/s       |
| 1080p      | `2073600`        | `30`       | 3000 kb/s       | 6000 kb/s       |
| 1080p      | `2073600`        | `60`       | 3000 kb/s       | 7000 kb/s       |

## Example configuration

The following example shows a configuration for the WebRTC streamer:

    {
        "video": {
            "bitrate_limits": [
                { "num_pixels": 921600, "fps": 60, "min_kbps": 1000, "max_kbps": 4500 }
            ],
            "nvidia_h264": {
                "multipass": true,
                "aq": true,
                "aq_strength": 5
            }
        }
    }

The `num_pixels` value here is calculated based on a 720p resolution, thus `1280 * 720 = 921600`.

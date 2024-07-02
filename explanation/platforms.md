(exp-platforms)=
# Supported platforms

Anbox Cloud currently supports the `swrast`, `null`, `webrtc` platforms. This guide covers the display settings configuration for these platforms.

To instruct an instance to use a platform, include the `--platform` (or `-p`) flag when launching the instance:

    amc launch -p webrtc <application>

## Configuration for `swrast` platform

```{caution}
The `swrast` platform is deprecated and has been replaced with the `webrtc` platform starting with Anbox Cloud 1.13. You can still explicitly specify `swrast` as platform name, but internally, it is mapped to the `webrtc` platform. The `webrtc` platform provides backward compatibility with the display settings described below.
```

Anbox Cloud provides a way of add user data to the Android container upon its launch which can configure the display settings for `swrast` platform.

By default, when launching an Android container on the `swrast` platform without specifying the display settings through user data, the following display specification will be used:

Display specs   | Value
----------------|-------
Width           | 1280
Height          | 720
FPS             | 60
Density         | 160

If you want to change the display settings of the Android container, you need to provide a combination of a numeric formatting string as follows:

    <Display width>,<Display height>,<FPS>,<Display density>

The first two fields which imply display width and display height respectively are required, however the latter two are optional. When launching an instance, mention the display settings via user data:

    amc launch --userdata="960,720,30,120" -p swrast <application>

Then the specified display setting will be applied after the instance gets started.

(sec-null-platform)=
## Configuration for `null` platform

Display settings for the `null` platform can be configured in the same way as for the `swrast` platform.

Instead of supplying the display settings via `userdata` through the `amc launch` command, they can be alternatively written before the start of the Anbox runtime (e.g. in a `pre-start` hook) to `/var/lib/anbox/display_settings`. The format remains the same as when supplied as `userdata`.

## Configuration for `webrtc` platform

The `webrtc` platform can be configured through user data provided to the instance in JSON format. AMS puts the configuration data at `/var/lib/anbox/userdata`.

Field name | Type | Default | Description
-----------|------|---------|------------
`display_width` | `int` | `1280` | Width of the display provided to Android.
`display_height` | `int` | `720` | Height of the display provided to Android.
`display_density` | `int` | `240` | Density of the display provided to Android.
`fps` | `int` | `60` | Refresh rate of the display provided to Android.

For example, to configure the platform for a display height of 1080p and 60 FPS, set the user data for an instance like this:

    amc launch -p webrtc --userdata '{"display_width":1920, "display_height":1080, "fps": 60}'

## Related topics

* {ref}`exp-platforms`

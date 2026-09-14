---
myst:
  html_meta:
    "description": "Explanation of Anbox Cloud platforms (swrast, null, webrtc), covering what each does and how to configure display settings."
---

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

### Single-display configuration

Use the following fields to configure a single display through user data:

Field name | Type | Default | Description
-----------|------|---------|------------
`display_width` | `int` | `1280` | Width of the display provided to Android.
`display_height` | `int` | `720` | Height of the display provided to Android.
`display_density` | `int` | `240` | Density of the display provided to Android.
`fps` | `int` | `60` | Refresh rate of the display provided to Android.

For example, to configure the platform for a display height of 1080p and 60 FPS, set the user data for an instance like this:

    amc launch -p webrtc --userdata '{"display_width":1920, "display_height":1080, "fps": 60}'

(sec-webrtc-platform-multi-display)=
### Multi-display configuration

For multi-display instances, AMS passes a `displays` array to the runtime in the session data. It is derived from `config.displays` in the instance creation request. Each entry contains `width`, `height`, `density` and `fps`. The first entry defines the primary display (display `0`), and subsequent entries define secondary displays in order.

For example, the display-related portion of the generated session data for two displays has this shape:

```json
{
  "displays": [
    {
      "width": 1920,
      "height": 1080,
      "density": 240,
      "fps": 60
    },
    {
      "width": 1280,
      "height": 720,
      "density": 160,
      "fps": 30
    }
  ],
  "display_width": 1920,
  "display_height": 1080,
  "display_density": 240,
  "fps": 60
}
```

AMS populates the flat `display_width`, `display_height`, `display_density` and `fps` fields from the primary display for compatibility with older runtimes. These fields do not describe the secondary displays.

Configure multiple displays through AMS when creating the instance. The single-display user data fields do not configure additional displays. See {ref}`exp-multi-display` for supported images, display limits and the display lifecycle.

## Related topics

- {ref}`exp-platforms`

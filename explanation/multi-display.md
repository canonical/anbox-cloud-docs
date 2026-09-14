---
myst:
  html_meta:
    "description": "How multi-display streaming works in Anbox Cloud, including its use cases, display configuration, streaming behavior and limitations."
---

(exp-multi-display)=
# Multi-display

Multi-display lets one Anbox Cloud instance provide several independent Android displays through a single streaming session. Each display can show different content rather than mirroring the primary display and have its own resolution, density, frame rate and video output.

The feature is intended for Android workloads that need more than one display from the same Android environment. It is supported for instances that use [virtualized Android images](https://canonical.com/anbox-cloud/docs/reference/provided-images/). It is not supported for instances that use containerized Android.

## Use cases

Multiple displays are useful when a workload needs several outputs from the same Android environment:

- Automotive systems can show an instrument cluster and infotainment display simultaneously.
- Productivity applications can present content across multiple virtual displays.
- Digital signage can show independent content on different displays.
- QA and testing tools can observe several Android display outputs at once.

## Display configuration

Configure the displays when you create the instance. The first configured display is the primary display and the remaining displays are secondary displays, in the order you configure them.

Each display can have its own resolution, density and frame rate. For example, one display at 1080p and 60 FPS and another at 720p and 30 FPS.

If you do not set values for a display, it uses the defaults: 720p resolution, 240 DPI density and 60 FPS frame rate

All displays are available when Android starts. You cannot add, remove or reconfigure a display while the instance is running. To use a different display configuration, create another instance.

## Streaming multiple displays

When streaming is enabled, a single streaming session carries all configured displays. Each display is delivered as a separate video track, while one audio track is shared across the session. This allows the streaming client to present and interact with each display independently.

The Anbox Streaming SDK provides the interfaces needed to associate each video track with its display and route input to the correct display. See {ref}`sec-streaming-sdk` for information about implementing a multi-display streaming client.

## Input and display focus

The dashboard routes pointer and touch input to the display where the interaction occurs. Interacting with a display also gives it focus in Android, which then routes captured keyboard input to that display. Before typing, interact with the display that should receive the input.

The dashboard highlights the last display you interacted with. Display-specific controls, such as **Home**, **Back** and **Capture keyboard**, apply to this display and remain disabled until you select one.

The dashboard highlight might not always match Android's focus. Android focus can also change without a dashboard interaction, for example when an activity is started on another display through ADB. If keyboard input goes to an unexpected display, interact with the intended display to restore its focus.

For details about the available controls, see {ref}`ref-stream-controls-bar`.

## Limitations

- Multi-display is supported only for instances with virtualized Android. You can configure a maximum of four displays per instance, including the primary display.
- Displays are cold-plugged before Android starts. Adding or removing displays while the instance is running is not supported.
- The dashboard does not support rotating or resizing displays.
- All streamed displays share one audio track.

## Related topics

- {ref}`exp-application-streaming`
- {ref}`exp-android-execution-models`
- {ref}`exp-capacity-planning`
- {ref}`howto-create-multi-display-instance`
- [Cuttlefish multi-display support](https://source.android.com/docs/devices/cuttlefish/multi-display)

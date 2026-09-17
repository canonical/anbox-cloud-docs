---
myst:
  html_meta:
    "description": "How multi-display streaming works in Anbox Cloud, including display configuration, runtime lifecycle, WebRTC tracks, input routing and resource constraints."
---

(exp-multi-display)=
# Multi-display streaming

Multi-display streaming exposes several independent Android displays from one Anbox Cloud instance through a single streaming session. Each display has its own video output and can show different content. The displays are not mirrors of the primary display.

An Android display is configured when the instance is created. Its client-side presentation is a video element attached to a received video track.

## Use cases

Multiple displays are useful when a workload needs several outputs from the same Android environment:

- Automotive systems can show an instrument cluster and infotainment display simultaneously.
- Productivity applications can present content across multiple virtual displays.
- Digital signage can show independent content on different displays.
- QA and testing tools can observe several Android display outputs at once.

Carrying these outputs in one session avoids the overhead of establishing a separate streaming session for each display.

(sec-multi-display-constraints)=
## Constraints

Multi-display support in Anbox Cloud 1.31.0 has the following scope:

| Aspect | Supported behavior |
| --- | --- |
| Images | Multiple displays require a Cuttlefish-based `euphotic` image. AMS rejects multi-display configuration for unsupported images. |
| Display count | Up to four displays per instance, including the primary display. |
| Display lifecycle | All displays are configured at instance creation and provisioned at boot. Adding or removing Android displays while the instance is running is not supported. |
| Display configuration | Each display can have its own resolution, density and frame rate. |
| Audio | One audio track is shared across all displays; there is no separate audio track per display. |
| Rendering and encoding | The initial implementation uses software rendering and video encoding, not GPU acceleration. |
| Dashboard controls | Display rotation and resizing are unavailable in the initial multi-display implementation. |

(sec-multi-display-how-it-works)=
## How it works

Four subsystems carry a display from its configuration to the browser:

1. The Anbox Management Service (AMS) validates the display configuration and passes it to the instance.
2. Anbox runtime provisions the virtual displays and identifies the source display of each frame.
3. The WebRTC platform renders and encodes each display through a dedicated pipeline, producing one video track per display.
4. The Anbox Streaming SDK associates each track with a display and renders it in a separate video element.

### Configuration and display identity

AMS accepts an ordered list of display configurations. The first entry defines the primary display, with display ID `0`. Subsequent entries define secondary displays with IDs `1`, `2` and `3`. Each entry describes the display's width, height, density and frame rate.

This identity connects the configuration, frame delivery, video track and input routing. For example, it lets the client distinguish the infotainment display from the instrument cluster within the same instance and session.

### Runtime provisioning

The runtime uses cold-plugging: it provisions all required displays before Android boots. The current QEMU-backed Cuttlefish environment does not support the display hotplugging mechanism available with Cuttlefish's CrosVM backend. The display count is therefore static.

The runtime configures multiple outputs, called scanout heads, on one virtual graphics device. It does not add a separate graphics device for each display. Each output has its own framebuffer. Display metadata describes its dimensions, density and refresh rate so that Android can recognize and manage independent displays.

When Android produces a frame, QEMU delivers it to the runtime through its D-Bus display interface. The runtime identifies which display the frame belongs to and passes that display ID through the Anbox Platform SDK to the WebRTC platform.

### Independent video pipelines, shared session

Each display has a dedicated frame renderer and thread, with an independent video encoding pipeline. This avoids making all displays wait on a single rendering pipeline and allows mixed configurations, such as a primary display at 60 FPS and a secondary display at 30 FPS.

During session negotiation, the WebRTC platform allocates a video transceiver for each configured display. The resulting video tracks travel through the same WebRTC peer connection. Audio remains session-wide.

Separate pipelines reduce processing bottlenecks, but they do not provide dedicated host resources or separate network capacity. All displays still compete for the instance's CPU and memory and the available network bandwidth.

### Client-side presentation

The Anbox Streaming SDK discovers the display tracks when the connection is established.

The SDK wraps each video track in its own `MediaStream` so that each video element renders only its assigned display. Consumers attach a display to a container in response to a track-added callback. They do not need to know the display count in advance.

This event-driven attachment is dynamic only on the client side. Track-added and track-removed callbacks describe streaming track availability, not the creation or removal of Android displays. Similarly, hiding a display in the client does not deallocate its virtual hardware or stop its server-side pipeline.

The primary display also anchors the session lifecycle: when its video track ends, the SDK closes the session. When a secondary track ends, the SDK notifies the consumer so that it can detach that display's presentation.

(sec-multi-display-input)=
## Input routing and focus

Touch and mouse messages carry a display ID over the control data channel. The streaming server and runtime use that ID to deliver input to the intended display rather than always directing it to the primary display. For backward compatibility, messages without a display ID target display `0`.

Keyboard input follows Android's native focus management. A touch interaction can focus a display, after which Android routes keyboard events to it. Other Android events, such as starting an activity through ADB, can also change focus.

The dashboard highlights the last display that received a touch interaction. That highlight is a client-side indication, not an authoritative view of Android focus. An activity started elsewhere can change Android focus without updating the highlight. Fitting a display into the available browser space is likewise a presentation change, not a focus change.

(sec-multi-display-performance)=
## Resource and performance considerations

Sharing a session reduces session overhead, but each additional display still requires rendering, framebuffers, graphics buffers, video encoding and network traffic. With software rendering and encoding, active displays increase CPU demand substantially. Memory demand also grows as additional display buffers are allocated.

Resource planning therefore needs to account for display count, resolution, frame rate and how frequently content changes. Insufficient CPU capacity can cause frame drops and increased encoding latency. Allocating more CPU and memory to each instance improves its available capacity. However, it reduces the number of instances that a node can host.

(sec-multi-display-static-frames)=
### Static frame suppression

Static frame suppression reduces unnecessary encoding and transmission when a display's content is unchanged. It is enabled by default for multi-display instances through the `webrtc.suppress_static_frames` feature flag.

For active content, the renderer follows the display's configured frame rate. For static content, it avoids repeatedly sending the cached frame at that rate. Instead, it sends periodic keep-alive frames to maintain the connection and encoding quality. The initial implementation uses a keep-alive rate of 3 FPS.

This is particularly useful when one display is active while another shows mostly unchanged content. It reduces CPU usage and bandwidth for idle displays without removing them from Android or the streaming session.

Setting `webrtc.suppress_static_frames=false` disables suppression when a workload needs a consistent target frame rate or encounters problems with suppression. Disabling it increases the work required for static displays. It does not guarantee that the target frame rate can be sustained with insufficient resources.

(sec-multi-display-compatibility)=
## Single-display compatibility

Existing single-display workflows remain supported. AMS retains the legacy single-display configuration for backward compatibility and includes the primary display's configuration in the legacy session-data fields for older runtimes.

The SDK retains its existing single-display target-element option. Multi-display consumers use per-track attachment instead. These compatibility paths preserve single-display behavior. They do not give older runtimes or clients multi-display support.

## Related topics

- {ref}`exp-application-streaming`
- {ref}`exp-android-execution-models`
- {ref}`exp-capacity-planning`
- [Cuttlefish multi-display support](https://source.android.com/docs/devices/cuttlefish/multi-display)

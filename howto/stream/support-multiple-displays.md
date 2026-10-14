---
myst:
  html_meta:
    "description": "How to integrate the Anbox Streaming SDK into a web stream client to support multiple displays using the attachDisplay API."
---

(howto-support-multiple-displays)=
# Support multiple displays in a stream client

When an instance with multiple displays (see {ref}`exp-multi-display`) is streamed, the stream client receives a separate video track for each display and controls how the displays are arranged.

The [Anbox Streaming SDK](https://github.com/canonical/anbox-streaming-sdk) provides the `attachDisplay` method, giving the client full control over where each display is rendered at runtime. Setting up a stream client for a single display and for multiple displays follows the same general process. This guide covers the steps specific to multi-display. For the complete stream-client setup, see {ref}`tut-set-up-stream-client`. For an overview of the feature, see {ref}`exp-multi-display`.

## Initialize AnboxStream without targetElement

In legacy single-display mode, if you pass the `targetElement` option to `AnboxStream`, the SDK automatically renders the video of the primary display into that element, leaving you with no control over individual display layouts.

In multi-display mode, omit `targetElement` when initializing `AnboxStream`. Each time `videoTrackAdded` reports a display, call `attachDisplay(displayId, containerId)` to specify where that display is rendered. Repeat this for every reported display, including the primary display.

## Attach displays dynamically

The Anbox Streaming SDK discovers available display tracks once the WebRTC peer connection is established. It invokes `videoTrackAdded` for each available track and `videoTrackRemoved` when a track ends. Both callbacks receive the display ID.

The integration flow follows these steps:

1. Initialize the `AnboxStream` object without `targetElement`, and register the `videoTrackAdded` and `videoTrackRemoved` callback functions.
1. When the `videoTrackAdded` callback fires, locate or create a video container element for that display in the DOM. You can either create the video container dynamically on the fly or use a pre-existing element with pre-configured CSS layouts or styling.
1. Once the video container has been mounted to the DOM, call `attachDisplay` with the display ID and the container's `id`. The SDK injects the `<video>` element into the container and routes input events for that display.
1. When `videoTrackRemoved` fires, remove the video container of that display from the layout.

```html
<div id="displays"></div>

<script>
  const stream = new AnboxStream({
    // No targetElement here.
    connector: { /* ... */ },
    callbacks: {
      videoTrackAdded: (displayId) => {
        const container = document.createElement("div");
        container.id = `anbox-stream-display-${displayId}`;
        document.getElementById("displays").appendChild(container);

        stream.attachDisplay(displayId, container.id);
      },
      videoTrackRemoved: (displayId) => {
        document.getElementById(`anbox-stream-display-${displayId}`)?.remove();
      },
    },
  });

  stream.connect();
</script>
```

Because you own the containers, you can lay them out however you like, for example side by side, in tabs, or as a main view with smaller previews in grid. Size each container as needed, and the SDK fits the video of that display into it.

## Target a specific display

In a multi-display mode, several SDK methods accept a `displayId` parameter to target a specific display.
For example, call `requestFullscreen` to show a single display in full screen:

```javascript
stream.requestFullscreen(displayId);
```

For a complete list of supported methods and additional details, please refer to the [Anbox Streaming SDK](https://github.com/canonical/anbox-streaming-sdk).

## Related topics

- {ref}`tut-set-up-stream-client`
- {ref}`sec-streaming-sdk`
- {ref}`exp-multi-display`
- {ref}`howto-create-multi-display-instance`

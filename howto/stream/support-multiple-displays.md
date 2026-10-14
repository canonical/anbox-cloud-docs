---
myst:
  html_meta:
    "description": "How to integrate the Anbox Streaming SDK into a web stream client to support multiple displays using the attachDisplay API."
---

(howto-support-multiple-displays)=
# Support multiple displays in a stream client

An AMS instance can stream with more than one display (see {ref}`exp-multi-display`), and a stream client has to lay out the video of each display itself.
To support this, the [Anbox Streaming SDK](https://github.com/canonical/anbox-streaming-sdk) provides the `attachDisplay` API, which lets the client attach a display to a video container element of its own choosing at runtime.

Setting up a stream client for a single display and for multiple displays follows the same flow.
This guide only covers what differs.
For the complete walkthrough, see {ref}`tut-set-up-stream-client`.

## Omit `targetElement`

* Legacy Single-Display Mode: If you pass the `targetElement` option to AnboxStream, the SDK automatically injects the video of display 0(the primary display) into that element, leaving you with no control over individual display layouts.
* Multi display Mode: Omit `targetElement` during initialization. In this mode, you must explicitly call `attachDisplay(displayId, containerId)` for every active display (including display 0, the primary display) to define where it should be rendered.

## Attach displays dynamically

The SDK does not know in advance how many displays the instance has.  It reports each display through the `videoTrackAdded` callback, and reports a display going away through `videoTrackRemoved`. Both callbacks receive the display ID, which starts at 0.

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

Because you own the containers, you can lay them out however you like, for example side by side, in tabs, or as a main display with thumbnails. Size each container as needed, and the SDK fits the video of that display into it.

## Target a specific display

Several SDK methods accept a `displayId` parameter, allowing you to target a specific screen in a multi-display layout.
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

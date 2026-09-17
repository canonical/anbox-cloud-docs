---
myst:
  html_meta:
    "description": "How to create and stream an Anbox Cloud instance with multiple displays, configure display settings, and adjust the multi-display view."
---

(howto-create-multi-display-instance)=
# Create an instance with multiple displays
This guide shows you how to create an instance with multiple displays. A multi-display instance can have up to four displays, each with its own resolution, frame rate and density.

Multi-display is supported only with {term}`Virtualized Android`. For an overview of multi-display instances, see <>.

::::{tab-set}
:::{tab-item} CLI
:sync: cli


:::

:::{tab-item} Dashboard
:sync: dashboard

To create an instance with multiple displays:

1. Go to the *Instances* page, click *Create instance*.
2. In the Source section:
    - From the *Create the instance from* dropdown, select `Image`.
    - From the *Image* dropdown, select a {ref}`Virtualized Android image <ref-provided-images>`, such as `resolute:android16-cf:amd64`.
3. Expand the Displays section.
    - Click *Add display* to add another display. You can configure up to four displays in total.
    - For each display, configure the following settings as required:
        - Screen resolution
        - Frame rate
        - Display density (DPI)
        - Screen orientation
4. Optionally, configure the remaining fields in the {ref}`instance creation form <howto-create-instance>`.
5. Click *Create and start*.

Alternatively, you can create a multi-display instance directly from the *Images* page. Locate a euphotic variant image and click the *Create instance* shortcut. This opens the instance creation form with *Create the instance from* and *Image* fields already populated with the selected image.

```{note}
You cannot add, edit, or remove displays after creating the instance.
```

## Stream the displays

Once the multi-display instance is running, click *Stream* ( ![stream icon](/images/icons/stream-icon.png) ) to open the *Stream* page. The page shows all the configured displays and provides the {ref}`Stream controls bar <ref-stream-controls-bar>` for interacting with the multi-display instance.

When the *Stream* page first opens, no display is focused. Interact with a display to focus it. The display-specific controls in the *Stream controls bar* apply only to the focused display. Until a display is focused, controls that require one remain unavailable.

For example, when *Capture keyboard input* is enabled, keyboard input is sent to the focused display.

## Adjust the view

Use *Zoom in* () and *Zoom out* (), or use the mouse wheel, to adjust the view. You can pan across the stream page to move around the display area.

To fit all displays within the view, click *Fit all* ().

To fit a single display within the view, hover over it and click *Fit* (). The other displays are temporarily hidden. To return to the view showing all displays, click *Show all* ().

```{note}
*Rotate left*, *Rotate right*, and *Resize* are not supported for multi-display instances.
```

:::
::::

## Related topics

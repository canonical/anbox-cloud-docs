---
myst:
  html_meta:
    "description": "How to create and stream an Anbox Cloud instance with multiple displays, configure display settings, and adjust the multi-display view."
---

(howto-create-multi-display-instance)=
# Create an instance with multiple displays
This guide shows you how to create an instance with multiple displays. A multi-display instance can have up to four displays, each with its own resolution, frame rate and density.

Multi-display is supported only with {term}`Virtualized Android`. For an overview of multi-display support in Anbox Cloud, see {ref}`exp-multi-display`.

::::{tab-set}
:::{tab-item} CLI
:sync: cli

To create an instance with multiple displays, use `amc launch` with one `--display` flag per display. You can pass `--display` up to four times to configure up to four displays.

Each `--display` flag takes a comma-separated list of `key=value` pairs, in the following format:

    --display=width=<W>,height=<H>[,dpi=<D>,fps=<FPS>]

- `width` and `height` are required and must each be greater than `0`.
- `dpi` is optional. If not set, it defaults to `320`.
- `fps` is optional and must be between `0` and `60`. If not set, it defaults to `60`, or to `30` if the instance has no GPU slots assigned.

`--display` cannot be combined with the legacy `--display-size`, `--display-density`, and `--fps` flags, which only configure a single display.

For example, the following command creates an instance with four displays, each with its own resolution, density and frame rate:

```bash
amc launch resolute:aaos16-cf:amd64 --enable-streaming --name multi-display-instance --display=width=1280,height=720,fps=60 --display=width=480,height=640,dpi=120 --display=width=800,height=600,fps=30 --display=width=1280,height=720,fps=30
```

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

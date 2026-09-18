(ref-stream-controls-bar)=
# Stream controls bar
The *Stream controls bar* appears on the right side of the *Stream* page. The controls are grouped into three sections based on whether they affect the whole instance, an individual display, or the streaming session.

![Stream multi-display instance](/images/stream-sidebar/stream-multi-display-instance.png)

## Instance and Android controls

These controls affect the instance or Android as a whole rather than a specific display. In multi-display instances, their behavior does not depend on which display is focused.

### Connect ADB

*Button:* ![Connect ADB](/images/stream-sidebar/connect-adb-icon.png){width=30px}

*Shortcut: `Ctrl + Shift + C`*

The **Connect ADB** action generates a pre-signed URL that can be used to connect to the Android Debug Bridge (ADB) for the running instance. It also provides [instructions](/howto/android/access-android-instance.md) on how to use the URL. This allows developers to interact with the Android instance using ADB commands, which is useful for debugging and testing applications.

### Open developer tools

*Button:* ![Developer Tools Toggle](/images/stream-sidebar/developer-tools-toggle-icon.png){width=30px}

*Shortcut: `Ctrl + Shift + D`*

The **Open developer tools** action opens a panel with various tools for developers to interact with the streaming session, including a terminal and logs for the running instance.

### Set location

*Button:* ![Location Toggle](/images/stream-sidebar/location-toggle-icon.png){width=30px}

*Shortcut: `Ctrl + Shift + G`*

The **Set location** action opens a panel where you can set the geographic location (GPS coordinates) for the virtual device. This is useful for testing applications that rely on location services.

When you set a location, the virtual device behaves as if it is physically present at those coordinates.

### Volume up

*Button:* ![Volume Up Toggle](/images/stream-sidebar/volume-up-toggle-icon.png){width=30px}

*Shortcut: `Ctrl + Shift + ArrowUp`*

The **Volume up** action increases the volume of the Android device, simulating a volume button press on a physical device.

### Volume down

*Button:* ![Volume Down Toggle](/images/stream-sidebar/volume-down-toggle-icon.png){width=30px}

*Shortcut: `Ctrl + Shift + ArrowDown`*

The **Volume down** action decreases the volume of the Android device, simulating a volume button press on a physical device.

### Power

*Button:* ![Power](/images/stream-sidebar/power-toggle-icon.png){width=30px}

*Shortcut: `Ctrl + Shift + P`*

The **Power** action turns the display of the Android device on or off, simulating a power button press on a physical device.

## Display-specific controls

These controls affect an individual display. In a single-display stream, they apply to the only display. In a multi-display stream, supported controls apply to the focused display. You must focus a display before using them.

```{note}
The *Rotate left*, *Rotate right*, and *Resize* controls are not supported for multi-display instances.
```

### Home

*Button:* ![Home Button](/images/stream-sidebar/home-icon.png){width=30px}

*Shortcut: `Ctrl + Shift + H`*

The **Home** action simulates a home button press on a physical device.

### Back

*Button:* ![Back Button](/images/stream-sidebar/back-icon.png){width=30px}

*Shortcut: `Ctrl + Shift + E`*

The **Back** action simulates a back button press on a physical device.

### Release / Capture keyboard

*Button:* ![Release Keyboard Toggle](/images/stream-sidebar/release-keyboard-toggle-icon.png){width=30px}

*Shortcut: `Ctrl + Shift + K`*

The **Release / Capture keyboard** action allows you to switch the capture of keyboard events by the Android device on and off. When the capture is off, the key events will be sent to the browser's page.

### Rotate left

*Button:* ![Rotate Left Toggle](/images/stream-sidebar/rotate-left-toggle-icon.png){width=30px}

*Shortcut: `Ctrl + Shift + ArrowLeft`*

The **Rotate left** action rotates the stream to the left by 90 degrees.

### Rotate right

*Button:* ![Rotate Right Toggle](/images/stream-sidebar/rotate-right-toggle-icon.png){width=30px}

*Shortcut: `Ctrl + Shift + ArrowRight`*

The **Rotate right** action rotates the stream to the right by 90 degrees.

### Enable / Disable stream resize

*Button:* ![Stream Resize Toggle](/images/stream-sidebar/stream-resize-toggle-icon.png){width=30px}

*Shortcut: `Ctrl + Shift + R`*

The **Enable / Disable stream resize** action allows you to toggle resize mode, which allows to resize the stream, or reset its size to fit the whole available space.

### Full screen

*Button:* ![Full Screen Toggle](/images/stream-sidebar/full-screen-toggle-icon.png){width=30px}

*Shortcut: `Ctrl + Shift + F`*

The **Full screen** action toggles the streaming session between full-screen and windowed mode.

### Show statistics

*Button:* ![Statistics Toggle](/images/stream-sidebar/statistics-toggle-icon.png){width=30px}

*Shortcut: `Ctrl + Shift + M`*

The **Show statistics** action opens a panel that displays real-time streaming statistics. This information is useful for monitoring the performance and quality of the stream and can help diagnose streaming issues.

### Take a screenshot

*Button:* ![Screenshot Toggle](/images/stream-sidebar/screenshot-toggle-icon.png){width=30px}

*Shortcut: `Ctrl + Shift + I`*

The **Take a screenshot** action takes a screenshot of the Android device.

### Start / Stop screen recording

*Button:* ![Screen Record Toggle](/images/stream-sidebar/screen-record-toggle-icon.png){width=30px}

*Shortcut: `Ctrl + Shift + O`*

The **Start / Stop screen recording** action starts recording a video of the streaming session. Clicking the button a second time stops the recording and saves the video to your local device. This is useful for creating demos, tutorials, or for troubleshooting.

## Session utilities

These actions support the streaming session rather than interaction with the instance or its displays. Use them to share the stream or download a bug report for troubleshooting.

### Set up sharing

*Button:* ![Share Stream](/images/stream-sidebar/share-icon.png){width=30px}

*Shortcut: `Ctrl + Shift + S`*

The **Set up sharing** action creates a temporary link to share your stream with another person, allowing them to take over the session from you. Note that simultaneous access is not allowed: when someone joins the stream, the currently connected user is disconnected.

### Download bug report

*Button:* ![Bug Report](/images/stream-sidebar/bug-report-icon.png){width=30px}

*Shortcut: `Ctrl + Shift + B`*

The **Download bug report** action provides a way to {ref}`collect <sec-bug-report>` information about a problem you encounter during a streaming session. When you initiate a bug report, the system collects relevant logs and session data that you can then send to developers to help them diagnose the issue.

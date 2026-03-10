(ref-stream-page-actions)=
# Stream Page Actions

When you are streaming an application or a device, a sidebar on the right side of the stream page provides access to several controls and information panels.

![Stream Page Actions Sidebar](/images/stream-sidebar/streaming-actions-sidebar-page.png)

This sidebar contains the following actions:

## Open developer tools

![Developer Tools Toggle](/images/stream-sidebar/developer-tools-toggle-icon.png)

*Shortcut: `Ctrl + Shift + D`*

The **Developer tools** action opens a panel with various tools for developers to interact with the streaming session, including a terminal and logs for the running instance.

## Set up sharing

![Share Stream](/images/stream-sidebar/share-icon.png)

*Shortcut: `Ctrl + Shift + S`*

The **Share** action creates a temporary link to share your stream with another person, allowing them to take over the session from you. Simultaneous access is not allowed. When the other person joins the stream, you are disconnected.


## Connect ADB

![Connect ADB](/images/stream-sidebar/connect-adb-icon.png)

*Shortcut: `Ctrl + Shift + C`*

The **Connect ADB** action generates a pre-signed URL that can be used to connect to the Android Debug Bridge (ADB) for the running instance. It also provides [instructions](/howto/android/access-android-instance.md) on how to use the URL. This allows developers to interact with the Android instance using ADB commands, which is useful for debugging and testing applications.

## Set location

*Shortcut: `Ctrl + Shift + G`*

![Location Toggle](/images/stream-sidebar/location-toggle-icon.png)

The **Location** action opens a panel where you can set the geographic location (GPS coordinates) for the virtual device. This is useful for testing applications that rely on location services.

When you set a location, the virtual device behaves as if it is physically present at those coordinates.

This action might be missing from the sidebar for AAOS applications. In this case, the location toggle is in the "Controls" panel.

## Statistics

![Statistics Toggle](/images/stream-sidebar/statistics-toggle-icon.png)

*Shortcut: `Ctrl + Shift + M`*

The **Statistics** action opens a panel that displays real-time streaming statistics. This information is useful for monitoring the performance and quality of the stream and can help diagnose streaming issues.

## Full screen

![Full Screen Toggle](/images/stream-sidebar/full-screen-toggle-icon.png)

*Shortcut: `Ctrl + Shift + F`*

The **Full screen** action toggles the streaming session between full-screen and windowed mode.

## Enable/Disabled stream resize

![Stream Resize Toggle](/images/stream-sidebar/stream-resize-toggle-icon.png)

*Shortcut: `Ctrl + Shift + R`*

The **Stream resize** action allows you to toggle resize mode, which allows to resize the stream, or reset its size to fit the whole available space.

## Rotate left

![Rotate Left Toggle](/images/stream-sidebar/rotate-left-toggle-icon.png)

*Shortcut: `Ctrl + Shift + ArrowLeft`*

The **Rotate left** action rotates the stream to the left by 90 degrees.

## Rotate right

![Rotate Right Toggle](/images/stream-sidebar/rotate-right-toggle-icon.png)

*Shortcut: `Ctrl + Shift + ArrowRight`*

The **Rotate right** action rotates the stream to the right by 90 degrees.

## Volume up

![Volume Up Toggle](/images/stream-sidebar/volume-up-toggle-icon.png)

*Shortcut: `Ctrl + Shift + ArrowUp`*

The **Volume up** action increases the volume of the Android device, simulating a volume button press on a physical device.

## Volume down

![Volume Down Toggle](/images/stream-sidebar/volume-down-toggle-icon.png)

*Shortcut: `Ctrl + Shift + ArrowDown`*

The **Volume down** action decreases the volume of the Android device, simulating a volume button press on a physical device.

## Power

![Power](/images/stream-sidebar/power-toggle-icon.png)

*Shortcut: `Ctrl + Shift + P`*

The **Power** action turns the display of the Android device on or off, simulating a power button press on a physical device.

## Home

![Home Button](/images/stream-sidebar/home-icon.png)

*Shortcut: `Ctrl + Shift + H`*

The **Home** action simulates a home button press on a physical device.

## Back

![Back Button](/images/stream-sidebar/back-icon.png)

*Shortcut: `Ctrl + Shift + E`*

The **Back** action simulates a back button press on a physical device.

## Download bug report

![Bug Report](/images/stream-sidebar/bug-report-icon.png)

*Shortcut: `Ctrl + Shift + B`*

The **Bug report** action provides a way to [collect](/howto/troubleshoot/index.md#bug-report-diagnostic-facility) information about a problem you encounter during a streaming session. When you initiate a bug report, the system collects relevant logs and session data that you can then send to developers to help them diagnose the issue.

## Release / Capture keyboard

![Release Keyboard Toggle](/images/stream-sidebar/release-keyboard-toggle-icon.png)

*Shortcut: `Ctrl + Shift + K`*

The **Release / Capture keyboard** action allows you to switch the capture of keyboard events by the Android device on and off. When the capture is off, you can use your keyboard for other tasks on your computer.

## Take a screenshot

![Screenshot Toggle](/images/stream-sidebar/screenshot-toggle-icon.png)

*Shortcut: `Ctrl + Shift + I`*

The **Screenshot** action takes a screenshot of the Android device.

## Start / Stop screen recording

![Screen Record Toggle](/images/stream-sidebar/screen-record-toggle-icon.png)

*Shortcut: `Ctrl + Shift + O`*

The **Screen record** action starts recording a video of the streaming session. Clicking the button a second time stops the recording and saves the video to your local device. This is useful for creating demos, tutorials, or for troubleshooting.
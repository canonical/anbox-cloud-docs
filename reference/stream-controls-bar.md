(ref-stream-controls-bar)=
# Stream controls bar
The *Stream controls bar* appears on the right side of the *Stream* page. The controls are grouped into three sections based on whether they affect the whole instance, an individual display, or the streaming session.

![Stream multi-display instance](/images/stream-sidebar/stream-multi-display-instance.png)

## Instance and Android controls

These controls affect the instance or Android as a whole rather than a specific display. In multi-display instances, their behavior does not depend on which display is focused.

| Control | Button | Shortcut | Description |
| :---- | :---- | :---- | :---- |
| **Connect ADB** | ![Connect ADB](/images/stream-sidebar/connect-adb-icon.png){width=30px} | `Ctrl + Shift + C` | Generates a pre-signed URL that you can use to connect to the running instance with {ref}`Android Debug Bridge (ADB) <howto-access-android-instance>`. |
| **Developer tools** | ![Developer Tools Toggle](/images/stream-sidebar/developer-tools-toggle-icon.png){width=30px} | `Ctrl + Shift + D` | Opens the {ref}`developer tools panel <howto-stream-developer-tools>`, where you can access a terminal and view logs for the running instance. |
| **Set Location** | ![Location Toggle](/images/stream-sidebar/location-toggle-icon.png){width=30px} | `Ctrl + Shift + G` | Sets the {ref}`geographic location <howto-configure-geographic-location>` (GPS coordinates) of the Android device. |
| **Volume up** | ![Volume Up Toggle](/images/stream-sidebar/volume-up-toggle-icon.png){width=30px} | `Ctrl + Shift + ArrowUp` | Increases the volume, equivalent to pressing the volume-up button on an Android device. |
| **Volume down** | ![Volume Down Toggle](/images/stream-sidebar/volume-down-toggle-icon.png){width=30px} | `Ctrl + Shift + ArrowDown` | Decreases the volume, equivalent to pressing the volume-down button on an Android device. |
| **Power** | ![Power](/images/stream-sidebar/power-toggle-icon.png){width=30px} | `Ctrl + Shift + P` | Puts the Android device to sleep or wakes it, equivalent to a short press of the power button. |

## Display-specific controls

These controls affect an individual display. In a single-display stream, they apply to the only display. In a multi-display stream, supported controls apply to the focused display. You must focus a display before using them.

| Control | Button | Shortcut | Description | Multi-display behavior |
| ----- | ----- | ----- | ----- | ----- |
| **Home** | ![Home Button](/images/stream-sidebar/home-icon.png){width=30px} | `Ctrl + Shift + H` | Returns the display to the Android home screen, equivalent to pressing the Home button on an Android device. | Applies to the focused display. |
| **Back** | ![Back Button](/images/stream-sidebar/back-icon.png){width=30px} | `Ctrl + Shift + E` | Performs the Android Back action, equivalent to pressing the Back button on an Android device. | Applies to the focused display. |
| **Release / Capture keyboard** | ![Release Keyboard Toggle](/images/stream-sidebar/release-keyboard-toggle-icon.png){width=30px} | `Ctrl + Shift + K` | Controls whether keyboard input is sent to the display or handled by the browser. | When keyboard capture is enabled, keyboard input is sent to the focused display. |
| **Rotate left** | ![Rotate Left Toggle](/images/stream-sidebar/rotate-left-toggle-icon.png){width=30px} | `Ctrl + Shift + ArrowLeft` | Rotates the display 90 degrees to the left. | Not available for multi-display instances. |
| **Rotate right** | ![Rotate Right Toggle](/images/stream-sidebar/rotate-right-toggle-icon.png){width=30px} | `Ctrl + Shift + ArrowRight` | Rotates the display 90 degrees to the right. | Not available for multi-display instances. |
| **Enable / Disable stream resize** | ![Stream Resize Toggle](/images/stream-sidebar/stream-resize-toggle-icon.png){width=30px} | `Ctrl + Shift + R` | Enables stream resizing. Adjust the resize frame to the desired dimensions, then click the control again to apply the new size. The resized dimensions apply only to the current streaming session. Starting a new stream restores the default size. | Not available for multi-display instances. |
| **Full screen** | ![Full Screen Toggle](/images/stream-sidebar/full-screen-toggle-icon.png){width=30px} | `Ctrl + Shift + F` | Shows the display in full-screen mode. Press the `Esc` key on your keyboard to exit full-screen mode. | Shows the focused display in full-screen mode. |
| **Show statistics** | ![Statistics Toggle](/images/stream-sidebar/statistics-toggle-icon.png){width=30px} | `Ctrl + Shift + M` | Opens a panel with {ref}`real-time streaming statistics <howto-streaming-statistics>` for monitoring performance and troubleshooting streaming issues. | Shows statistics for the focused display. |
| **Take a screenshot** | ![Screenshot Toggle](/images/stream-sidebar/screenshot-toggle-icon.png){width=30px} | `Ctrl + Shift + I` | Captures an image of the display and downloads it to your system. | Captures the focused display. |
| **Start / Stop screen recording** | ![Screen Record Toggle](/images/stream-sidebar/screen-record-toggle-icon.png){width=30px} | `Ctrl + Shift + O` | Starts recording the display. Click the control again to stop the recording and download the video to your system. | Records the display that is focused when recording starts. Changing focus does not switch the recording to another display. |

## Session utilities

These actions support the streaming session rather than interaction with the instance or its displays. Use them to share the stream or download a bug report for troubleshooting.

| Control | Button | Shortcut | Description |
| ----- | ----- | ----- | ----- |
| **Set up sharing** | ![Share Stream](/images/stream-sidebar/share-icon.png){width=30px} | `Ctrl + Shift + S` | Creates a temporary link for another user to join the streaming session. Only one user can be connected at a time. When another user joins, the currently connected user is disconnected. |
| **Download bug report** | ![Bug Report](/images/stream-sidebar/bug-report-icon.png){width=30px} | `Ctrl + Shift + B` | Collects relevant logs and session data in a {ref}`bug report <sec-bug-report>` that you can use to troubleshoot issues related to the streaming session. |

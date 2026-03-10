# Stream Page Actions

When you are streaming an application or a device, a sidebar on the right side of the stream page provides access to several controls and information panels.

![Stream Page Actions Sidebar](/images/stream-sidebar/streaming-actions-sidebar.png)

This sidebar contains the following actions:
## Developer tools

![Developer Tools Toggle](/images/stream-sidebar/developer-tools-toggle-icon.png)

Shortcut: Ctrl + Shift + D


The **Developer tools** action opens a panel that provides various tools for developers to interact with the streaming session. These tools include the terminal and logs for the running instance.

## Share

![Share Stream](/images/stream-sidebar/share-icon.png)

The **Share** action allows you to create a temporary link to share your current streaming session with others. This is useful for collaboration or for demonstrating an application to someone who does not have an account.

## Connect ADB

![Connect ADB ](/images/stream-sidebar/connect-adb-icon.png)

The **Connect ADB** action provides [instructions](/howto/android/access-android-instance.md) to connect to the Android Debug Bridge (ADB) for the running instance. This allows developers to interact with the Android instance using ADB commands, which is useful for debugging and testing applications.


## Statistics

![Statistics Toggle](/images/stream-sidebar/statistics-toggle-icon.png)

The **Statistics** action opens a panel that displays real-time streaming statistics. This information is useful for monitoring the performance and quality of the stream.

Reviewing these statistics can help diagnose streaming issues.

## Location

![Location Toggle](/images/stream-sidebar/location-toggle-icon.png)

The **Location** action opens a panel where you can set the geographic location (GPS coordinates) for the virtual device. This is useful for testing applications that rely on location services, such as maps or navigation apps.

When you set a location, the virtual device behaves as if it is physically present at those coordinates.

**Note:** This action may be missing from the sidebar if the application you are streaming is an AAOS application. In this case, the location toggle will be present in the  "Controls" panel.

## Full screen

![Full Screen Toggle](/images/stream-sidebar/full-screen-toggle-icon.png)

The **Full screen** action allows you to toggle the streaming session between full-screen mode and windowed mode. This can enhance your viewing experience by utilizing the entire screen for the stream.

## Bug Report

![Bug Report](/images/stream-sidebar/bug-report-icon.png)

The **Bug Report** action provides a way to [capture and submit](/howto/troubleshoot/index.md#bug-report-diagnostic-facility) information about a problem you encounter during a streaming session. When you initiate a bug report, the system collects relevant logs and session data to help developers diagnose the issue.


## Release keyboard

![Release Keyboard Toggle](/images/stream-sidebar/release-keyboard-toggle-icon.png)

Shortcut: Ctrl + K


The **Release keyboard** action allows you to release the keyboard focus from the streaming session. This is useful when you want to interact with other parts of your system without closing the stream.

When you click this action, the keyboard input will no longer be directed to the streaming session, allowing you to use your keyboard for other tasks.
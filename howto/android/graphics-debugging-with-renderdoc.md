[Renderdoc](https://github.com/baldurk/renderdoc) is a graphics frame debugger which supports Android applications.

Debugging graphics can be challenging and [Renderdoc](https://github.com/baldurk/renderdoc) is a great tool to provide insight into Vulkan and OpenGL command execution. The following describes how you can use Renderdoc with Anbox Cloud.

## Install Renderdoc

Renderdoc provides binary builds [here](https://renderdoc.org/builds). These come with all prerequisites to be able to capture on Android.

For capturing Android applications you need to install the Android SDK as Renderdoc requires a few tools like [ADB](https://developer.android.com/tools/adb) or [AAPT2](https://developer.android.com/tools/aapt2). As easiest option, download and install [Android Studio](https://developer.android.com/studio) which you can then use to install the SDK.

## Configure Renderdoc

Capturing applications running in Android with Renderdoc is not much different than what is described in [the official documentation](https://renderdoc.org/docs/how/how_android_capture.html). The most important part is to configure the path to the Android SDK in the Renderdoc settings. See [here](https://renderdoc.org/docs/window/settings_window.html#android-options) for more details.

## Configure Anbox

In order to run Renderdoc with Anbox Cloud, create an instance with its ADB port exposed:

    amc launch -s adb ...

Afterwards connect to Android by running

    adb connect <host IP>:9001

The device will show up in the output of

    adb devices

You can find more information in [Access an instance](https://discourse.ubuntu.com/t/how-to-access-an-instance/17772).

Renderdoc can only inject itself into applications which have debug mode turn on. See [here](https://renderdoc.org/docs/how/how_android_capture.html#how-do-i-use-renderdoc-on-android) for more details.

## Capture a trace

Capturing a trace on Anbox Cloud is no different after the initial setup than on any other Android devices and you can follow the instructions [in the official documentation](https://renderdoc.org/docs/how/how_android_capture.html#).

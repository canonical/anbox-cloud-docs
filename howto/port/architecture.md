(howto-choose-apk-architecture)=
# How to choose APK architecture

In most cases, an Android app is not distributed as a universal APK. If the app contains native libraries, the [ABI split approach](https://developer.android.com/studio/build/configure-apk-splits) is used to produce different APK files for the different architectures. Before creating an application in AMS, you must determine which architecture to use.

There are several ways to detect for what architecture an APK's native libraries are built. Since an APK file is just a zip file, a straight-forward way to determine the available architectures is to unzip the APK file and check the sub-folders in the `libs` folder. Typically, they are:

- `armeabi-v7a`: native code compiled for ARMv7 architecture CPUs (32-bit)
- `arm64-v8a`: native code compiled for ARMv8 architecture CPUs (64-bit)
- `x86`: native code compiled for x86 architecture CPUs (32-bit)
- `x86_64`: native code compiled x86-64 architecture CPUs (64-bit)

Which APK to use to create the Anbox Cloud application depends on the architecture of your Anbox Cloud deployment:

- If the instance layer runs on 64-bit x86 hardware, use an APK that supports the `x86` or `x86_64` architecture.
- If the instance layer runs on 64-bit Arm hardware, use an APK that supports the `armeabi-v7a` or `arm64-v8a` architecture.

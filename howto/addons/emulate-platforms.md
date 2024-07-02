(howto-emulate-platforms-example)=
# Example: Emulate platforms

To provide support for platforms that are not natively supported by your application (for example, you want to run an x86_64 application on Arm), use a hook.

Create a hook that installs the software for binary translation and add the top-level key `provides` to your addon manifest. List the architectures that the addon supports, in the value for the `provides` key.

```yaml
name: my-addon
description: provides support for x86_64 architecture
provides:
  abi-support:
    - arm64-v8a
    - armeabi-v7a
```

This manifest instructs the Anbox Management Service(AMS) that an application can be scheduled on `arm64-v8a` and `armeabi-v7a` systems even if no native support is detected in the APK.

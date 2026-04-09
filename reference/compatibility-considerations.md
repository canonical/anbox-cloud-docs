(ref-compatibility-considerations)=
# Compatibility Considerations

Anbox Cloud runs Android inside [LXC](https://linuxcontainers.org/lxc/introduction/) containers to deliver a complete AOSP experience (see {ref}`ref-android-features`). While this approach provides efficient, scalable Android instances, the containerized environment imposes certain constraints that can affect application compatibility.

## Application and game compatibility

Running Android inside an LXC container means that some OS-level security and isolation features are unavailable or configured differently from a physical device. Some applications, particularly games, include integrity checks or anti-cheat mechanisms that probe the runtime environment, and these checks may fail as a result.

The following constraints are known to cause compatibility issues:

- **SELinux is disabled:** SELinux is not enforced inside the Android container. Anbox Cloud relies on AppArmor (via LXD) for security, with no native support for SELinux. Applications that check whether SELinux is enforcing will detect this and may refuse to run.

- **Emulator environment detection:** Applications may inspect system properties or hardware identifiers to detect whether they are running inside an emulator or a virtualized environment. Because Anbox Cloud shares characteristics with such environments, these checks may trigger a false positive.

- **Container environment detection:** Missing hardware nodes or other artifacts of the container environment may be visible to applications. Applications that scan for signs of a container or rooted environment may detect these and refuse to run.

Applications that rely on any of these checks may not work as expected in Anbox Cloud. This is an architectural characteristic of container virtualization and should be taken into account during the application design and testing phase.

## Dependency on vendor services

Some applications depend on vendor provided services that are not part of AOSP and are not included in Anbox Cloud:

- **Google Play Services(GMS):** Some applications, including those that use Google Maps, or Google Sign-In require Google Mobile Services to be present. Anbox Cloud does not ship with GMS, and applications with a hard dependency on it will not function unless GMS is separately installed under your own licensing agreement.

- **Other vendor services:** Applications that depend on equivalent services from other vendors mobile services, are similarly affected if those services are not present in the Android instance.

## Unsupported Android features

Applications relying on unsupported Android features may not work correctly or may fail to launch, such as Bluetooth or NFC. For a complete list of supported and unsupported features, see {ref}`ref-android-features`.

## Recommendations

If you encounter application compatibility issues caused by these factors:

- Check the application's documentation or support channels to understand its integrity requirements.
- Where possible, request a build of the application that is intended for cloud or virtualized environments.
- Review the {ref}`ref-android-features` page to confirm whether a specific Android feature the application depends on is supported.

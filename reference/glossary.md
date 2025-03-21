(ref-glossary)=
# Glossary

```{glossary}

Addons
    A piece of code that can be used to extend and customize images in Anbox Cloud.

    See {ref}`ref-addon-manifest` for more information.

Amazon Web Services (AWS)
    A cloud platform provided by Amazon that can be used to host Anbox Cloud.

    See [the AWS website](https://aws.amazon.com/) for more information.

AMS Node Controller
    A service that runs on every LXD node and puts the appropriate firewall rules in place when an instance is started or stopped.

AMS SDK
    An SDK that provides Go language bindings for connecting to AMS through the exposed REST API.

    See {ref}`sec-ams-sdk` for more information.

Anbox
    A component of Anbox Cloud that facilitates booting an Android system on a regular GNU/Linux system. The concepts of the Anbox component in Anbox Cloud are similar to the [Anbox open source project](https://github.com/anbox/anbox), but the Anbox open source project is an independent project that is not related to or used in Anbox Cloud.

Anbox Application Manager (AAM)
    A utility (`aam`) that is installed in the Anbox image and that can be used for various tasks, for example, to back up and restore Android application data.

    See {ref}`howto-backup-restore-application-data` for more information.

Anbox Application Registry (AAR)
    A central repository for applications created in Anbox Cloud. Using an AAR is very useful for larger deployments to keep applications in sync.

    See {ref}`exp-aar` for more information.

Anbox Cloud
    A rich software stack that enables you to run Android applications in the cloud for all kinds of different use cases, including high-performance streaming of graphics to desktop and mobile client devices.

    See {ref}`exp-anbox-cloud` for more information.

Anbox Cloud Appliance
    A self-contained deployment variant of Anbox Cloud.

    See {ref}`sec-variants` for more information.

Anbox Cloud cluster
    A deployment of the Anbox Cloud, either just the core stack or the core stack along with the streaming stack.

Anbox Cloud subcluster
    The group of components that is made up of LXD, AMS node controller, and the {term}`Control node` hosting the AMS, AMC, and etcd.

Anbox Management Client (AMC)
    The command line interface that is used to manage the Anbox Management Service (AMS).

Anbox Management Service (AMS)
    The service that handles all aspects of the application and instance life cycle in Anbox Cloud. AMS is responsible for managing instances, applications, addons, updates and more, ensuring high density, performance and fast startup times for the instances.
    AMS uses [etcd](https://etcd.io/) as database. It connects to LXD over its REST API.

    See {ref}`exp-ams` for more information.

Anbox Platform SDK
    A C/C++ SDK that provides support for developing custom platform plugins, which allows users to integrate Anbox with their existing infrastructure.

    See {ref}`sec-platform-sdk` for more information.

Anbox shell
    A command-line tool (`anbox-shell`) that provides an ADB shell with root permissions granted, which you can use to access the Android system in the instance.

    See {ref}`howto-access-android-instance` for more information.

Anbox Streaming SDK
    An SDK that allows the development of custom streaming clients, using JavaScript.

    See {ref}`sec-streaming-sdk` for more information.

Android app
    An application for the Android mobile operating system, usually provided as APK. To distinguish Android apps from Anbox Cloud applications, this documentation refers to Android apps as *apps*, not *applications*.

Android Archive (AAR)
    A compiled version of an Android library that can be used as a dependency for an Android app module.

    See [Create an Android library](https://developer.android.com/studio/projects/android-library) in the Android developer documentation.

Android Debug Bridge (ADB)
    A command-line tool that is included in the Android SDK Platform-Tools package and that allows to connect to and communicate with an Android device from your computer.

    See [Android Debug Bridge (ADB)](https://developer.android.com/studio/command-line/adb) in the Android developer documentation.

Android Package Kit (APK)
    The file format used to package apps for the Android operating system.

Appium
    An open-source test automation tool that can be used to test native, mobile and hybrid web applications on Android.

    See [the Appium website](http://appium.io/) for more information.

Application
    One of the main objects of Anbox Cloud. An application encapsulates an Android app and manages it within the Anbox Cloud cluster.

    See {ref}`exp-applications` for more information.

Application instance
    An instance that is created when launching an application.

    See {ref}`sec-application-raw-instances` for more information.

Application manifest
    A file that defines the attributes of an Anbox Cloud application.

    See {ref}`ref-application-manifest` for more information.

Base instance
    A temporary instance that is used when bootstrapping an application. It is automatically deleted when the application bootstrap is completed.

    See {ref}`sec-regular-base-instances` for more information.

Boot package
    The package to launch in an application instance once the system has booted.

Bootstrap process
    The process that builds the application and optimizes it to run on Anbox Cloud.

    See {ref}`sec-application-bootstrap` for more information.

Control node
    The machine on which the components that make up the management layer, AMS, AMC, and etcd, are installed.

Core stack
    The core parts of the Anbox Cloud stack that are required for all deployments. As a bare minimum, an Anbox Cloud deployment requires the following services:

    - AMS
    - etcd
    - At least 1 LXD worker
    - 1 AMS Node Controller per LXD worker
    - Easy-RSA

    See {ref}`exp-anbox-cloud` for more information.

Coturn
    An open-source implementation of a STUN/TURN server needed for WebRTC to work behind NATs and firewalls.

    See [the Coturn project on GitHub](https://github.com/coturn/coturn) for more information.

Graphics Processing Unit (GPU)
    A specialized processor that is designed to accelerate image processing and graphics rendering for output to a display device.

High availability (HA)
    The characteristic of a system to continuously be available without failing for a higher-than-normal period of time. Anbox Cloud ensures high availability by keeping replicas of every service, which avoids having a single point of failure.

    See {ref}`howto-enable-ha` for more information.

Hook
    Code that is invoked at different points in time in the life cycle of an instance. Hooks are part of addons or applications.

    See {ref}`ref-hooks` for more information.

Image
    The base for an instance, which contains all necessary components like Anbox or the Android root file system. Anbox Cloud provides images based on different Android and Ubuntu versions and different architectures.

    The images can be an Anbox Cloud AOSP image which is based on the Android Open Source Project (AOSP), an operating system typically used in mobile devices or an Anbox Cloud AAOS image which is based on the Android Automotive OS (AAOS), an infotainment platform used in automobiles.

    See {ref}`howto-manage-images` and {ref}`ref-provided-images` for more information.

Instance
    An instance is a container or a virtual machine used to launch an application or an image. Every time you launch an application or an image, Anbox Cloud creates an instance for it. Every instance provides a full Android system.

    See {ref}`exp-instances` for more information.

Instance type
    An abstraction for a set of resources that is available to an instance.

    See {ref}`sec-application-manifest-instance-type` for more information.

    ```{note}
    The `instance-type` attribute in the application manifest will be deprecated effective version 1.20 and will be removed in future releases. After the `instance-type` attribute becomes unsupported, this term will be replaced with the term *Resource preset*.
    ```

Juju
    A charmed operator framework that helps you deploy, integrate and manage applications across multiple environments. Anbox Cloud is installed using Juju. The Anbox Cloud Appliance uses Juju under the hood.

    See [the Juju website](https://juju.is/) for more information.

LXD
    A system container and virtual machine manager that offers a unified user experience around full Linux systems running inside containers or virtual machines. Anbox Cloud is based on LXD.

    See [the LXD website](https://ubuntu.com/lxd) for more information.

LXD cluster
    A set of LXD nodes that share the same distributed database that holds the configuration for the cluster members and their instances.

LXD worker node
    In a clustering setup for a charmed Anbox Cloud deployment, all nodes other than the {term}`Control node` are worker nodes. If you have a streaming stack, all nodes other than the control node and the two nodes that are dedicated to host the streaming services are worker nodes. Each worker node runs LXD in clustering mode, and this LXD cluster is used to host the Android containers.

Neural Autonomic Transport System (NATS)
    An open-source messaging system that the components of the streaming stack use to communicate.

    See [the NATS website](https://nats.io/) for more information.

Platform
    An abstraction layer that is provided by Anbox to access the hardware resources of the host system from the Android system. Anbox Cloud supports three platforms: `null` (without rendering), `webrtc` (WebRTC) and `swrast` (software rendering).

    See {ref}`exp-platforms` for more information.

Prometheus
    An open-source application used for event monitoring and alerting, which records real-time metrics about system events.

    See [the Prometheus website](https://prometheus.io/) for more information.

Raw instance
    An instance that is created when launching an image. It runs the full Android system, without any additional apps installed.

    See {ref}`sec-application-raw-instances` for more information.

Regular instance
    An instance that is launched from either an application or an image. It exists until it is deleted.

    See {ref}`sec-regular-base-instances` for more information.

Scrcpy
    An open-source screen mirroring application that allows displaying and controlling Android devices from a desktop computer.

    See [the scrcpy project on GitHub](https://github.com/Genymobile/scrcpy) for more information.

Session
    The interaction between a streaming client and the application instance during streaming. A session contains, among other information, user data and application information and provides an entry point for both the client and the instance to start the signaling process.

    See {ref}`exp-application-streaming` for more information.

Snap
    A software package for a desktop, cloud or IoT application that is easy to install, secure, cross‐platform and dependency‐free.

    See [the Snapcraft website](https://snapcraft.io/) for more information.

Software Rasterization (`swrast`)
    An LLVMpipe-based software rendering platform that is useful for visual tests but does not provide audio input/output.

    See {ref}`exp-platforms` for more information.

Stream agent
    The software running on a server connected to Anbox Cloud, which connects AMS to the stream gateway and allows distribution from the gateway to multiple independent AMS installations.

    See {ref}`exp-application-streaming` for more information.

Stream gateway
    The central component that connects clients with stream agents. Its role is to choose the best possible region depending on the user location and server capacities.

    See {ref}`exp-application-streaming` for more information.

Streaming stack
    A collection of components designed to run containers or virtual machines and stream their visual output to clients via WebRTC. Streaming can happen through GPUs or through software rendering.

    See {ref}`exp-application-streaming` for more information.

STUN/TURN server
    A server that finds the most optimal network path between a client and the instance running its application.

Ubuntu Pro
    Canonical’s service package for Ubuntu that provides enterprise security and support for open-source applications, with managed service offerings available. Note the difference between Ubuntu Pro (Infra-only) and Ubuntu Pro subscriptions. Anbox Cloud requires an Ubuntu Pro subscription.

    See [Ubuntu Pro](https://ubuntu.com/support) for more information.

Ubuntu One
    A central user account system used by all Canonical sites and services. You need an Ubuntu One account to purchase the Ubuntu Pro subscription that is required to run Anbox Cloud, and to log in to the web dashboard.

    See [Ubuntu One](https://login.ubuntu.com/) for more information.

Watchdog
    A software component that monitors the app in an instance and terminates the instance if the app crashes or is moved to the background.

    See {ref}`sec-application-manifest-watchdog` for more information.

Web dashboard
    A web GUI for Anbox Cloud from where developers can create, manage and stream applications from their web browser.

    See {ref}`exp-web-dashboard` for more information.

WebRTC
    A standard for media capture devices and peer-to-peer connectivity that can be used to add real-time communication capabilities to an application. It supports video, voice, and generic data to be sent between peers.

    See [the WebRTC website](https://webrtc.org/) for more information.
```

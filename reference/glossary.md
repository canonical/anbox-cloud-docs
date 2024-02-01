[Details="Alphabetical list of terms"]
- [AAM](#aam)
- [AAR (Anbox Application Registry)](#aar)
- [AAR (Android Archive)](#android-archive)
- [ADB](#adb)
- [AMC](#amc)
- [AMS](#ams)
- [AMS Node Controller](#ams-node-controller)
- [AMS SDK](#ams-sdk)
- [APK](#apk)
- [AWS](#aws)
- [Addon](#addon)
- [Amazon Web Services](#aws)
- [Anbox](#anbox)
- [Anbox Application Manager](#aam)
- [Anbox Application Registry](#aar)
- [Anbox Cloud](#anbox-cloud)
- [Anbox Cloud Appliance](#anbox-cloud-appliance)
- [Anbox Cloud cluster](#anbox-cloud-cluster)
- [Anbox Cloud subcluster](#anbox-cloud-subcluster)
- [Anbox Management Client](#amc)
- [Anbox Management Service](#ams)
- [Anbox Platform SDK](#anbox-platform-sdk)
- [Anbox shell](#anbox-shell)
- [Anbox Streaming SDK](#anbox-streaming-sdk)
- [Android app](#android-app)
- [Android Archive](#android-archive)
- [Android Debug Bridge](#adb)
- [Android Package Kit](#apk)
- [Appium](#appium)
- [Application](#application)
- [Application instance](#application-instance)
- [Application manifest](#application-manifest)
- [Base instance](#base-instance)
- [Boot package](#boot-package)
- [Bootstrap process](#bootstrap-process)
- [Control node](#control-node)
- [Core stack](#core-stack)
- [Coturn](#coturn)
- [GPU](#gpu)
- [Graphics Processing Unit](#gpu)
- [HA](#ha)
- [High availability](#ha)
- [Hook](#hook)
- [Image](#image)
- [Instance](#instance)
- [Instance type](#instance-type)
- [Juju](#juju)
- [LXD](#lxd)
- [LXD cluster](#lxd-cluster)
- [LXD worker node](#lxd-worker-node)
- [Manifest](#application-manifest)
- [NATS](#nats)
- [Neural Autonomic Transport System](#nats)
- [Node controller](#ams-node-controller)
- [NRPE](#nrpe)
- [Platform](#platform)
- [Prometheus](#prometheus)
- [Raw instance](#raw-instance)
- [Regular instance](#regular-instance)
- [STUN/TURN server](#stun/turn-server)
- [Scrcpy](#scrcpy)
- [Session](#session)
- [Snap](#snap)
- [Software Rasterization](#swrast)
- [Stream agent](#stream-agent)
- [Stream gateway](#stream-gateway)
- [Streaming stack](#streaming-stack)
- [`swrast`](#swrast)
- [Ubuntu Pro](#ubuntu-pro)
- [Ubuntu One](#ubuntu-one)
- [Watchdog](#watchdog)
- [Web dashboard](#web-dashboard)
- [WebRTC](#webrtc)

[/Details]

## Definitions

<a name="addon"></a>
### Addon

A piece of code that can be used to extend and customise images in Anbox Cloud.

See https://discourse.ubuntu.com/t/addons/25293.

<a name="aws"></a>
### Amazon Web Services (AWS)

A cloud platform provided by Amazon that can be used to host Anbox Cloud.

See [the AWS website](https://aws.amazon.com/).

<a name="ams-node-controller"></a>
### AMS Node Controller

A service that runs on every LXD node and puts the appropriate firewall rules in place when an instance is started or stopped.

<a name="ams-sdk"></a>
### AMS SDK

An SDK that provides Go language bindings for connecting to AMS through the exposed REST API.

See [AMS SDK](https://discourse.ubuntu.com/t/anbox-cloud-sdks/17844#ams-sdk-4).

<a name="anbox"></a>
### Anbox

A component of Anbox Cloud that facilitates booting an Android system on a regular GNU/Linux system. The concepts of the Anbox component in Anbox Cloud are similar to the [Anbox open source project](https://github.com/anbox/anbox), but the Anbox open source project is an independent project that is not related to or used in Anbox Cloud.

<a name="aam"></a>
### Anbox Application Manager (AAM)

A utility (`aam`) that is installed in the Anbox image and that can be used for various tasks, for example, to back up and restore Android application data.

See https://discourse.ubuntu.com/t/back-up-and-restore-application-data/24183.

<a name="aar"></a>
### Anbox Application Registry (AAR)

A central repository for applications created in Anbox Cloud. Using an AAR is very useful for larger deployments to keep applications in sync.

See https://discourse.ubuntu.com/t/anbox-application-registry-aar/17761.

<a name="anbox-cloud"></a>
### Anbox Cloud

A rich software stack that enables you to run Android applications in the cloud for all kinds of different use cases, including high-performance streaming of graphics to desktop and mobile client devices.

See https://discourse.ubuntu.com/t/about-anbox-cloud/17802.

<a name="anbox-cloud-appliance"></a>
### Anbox Cloud Appliance

A self-contained deployment variant of Anbox Cloud.

See [Variants](https://discourse.ubuntu.com/t/anbox-cloud/17802#variants-1).

<a name="anbox-cloud-cluster"></a>
### Anbox Cloud cluster

A deployment of the Anbox Cloud, either just the core stack or the core stack along with the streaming stack.

<a name="anbox-cloud-subcluster"></a>
### Anbox Cloud subcluster

The group of components that is made up of LXD, AMS node controller, and the [control node](#control-node) hosting the AMS, AMC, and etcd.

<a name="amc"></a>
### Anbox Management Client (AMC)

The command line interface that is used to manage the Anbox Management Service (AMS).

<a name="ams"></a>
### Anbox Management Service (AMS)

The service that handles all aspects of the application and instance life cycle in Anbox Cloud. AMS is responsible for managing instances, applications, addons, updates and more, ensuring high density, performance and fast startup times for the instances.

AMS uses [etcd](https://etcd.io/) as database. It connects to LXD over its REST API.

See https://discourse.ubuntu.com/t/anbox-management-service-ams/24321.

<a name="anbox-platform-sdk"></a>
### Anbox Platform SDK

A C/C++ SDK that provides support for developing custom platform plugins, which allows users to integrate Anbox with their existing infrastructure.

See [Anbox Platform SDK](https://discourse.ubuntu.com/t/anbox-cloud-sdks/17844#anbox-platform-sdk).

<a name="anbox-shell"></a>
### Anbox shell

A command-line tool (`anbox-shell`) that provides an ADB shell with root permissions granted, which you can use to access the Android system in the instance.

See [Access an instance with AMC](https://discourse.ubuntu.com/t/17772#access-an-instance-with-amc-1).

<a name="anbox-streaming-sdk"></a>
### Anbox Streaming SDK

An SDK that allows the development of custom streaming clients, using JavaScript.

See [Anbox Streaming SDK](https://discourse.ubuntu.com/t/anbox-cloud-sdks/17844#anbox-cloud-streaming-sdk-8).

<a name="android-app"></a>
### Android app

An application for the Android mobile operating system, usually provided as APK. To distinguish Android apps from Anbox Cloud applications, this documentation refers to Android apps as "apps", not "applications".

<a name="android-archive"></a>
### Android Archive (AAR)

A compiled version of an Android library that can be used as a dependency for an Android app module.

See [Create an Android library](https://developer.android.com/studio/projects/android-library) in the Android developer documentation.

<a name="adb"></a>
### Android Debug Bridge (ADB)

A command-line tool that is included in the Android SDK Platform-Tools package and that allows to connect to and communicate with an Android device from your computer.

See [Android Debug Bridge (ADB)](https://developer.android.com/studio/command-line/adb) in the Android developer documentation.

<a name="apk"></a>
### Android Package Kit (APK)

The file format used to package apps for the Android operating system.

<a name="appium"></a>
### Appium

An open-source test automation tool that can be used to test native, mobile and hybrid web applications on Android.

See [the Appium website](http://appium.io/).

<a name="application"></a>
### Application

One of the main objects of Anbox Cloud. An application encapsulates an Android app and manages it within the Anbox Cloud cluster.

See https://discourse.ubuntu.com/t/about-applications/17760.

<a name="application-instance"></a>
### Application instance

An instance that is created when launching an application.

See [Application instances vs. raw instances](https://discourse.ubuntu.com/t/17763#application-vs-raw).

<a name="application-manifest"></a>
### Application manifest

A file that defines the attributes of an Anbox Cloud application.

See https://discourse.ubuntu.com/t/application-manifest/24197.

<a name="base-instance"></a>
### Base instance

A temporary instance that is used when bootstrapping an application. It is automatically deleted when the application bootstrap is completed.

See https://discourse.ubuntu.com/t/17763#regular-vs-base.

<a name="boot-package"></a>
### Boot package

The package to launch in an application instance once the system has booted.

<a name="bootstrap-process"></a>
### Bootstrap process

The process that builds the application and optimises it to run on Anbox Cloud.

See [Bootstrap process](https://discourse.ubuntu.com/t/about-applications/17760#bootstrap-process-2).

<a name="control-node"></a>
### Control node

The machine on which the components that make up the management layer, AMS, AMC, and etcd, are installed.

<a name="core-stack"></a>
### Core stack

The core parts of the Anbox Cloud stack that are required for all deployments. As a bare minimum, an Anbox Cloud deployment requires the following services:

- AMS
- etcd
- At least 1 LXD worker
- 1 AMS Node Controller per LXD worker
- Easy-RSA

See https://discourse.ubuntu.com/t/about-anbox-cloud/17802.

<a name="coturn"></a>
### Coturn

An open-source implementation of a STUN/TURN server needed for WebRTC to work behind NATs and firewalls.

See [the Coturn project on GitHub](https://github.com/coturn/coturn).

<a name="gpu"></a>
### Graphics Processing Unit (GPU)

A specialised processor that is designed to accelerate image processing and graphics rendering for output to a display device.

<a name="ha"></a>
### High availability (HA)

The characteristic of a system to continuously be available without failing for a higher-than-normal period of time. Anbox Cloud ensures high availability by keeping replicas of every service, which avoids having a single point of failure.

See [Enable high availability](https://discourse.ubuntu.com/t/enable-high-availability/17754).

<a name="hook"></a>
### Hook

Code that is invoked at different points in time in the life cycle of an instance. Hooks are part of addons or applications.

See [Hooks](https://discourse.ubuntu.com/t/hooks/28555).

<a name="image"></a>
### Image

The base for an instance, which contains all necessary components like Anbox or the Android root file system. Anbox Cloud provides images based on different Android and Ubuntu versions and different architectures.

The images can be an Anbox Cloud AOSP image which is based on the Android Open Source Project (AOSP), an operating system typically used in mobile devices or an Anbox Cloud AAOS image which is based on the Android Automotive OS (AAOS), an infotainment platform used in automobiles.

See [Manage images](https://discourse.ubuntu.com/t/manage-images/17758) and [Provided images](https://discourse.ubuntu.com/t/provided-images/24185).

<a name="instance"></a>
### Instance

An instance is a container or a virtual machine used to launch an application or an image. Every time you launch an application or an image, Anbox Cloud creates an instance for it. Every instance provides a full Android system.

See https://discourse.ubuntu.com/t/17763.

<a name="instance-type"></a>
### Instance type

An abstraction for a set of resources that is available to an instance.

See https://discourse.ubuntu.com/t/application-manifest/24197#instance-type-1.

[note type="information" status="Note"] The `instance-type` attribute in the application manifest will be deprecated effective version 1.20 and will be removed in future releases. After the `instance-type` attribute becomes unsupported, this term will be replaced with the term *Resource preset*.[/note]

<a name="juju"></a>
### Juju

A charmed operator framework that helps you deploy, integrate and manage applications across multiple environments. Anbox Cloud is installed using Juju. The Anbox Cloud Appliance uses Juju under the hood.

See [the Juju website](https://juju.is/).

<a name="lxd"></a>
### LXD

A system container and virtual machine manager that offers a unified user experience around full Linux systems running inside containers or virtual machines. Anbox Cloud is based on LXD.

See [the LXD website](https://ubuntu.com/lxd).

<a name="lxd-cluster"></a>
### LXD cluster

A set of LXD nodes that share the same distributed database that holds the configuration for the cluster members and their instances.

<a name="lxd-worker-node"></a>
### LXD worker node

In a clustering setup for a full Anbox Cloud deployment, all nodes other than the [control node](#control-node) are worker nodes. If you have a streaming stack, all nodes other than the [control node](#control-node) and the two nodes that are dedicated to host the streaming services are worker nodes. Each worker node runs LXD in clustering mode, and this LXD cluster is used to host the Android containers.

<a name="nats"></a>
### Neural Autonomic Transport System (NATS)

An open-source messaging system that the components of the streaming stack use to communicate.

See [the NATS website](https://nats.io/).

<a name="platform"></a>
### Platform

An abstraction layer that is provided by Anbox to access the hardware resources of the host system from the Android system. Anbox Cloud supports three platforms: `null` (without rendering), `webrtc` (WebRTC) and `swrast` (software rendering).

See https://discourse.ubuntu.com/t/anbox-platforms/18733.

<a name="prometheus"></a>
### Prometheus

An open-source application used for event monitoring and alerting, which records real-time metrics about system events.

See [the Prometheus website](https://prometheus.io/).

<a name="raw-instance"></a>
### Raw instance

An instance that is created when launching an image. It runs the full Android system, without any additional apps installed.

See [Application instances vs. raw instances](https://discourse.ubuntu.com/t/17763#application-vs-raw).

<a name="regular-instance"></a>
### Regular instance

An instance that is launched from either an application or an image. It exists until it is deleted.

See [Regular instances vs. base instances](https://discourse.ubuntu.com/t/17763#regular-vs-base).

<a name="scrcpy"></a>
### Scrcpy

An open-source screen mirroring application that allows displaying and controlling Android devices from a desktop computer.

See [the scrcpy project on GitHub](https://github.com/Genymobile/scrcpy).

<a name="session"></a>
### Session

The interaction between a streaming client and the application instance during streaming. A session contains, among other information, user data and application information and provides an entry point for both the client and the instance to start the signalling process.

See https://discourse.ubuntu.com/t/about-application-streaming/17769.

<a name="snap"></a>
### Snap

A software package for a desktop, cloud or IoT application that is easy to install, secure, cross‐platform and dependency‐free.

See [the Snapcraft website](https://snapcraft.io/).

<a name="swrast"></a>
### Software Rasterization (`swrast`)

An LLVMpipe-based software rendering platform that is useful for visual tests but does not provide audio input/output.

See https://discourse.ubuntu.com/t/anbox-platforms/18733.

<a name="stream-agent"></a>
### Stream agent

The software running on a server connected to Anbox Cloud, which connects AMS to the stream gateway and allows distribution from the gateway to multiple independent AMS installations.

See https://discourse.ubuntu.com/t/about-application-streaming/17769.

<a name="stream-gateway"></a>
### Stream gateway

The central component that connects clients with stream agents. Its role is to choose the best possible region depending on the user location and server capacities.

See https://discourse.ubuntu.com/t/about-application-streaming/17769.

<a name="streaming-stack"></a>
### Streaming stack

A collection of components designed to run containers or virtual machines and stream their visual output to clients via WebRTC. Streaming can happen through GPUs or through software rendering.

See https://discourse.ubuntu.com/t/about-application-streaming/17769.

<a name="stun/turn-server"></a>
### STUN/TURN server

A server that finds the most optimal network path between a client and the instance running its application.

<a name="ubuntu-pro"></a>
### Ubuntu Pro

Canonical’s service package for Ubuntu that provides enterprise security and support for open-source applications, with managed service offerings available. Note the difference between Ubuntu Pro (Infra-only) and Ubuntu Pro subscriptions. Anbox Cloud requires an Ubuntu Pro subscription.

See [Ubuntu Pro](https://ubuntu.com/support).

<a name="ubuntu-one"></a>
### Ubuntu One

A central user account system used by all Canonical sites and services. You need an Ubuntu One account to purchase the Ubuntu Pro subscription that is required to run Anbox Cloud, and to log in to the web dashboard.

See [Ubuntu One](https://login.ubuntu.com/).

<a name="watchdog"></a>
### Watchdog

A software component that monitors the app in an instance and terminates the instance if the app crashes or is moved to the background.

See [Watchdog settings](https://discourse.ubuntu.com/t/application-manifest/24197#watchdog-5).

<a name="web-dashboard"></a>
### Web dashboard

A web GUI for Anbox Cloud from where developers can create, manage and stream applications from their web browser.

See https://discourse.ubuntu.com/t/use-the-web-dashboard/20871.

<a name="webrtc"></a>
### WebRTC

A standard for media capture devices and peer-to-peer connectivity that can be used to add real-time communication capabilities to an application. It supports video, voice, and generic data to be sent between peers.

See [the WebRTC website](https://webrtc.org/).

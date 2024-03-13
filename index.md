Anbox Cloud enables running Android apps on any cloud platform at scale. It uses system containers or virtual machines to run the nested Android containers and [Juju](https://juju.is/) for deployment in a cloud environment.

Anbox Cloud supports x86 and Arm64 hardware, providing the same set of features for both architectures.

Since Anbox Cloud uses system containers or virtual machines to emulate Android systems, you can achieve the isolation and security level of a virtual machine without the associated overhead. Therefore, compared to other Android emulation solutions, Anbox Cloud can provide at least twice the density and can serve up to 100 Android instances per server.

Due to its highly scalable nature and performance optimisation, delivering device-agnostic mobile applications is very easy. Popular use cases of Anbox Cloud include mobile game streaming services, corporate application streaming, application automation and testing.

## In this documentation

| | |
|--|--|
|  [Tutorials](https://discourse.ubuntu.com/t/tutorials/28826)</br>  Get started - a hands-on introduction to Anbox Cloud for new users </br> |  [How-to guides](https://discourse.ubuntu.com/t/how-to-guides/28827) </br> Step-by-step guides covering key operations and common tasks |
|  [Explanation](https://discourse.ubuntu.com/t/explanation/28829) </br> Concepts - discussion and clarification of key topics, architecture  | [Reference](https://discourse.ubuntu.com/t/reference/28828) </br> Technical information - specifications, APIs |

## Project and community

Anbox Cloud is a Canonical product. It originally grew out of the [Anbox open-source project](https://github.com/anbox), but its code base is now completely independent.

- [Get support through Ubuntu Pro](https://ubuntu.com/support)
- Forums:
    - [Ask questions about Anbox Cloud](https://discourse.ubuntu.com/c/anbox-cloud/users/148)
    - [Contribute to Anbox Cloud documentation](https://discourse.ubuntu.com/c/anbox-cloud/documentation/50)
    - [Give feedback on Anbox Cloud documentation](https://forms.gle/6yzgLbwN8rVYSdvG9)
    - [Follow Anbox Cloud release announcements](https://discourse.ubuntu.com/c/anbox-cloud/announcements/55)
- [Release roadmap](https://discourse.ubuntu.com/t/release-roadmap/19359)
- [Release notes](https://discourse.ubuntu.com/t/release-notes/17842)
- [Troubleshoot](https://discourse.ubuntu.com/t/how-to-troubleshoot-anbox-cloud/17837) and [report](https://bugs.launchpad.net/anbox-cloud/+bugs) issues with Anbox Cloud

Thinking about using Anbox Cloud for your next project? [Get in touch!](https://anbox-cloud.io/contact-us)

## Navigation

[details=Navigation]
| Level | Path | Navlink |
| -- | -- | -- |
| 0 | / | [Anbox Cloud documentation](https://discourse.ubuntu.com/t/anbox-cloud-documentation/17029) |
| 0 | | |
| 1 | tutorial/landing | [Tutorials](https://discourse.ubuntu.com/t/tutorials/28826) |
| 2 | tutorial/installing-appliance | [1. Install the appliance](https://discourse.ubuntu.com/t/install-appliance/22681) |
| 2 | tutorial/getting-started-dashboard | [2. Get started using the web dashboard](https://discourse.ubuntu.com/t/getting-started-with-anbox-cloud-web-dashboard/24958)|
| 2 | tutorial/getting-started | [3. Get started using the CLI](https://discourse.ubuntu.com/t/getting-started/17756)|
| 2 | tutorial/stream-client | [4. Set up a stream client (Optional)](https://discourse.ubuntu.com/t/set-up-a-stream-client/37328) |
| 2 | tutorial/creating-addon | [5. Create an addon (Optional)](https://discourse.ubuntu.com/t/creating-an-addon/25284)|
| 0 | | |
| 1 | howto/landing | [How-to guides](https://discourse.ubuntu.com/t/how-to-guides/28827) |
| 2 | howto/install-appliance/landing | [Install the appliance](https://discourse.ubuntu.com/t/how-to-install-the-anbox-cloud-appliance/29702) |
| 3 | howto/install-appliance/aws | [Install on AWS](https://discourse.ubuntu.com/t/how-to-install-the-appliance-on-aws/29703) |
| 3 | howto/install-appliance/azure | [Install on Azure](https://discourse.ubuntu.com/t/how-to-install-the-appliance-on-azure/30824) |
| 3 | howto/install-appliance/google-cloud | [Install on Google Cloud](https://discourse.ubuntu.com/t/36254) |
| 2 | howto/install/landing | [Install Anbox Cloud](https://discourse.ubuntu.com/t/install-anbox-cloud/24336)|
| 3 | howto/install/deploy-juju | [Deploy with Juju](https://discourse.ubuntu.com/t/install-with-juju/17744) |
| 3 | howto/install/deploy-bare-metal | [Deploy on bare metal](https://discourse.ubuntu.com/t/deploy-anbox-cloud-on-bare-metal/26378) |
| 3 | howto/install/customise | [Customise the installation](https://discourse.ubuntu.com/t/installation-customizing/17747)|
| 3 | howto/install/high-availability | [Enable High Availability](https://discourse.ubuntu.com/t/high-availability/17754)|
| 3 | howto/install/validate | [Validate the deployment](https://discourse.ubuntu.com/t/validation/20329)|
| 2 | howto/update/landing | [Update an installation](https://discourse.ubuntu.com/t/update-your-installation/24331)|
| 3 | howto/update/control | [Control updates](https://discourse.ubuntu.com/t/control-updates/24959)|
| 3 | howto/update/upgrade-appliance | [Upgrade the appliance](https://discourse.ubuntu.com/t/upgrade-anbox-cloud-appliance/24186)|
| 3 | howto/update/upgrade-anbox | [Upgrade Anbox Cloud](https://discourse.ubuntu.com/t/upgrading-from-previous-versions/17750)|
| 2 | howto/manage/landing| [Manage Anbox Cloud](https://discourse.ubuntu.com/t/manage-anbox-cloud/24337) |
| 3 | howto/manage/tls-for-appliance | [Set up TLS for appliance](https://discourse.ubuntu.com/t/set-up-tls-for-the-anbox-cloud-appliance/28552) |
| 3 | howto/manage/images | [Manage Anbox Cloud images](https://discourse.ubuntu.com/t/managing-images/17758)|
| 3 | howto/manage/ams-access | [Control AMS remotely](https://discourse.ubuntu.com/t/managing-ams-access/17774)|
| 3 | howto/manage/benchmarks | [Run benchmarks](https://discourse.ubuntu.com/t/benchmarking-a-deployment/17770)|
| 3 | howto/manage/resize-storage | [Resize LXD storage](https://discourse.ubuntu.com/t/resize-lxd-storage/32569)|
| 2 | howto/manage/web-dashboard | [Use the web dashboard](https://discourse.ubuntu.com/t/web-dashboard/20871)|
| 2 | howto/application/landing | [Manage applications](https://discourse.ubuntu.com/t/manage-applications/24333) |
| 3 | howto/application/create | [Create an application](https://discourse.ubuntu.com/t/create-an-application/24198)|
| 3 | howto/application/stream | [Stream an application](https://discourse.ubuntu.com/t/how-to-stream-applications/42688)|
| 3 | howto/application/wait | [Wait for an application](https://discourse.ubuntu.com/t/wait-for-an-application/24202)|
| 3 | howto/application/list | [List applications](https://discourse.ubuntu.com/t/list-applications/24200)|
| 3 | howto/application/userdata | [Pass custom data](https://discourse.ubuntu.com/t/how-to-pass-custom-data-to-an-application/30368)|
| 3 | howto/application/test | [Test your application](https://discourse.ubuntu.com/t/usecase-application-testing/17775)|
| 3 | howto/application/update | [Update an application](https://discourse.ubuntu.com/t/update-an-application/24201)|
| 3 | howto/application/delete | [Delete an application](https://discourse.ubuntu.com/t/delete-an-application/24199)|
| 3 | howto/application/extend | [Extend an application](https://discourse.ubuntu.com/t/extand-an-application/28554)|
| 2 | howto/application/virtual-devices | [Create a virtual device](https://discourse.ubuntu.com/t/virtual-devices/19069)|
| 2 | howto/aar/landing | [Manage AAR](https://discourse.ubuntu.com/t/manage-aar/36807)|
| 3 | howto/aar/deploy | [Deploy an AAR](https://discourse.ubuntu.com/t/installation-application-registry/17749)|
| 3 | howto/aar/configure | [Configure an AAR](https://discourse.ubuntu.com/t/configure-an-aar/24319)|
| 3 | howto/aar/revoke | [Revoke an AAR client](https://discourse.ubuntu.com/t/revoke-an-aar-client/24320)|
| 2 | howto/port/landing | [Port Android apps](https://discourse.ubuntu.com/t/port-android-apps/17776)|
| 3 | howto/port/permissions | [Grant permissions](https://discourse.ubuntu.com/t/grant-runtime-permissions/26054)|
| 3 | howto/port/architecture | [Choose APK architecture](https://discourse.ubuntu.com/t/choose-apk-architecture/26055)|
| 3 | howto/port/obb-files | [Port APKs with OBB files](https://discourse.ubuntu.com/t/port-apks-with-obb-files/26056)|
| 3 | howto/port/configure-watchdog | [Configure the watchdog](https://discourse.ubuntu.com/t/configure-the-watchdog/26057)|
| 3 | howto/port/install-system-app | [Install APK as a system app](https://discourse.ubuntu.com/t/install-an-apk-as-a-system-app/27086)|
| 2 | howto/instance/landing | [Manage instances](https://discourse.ubuntu.com/t/24335) |
| 3 | howto/instance/create | [Create an instance](https://discourse.ubuntu.com/t/24327)|
| 3 | howto/instance/start | [Start an instance](https://discourse.ubuntu.com/t/33924)|
| 3 | howto/instance/wait | [Wait for an instance](https://discourse.ubuntu.com/t/24330)|
| 3 | howto/instance/access | [Access an instance](https://discourse.ubuntu.com/t/17772)|
| 3 | howto/instance/list | [List instances](https://discourse.ubuntu.com/t/24328)|
| 3 | howto/instance/geographic-location | [Configure geographic location](https://discourse.ubuntu.com/t/17782)|
| 3 | howto/instance/logs | [View the instance logs](https://discourse.ubuntu.com/t/24329)|
| 3 | howto/instance/stop | [Stop an instance](https://discourse.ubuntu.com/t/33925)|
| 3 | howto/instance/backup-and-restore | [Back up and restore application data](https://discourse.ubuntu.com/t/24183)|
| 3 | howto/instance/delete | [Delete an instance](https://discourse.ubuntu.com/t/24325)|
| 3 | howto/instance/expose-services | [Expose services](https://discourse.ubuntu.com/t/24326)|
| 2 | howto/addons/landing | [Use addons](https://discourse.ubuntu.com/t/managing-addons/17759)|
| 3 | howto/addons/create | [Create addons](https://discourse.ubuntu.com/t/create-an-addon/40632)|
| 3 | howto/addons/enable-globally | [Enable globally](https://discourse.ubuntu.com/t/enable-an-addon-globally/25285)|
| 3 | howto/addons/update | [Update addons](https://discourse.ubuntu.com/t/update-addons/25286)|
| 3 | howto/addons/migrate | [Migrate from previous versions](https://discourse.ubuntu.com/t/migrate-from-previous-addon-versions/25287)|
| 3 | howto/addons/install-tools | [Example: Install tools](https://discourse.ubuntu.com/t/example-install-tools/25288)|
| 3 | howto/addons/backup-and-restore | [Example: Back up data](https://discourse.ubuntu.com/t/example-back-up-data/25289)|
| 3 | howto/addons/customise-android | [Example: Customise Android](https://discourse.ubuntu.com/t/example-customise-android/25290)|
| 3 | howto/addons/emulate-platforms | [Example: Emulate platforms](https://discourse.ubuntu.com/t/example-emulate-platforms/25291)|
| 2 | howto/stream/landing | [Implement streaming](https://discourse.ubuntu.com/t/implement-streaming/24332) |
| 3 | howto/stream/access | [Access the stream gateway](https://discourse.ubuntu.com/t/managing-stream-gateway-access/17784) |
| 3 | howto/stream/oob-data | [Exchange OOB data](https://discourse.ubuntu.com/t/exchange-out-of-band-data/21834)|
| 3 | howto/stream/client-side-keyboard | [Use a client-side keyboard](https://discourse.ubuntu.com/t/integrate-a-client-side-virtual-keyboard/23643)|
| 2 | howto/cluster/landing | [Manage the cluster](https://discourse.ubuntu.com/t/manage-cluster-nodes/24334) |
| 3 | howto/cluster/configure-nodes | [Configure cluster nodes](https://discourse.ubuntu.com/t/configure-cluster-nodes/28716) |
| 3 | howto/cluster/scale-up | [Scale up a LXD cluster](https://discourse.ubuntu.com/t/scale-up-a-lxd-cluster/24322)|
| 3 | howto/cluster/scale-down | [Scale down a LXD cluster](https://discourse.ubuntu.com/t/scale-down-a-lxd-cluster/24323)|
| 2 | howto/anbox/landing | [Work with the Anbox runtime](https://discourse.ubuntu.com/t/how-to-work-with-the-anbox-runtime/33098) |
| 3 | howto/anbox/develop-platform | [Develop a platform plugin](https://discourse.ubuntu.com/t/how-to-develop-a-platform-plugin/33099) |
| 3 | howto/anbox/develop-addon | [Develop and test addons](https://discourse.ubuntu.com/t/develop-and-test-addons-in-development-mode/36914) |
| 3 | howto/anbox/enable-virgl | [Enable VirGL](https://discourse.ubuntu.com/t/how-to-enable-virgl/42426) |
| 2 | howto/android/landing | [Work with Android](https://discourse.ubuntu.com/t/how-to-work-with-android-in-anbox-cloud/42428) |
| 3 | howto/android/graphics-debugging-with-renderdoc | [Graphics debugging with Renderdoc](https://discourse.ubuntu.com/t/how-to-debug-graphics-with-renderdoc/42427) |
| 2 | howto/troubleshoot/landing | [Troubleshoot Anbox Cloud](https://discourse.ubuntu.com/t/how-to-troubleshoot-anbox-cloud/17837)|
| 3 | howto/troubleshoot/initial-setup | [Troubleshoot initial setup](https://discourse.ubuntu.com/t/troubleshoot-issues-with-initial-setup/35704)|
| 3 | howto/troubleshoot/logs | [View logs](https://discourse.ubuntu.com/t/managing-logs/17771)|
| 3 | howto/troubleshoot/application-creation | [Troubleshoot application creation](https://discourse.ubuntu.com/t/troubleshoot-issues-with-application-creation/35702)|
| 3 | howto/troubleshoot/instance-failures | [Troubleshoot instance failures](https://discourse.ubuntu.com/t/35703)|
| 3 | howto/troubleshoot/lxd-cluster | [Troubleshoot LXD cluster](https://discourse.ubuntu.com/t/troubleshoot-issues-with-lxd-clustering/35705)|
| 3 | howto/troubleshoot/dashboard-issues | [Troubleshoot dashboard issues](https://discourse.ubuntu.com/t/36105)
| 3 | howto/troubleshoot/streaming-issues | [Troubleshoot streaming issues](https://discourse.ubuntu.com/t/how-to-debug-streaming-issues/31341)|
| 2 | howto/monitor/landing | [Monitor Anbox Cloud](https://discourse.ubuntu.com/t/monitor-anbox-cloud/24338) |
| 0 | | |
| 1 | reference/landing | [Reference](https://discourse.ubuntu.com/t/reference/28828) |
| 2 | reference/releases-versions | [Releases and versions](https://discourse.ubuntu.com/t/releases-and-versions/37993) |
| 3 | reference/roadmap | [Release roadmap](https://discourse.ubuntu.com/t/release-roadmap/19359)|
| 3 | reference/release-notes/release-notes | [Release notes](https://discourse.ubuntu.com/t/release-notes/17842)|
| 3 | reference/supported-versions | [Supported versions](https://discourse.ubuntu.com/t/supported-versions/21046) |
| 3 | reference/component-versions | [Component versions](https://discourse.ubuntu.com/t/component-versions/21413)|
| 2 | reference/requirements | [Requirements](https://discourse.ubuntu.com/t/installation-requirements/17734) |
| 2 | reference/appliance-command-reference/landing | [Appliance command reference](https://discourse.ubuntu.com/t/39525)|
| 2 | reference/amc-command-reference/landing | [AMC command reference](https://discourse.ubuntu.com/t/40797) |
| 2 | reference/provided-images | [Provided images](https://discourse.ubuntu.com/t/provided-images/24185)|
| 2 | reference/supported-rendering-resources | [Supported rendering resources](https://discourse.ubuntu.com/t/supported-rendering-resources/37322) |
| 2 | reference/supported-codecs | [Supported codecs](https://discourse.ubuntu.com/t/37323)|
| 2 | reference/android-features | [Supported Android features](https://discourse.ubuntu.com/t/supported-android-features/28825)|
| 2 | reference/anbox-features | [Supported Anbox features](https://discourse.ubuntu.com/t/supported-features-aosp-vs-aaos/42520)|
| 2 | reference/ams-configuration | [AMS configuration](https://discourse.ubuntu.com/t/ams-configuration/20872)|
| 2 | reference/application-manifest | [Application manifest](https://discourse.ubuntu.com/t/application-manifest/24197)|
| 2 | reference/api-reference | [APIs](https://discourse.ubuntu.com/t/api-reference/24339) |
| 3 | reference/ams-http-api | [AMS HTTP API](https://canonical.github.io/anbox-cloud.github.com/latest/ams/)|
| 3 | reference/anbox-https-api | [Anbox HTTP API](https://discourse.ubuntu.com/t/anbox-http-api-reference/17819)|
| 3 | reference/anbox-stream-gateway | [Stream Gateway API](https://canonical.github.io/anbox-cloud.github.com/latest/anbox-stream-gateway/)|
| 3 | reference/anbox-platform-sdk-api | [Anbox Platform SDK API](https://canonical.github.io/anbox-cloud.github.com/latest/anbox-platform-sdk/)|
| 2 | reference/sdks | [Anbox Cloud SDKs](https://discourse.ubuntu.com/t/anbox-cloud-sdks/17844)|
| 2 | reference/network-ports | [Network ports](https://discourse.ubuntu.com/t/network-ports/33650)|
| 2 | reference/addon-manifest | [Addon manifest](https://discourse.ubuntu.com/t/addons/25293)|
| 2 | reference/hooks | [Hooks](https://discourse.ubuntu.com/t/hooks/28555)|
| 2 | reference/webrtc-streamer | [WebRTC streamer](https://discourse.ubuntu.com/t/webrtc-streamer/30195)|
| 2 | reference/prometheus | [Prometheus metrics](https://discourse.ubuntu.com/t/prometheus-metrics/19521)|
| 2 | reference/perf-benchmarks | [Performance benchmarks](https://discourse.ubuntu.com/t/performance-benchmarks/24709)|
| 2 | reference/license-information | [License information](https://discourse.ubuntu.com/t/license-information/36649) |
| 2 | reference/glossary | [Glossary](https://discourse.ubuntu.com/t/glossary/26204)|
| 0 | | |
| 1 | explanation/landing | [Explanation](https://discourse.ubuntu.com/t/explanation/28829) |
| 2 | explanation/anbox-cloud | [Anbox Cloud](https://discourse.ubuntu.com/t/anbox-cloud-overview/17802) |
| 2 | explanation/rendering-architecture | [Rendering architecture](https://discourse.ubuntu.com/t/about-rendering-architecture/35129)
| 2 | explanation/security | [Security](https://discourse.ubuntu.com/t/about-security/31217)|
| 2 | explanation/ams | [AMS](https://discourse.ubuntu.com/t/about-ams/24321)|
| 2 | explanation/aar | [AAR](https://discourse.ubuntu.com/t/application-registry/17761)|
| 2 | explanation/web-dashboard | [Dashboard](https://discourse.ubuntu.com/t/anbox-cloud-web-dashboard/41847)
| 2 | explanation/applications | [Applications](https://discourse.ubuntu.com/t/managing-applications/17760)|
| 3 | explanation/resources | [Resources and resource presets](https://discourse.ubuntu.com/t/24960)|
| 2 | explanation/addons | [Addons](https://discourse.ubuntu.com/t/addons/38727)|
| 2 | explanation/application-streaming | [Application streaming](https://discourse.ubuntu.com/t/streaming-android-applications/17769)|
| 2 | explanation/instances | [Instances](https://discourse.ubuntu.com/t/17763)|
| 2 | explanation/platforms | [Platforms](https://discourse.ubuntu.com/t/anbox-platforms/18733)|
| 2 | explanation/gpus-instances | [GPUs and instances](https://discourse.ubuntu.com/t/17768)|
| 2 | explanation/clustering | [Clustering](https://discourse.ubuntu.com/t/capacity-planning/17765)|
| 2 | explanation/performance | [Performance](https://discourse.ubuntu.com/t/about-performance/29416) |
| 2 | explanation/capacity-planning | [Capacity planning](https://discourse.ubuntu.com/t/about-capacity-planning/28717) |
| 2 | explanation/production | [Production planning](https://discourse.ubuntu.com/t/about-production-planning/34648) |
| 0 | | |
| 1 | |[Documentation feedback](https://forms.gle/6yzgLbwN8rVYSdvG9)|
| 0 | | |
|   | reference/release-notes/1.21.1 | [Release notes - Anbox Cloud 1.21.1](https://discourse.ubuntu.com/t/43279)|
|   | reference/release-notes/1.21.0 | [Release notes-Anbox Cloud 1.21.0](https://discourse.ubuntu.com/t/42429)|
|   | reference/release-notes/1.20.2 | [Release notes-Anbox Cloud 1.20.2](https://discourse.ubuntu.com/t/41686)|
|   | reference/release-notes/1.20.1 | [Release notes-Anbox Cloud 1.20.1](https://discourse.ubuntu.com/t/40988)|
|   | reference/release-notes/1.20.0 | [Release notes-Anbox Cloud 1.20.0](https://discourse.ubuntu.com/t/40281)|
|   | reference/release-notes/1.19.2 | [Release notes-Anbox Cloud 1.19.2](https://discourse.ubuntu.com/t/39311)|
|   | reference/release-notes/1.19.1 | [Release notes-Anbox Cloud 1.19.1](https://discourse.ubuntu.com/t/38595)|
|   | reference/release-notes/1.19.0-fix1 | [Hotfix release announcement](https://discourse.ubuntu.com/t/38250)|
|   | reference/release-notes/1.19.0 | [Release notes-Anbox Cloud 1.19.0](https://discourse.ubuntu.com/t/37849)|
|   | reference/release-notes/1.18.2 | [Release notes-Anbox Cloud 1.18.2](https://discourse.ubuntu.com/t/36916)|
|   | reference/release-notes/1.18.1 | [Release notes-Anbox Cloud 1.18.1](https://discourse.ubuntu.com/t/36309)|
|   | reference/release-notes/1.18.0 | [Release notes-Anbox Cloud 1.18.0](https://discourse.ubuntu.com/t/35812)|
|   | reference/release-notes/1.17.2 | [Release notes-Anbox Cloud 1.17.2](https://discourse.ubuntu.com/t/35195)|
|   | reference/release-notes/1.17.1 | [Release notes-Anbox Cloud 1.17.1](https://discourse.ubuntu.com/t/34573)|
|   | reference/release-notes/1.17.0 | [Release notes-Anbox Cloud 1.17.0](https://discourse.ubuntu.com/t/33927)|
|   | reference/release-notes/1.16.4 | [Release notes-Anbox Cloud 1.16.4](https://discourse.ubuntu.com/t/33437)|
|   | reference/release-notes/1.16.3 | [Release notes-Anbox Cloud 1.16.3](https://discourse.ubuntu.com/t/33261)|
|   | reference/release-notes/1.16.2 | [Release notes-Anbox Cloud 1.16.2](https://discourse.ubuntu.com/t/33161)|
|   | reference/release-notes/1.16.1 | [Release notes-Anbox Cloud 1.16.1](https://discourse.ubuntu.com/t/32733)|
|   | reference/release-notes/1.16.0 | [Release notes-Anbox Cloud 1.16.0](https://discourse.ubuntu.com/t/32264)|
|   | reference/release-notes/1.15.3 | [Release notes-Anbox Cloud 1.15.3](https://discourse.ubuntu.com/t/31616)|
|   | reference/release-notes/1.15.2 | [Release notes-Anbox Cloud 1.15.2](https://discourse.ubuntu.com/t/31322)|
|   | reference/release-notes/1.15.1 | [Release notes-Anbox Cloud 1.15.1](https://discourse.ubuntu.com/t/30585)|
|   | reference/release-notes/1.15.0 | [Release notes-Anbox Cloud 1.15.0](https://discourse.ubuntu.com/t/30196)|
|   | reference/release-notes/1.14.2 | [Release notes-Anbox Cloud 1.14.2](https://discourse.ubuntu.com/t/29553)|
|   | reference/release-notes/1.14.1 | [Release notes-Anbox Cloud 1.14.1](https://discourse.ubuntu.com/t/28952)|
|   | reference/release-notes/1.14.0 | [Release notes-Anbox Cloud 1.14.0](https://discourse.ubuntu.com/t/28557)|
|   | reference/release-notes/1.13.2 | [Release notes-Anbox Cloud 1.13.2](https://discourse.ubuntu.com/t/27701)|
|   | reference/release-notes/1.13.1 | [Release notes-Anbox Cloud 1.13.1](https://discourse.ubuntu.com/t/27254)|
|   | reference/release-notes/1.13.0 | [Release notes-Anbox Cloud 1.13.0](https://discourse.ubuntu.com/t/26857)|
|   | reference/release-notes/1.12.5 | [Release notes-Anbox Cloud 1.12.5](https://discourse.ubuntu.com/t/26380)|
|   | reference/release-notes/1.12.4 | [Release notes-Anbox Cloud 1.12.4](https://discourse.ubuntu.com/t/26263)|
|   | reference/release-notes/1.12.3 | [Release notes-Anbox Cloud 1.12.3](https://discourse.ubuntu.com/t/26252)|
|   | reference/release-notes/1.12.2 | [Release notes-Anbox Cloud 1.12.2](https://discourse.ubuntu.com/t/25819)|
|   | reference/release-notes/1.12.1 | [Release notes-Anbox Cloud 1.12.1](https://discourse.ubuntu.com/t/25542)|
|   | reference/release-notes/1.12.0 | [Release notes-Anbox Cloud 1.12.0](https://discourse.ubuntu.com/t/25295)|
|   | reference/release-notes/1.11.5 | [Release notes-Anbox Cloud 1.11.5](https://discourse.ubuntu.com/t/26739)|
|   | reference/release-notes/1.11.4 | [Release notes-Anbox Cloud 1.11.4](https://discourse.ubuntu.com/t/25018)|
|   | reference/release-notes/1.11.3 | [Release notes-Anbox Cloud 1.11.3](https://discourse.ubuntu.com/t/24705)|
|   | reference/release-notes/1.11.2 | [Release notes-Anbox Cloud 1.11.2](https://discourse.ubuntu.com/t/24293)|
|   | reference/release-notes/1.11.1 | [Release notes-Anbox Cloud 1.11.1](https://discourse.ubuntu.com/t/23772)|
|   | reference/release-notes/1.11.0 | [Release notes-Anbox Cloud 1.11.0](https://discourse.ubuntu.com/t/23590)|
|   | reference/release-notes/1.10.3 | [Release notes-Anbox Cloud 1.10.3](https://discourse.ubuntu.com/t/23267)|
|   | reference/release-notes/1.10.2 | [Release notes-Anbox Cloud 1.10.2](https://discourse.ubuntu.com/t/22692)|
|   | reference/release-notes/1.10.1 | [Release notes-Anbox Cloud 1.10.1](https://discourse.ubuntu.com/t/22280)|
|   | reference/release-notes/1.10.0 | [Release notes-Anbox Cloud 1.10.0](https://discourse.ubuntu.com/t/22205)|
|   | reference/release-notes/1.9.5 | [Release notes-Anbox Cloud 1.9.5](https://discourse.ubuntu.com/t/22259)|
|   | reference/release-notes/1.9.4 | [Release notes-Anbox Cloud 1.9.4](https://discourse.ubuntu.com/t/22148)|
|   | reference/release-notes/1.9.3 | [Release notes-Anbox Cloud 1.9.3](https://discourse.ubuntu.com/t/21795)|
|   | reference/release-notes/1.9.2 | [Release notes-Anbox Cloud 1.9.2](https://discourse.ubuntu.com/t/21420)|
|   | reference/release-notes/1.9.1 | [Release notes-Anbox Cloud 1.9.1](https://discourse.ubuntu.com/t/21232)|
|   | reference/release-notes/1.9.0 | [Release notes-Anbox Cloud 1.9.0](https://discourse.ubuntu.com/t/20870)|
|   | reference/release-notes/1.8.3 | [Release notes-Anbox Cloud 1.8.3](https://discourse.ubuntu.com/t/20435)|
|   | reference/release-notes/1.8.2 | [Release notes-Anbox Cloud 1.8.2](https://discourse.ubuntu.com/t/19951)|
|   | reference/release-notes/1.8.1 | [Release notes-Anbox Cloud 1.8.1](https://discourse.ubuntu.com/t/19319)|
|   | reference/release-notes/1.8.0 | [Release notes-Anbox Cloud 1.8.0](https://discourse.ubuntu.com/t/19200)|
|   | reference/release-notes/1.7.4 | [Release notes-Anbox Cloud 1.7.4](https://discourse.ubuntu.com/t/18812)|
|   | reference/release-notes/1.7.3 | [Release notes-Anbox Cloud 1.7.3](https://discourse.ubuntu.com/t/18458)|
|   | reference/release-notes/1.7.2 | [Release notes-Anbox Cloud 1.7.2](https://discourse.ubuntu.com/t/18265)|
|   | reference/release-notes/1.7.1 | [Release notes-Anbox Cloud 1.7.1](https://discourse.ubuntu.com/t/17977)|
|   | reference/appliance-command-reference/ams | [Appliance command reference - ams](https://discourse.ubuntu.com/t/39517)|
|   | reference/appliance-command-reference/dashboard | [Appliance command reference - dashboard](https://discourse.ubuntu.com/t/39520)|
|   | reference/appliance-command-reference/destroy | [Appliance command reference - destroy](https://discourse.ubuntu.com/t/39521)|
|   | reference/appliance-command-reference/gateway | [Appliance command reference - gateway](https://discourse.ubuntu.com/t/39522)|
|   | reference/appliance-command-reference/help | [Appliance command reference - help](https://discourse.ubuntu.com/t/39523)|
|   | reference/appliance-command-reference/init | [Appliance command reference - init](https://discourse.ubuntu.com/t/39524)|
|   | reference/appliance-command-reference/status | [Appliance command reference - status](https://discourse.ubuntu.com/t/39527)|
|   | reference/appliance-command-reference/upgrade | [Appliance command reference - upgrade](https://discourse.ubuntu.com/t/39528)|
|   | reference/amc-command-reference/addon | [AMC command reference - addon](https://discourse.ubuntu.com/t/40775) |
|   | reference/amc-command-reference/application | [AMC command reference - application](https://discourse.ubuntu.com/t/40776) |
|   | reference/amc-command-reference/benchmark | [AMC command reference - benchmark](https://discourse.ubuntu.com/t/40777) |
|   | reference/amc-command-reference/completion | [AMC command reference - completion](https://discourse.ubuntu.com/t/40778) |
|   | reference/amc-command-reference/config | [AMC command reference - config](https://discourse.ubuntu.com/t/40779) |
|   | reference/amc-command-reference/delete | [AMC command reference - delete](https://discourse.ubuntu.com/t/40780) |
|   | reference/amc-command-reference/exec | [AMC command reference - exec](https://discourse.ubuntu.com/t/40781) |
|   | reference/amc-command-reference/help | [AMC command reference - help](https://discourse.ubuntu.com/t/40782) |
|   | reference/amc-command-reference/image | [AMC command reference - image](https://discourse.ubuntu.com/t/40783) |
|   | reference/amc-command-reference/info | [AMC command reference - info](https://discourse.ubuntu.com/t/40784) |
|   | reference/amc-command-reference/init | [AMC command reference - init](https://discourse.ubuntu.com/t/40785) |
|   | reference/amc-command-reference/launch | [AMC command reference - launch](https://discourse.ubuntu.com/t/40786) |
|   | reference/amc-command-reference/list | [AMC command reference - list](https://discourse.ubuntu.com/t/40787) |
|   | reference/amc-command-reference/logs | [AMC command reference - logs](https://discourse.ubuntu.com/t/40788) |
|   | reference/amc-command-reference/node | [AMC command reference - node](https://discourse.ubuntu.com/t/40789) |
|   | reference/amc-command-reference/remote | [AMC command reference - remote](https://discourse.ubuntu.com/t/40790) |
|   | reference/amc-command-reference/shell | [AMC command reference - shell](https://discourse.ubuntu.com/t/40791) |
|   | reference/amc-command-reference/show-log | [AMC command reference - show-log](https://discourse.ubuntu.com/t/40792) |
|   | reference/amc-command-reference/show | [AMC command reference - show](https://discourse.ubuntu.com/t/40793) |
|   | reference/amc-command-reference/start | [AMC command reference - start](https://discourse.ubuntu.com/t/40794) |
|   | reference/amc-command-reference/stop | [AMC command reference - stop](https://discourse.ubuntu.com/t/40795) |
|   | reference/amc-command-reference/wait | [AMC command reference - wait](https://discourse.ubuntu.com/t/40796) |
[/details]

## Redirects

[details=Mapping table]
| Path | Location |
| ---- | -------- |
| /docs/tut/creating-addon | /docs/tutorial/creating-addon |
| /docs/tut/getting-started-dashboard | /docs/tutorial/getting-started-dashboard |
| /docs/tut/getting-started | /docs/tutorial/getting-started |
| /docs/tut/installing-appliance | /docs/tutorial/installing-appliance |
| /docs/tut/landing | /docs/tutorial/landing |
| /docs/tut/stream-client | /docs/tutorial/stream-client |
| /docs/ref/addon-manifest | /docs/reference/addon-manifest |
| /docs/ref/ams-configuration | /docs/reference/ams-configuration |
| /docs/ref/anbox-https-api | /docs/reference/anbox-https-api |
| /docs/ref/android-features | /docs/reference/android-features |
| /docs/ref/api-reference | /docs/reference/api-reference |
| /docs/ref/application-manifest | /docs/reference/application-manifest |
| /docs/ref/component-versions | /docs/reference/component-versions |
| /docs/ref/glossary | /docs/reference/glossary |
| /docs/ref/hooks | /docs/reference/hooks |
| /docs/ref/landing | /docs/reference/landing |
| /docs/ref/license-information | /docs/reference/license-information |
| /docs/ref/network-ports | /docs/reference/network-ports |
| /docs/ref/perf-benchmarks | /docs/reference/perf-benchmarks |
| /docs/ref/prometheus | /docs/reference/prometheus |
| /docs/ref/provided-images | /docs/reference/provided-images |
| /docs/ref/releases-versions | /docs/reference/releases-version |
| /docs/ref/requirements | /docs/reference/requirements |
| /docs/ref/roadmap | /docs/reference/roadmap |
| /docs/ref/sdks | /docs/reference/sdks |
| /docs/ref/supported-codecs | /docs/reference/supported-codecs |
| /docs/ref/supported-rendering-resources | /docs/reference/supported-rendering-resources |
| /docs/ref/supported-versions | /docs/reference/supported-versions |
| /docs/ref/webrtc-streamer | /docs/reference/webrtc-streamer |
| /docs/ref/release-notes | /docs/reference/release-notes |
| /docs/ref/appliance-command-reference/landing | /docs/reference/appliance-command-reference/landing|
| /docs/ref/appliance-command-reference/ams | /docs/reference/appliance-command-reference/ams|
| /docs/ref/appliance-command-reference/cluster | /docs/reference/appliance-command-reference/cluster|
| /docs/ref/appliance-command-reference/dashboard | /docs/reference/appliance-command-reference/dashboard|
| /docs/ref/appliance-command-reference/destroy | /docs/reference/appliance-command-reference/destroy|
| /docs/ref/appliance-command-reference/gateway | /docs/reference/appliance-command-reference/gateway|
| /docs/ref/appliance-command-reference/help | /docs/reference/appliance-command-reference/help|
| /docs/ref/appliance-command-reference/init | /docs/reference/appliance-command-reference/init|
| /docs/ref/appliance-command-reference/landing | /docs/reference/appliance-command-reference/landing|
| /docs/ref/appliance-command-reference/status | /docs/reference/appliance-command-reference/status|
| /docs/ref/appliance-command-reference/upgrade | /docs/reference/appliance-command-reference/upgrade|
| /docs/ref/amc-command-reference/landing | /docs/reference/amc-command-reference/landing|
| /docs/ref/amc-command-reference/addon | /docs/reference/amc-command-reference/addon|
| /docs/ref/amc-command-reference/application | /docs/reference/amc-command-reference/application|
| /docs/ref/amc-command-reference/benchmark | /docs/reference/amc-command-reference/benchmark|
| /docs/ref/amc-command-reference/completion | /docs/reference/amc-command-reference/completion|
| /docs/ref/amc-command-reference/config | /docs/reference/amc-command-reference/config|
| /docs/ref/amc-command-reference/delete | /docs/reference/amc-command-reference/delete|
| /docs/ref/amc-command-reference/exec | /docs/reference/amc-command-reference/exec|
| /docs/ref/amc-command-reference/help | /docs/reference/amc-command-reference/help|
| /docs/ref/amc-command-reference/image | /docs/reference/amc-command-reference/image|
| /docs/ref/amc-command-reference/info | /docs/reference/amc-command-reference/info|
| /docs/ref/amc-command-reference/init | /docs/reference/amc-command-reference/init|
| /docs/ref/amc-command-reference/launch | /docs/reference/amc-command-reference/launch|
| /docs/ref/amc-command-reference/list | /docs/reference/amc-command-reference/list|
| /docs/ref/amc-command-reference/logs | /docs/reference/amc-command-reference/logs|
| /docs/ref/amc-command-reference/node | /docs/reference/amc-command-reference/node|
| /docs/ref/amc-command-reference/remote | /docs/reference/amc-command-reference/remote|
| /docs/ref/amc-command-reference/shell | /docs/reference/amc-command-reference/shell|
| /docs/ref/amc-command-reference/show-log | /docs/reference/amc-command-reference/show-log|
| /docs/ref/amc-command-reference/show | /docs/reference/amc-command-reference/show|
| /docs/ref/amc-command-reference/start | /docs/reference/amc-command-reference/start|
| /docs/ref/amc-command-reference/stop | /docs/reference/amc-command-reference/stop|
| /docs/ref/amc-command-reference/wait | /docs/reference/amc-command-reference/wait|
| /docs/exp/landing | /docs/explanation/landing |
| /docs/exp/aar | /docs/explanation/aar |
| /docs/exp/addons | /docs/explanation/addons |
| /docs/exp/ams | /docs/explanation/ams |
| /docs/exp/anbox-cloud | /docs/explanation/anbox-cloud |
| /docs/exp/application-streaming | /docs/explanation/application-streaming |
| /docs/exp/applications | /docs/explanation/applications |
| /docs/exp/capacity-planning | /docs/explanation/capacity-planning |
| /docs/exp/clustering | /docs/explanation/clustering |
| /docs/exp/gpus-instances | /docs/explanation/gpus-instances |
| /docs/exp/instances | /docs/explanation/instances |
| /docs/exp/performance | /docs/explanation/performance |
| /docs/exp/platforms | /docs/explanation/platforms |
| /docs/exp/production | /docs/explanation/production |
| /docs/exp/rendering-architecture | /docs/explanation/rendering-architecture |
| /docs/exp/resources | /docs/explanation/resources |
| /docs/exp/security | /docs/explanation/security |
| /docs/manage/container-access | /docs/howto/instance/access |
| /docs/howto/container/view-log | /docs/howto/instance/logs |
| /docs/usage/usecase-container-configuration | /docs/howto/instance/geographic-location |
| /docs/howto/containers/backup-and-restore | /docs/howto/instance/backup-and-restore |
| /docs/howto/stream/web-client | /docs/tut/stream-client |
| /docs/howto/troubleshoot/collect-info | /docs/howto/troubleshoot/landing |
| /docs/manage/managing-containers | /docs/exp/instances |
| /docs/exp/gpu-support | /docs/explanation/gpus-instances |
| /docs/howto/container/launch | /docs/howto/instance/create |
| /docs/howto/stream/debug | /docs/howto/troubleshoot/streaming-issues |
| /docs/howto/manage/logs | /docs/howto/troubleshoot/logs |
| /docs/ref/platforms | /docs/explanation/platforms |
| /docs/ref/instance-types | /docs/reference/application-manifest |
| /docs/ref/supported-video-codecs | /docs/reference/supported-codecs |
| /docs/howto/addons/best-practices | /docs/explanation/addons |
| /docs/ref/addons | /docs/reference/addon-manifest |
| /docs/howto/manage/manage-appliance | /docs/reference/appliance-command-reference/landing |
| /docs/exp/containers | /docs/explanation/instances |
| /docs/howto/container | /docs/howto/instance |
| /docs/howto/troubleshoot/container-failures | /docs/howto/troubleshoot/instance-failures |
| /docs/howto/container/access | /docs/howto/instance/access |
| /docs/howto/container/backup-and-restore | /docs/howto/instance/backup-and-restore |
| /docs/howto/container/create | /docs/howto/instance/create |
| /docs/howto/container/delete | /docs/howto/instance/delete |
| /docs/howto/container/expose-service | /docs/howto/instance/expose-service |
| /docs/howto/container/geographic-location | /docs/howto/instance/geographic-location |
| /docs/howto/container/landing | /docs/howto/instance/landing |
| /docs/howto/container/list | /docs/howto/instance/list |
| /docs/howto/container/logs | /docs/howto/instance/logs |
| /docs/howto/container/start | /docs/howto/instance/start |
| /docs/howto/container/stop | /docs/howto/instance/stop |
| /docs/howto/container/wait | /docs/howto/instance/wait |
| /docs/howto/application/resources | /docs/explanation/resources |
[/details]

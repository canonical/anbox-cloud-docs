Anbox Cloud enables running Android apps on any cloud platform at scale. It uses system containers or virtual machines to run the nested Android containers and [Juju](https://juju.is/) for deployment in a cloud environment.

Anbox Cloud supports x86 and Arm64 hardware, providing the same set of features for both architectures.

Since Anbox Cloud uses system containers or virtual machines to emulate Android systems, you can achieve the isolation and security level of a virtual machine without the associated overhead. Therefore, compared to other Android emulation solutions, Anbox Cloud can provide at least twice the density and can serve up to 100 Android instances per server.

Due to its highly scalable nature and performance optimisation, delivering device-agnostic mobile applications is very easy. Popular use cases of Anbox Cloud include mobile game streaming services, corporate application streaming, application automation and testing.

## In this documentation
| | |
|--|--|
|  [Tutorials](https://discourse.ubuntu.com/t/tutorials/28826)</br>  Get started - a hands-on introduction to Anbox Cloud for new users </br> |  [How-to guides](https://discourse.ubuntu.com/t/how-to-guides/28827) </br> Step-by-step guides covering key operations and common tasks |
|  [Explanation](https://discourse.ubuntu.com/t/explanation/28829) </br> Concepts - discussion and clarification of key topics, architecture  | [Reference](https://discourse.ubuntu.com/t/reference/28828) </br> Technical information - specifications, APIs |

<a name="project-community"></a>
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
| 1 | tut/landing | [Tutorials](https://discourse.ubuntu.com/t/tutorials/28826) |
| 2 | tut/installing-appliance | [1. Install the appliance](https://discourse.ubuntu.com/t/install-appliance/22681) |
| 2 | tut/getting-started-dashboard | [2. Get started using the web dashboard](https://discourse.ubuntu.com/t/getting-started-with-anbox-cloud-web-dashboard/24958)|
| 2 | tut/getting-started | [3. Get started using the CLI](https://discourse.ubuntu.com/t/getting-started/17756)|
| 2 | tut/stream-client | [4. Set up a stream client (Optional)](https://discourse.ubuntu.com/t/set-up-a-stream-client/37328) |
| 2 | tut/creating-addon | [5. Create an addon (Optional)](https://discourse.ubuntu.com/t/creating-an-addon/25284)|
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
| 2 | howto/dashboard/web-dashboard | [Use the web dashboard](https://discourse.ubuntu.com/t/web-dashboard/20871)|
| 2 | howto/application/landing | [Manage applications](https://discourse.ubuntu.com/t/manage-applications/24333) |
| 3 | howto/application/create | [Create an application](https://discourse.ubuntu.com/t/create-an-application/24198)|
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
| 3 | howto/addons/create | [Create addons] (https://discourse.ubuntu.com/t/create-an-addon/40632)|
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
| 3 | howto/cluster/appliance | [Join a machine to the appliance](https://discourse.ubuntu.com/t/how-to-join-a-machine-to-the-anbox-cloud-appliance/29054) |
| 3 | howto/cluster/configure-nodes | [Configure cluster nodes](https://discourse.ubuntu.com/t/configure-cluster-nodes/28716) |
| 3 | howto/cluster/scale-up | [Scale up a LXD cluster](https://discourse.ubuntu.com/t/scale-up-a-lxd-cluster/24322)|
| 3 | howto/cluster/scale-down | [Scale down a LXD cluster](https://discourse.ubuntu.com/t/scale-down-a-lxd-cluster/24323)|
| 2 | howto/anbox/landing | [Work with the Anbox runtime](https://discourse.ubuntu.com/t/how-to-work-with-the-anbox-runtime/33098) |
| 3 | howto/anbox/develop-platform | [Develop a platform plugin](https://discourse.ubuntu.com/t/how-to-develop-a-platform-plugin/33099) |
| 3 | howto/anbox/develop-addon | [Develop and test addons](https://discourse.ubuntu.com/t/develop-and-test-addons-in-development-mode/36914) |
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
| 1 | ref/landing | [Reference](https://discourse.ubuntu.com/t/reference/28828) |
| 2 | ref/releases-versions | [Releases and versions](https://discourse.ubuntu.com/t/releases-and-versions/37993) |
| 3 | ref/roadmap | [Release roadmap](https://discourse.ubuntu.com/t/release-roadmap/19359)|
| 3 | ref/release-notes | [Release notes](https://discourse.ubuntu.com/t/release-notes/17842)|
| 3 | ref/supported-versions | [Supported versions](https://discourse.ubuntu.com/t/supported-versions/21046) |
| 3 | ref/component-versions | [Component versions](https://discourse.ubuntu.com/t/component-versions/21413)|
| 2 | ref/requirements | [Requirements](https://discourse.ubuntu.com/t/installation-requirements/17734) |
| 2 | ref/appliance-command-reference/landing | [Appliance command reference](https://discourse.ubuntu.com/t/39525)|
| 2 | ref/amc-command-reference/landing | [AMC command reference](https://discourse.ubuntu.com/t/40797) |
| 2 | ref/provided-images | [Provided images](https://discourse.ubuntu.com/t/provided-images/24185)|
| 2 | ref/supported-rendering-resources | [Supported rendering resources](https://discourse.ubuntu.com/t/supported-rendering-resources/37322) |
| 2 | ref/supported-codecs | [Supported codecs](https://discourse.ubuntu.com/t/37323)|
| 2 | ref/android-features | [Supported Android features](https://discourse.ubuntu.com/t/supported-android-features/28825)|
| 2 | ref/ams-configuration | [AMS configuration](https://discourse.ubuntu.com/t/ams-configuration/20872)|
| 2 | ref/application-manifest | [Application manifest](https://discourse.ubuntu.com/t/application-manifest/24197)|
| 2 | ref/api-reference | [APIs](https://discourse.ubuntu.com/t/api-reference/24339) |
| 3 | ref/ams-http-api | [AMS HTTP API](https://anbox-cloud.github.io/latest/ams/)|
| 3 | ref/anbox-https-api | [Anbox HTTP API](https://discourse.ubuntu.com/t/anbox-http-api-reference/17819)|
| 3 | ref/anbox-stream-gateway | [Stream Gateway API](https://anbox-cloud.github.io/latest/anbox-stream-gateway/)|
| 3 | ref/anbox-platform-sdk-api | [Anbox Platform SDK API](https://anbox-cloud.github.io/latest/anbox-platform-sdk/)|
| 2 | ref/sdks | [Anbox Cloud SDKs](https://discourse.ubuntu.com/t/anbox-cloud-sdks/17844)|
| 2 | ref/network-ports | [Network ports](https://discourse.ubuntu.com/t/network-ports/33650)|
| 2 | ref/addon-manifest | [Addon manifest](https://discourse.ubuntu.com/t/addons/25293)|
| 2 | ref/hooks | [Hooks](https://discourse.ubuntu.com/t/hooks/28555)|
| 2 | ref/webrtc-streamer | [WebRTC streamer](https://discourse.ubuntu.com/t/webrtc-streamer/30195)|
| 2 | ref/prometheus | [Prometheus metrics](https://discourse.ubuntu.com/t/prometheus-metrics/19521)|
| 2 | ref/perf-benchmarks | [Performance benchmarks](https://discourse.ubuntu.com/t/performance-benchmarks/24709)|
| 2 | ref/license-information | [License information](https://discourse.ubuntu.com/t/license-information/36649) |
| 2 | ref/glossary | [Glossary](https://discourse.ubuntu.com/t/glossary/26204)|
| 0 | | |
| 1 | exp/landing | [Explanation](https://discourse.ubuntu.com/t/explanation/28829) |
| 2 | exp/anbox-cloud | [Anbox Cloud](https://discourse.ubuntu.com/t/anbox-cloud-overview/17802) |
| 2 | exp/rendering-architecture | [Rendering architecture](https://discourse.ubuntu.com/t/about-rendering-architecture/35129)
| 2 | exp/security | [Security](https://discourse.ubuntu.com/t/about-security/31217)|
| 2 | exp/ams | [AMS](https://discourse.ubuntu.com/t/about-ams/24321)|
| 2 | exp/aar | [AAR](https://discourse.ubuntu.com/t/application-registry/17761)|
| 2 | exp/applications | [Applications](https://discourse.ubuntu.com/t/managing-applications/17760)|
| 3 | exp/resources | [Resources and resource presets](https://discourse.ubuntu.com/t/24960)|
| 2 | exp/addons | [Addons](https://discourse.ubuntu.com/t/addons/38727)|
| 2 | exp/application-streaming | [Application streaming](https://discourse.ubuntu.com/t/streaming-android-applications/17769)|
| 2 | exp/instances | [Instances](https://discourse.ubuntu.com/t/17763)|
| 2 | exp/platforms | [Platforms](https://discourse.ubuntu.com/t/anbox-platforms/18733)|
| 2 | exp/gpus-instances | [GPUs and instances](https://discourse.ubuntu.com/t/17768)|
| 2 | exp/clustering | [Clustering](https://discourse.ubuntu.com/t/capacity-planning/17765)|
| 2 | exp/performance | [Performance](https://discourse.ubuntu.com/t/about-performance/29416) |
| 2 | exp/capacity-planning | [Capacity planning](https://discourse.ubuntu.com/t/about-capacity-planning/28717) |
| 2 | exp/production | [Production planning](https://discourse.ubuntu.com/t/about-production-planning/34648) |
| 0 | | |
| 1 | |[Documentation feedback](https://forms.gle/6yzgLbwN8rVYSdvG9)|
| 0 | | |
|   | release-notes/1.20.2 | [Release notes-Anbox Cloud 1.20.2](https://discourse.ubuntu.com/t/41686)|
|   | release-notes/1.20.1 | [Release notes-Anbox Cloud 1.20.1](https://discourse.ubuntu.com/t/40988)|
|   | release-notes/1.20.0 | [Release notes-Anbox Cloud 1.20.0](https://discourse.ubuntu.com/t/40281)|
|   | release-notes/1.19.2 | [Release notes-Anbox Cloud 1.19.2](https://discourse.ubuntu.com/t/39311)|
|   | release-notes/1.19.1 | [Release notes-Anbox Cloud 1.19.1](https://discourse.ubuntu.com/t/38595)|
|   | release-notes/1.19.0-fix1 | [Hotfix release announcement](https://discourse.ubuntu.com/t/38250)|
|   | release-notes/1.19.0 | [Release notes-Anbox Cloud 1.19.0](https://discourse.ubuntu.com/t/37849)|
|   | release-notes/1.18.2 | [Release notes-Anbox Cloud 1.18.2](https://discourse.ubuntu.com/t/36916)|
|   | release-notes/1.18.1 | [Release notes-Anbox Cloud 1.18.1](https://discourse.ubuntu.com/t/36309)|
|   | release-notes/1.18.0 | [Release notes-Anbox Cloud 1.18.0](https://discourse.ubuntu.com/t/35812)|
|   | release-notes/1.17.2 | [Release notes-Anbox Cloud 1.17.2](https://discourse.ubuntu.com/t/35195)|
|   | release-notes/1.17.1 | [Release notes-Anbox Cloud 1.17.1](https://discourse.ubuntu.com/t/34573)|
|   | release-notes/1.17.0 | [Release notes-Anbox Cloud 1.17.0](https://discourse.ubuntu.com/t/33927)|
|   | release-notes/1.16.4 | [Release notes-Anbox Cloud 1.16.4](https://discourse.ubuntu.com/t/33437)|
|   | release-notes/1.16.3 | [Release notes-Anbox Cloud 1.16.3](https://discourse.ubuntu.com/t/33261)|
|   | release-notes/1.16.2 | [Release notes-Anbox Cloud 1.16.2](https://discourse.ubuntu.com/t/33161)|
|   | release-notes/1.16.1 | [Release notes-Anbox Cloud 1.16.1](https://discourse.ubuntu.com/t/32733)|
|   | release-notes/1.16.0 | [Release notes-Anbox Cloud 1.16.0](https://discourse.ubuntu.com/t/32264)|
|   | release-notes/1.15.3 | [Release notes-Anbox Cloud 1.15.3](https://discourse.ubuntu.com/t/31616)|
|   | release-notes/1.15.2 | [Release notes-Anbox Cloud 1.15.2](https://discourse.ubuntu.com/t/31322)|
|   | release-notes/1.15.1 | [Release notes-Anbox Cloud 1.15.1](https://discourse.ubuntu.com/t/30585)|
|   | release-notes/1.15.0 | [Release notes-Anbox Cloud 1.15.0](https://discourse.ubuntu.com/t/30196)|
|   | release-notes/1.14.2 | [Release notes-Anbox Cloud 1.14.2](https://discourse.ubuntu.com/t/29553)|
|   | release-notes/1.14.1 | [Release notes-Anbox Cloud 1.14.1](https://discourse.ubuntu.com/t/28952)|
|   | release-notes/1.14.0 | [Release notes-Anbox Cloud 1.14.0](https://discourse.ubuntu.com/t/28557)|
|   | release-notes/1.13.2 | [Release notes-Anbox Cloud 1.13.2](https://discourse.ubuntu.com/t/27701)|
|   | release-notes/1.13.1 | [Release notes-Anbox Cloud 1.13.1](https://discourse.ubuntu.com/t/27254)|
|   | release-notes/1.13.0 | [Release notes-Anbox Cloud 1.13.0](https://discourse.ubuntu.com/t/26857)|
|   | release-notes/1.12.5 | [Release notes-Anbox Cloud 1.12.5](https://discourse.ubuntu.com/t/26380)|
|   | release-notes/1.12.4 | [Release notes-Anbox Cloud 1.12.4](https://discourse.ubuntu.com/t/26263)|
|   | release-notes/1.12.3 | [Release notes-Anbox Cloud 1.12.3](https://discourse.ubuntu.com/t/26252)|
|   | release-notes/1.12.2 | [Release notes-Anbox Cloud 1.12.2](https://discourse.ubuntu.com/t/25819)|
|   | release-notes/1.12.1 | [Release notes-Anbox Cloud 1.12.1](https://discourse.ubuntu.com/t/25542)|
|   | release-notes/1.12.0 | [Release notes-Anbox Cloud 1.12.0](https://discourse.ubuntu.com/t/25295)|
|   | release-notes/1.11.5 | [Release notes-Anbox Cloud 1.11.5](https://discourse.ubuntu.com/t/26739)|
|   | release-notes/1.11.4 | [Release notes-Anbox Cloud 1.11.4](https://discourse.ubuntu.com/t/25018)|
|   | release-notes/1.11.3 | [Release notes-Anbox Cloud 1.11.3](https://discourse.ubuntu.com/t/24705)|
|   | release-notes/1.11.2 | [Release notes-Anbox Cloud 1.11.2](https://discourse.ubuntu.com/t/24293)|
|   | release-notes/1.11.1 | [Release notes-Anbox Cloud 1.11.1](https://discourse.ubuntu.com/t/23772)|
|   | release-notes/1.11.0 | [Release notes-Anbox Cloud 1.11.0](https://discourse.ubuntu.com/t/23590)|
|   | release-notes/1.10.3 | [Release notes-Anbox Cloud 1.10.3](https://discourse.ubuntu.com/t/23267)|
|   | release-notes/1.10.2 | [Release notes-Anbox Cloud 1.10.2](https://discourse.ubuntu.com/t/22692)|
|   | release-notes/1.10.1 | [Release notes-Anbox Cloud 1.10.1](https://discourse.ubuntu.com/t/22280)|
|   | release-notes/1.10.0 | [Release notes-Anbox Cloud 1.10.0](https://discourse.ubuntu.com/t/22205)|
|   | release-notes/1.9.5 | [Release notes-Anbox Cloud 1.9.5](https://discourse.ubuntu.com/t/22259)|
|   | release-notes/1.9.4 | [Release notes-Anbox Cloud 1.9.4](https://discourse.ubuntu.com/t/22148)|
|   | release-notes/1.9.3 | [Release notes-Anbox Cloud 1.9.3](https://discourse.ubuntu.com/t/21795)|
|   | release-notes/1.9.2 | [Release notes-Anbox Cloud 1.9.2](https://discourse.ubuntu.com/t/21420)|
|   | release-notes/1.9.1 | [Release notes-Anbox Cloud 1.9.1](https://discourse.ubuntu.com/t/21232)|
|   | release-notes/1.9.0 | [Release notes-Anbox Cloud 1.9.0](https://discourse.ubuntu.com/t/20870)|
|   | release-notes/1.8.3 | [Release notes-Anbox Cloud 1.8.3](https://discourse.ubuntu.com/t/20435)|
|   | release-notes/1.8.2 | [Release notes-Anbox Cloud 1.8.2](https://discourse.ubuntu.com/t/19951)|
|   | release-notes/1.8.1 | [Release notes-Anbox Cloud 1.8.1](https://discourse.ubuntu.com/t/19319)|
|   | release-notes/1.8.0 | [Release notes-Anbox Cloud 1.8.0](https://discourse.ubuntu.com/t/19200)|
|   | release-notes/1.7.4 | [Release notes-Anbox Cloud 1.7.4](https://discourse.ubuntu.com/t/18812)|
|   | release-notes/1.7.3 | [Release notes-Anbox Cloud 1.7.3](https://discourse.ubuntu.com/t/18458)|
|   | release-notes/1.7.2 | [Release notes-Anbox Cloud 1.7.2](https://discourse.ubuntu.com/t/18265)|
|   | release-notes/1.7.1 | [Release notes-Anbox Cloud 1.7.1](https://discourse.ubuntu.com/t/17977)|
|   | ref/appliance-command-reference/ams | [Appliance command reference - ams](https://discourse.ubuntu.com/t/39517)|
|   | ref/appliance-command-reference/cluster | [Appliance command reference - cluster](https://discourse.ubuntu.com/t/39519)|
|   | ref/appliance-command-reference/dashboard | [Appliance command reference - dashboard](https://discourse.ubuntu.com/t/39520)|
|   | ref/appliance-command-reference/destroy | [Appliance command reference - destroy](https://discourse.ubuntu.com/t/39521)|
|   | ref/appliance-command-reference/gateway | [Appliance command reference - gateway](https://discourse.ubuntu.com/t/39522)|
|   | ref/appliance-command-reference/help | [Appliance command reference - help](https://discourse.ubuntu.com/t/39523)|
|   | ref/appliance-command-reference/init | [Appliance command reference - init](https://discourse.ubuntu.com/t/39524)|
|   | ref/appliance-command-reference/status | [Appliance command reference - status](https://discourse.ubuntu.com/t/39527)|
|   | ref/appliance-command-reference/upgrade | [Appliance command reference - upgrade](https://discourse.ubuntu.com/t/39528)|
|   | ref/amc-command-reference/addon | [AMC command reference - addon](https://discourse.ubuntu.com/t/40775) |
|   | ref/amc-command-reference/application | [AMC command reference - application](https://discourse.ubuntu.com/t/40776) |
|   | ref/amc-command-reference/benchmark | [AMC command reference - benchmark](https://discourse.ubuntu.com/t/40777) |
|   | ref/amc-command-reference/completion | [AMC command reference - completion](https://discourse.ubuntu.com/t/40778) |
|   | ref/amc-command-reference/config | [AMC command reference - config](https://discourse.ubuntu.com/t/40779) |
|   | ref/amc-command-reference/delete | [AMC command reference - delete](https://discourse.ubuntu.com/t/40780) |
|   | ref/amc-command-reference/exec | [AMC command reference - exec](https://discourse.ubuntu.com/t/40781) |
|   | ref/amc-command-reference/help | [AMC command reference - help](https://discourse.ubuntu.com/t/40782) |
|   | ref/amc-command-reference/image | [AMC command reference - image](https://discourse.ubuntu.com/t/40783) |
|   | ref/amc-command-reference/info | [AMC command reference - info](https://discourse.ubuntu.com/t/40784) |
|   | ref/amc-command-reference/init | [AMC command reference - init](https://discourse.ubuntu.com/t/40785) |
|   | ref/amc-command-reference/launch | [AMC command reference - launch](https://discourse.ubuntu.com/t/40786) |
|   | ref/amc-command-reference/list | [AMC command reference - list](https://discourse.ubuntu.com/t/40787) |
|   | ref/amc-command-reference/logs | [AMC command reference - logs](https://discourse.ubuntu.com/t/40788) |
|   | ref/amc-command-reference/node | [AMC command reference - node](https://discourse.ubuntu.com/t/40789) |
|   | ref/amc-command-reference/remote | [AMC command reference - remote](https://discourse.ubuntu.com/t/40790) |
|   | ref/amc-command-reference/shell | [AMC command reference - shell](https://discourse.ubuntu.com/t/40791) |
|   | ref/amc-command-reference/show-log | [AMC command reference - show-log](https://discourse.ubuntu.com/t/40792) |
|   | ref/amc-command-reference/show | [AMC command reference - show](https://discourse.ubuntu.com/t/40793) |
|   | ref/amc-command-reference/start | [AMC command reference - start](https://discourse.ubuntu.com/t/40794) |
|   | ref/amc-command-reference/stop | [AMC command reference - stop](https://discourse.ubuntu.com/t/40795) |
|   | ref/amc-command-reference/wait | [AMC command reference - wait](https://discourse.ubuntu.com/t/40796) |
[/details]

## Redirects

[details=Mapping table]
| Path | Location |
| ---- | -------- |
| /docs/manage/container-access | /docs/howto/instance/access |
| /docs/howto/container/view-log | /docs/howto/instance/logs |
| /docs/usage/usecase-container-configuration | /docs/howto/instance/geographic-location |
| /docs/howto/containers/backup-and-restore | /docs/howto/instance/backup-and-restore |
| /docs/exp/gpu-support | /docs/exp/gpus-instances |
| /docs/howto/container/launch | /docs/howto/instance/create |
| /docs/howto/stream/debug | /docs/howto/troubleshoot/streaming-issues |
| /docs/howto/manage/web-dashboard | /docs/howto/dashboard/web-dashboard |
| /docs/howto/manage/logs | /docs/howto/troubleshoot/logs |
| /docs/ref/platforms | /docs/exp/platforms |
| /docs/ref/instance-types | /docs/ref/application-manifest |
| /docs/ref/supported-video-codecs | /docs/ref/supported-codecs |
| /docs/howto/addons/best-practices | /docs/exp/addons |
| /docs/ref/addons | /docs/ref/addon-manifest |
| /docs/howto/manage/manage-appliance | /docs/ref/appliance-command-reference/landing |
| /docs/exp/containers | /docs/exp/instances |
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
| /docs/howto/application/resources | /docs/exp/resources |
[/details]

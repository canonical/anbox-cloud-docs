(ref-ams-configuration)=
# AMS configuration

The Anbox Management Service (AMS) provides various configuration items to customise its behaviour. The following table lists the available configuration items and their meaning.

| Name<br/>*(Type, Default)* | Description           |
|-----|-----------------------|
| `agent.api.fingerprint`<br/>*(string, N/A)*  | Fingerprint of certificate in the AMS trust store which is trusted when communicating with the stream agent. |
| `agent.api.token`<br/>*(string, N/A)* | Token to be used for API authentication with stream agent. |
| `agent.api.url`<br/>*(string, N/A)* | URL for stream agent API endpoint. |
| `application.addons`<br/>*(string, N/A)* | Comma-separated list of addons that every application managed by AMS will use. See {ref}`howto-enable-addons-globally`. |
| `application.auto_publish`<br/>*(bool, `true`)* | If set to `true`, AMS automatically published new application versions when the bootstrap process is finished. `false` disables this. See {ref}`sec-publish-app-versions`. |
| `application.auto_update`<br/>*(bool, `true`)* | If set to `true`, AMS automatically updates applications whenever any dependencies (parent image, addons, global configuration) change. `false` disables this. See {ref}`sec-configure-automatic-app-updates`. |
| `application.default_abi`<br/>*(string, N/A)* | Default Android ABI that applications should use. See [Android ABIs](https://developer.android.com/ndk/guides/abis) for a list of available ABIs. |
| `application.max_published_versions`<br/>*(integer, `3`)* | Maximum number of published versions per application. If the number of versions of an application exceeds this configuration, AMS will automatically clean up older versions. |
| `container.apt_mirror`<br/>*(string,<br/>`http://archive.ubuntu.com` (AMD64)<br/> `http://ports.ubuntu.com` (ARM64))*<br/>*(Deprecated)* | APT mirror to use within the containers. This configuration item is deprecated since 1.20, use `instance.apt_mirror` instead. |
| `container.default_platform`<br/>*(string, N/A)*<br/>*(Deprecated)* | The name of the platform that Anbox Cloud uses by default to launch containers. This configuration item is deprecated since 1.20, use `instance.default_platform` instead. |
| `container.features`<br/>*(string, N/A)*<br/>*(Deprecated)* | Comma-separated list of features to enable (see list below). This configuration item is deprecated since 1.20, use `instance.features` instead. |
| `container.network_proxy`<br/>*(string, N/A)*<br/>*(Deprecated)* | Network proxy to use inside the containers. This configuration item is deprecated since 1.20, use `instance.network_proxy` instead. |
| `container.security_updates`<br/>*(bool, `true`)*<br/>*(Deprecated)* | If set to `true`, automatic Ubuntu security updates are applied during the application bootstrap process. `false` disables this. |
| `core.proxy_http`<br/>*(string, N/A)* | HTTP proxy to use for HTTP requests that AMS performs. |
| `core.proxy_https`<br/>*(string, N/A)* | HTTPS proxy to use for HTTPS requests that AMS performs. |
| `core.proxy_ignore_hosts`<br/>*(string, N/A)* | Comma-separated list that defines the hosts for which a configured proxy is not used. |
| `core.trust_password`<br/>*(string, N/A)* | The AMS trust password. |
| `cpu.limit_mode`<br/>*(string, `scheduler`)* | The mode AMS uses to limit CPU access for an instance. See {ref}`exp-performance` for details. Possible values are: `scheduler`, `pinning` |
| `gpu.allocation_mode`<br/>*(string, `all`)* | Method of allocating GPUs: `all` tells AMS to allocate all available GPUs on a system to an instance. `single` allocates only a single GPU. |
| `gpu.type`<br/>*(string, `none`)* | Type of GPU: `none`, `intel`, `nvidia`, `amd` |
| `images.allow_insecure`<br/>*(bool, `false`)* | If set to `true`, AMS allows accepting untrusted certificates provided by the configured image server. |
| `images.auth`<br/>*(string, N/A)* | Authentication details for AMS to access the image server. When reading this configuration, a Boolean value that indicates whether the item is set is returned, to avoid exposing credentials. |
| `images.update_interval`<br/>*(string, `5m`)* | Frequency of image updates (for example: 1h, 30m). |
| `images.url`<br/>*(string, `https://images.anbox-cloud.io/stable/`)*  | URL of the image server to use. |
| `images.version_lockstep`<br/>*(bool, `true`)*  | Whether to put the version of the latest pulled image and the AMS version in a lockstep. This ensures that a deployment is not automatically updated to newer image versions if AMS is still at an older version. This only applies for new major and minor but not patch version updates. |
| `instance.apt_mirror`<br/>*(string,<br/>`http://archive.ubuntu.com` (AMD64) `http://ports.ubuntu.com` (ARM64))*   | APT mirror to use within the instances. |
| `instance.default_platform`<br/>*(string, N/A)*  | The name of the platform that Anbox Cloud uses by default to launch instances. |
| `instance.features`<br/>*(string, N/A)*  | Comma-separated list of features to enable (see list below). |
| `instance.network_proxy`<br/>*(string, N/A)* | Network proxy to use inside the instances. |
| `instance.security_updates`<br/>*(bool, `true`)*  | If set to `true`, automatic Ubuntu security updates are applied during the application bootstrap process. `false` disables this. This configuration item is deprecated since 1.20, use `instance.security_updates` instead. |
| `load_balancer.url`<br/>*(string, N/A)* | URL of the load balancer behind which AMS sits. The URL is handed to instances started by AMS to allow them to contact AMS through the load balancer and not via the address of an individual AMS instance. |
| `node.queue_size`<br/>*(integer, `100`)*  | Maximum size of the queue containing requests to start and stop instances per LXD node. Changing the value requires a restart of AMS. |
| `node.workers_per_queue`<br/>*(integer, `4`)*  | Number of workers processing instance start and stop requests. Changing the value requires a restart of AMS. |
| `registry.filter`<br/>*(string, N/A)*  | Comma-separated list of tags to filter for when applications are fetched from the {ref}`exp-aar`. If empty, no filter is applied. |
| `registry.fingerprint`<br/>*(string, N/A)*  | Fingerprint of the certificate that the {ref}`exp-aar` uses to TLS-secure its HTTPS endpoint. This is used by AMS for mutual TLS authentication with the registry. |
| `registry.mode`<br/>*(string, `pull`)*  | Mode in which the {ref}`exp-aar` client in AMS operates: `manual`, `pull`, `push` |
| `registry.update_interval`<br/>*(string, `1h`)*  | Frequency of {ref}`exp-aar` updates (for example: 1h, 30m). |
| `registry.url`<br/>*(string, N/A)*  | URL of the {ref}`exp-aar` to use. |
| `scheduler.strategy`<br/>*(string, `spread`)*  | Strategy that the internal instance scheduler in AMS uses to distribute instances across available LXD nodes: `binpack`, `spread` |

(sec-node-configuration)=
## Node-specific configuration

In a cluster setup, there are configuration items that can be customised for each node. The following table lists the available configuration items and their meaning.

| Name<br/>*(Type, Default)* |  Description            |
|--------------------------|-------------------------|
| `cpu-allocation-rate`<br/>*(integer, `4`)* | CPU allocation rate used for over-committing resources.  See {ref}`sec-over-committing`. |
| `cpus`<br/>*(integer, all available)* | Number of CPUs dedicated to instances. |
| `gpu-encoder-slots`<br/>*(integer, <br/>`0` for nodes without GPU or with AMD GPU<br/>`32` for nodes with NVIDIA GPU<br/>`10` for nodes with Intel GPU)* | Number of GPU encoder slots available on the node. |
| `gpu-slots`<br/>*(integer,<br/> `0` for nodes without GPU<br/>`32` for nodes with NVIDIA GPU<br/>`10` for nodes with AMD or Intel GPU)* | Number of GPU slots available on the node. See {ref}`sec-gpu-slots`. |
| `memory`<br/>*(integer, all available)* | Memory dedicated to instances. |
| `memory-allocation-rate`<br/>*(integer, `2`)* | Memory allocation rate used for over-committing resources.  See {ref}`sec-over-committing`. |
| `public-address`<br/>*(string, N/A)*| The public, reachable address of the node. |
| `subnet`<br/>*(string, N/A)* | The network subnet of the machine where the node runs. |
| `tags`<br/>*(string, N/A)*| Tags to identify the node. |
| `unschedulable`<br/>*(bool, `false`)* | When set to `true`, the node cannot be scheduled, which prevents new instances from being launched on it. |

See {ref}`howto-configure-cluster-nodes` for instructions on how to set these configuration items.

## Objects managed by AMS

AMS manages various objects such as applications, images, instances, nodes and addons. 

The object names must adhere to the following criteria:

* Minimum character limit: 3
* Maximum character limit: 255
* Can contain:
  - Alphabets (a-z, A-Z)
  - Numbers (0-9)
  - Allowed special characters: `-` (hyphen), `_` (underscore), `:` (colon), `.` (period).

When you create an instance, the same criteria apply to the following options as well:

* `boot_activity`
* `platform`
* `boot_package`

The object ids are generated by AMS and have a length of 20 characters.


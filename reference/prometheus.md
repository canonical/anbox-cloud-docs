(ref-prometheus-metrics)=
# Prometheus metrics

Anbox Cloud gathers various performance metrics that you can access through API endpoints.

The following sections list all metrics for each service endpoint.

## AMS

The Anbox Management Service provides metrics about the Anbox Cloud cluster (or the Anbox Cloud Application server) and the AMS API access.

### Objects

Metrics prefixed with `ams_cluster_` keep you informed about the status of your Anbox Cloud cluster.

| Name                                             | Description                                   | Status    |
|--------------------------------------------------|-----------------------------------------------|-----------|
| `ams_cluster_nodes_total`                        | Number of nodes in the cluster                | Available since 1.0.0 |
| `ams_cluster_applications_total`                 | Number of applications                        | Available since 1.0.0 |
| `ams_cluster_containers_total`                   | Number of containers currently in the cluster | Deprecated since 1.20.0, use `ams_cluster_instances_total` instead. |
| `ams_cluster_container_boot_time_seconds_count`  | Number of container boot time measured     | Deprecated since 1.20.0, use `ams_cluster_instance_boot_time_seconds_count` instead. |
| `ams_cluster_container_boot_time_seconds_sum`    | Sum of all container boot times and can be used to compute the average boot time |  Deprecated since 1.20.0, use `ams_cluster_instance_boot_time_seconds_sum` instead. |
| `ams_cluster_container_boot_time_seconds_bucket` | Container boot times bucket and can be used for alerting when above a threshold; see the [Prometheus documentation](https://prometheus.io/docs/practices/histograms/) for more information |  Deprecated since 1.20.0, use `ams_cluster_instance_boot_time_seconds_bucket` instead. |
| `ams_cluster_containers_per_application_total`   | Number of containers per application  | Deprecated since 1.20.0, use `ams_cluster_instances_per_application_total` instead. |
| `ams_cluster_containers_per_status_total`        | Number of containers per container status |  Deprecated since 1.20.0, use `ams_cluster_instances_per_status_total` instead. |
| `ams_cluster_containers_per_node_total`          | Number of containers per worker node |  Deprecated since 1.20.0, use `ams_cluster_instances_per_node_total` instead. |
| `ams_cluster_instances_total`                    | Number of instances currently in the cluster | Available since 1.20.0 |
| `ams_cluster_instance_boot_time_seconds_count`   | Number of instance boot time measured        | Available since 1.20.0 |
| `ams_cluster_instance_boot_time_seconds_sum`     | Sum of all instance boot times (can be used to compute the average boot time) |  Available since 1.20.0 |
| `ams_cluster_instance_boot_time_seconds_bucket`  | Instance boot times bucket (can be used for alerting when above a threshold; see the [Prometheus documentation](https://prometheus.io/docs/practices/histograms/) for more information) |  Available since 1.20.0 |
| `ams_cluster_instances_per_application_total`    | Number of instances per application          |  Available since 1.20.0 |
| `ams_cluster_instances_per_status_total`         | Number of instances per instance status     | Available since 1.20.0 |
| `ams_cluster_instances_per_node_total`           | Number of instances per worker node         |  Available since 1.20.0 |
| `ams_cluster_available_cpu_total`                | Total CPUs available in each worker node      | Available since 1.0.0 |
| `ams_cluster_used_cpu_total`                     | Used CPUs in each worker node                 | Available since 1.0.0 |
| `ams_cluster_available_memory_total`             | Total memory available in each worker node    | Available since 1.0.0 |
| `ams_cluster_used_memory_total`                  | Used memory in each worker node               | Available since 1.0.0 |

### API usage

Metrics prefixed with `ams_http_` allow to track access to the API.

These metrics are available since Anbox Cloud 1.10.0.

| Name                                       | Description                                           |
|--------------------------------------------|-------------------------------------------------------|
| `ams_http_in_flight_requests`              | Number of HTTP requests being processed at the moment |
| `ams_http_request_duration_seconds_bucket` | The HTTP request latency in seconds                   |
| `ams_http_request_size_bytes_bucket`       | The HTTP request size in bytes                        |
| `ams_http_requests_total`                  | Total number of HTTP requests made                    |
| `ams_http_response_size_bytes_bucket`      | The HTTP response sizes in bytes                      |

#### API handlers

To give a more granular approach to monitoring, the AMS API metrics contain handlers that identify the kind of API access.

The AMS API can be accessed through HTTP/HTTPS or a Unix domain socket. Therefore, the API metrics distinguish between `http`, `https` and `unix`. For example:

    ams_http_request_duration_seconds_bucket{handler="http_applications_GET",host="juju-2db13b-1",method="get",le="0.5"} 1
    ams_http_request_duration_seconds_bucket{handler="https_applications_GET",host="juju-2db13b-1",method="get",le="0.5"} 1
    ams_http_request_duration_seconds_bucket{handler="unix_applications_GET",host="juju-2db13b-1",method="get",le="0.5"} 1

All handler labels adopt the convention `<transport method>_<object>_<http method>`, for example, `unix_containers_POST`.

The following table contains all routes and their corresponding labels (ignoring the communication method prefix).

| Method  | Route                                       | Label                              |
|---------|---------------------------------------------|------------------------------------|
| `GET`   | `/1.0`                                      | `service_GET`                      |
| `GET`   | `/1.0/addons`                               | `addons_GET`                       |
| `POST`  | `/1.0/addons`                               | `addons_POST`                      |
| `GET`   | `/1.0/addons/<id>`                          | `addon_GET`                        |
| `PATCH` | `/1.0/addons/<id>`                          | `addon_PATCH`                      |
| `DELETE`| `/1.0/addons/<id>`                          | `addon_DELETE`                     |
| `DELETE`| `/1.0/addons/<id>/<version>`                | `addon_version_DELETE`             |
| `GET`   | `/1.0/applications`                         | `applications_GET`                 |
| `POST`  | `/1.0/applications`                         | `applications_POST`                |
| `GET`   | `/1.0/applications/<id>`                    | `application_GET`                  |
| `PATCH` | `/1.0/applications/<id>`                    | `application_PATCH`                |
| `DELETE`| `/1.0/applications/<id>`                    | `application_DELETE`               |
| `GET`   | `/1.0/applications/<id>/<version>`          | `application_version_GET`          |
| `PATCH` | `/1.0/applications/<id>/<version>`          | `application_version_PATCH`        |
| `DELETE`| `/1.0/applications/<id>/<version>`          | `application_version_DELETE`       |
| `GET`   | `/1.0/applications/<id>/manifest`           | `application_manifest_GET`         |
| `GET`   | `/1.0/applications/<id>/<version>/manifest` | `application_version_manifest_GET` |
| `GET`   | `/1.0/containers`                           | `containers_GET` (Deprecated)      |
| `POST`  | `/1.0/containers`                           | `containers_POST` (Deprecated)     |
| `GET`   | `/1.0/containers/<id>`                      | `container_GET` (Deprecated)       |
| `DELETE`| `/1.0/containers/<id>`                      | `container_DELETE` (Deprecated)    |
| `POST`  | `/1.0/containers/<id>/exec`                 | `container_exec_POST` (Deprecated) |
| `GET`   | `/1.0/containers/<id>/logs`                 | `container_logs_GET` (Deprecated)  |
| `GET`   | `/1.0/containers/<id>/logs/<name>`          | `container_log_GET` (Deprecated)   |
| `GET`   | `/1.0/instances`                            | `instances_GET`                    |
| `POST`  | `/1.0/instances`                            | `instances_POST`                   |
| `GET`   | `/1.0/instances/<id>`                       | `instance_GET`                     |
| `DELETE`| `/1.0/instances/<id>`                       | `instance_DELETE`                  |
| `POST`  | `/1.0/instances/<id>/exec`                  | `instance_exec_POST`               |
| `GET`   | `/1.0/instances/<id>/logs`                  | `instance_logs_GET`                |
| `GET`   | `/1.0/instances/<id>/logs/<name>`           | `instance_log_GET`                 |
| `GET`   | `/1.0/version`                              | `version_GET`                      |
| `GET`   | `/1.0/nodes`                                | `nodes_GET`                        |
| `POST`  | `/1.0/nodes`                                | `nodes_POST`                       |
| `GET`   | `/1.0/nodes/<id>`                           | `node_GET`                         |
| `PATCH` | `/1.0/nodes/<id>`                           | `node_PATCH`                       |
| `DELETE`| `/1.0/nodes/<id>`                           | `node_DELETE`                      |
| `GET`   | `/1.0/images`                               | `images_GET`                       |
| `POST`  | `/1.0/images`                               | `images_POST`                      |
| `GET`   | `/1.0/images/<id>`                          | `image_GET`                        |
| `PATCH` | `/1.0/images/<id>`                          | `image_PATCH`                      |
| `DELETE`| `/1.0/images/<id>`                          | `image_DELETE`                     |
| `DELETE`| `/1.0/images/<id>/<version>`                | `image_version_DELETE`             |
| `GET`   | `/1.0/config`                               | `config_GET`                       |
| `PATCH` | `/1.0/config`                               | `config_PATCH`                     |
| `GET`   | `/1.0/tasks`                                | `tasks_GET`                        |
| `GET`   | `/1.0/registry/applications`                | `registry_applications_GET`        |
| `DELETE`| `/1.0/registry/applications/<id>`           | `registry_application_DELETE`      |
| `POST`  | `/1.0/registry/applications/<id>/push`      | `registry_application_push_POST`   |
| `POST`  | `/1.0/registry/applications/<id>/pull`      | `registry_application_pull_POST`   |
| `GET`   | `/1.0/artifacts/<id>`                       | `internal_artifacts_GET`           |
| `PATCH` | `/1.0/containers/<id>`                      | `internal_containers_PATCH` (Deprecated)|
| `PATCH` | `/1.0/instances/<id>`                       | `internal_instances_PATCH`         |


## Anbox Stream Gateway

The Anbox Stream Gateway provides metrics about the streaming activities of your cluster or server and the Anbox Stream Gateway API access.

### Objects

Metrics prefixed with `anbox_stream_gateway_` give information about your cluster related to streaming, for example, the number of sessions and agents.

These metrics are available since Anbox Cloud 1.7.2.

| Name                                       | Description                                     |
|--------------------------------------------|-------------------------------------------------|
| `anbox_stream_gateway_sessions_total`      | Total number of sessions, categorized by status |
| `anbox_stream_gateway_accounts_total`      | Total number of accounts                        |
| `anbox_stream_gateway_agents_total`        | Number of active agents                         |
| `anbox_stream_gateway_agents_unresponsive` | Number of unresponsive agents                   |

### API usage

Metrics prefixed with `anbox_stream_gateway_http_` allow to track access to the streaming API.

These metrics are available since Anbox Cloud 1.9.0.

| Name                                                        | Description                                           |
|-------------------------------------------------------------|-------------------------------------------------------|
| `anbox_stream_gateway_http_in_flight_requests`              | Number of HTTP requests being processed at the moment |
| `anbox_stream_gateway_http_request_duration_seconds_bucket` | The HTTP request latency in seconds                   |
| `anbox_stream_gateway_http_request_size_bytes_bucket`       | The HTTP request size in bytes                        |
| `anbox_stream_gateway_http_requests_total`                  | Total number of HTTP requests made                    |
| `anbox_stream_gateway_http_response_size_bytes_bucket`      | The HTTP response sizes in bytes                      |

#### API handlers

To give a more granular approach to monitoring, the Anbox Stream Gateway API metrics contain handlers that identify the route that is accessed. The routes are indicated in the handler labels. For example:

    anbox_stream_gateway_http_request_duration_seconds_bucket{handler="get_sessions",host="juju-2db13b-1",method="get",le="0.5"} 1

In this case, the label for the route is `get_sessions`.

The following table contains all routes and their corresponding labels.

| Method   | Route                               | Label                        |
|----------|-------------------------------------|------------------------------|
| `GET`    | `/1.0/status`                       | `get_service_status`         |
| `POST`   | `/1.0/sessions`                     | `create_new_session`         |
| `GET`    | `/1.0/sessions`                     | `get_sessions`               |
| `GET`    | `/1.0/sessions/<id>`                | `get_session`                |
| `DELETE` | `/1.0/sessions/<id>`                | `delete_session`             |
| `DELETE` | `/1.0/sessions`                     | `delete_sessions`            |
| `POST`   | `/1.0/sessions/<id>/join`           | `join_session`               |
| `GET`    | `/1.0/sessions/<id>/sockets/master` | `streaming_websocket_master`  <!-- wokeignore:rule=master --> |
| `GET`    | `/1.0/sessions/<id>/sockets/slave`  | `streaming_websocket_slave`  <!-- wokeignore:rule=slave -->  |
| `GET`    | `/1.0/applications`                 | `get_applications`           |
| `GET`    | `/1.0/regions`                      | `get_regions`                |


## Anbox Runtime metrics

For every instance running inside Anbox Cloud, the Anbox runtime provides a set of metrics.

### Graphics

| Name                                                        | Type      | Description                               |
|-------------------------------------------------------------|-----------|-------------------------------------------|
| `anbox_gralloc_buffer_allocations_total`                    | Counter   | Total number of buffer allocations |
| `anbox_vulkan_buffer_memory_size_total`                     | Counter   | Total memory in bytes allocated for graphics buffers through Vulkan |
| `anbox_system_buffer_memory_size_total`                     | Counter   | Total memory in bytes allocated for graphics buffers from system memory |
| `anbox_webrtc_frame_renderer_latency`                       | Histogram | Latency in ms of frames processed by the frame renderer since were submitted |
| `anbox_webrtc_nvidia_packets_per_encoded_frame`             | Histogram | Number of packets per encoded frame |
| `anbox_webrtc_nvidia_bytes_per_encoded_frame`               | Histogram | Number of bytes per encoded frame |

### WebRTC

Metrics prefixed with `webrtc_` give you detailed insight about the WebRTC protocol for every streaming instance. See the [official W3C reference](https://www.w3.org/TR/webrtc-stats) for more information.

These metrics are available since Anbox Cloud 1.8.0.

| Name                                | Description                                                                                                |
|-------------------------------------|------------------------------------------------------------------------------------------------------------|
| `webrtc_frames_encoded`             | Total number of frames successfully encoded                                                                |
| `webrtc_key_frames_encoded`         | Total number of key frames, such as key frames in VP8 or IDR-frames in H.264 (`webrtc_key_frames_encoded - webrtc_frames_encoded` gives the number of delta frames) |
| `webrtc_total_encode_time`          | Total number of seconds that has been spent encoding the `webrtc_frames_encoded` frames (the average encode time can be calculated by dividing this value with `webrtc_frames_encoded`) |
| `webrtc_target_bitrate`             | The current encoder target in bits per second                                                              |
| `webrtc_bytes_sent`                 | Total number of bytes sent for a specific [SSRC](https://tools.ietf.org/html/rfc3550#section-3) (a SSRC represents one resource - video, audio or binary data - sent over a WebRTC track) |
| `webrtc_retransmitted_bytes_sent`   | Total number of bytes that were re-transmitted for a specific SSRC, only including payload bytes           |
| `webrtc_retransmitted_packets_sent` | Total number of packets that were re-transmitted for a specific SSRC                                       |
| `webrtc_total_packet_send_delay`    | Total number of seconds that packets have spent buffered locally before being transmitted onto the network |
| `webrtc_packets_sent`               | Total number of RTP packets sent for this SSRC (includes re-transmissions)                                 |
| `webrtc_nack_count`                 | Total number of Negative Acknowledgment (NACK) packets received by this sender                            |
| `webrtc_fir_count`                  | Total number of Full Intra Request (FIR) packets received by this sender (video only)                      |
| `webrtc_pli_count`                  | Total number of Picture Loss Indication (PLI) packets received by this sender (video only)                 |
| `webrtc_sli_count`                  | Total number of Slice Loss Indication (SLI) packets received by this sender (video only)                   |
| `webrtc_relay_in_use`               | Boolean value indicating if a relay ICE candidate type is in use for the stream                            |

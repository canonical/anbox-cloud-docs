Anbox Cloud gathers various performance metrics and makes them accessible through API endpoints. While Anbox Cloud does not provide its own observability solution, it supports implementing and integrating custom solutions for monitoring performance.

See [Prometheus metrics](https://discourse.ubuntu.com/t/prometheus-metrics/19521) for a list of available metrics and how to access them. [LXD Metric exporter for instances](https://discuss.linuxcontainers.org/t/lxd-metric-exporter-for-instances/11735) has a list of metrics available through LXD.

The implementation of a monitoring or observability solution depends on your specific use case and the tools that you want to use. See [Open source observability for enterprises](https://ubuntu.com/observability) for an overview of observability tools and stacks that are recommended and supported by Canonical.

The [How to monitor Anbox Cloud using COS](tbd) guide helps you to implement an observability solution by using the Canonical Observability Stack(COS).

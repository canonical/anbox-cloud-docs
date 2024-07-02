(howto-monitor-anbox)=
# How to monitor Anbox Cloud

Anbox Cloud gathers various performance metrics and makes them accessible through API endpoints. While Anbox Cloud does not provide its own observability solution, it supports implementing and integrating custom solutions for monitoring performance.

See {ref}`ref-prometheus-metrics` for a list of available metrics and how to access them. [LXD Metric exporter for instances](https://discuss.linuxcontainers.org/t/lxd-metric-exporter-for-instances/11735) has a list of metrics available through LXD.

The implementation of a monitoring or observability solution depends on your specific use case and the tools that you want to use. See [Open source observability for enterprises](https://ubuntu.com/observability) for an overview of observability tools and stacks that are recommended and supported by Canonical. In particular, see the [Canonical Observability Stack (LMA2)](https://juju.is/docs/lma2).

There are plans in the Anbox Cloud roadmap to provide better monitoring abilities by using the [Canonical Observability Stack](https://charmhub.io/topics/canonical-observability-stack).

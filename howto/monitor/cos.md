Anbox Cloud uses [Canonical Observability Stack(COS)](https://charmhub.io/topics/canonical-observability-stack) to enable users to collect and monitor their workloads.

Since Anbox Cloud uses Juju for deployment, by supporting [COS Lite](https://charmhub.io/topics/canonical-observability-stack/editions/lite) integration, we can export observability information with Prometheus, Loki and Grafana.

Currently, only the [AMS charm](https://charmhub.io/ams) supports COS Lite integration. To gather observability metrics for the AMS charm,

1. Deploy the COS Lite bundle. See the [COS Lite tutorial](https://charmhub.io/topics/canonical-observability-stack/tutorials/install-microk8s) for instructions.
2. Deploy the AMS charm as described in the [Instrumenting machine charms](https://charmhub.io/topics/canonical-observability-stack/tutorials/instrumenting-machine-charms) tutorial.

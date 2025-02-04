(howto-monitor-anbox)=
# How to monitor Anbox Cloud

Anbox Cloud collects various metrics and makes them accessible through API endpoints. While Anbox Cloud does not provide its own observability solution, it supports integrating with external solutions.

You can find a list of available metrics at {ref}`ref-prometheus-metrics`.

## Access metrics with the appliance

The Anbox Cloud Appliance provides a central metrics endpoint which aggregates metrics from all internal services and Anbox instances.

If you haven't enabled collecting metrics when initializing the appliance, run:

    sudo anbox-cloud-appliance enable metrics

If you want to disable collecting metrics, run:

    sudo anbox-cloud-appliance disable metrics

To retrieve the metrics in the [Prometheus data format](https://prometheus.io/docs/concepts/data_model/), run:

    sudo anbox-cloud-appliance config show

The output will list a `metrics.url` along with the TLS certificate of the endpoint referred by the URL. This certificate should be used to establish a secure and authenticated connection.

You can either configure a Prometheus instance to scrape the endpoint or manually retrieve the metrics via `curl`, for example

    # We need yq in order to parse and process the YAML output
    sudo apt install  -y yq jq

    metrics_url="$(sudo anbox-cloud-appliance config show | yq .metrics.url)"
    sudo anbox-cloud-appliance config show | yq .metrics.tls.certificate > metrics.pem
    curl --cacert ./metrics.pem "$metrics_url"


You will see all available metrics as output, including metrics for the individual Anbox instances.

(howto-monitor-anbox)=
# How to monitor Anbox Cloud

Anbox Cloud collects various metrics and makes them accessible through API endpoints. While Anbox Cloud does not provide its own observability solution, it supports integrating with external solutions.

You can find a list of available metrics at {ref}`ref-prometheus-metrics`.

## Access metrics with the appliance

The Anbox Cloud Appliance provides a central metrics endpoint which aggregates metrics from all internal services and Anbox instances.

If you haven't enabled metrics support at initialization time, you can do that now by running

    sudo anbox-cloud-appliance enable metrics

If you want to disable metrics again you can run

    sudo anbox-cloud-appliance disable metrics

Afterwards you can find the URL which you can use to retrieve the metrics in the [Prometheus data format](https://prometheus.io/docs/concepts/data_model/).

    sudo anbox-cloud-appliance config show

The output will list a `metrics.url` field which provides you the URL. The output will also provide the TLS certificate of the the endpoint the URL points to. This should be used to establish a secure and authenticated connection.

You can either configure a Prometheus instance to scrape the endpoint or manually retrieve the metrics via `curl`, for example

    # We need q in order to parse and process the YAML output
    sudo apt install  -y yq jq

    metrics_url="$(sudo anbox-cloud-appliance config show | yq .metrics.url)"
    sudo anbox-cloud-appliance config show | yq .metrics.tls.certificate > metrics.pem
    curl --cacert ./metrics.pem "$metrics_url"


As output you will see all available metrics, include metrics for the individual Anbox instances.

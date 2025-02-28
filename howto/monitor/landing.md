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

## Access metrics with a charmed Anbox Cloud

### Prerequisites
To collect and access metrics with a charmed deployment of Anbox Cloud, you need to have the [Canonical Observability Stack (COS)](https://charmhub.io/topics/canonical-observability-stack) installed.

The following steps describe a sample setup of COS, you should adjust it for your setup. For further information and recommendation, see the [official COS documentation](https://charmhub.io/topics/canonical-observability-stack/tutorials/install-microk8s).

First, deploy [MicroK8s](https://microk8s.io/) into a separate model on an existing Juju controller:

    juju add-model k8s
    juju deploy microk8s --base=ubuntu@22.04 --channel=edge --constraints="virt-type=virtual-machine cores=4 mem=6G root-disk=80G"

Once the deployment has completed, configure MicroK8s to host COS:

    juju ssh microk8s/0 -- sudo microk8s enable dns hostpath-storage
    juju ssh microk8s/0 -- sudo apt install -y jq
    IPADDR=$(juju ssh microk8s/0 -- ip -4 -j route get 2.2.2.2 | jq -r '.[] | .prefsrc')
    juju ssh microk8s/0 -- sudo microk8s enable metallb:$IPADDR-$IPADDR

Now that MicroK8s is ready, register it with the Juju controller:

    juju ssh microk8s/0 -- sudo microk8s config | juju add-k8s devk8s --controller dev

Finally, deploy COS:

    juju add-model cos devk8s
    curl -o offers.yaml -L https://raw.githubusercontent.com/canonical/cos-lite-bundle/refs/heads/main/overlays/offers-overlay.yaml
    curl -o storage.yaml -L https://raw.githubusercontent.com/canonical/cos-lite-bundle/refs/heads/main/overlays/storage-small-overlay.yaml
    juju deploy cos-lite --trust --overlay ./offers.yaml --overlay ./storage.yaml

To have an Anbox Cloud specific dashboard and alert rules, deploy the relevant configuration charm:

    juju deploy anbox-cloud-cos-configuration
    juju relate anbox-cloud-cos-configuration:grafana-dashboard grafana:grafana-dashboard

The deployment will take a while and you can use `juju status` to monitor the current status.

After the deployment has finished, you will need the Grafana endpoint and password for the `admin` user. To find these credentials, run:

    juju run grafana/leader get-admin-password --model cos

The next step is to integrate COS with Anbox Cloud by deploying the [Grafana Agent charm](https://charmhub.io/grafana-agent) to the model in which Anbox Cloud is deployed. In the following steps, we assume that the model is named `anbox-cloud`.

    juju switch anbox-cloud
    juju depoy grafana-agent
    juju relate ams:cos-agent grafana-agent:cos-agent
    juju relate anbox-stream-gateway:cos-agent grafana-agent:cos-agent

To connect `grafana-agent` with COS, establish the necessary Juju relations:

    juju consume admin/cos.prometheus-receive-remote-write
    juju relate grafana-agent prometheus-receive-remote-write
    juju consume admin/cos.loki-logging
    juju relate grafana-agent loki-logging
    juju consume admin/cos.grafana-dashboards
    juju relate grafana-agent grafana-dashboards

Once all relations are established, the Anbox Cloud dashboard is available within Grafana. You can access all metrics, including logs from the machines where the Grafana agent is deployed.

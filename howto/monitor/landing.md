(howto-monitor-anbox)=
# How to monitor Anbox Cloud

Anbox Cloud collects various metrics and makes them accessible through API endpoints. While Anbox Cloud does not provide its own observability solution, it supports integrating with external solutions.

You can find a list of available metrics at {ref}`ref-prometheus-metrics`.

## Enable metrics collection

Before you can monitor Anbox Cloud, you need to enable metrics collection in your deployment.

### For Anbox Cloud Appliance

If you haven't enabled collecting metrics when initializing the appliance, run:

```bash
sudo anbox-cloud-appliance enable metrics
```

If you want to disable collecting metrics, run:

```bash
sudo anbox-cloud-appliance disable metrics
```

### For Charmed Anbox Cloud

Metrics are enabled by default in Charmed Anbox Cloud. The AMS and Anbox Stream Gateway services expose their metrics via their respective endpoints.

## Access metrics directly

### With Anbox Cloud Appliance

The Anbox Cloud Appliance provides a central metrics endpoint which aggregates metrics from all internal services and Anbox instances.

To retrieve the metrics in the [Prometheus data format](https://prometheus.io/docs/concepts/data_model/), run:

```bash
sudo anbox-cloud-appliance config show
```

The output will list a `metrics.url` along with the TLS certificate of the endpoint. This certificate should be used to establish a secure and authenticated connection.

You can manually retrieve the metrics via `curl`, for example:

```bash
# We need yq in order to parse and process the YAML output
sudo apt install -y yq jq

metrics_url="$(sudo anbox-cloud-appliance config show | yq .metrics.url)"
sudo anbox-cloud-appliance config show | yq .metrics.tls.certificate > metrics.pem
curl --cacert ./metrics.pem "$metrics_url"
```

You will see all available metrics as output, including metrics for the individual Anbox instances.

### With Charmed Anbox Cloud

For Charmed Anbox Cloud, you can access metrics directly from each service. The AMS and Anbox Stream Gateway expose metrics on the `/metrics` endpoint.

First, get the IP addresses of the services:

```bash
# For AMS
AMS_IP=$(juju status ams --format json | jq -r '.applications.ams.units."ams/0"["public-address"]')
echo "AMS IP: $AMS_IP"

# For Anbox Stream Gateway
STREAM_GATEWAY_IP=$(juju status anbox-stream-gateway --format json | jq -r '.applications["anbox-stream-gateway"].units["anbox-stream-gateway/0"]["public-address"]')
echo "Anbox Stream Gateway IP: $STREAM_GATEWAY_IP"
```

You can then access the metrics in one of two ways:

1. If you have direct access to the services, use `curl` directly:

```bash
# For AMS
curl -k https://$AMS_IP:8444/metrics

# For Anbox Stream Gateway
curl -k https://$STREAM_GATEWAY_IP:4000/metrics
```

2. If you don't have direct access (e.g., when deployed on a public cloud), use SSH to tunnel the request:

```bash
# For AMS
juju ssh ams/0 -- curl -k -s https://$AMS_IP:8444/metrics

# For Anbox Stream Gateway
juju ssh anbox-stream-gateway/0 -- curl -k -s https://$STREAM_GATEWAY_IP:4000/metrics
```

Note that these endpoints may require authentication depending on your setup.

## Set up Canonical Observability Stack (COS)

For more comprehensive monitoring, you can use the [Canonical Observability Stack (COS)](https://charmhub.io/topics/canonical-observability-stack) with both Anbox Cloud Appliance and Charmed Anbox Cloud.

### Install COS

The following steps describe a sample setup of COS. Adjust it for your environment as needed. For further information, see the [official COS documentation](https://charmhub.io/topics/canonical-observability-stack/tutorials/install-microk8s) and the [documentation for Canonical K8s](https://documentation.ubuntu.com/canonical-kubernetes/latest/).

1. Deploy [Canonical K8s](https://ubuntu.com/kubernetes) into a separate model on an existing Juju controller:

   ```bash
   juju add-model k8s
   # This assumes you deploy on a LXD controller, adjust contraints
   # for your cloud provider as needed.
   juju deploy k8s --channel 1.32/stable --base "ubuntu@24.04" \
       --constraints="virt-type=virtual-machine cores=4 mem=6G root-disk=80G" \
       --config load-balancer-enabled=true
   ```

   Customize constraints as needed to match your underlying cloud and requirements.

2. Check the status of the deployment:

   ```bash
   juju status --watch 1s
   ```

3. Once the charm unit is reported active, customize its load balancer setup:

   ```bash
   sudo apt install -y jq
   addr="$(juju show-machine 0 --format json | jq -r '.machines[]."network-interfaces"[]."ip-addresses"[0]' | tail -n 1)"
   juju config k8s load-balancer-cidrs="$addr/32"
   ```

4. Register the K8s cluster with the Juju controller:

   ```bash
   juju run k8s/leader get-kubeconfig --format=json | jq -r '.[].results.kubeconfig' > kubeconfig
   KUBECONFIG=./kubeconfig juju add-k8s k8s-cloud
   ```

5. Deploy COS:

   ```bash
   juju add-model cos k8s-cloud
   curl -o offers.yaml -L https://raw.githubusercontent.com/canonical/cos-lite-bundle/refs/heads/main/overlays/offers-overlay.yaml
   curl -o storage.yaml -L https://raw.githubusercontent.com/canonical/cos-lite-bundle/refs/heads/main/overlays/storage-small-overlay.yaml
   juju deploy cos-lite --trust --overlay ./offers.yaml --overlay ./storage.yaml
   ```

6. Deploy the Anbox Cloud configuration charm for COS-specific dashboards and alerts:

   ```bash
   juju deploy --channel=1.25/stable anbox-cloud-cos-configuration
   juju relate anbox-cloud-cos-configuration:grafana-dashboard grafana:grafana-dashboard
   ```

7. Wait for the deployment to complete and check the status with `juju status`.

8. After the deployment is finished, get the Grafana endpoint and admin password:

   ```bash
   juju run grafana/leader get-admin-password --model cos
   ```

### Integrate COS with Anbox Cloud Appliance

To integrate COS with your Anbox Cloud Appliance, you can use the [prometheus-scrape-target-k8s](https://charmhub.io/prometheus-scrape-target-k8s) charm:

1. Switch to the COS model and get the metrics URL and certificate from your appliance:

   ```bash
   # Switch to the COS model
   juju switch cos

   # Get metrics URL and certificate
   sudo anbox-cloud-appliance config show
   ```

2. Extract the necessary information from the metrics URL. For example, if your metrics URL is:

   ```
   http://user:pass@10.1.0.10:9273/1.0/metrics
   ```

   You would extract:
   - `scheme`: `http`
   - `target`: `10.1.0.10:9273` (`hostname:port`)
   - `metrics_path`: `/1.0/metrics`
   - `basic_auth`: `user:pass`

3. Deploy the prometheus-scrape-target-k8s charm with the extracted values:

   ```bash
   juju deploy prometheus-scrape-target-k8s anbox-appliance-metrics \
     --config scheme=http \
     --config targets="10.1.0.10:9273" \
     --config metrics_path="/1.0/metrics" \
     --config basic_auth="user:pass" \
     --config tls_config_insecure_skip_verify=true

   # Relate to Prometheus
   juju relate anbox-appliance-metrics prometheus
   ```

4. Access the Grafana dashboard to view your metrics:

   ```bash
   juju status grafana
   juju run grafana/leader get-admin-password --model cos
   ```

### Integrate COS with Charmed Anbox Cloud

To integrate COS with Charmed Anbox Cloud:

1. Deploy the Grafana Agent charm to the model where Anbox Cloud is deployed:

   ```bash
   # Select the model where you have Anbox Cloud deployed
   juju switch anbox-cloud
   juju deploy grafana-agent --base ubuntu@22.04
   ```

2. Create the necessary relations between Anbox Cloud and the Grafana Agent:

   ```bash
   juju relate ams:cos-agent grafana-agent:cos-agent
   juju relate anbox-stream-gateway:cos-agent grafana-agent:cos-agent
   ```

3. Connect the Grafana Agent to COS:

   ```bash
   juju consume admin/cos.prometheus-receive-remote-write
   juju relate grafana-agent prometheus-receive-remote-write
   juju consume admin/cos.loki-logging
   juju relate grafana-agent loki-logging
   juju consume admin/cos.grafana-dashboards
   juju relate grafana-agent grafana-dashboards
   ```

Once all relations are established, the Anbox Cloud dashboard is available within Grafana. You can access all metrics, including logs from the machines where the Grafana agent is deployed.

(howto-harden)=
# How to harden your deployment

Anbox Cloud is designed with secure development practices but there are certain aspects to consider on your side to make sure the entire deployment is secure.

## Reduce attack surface

The following diagram illustrates the attack surface and potential points of threat.

![Anbox Cloud attack surface|690x398](/images/anbox_attack_surface.svg)

The threat points are:

### 1 - Web client

### 2 - Instances: Limit exposed ports and services
Limit the ports and services that you expose over the network. {ref}`ref-network-ports` lists the ports that are exposed externally by default. If your deployment exposes additional ports for communication between components, consider other ways the communication channel can be implemented without exposing more ports.

Disable services on inactive instances. The ideal scenario is to never expose an Anbox cloud service over the internet. Instead, use a proxy.

Exposing service endpoints is typically required when the instance needs to communicate with the service. Design your deployment to allow the instance to reach out and communicate with the control plane.

### 3 - AMC

### 4 - Stream gateway

- Expose endpoints only when required. When doing so, limit [API exposure](https://documentation.ubuntu.com/anbox-cloud/reference/api-reference/gateway-api/) by using a reverse proxy or a web application firewall.
  - `^/1.0/sessions/[a-zA-Z0-9-_:]+/sockets/(slave|adb)[/]?$` - This endpoint is required for streaming
  - `^/1.0/sessions/[a-zA-Z0-9-_:]+/connect$` - This endpoint is required for seamless ADB support

No other endpoint is required to be exposed over the public network and can be used instead through internal services.

- You can [adjust how strict the API rate limiting](https://charmhub.io/anbox-stream-gateway/configurations#max_http_requests_per_second) must be configured for the gateway API endpoint.
- Rotate authentication tokens used for the gateway API on a regular basis.

### 5- TURN/STUN: Disable TURN support if not needed

TURN is only needed to handle clients with complicated firewall or NAT configurations. If your users don't require TURN, disable support for it in the [coturn charm configuration](https://github.com/canonical/anbox-cloud-charms/blob/main/charms/coturn/templates/turnserver.conf) by setting both `enable_udp_relay` and `enable_tcp_relay` to `false`.

Keep in mind that irrespective of whether you are using STUN/TURN, using a public, externally hosted serve expands the attack surface. Hence consider using the built-in TURN/STUN server provided with the Anbox Cloud deployment for better security.

Alternatively you can also use an externally hosted STUN server and configure it as part of the [Anbox Stream Agent charm configuration](https://charmhub.io/anbox-stream-agent/configurations#extra_stun_servers). TURN is currently not supported to be externally hosted.

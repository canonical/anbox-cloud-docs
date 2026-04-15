(howto-harden)=
# Harden your deployment

Anbox Cloud is designed with secure development practices but there are certain aspects to consider on your side to make sure the entire deployment is secure.

## General guidelines

Consider the following simple yet impactful measures to ensure that you run a secure Anbox Cloud deployment:

- Always run the latest supported version of Anbox Cloud and keep your deployment up to date. See {ref}`ref-release-notes`.
- Make sure your deployment uses machines running a supported Ubuntu version. See {ref}`ref-requirements`.
- If you find a security issue, report it to the [Ubuntu security team](https://wiki.ubuntu.com/SecurityTeam/FAQ#Contact).

## Reduce attack surface

The following diagram illustrates the attack surface and potential points of threat.

![Anbox Cloud attack surface|690x398](/images/anbox_attack_surface.svg)

### 1 - Web client

- Consider the security measures, guidelines and benchmarks offered by Ubuntu Pro such as CIS, USG and Livepatch. For more information, see the Ubuntu Pro Client documentation for enabling [CIS/USG](https://canonical-ubuntu-pro-client.readthedocs-hosted.com/en/latest/howtoguides/enable_cis/) and [Livepatch](https://canonical-ubuntu-pro-client.readthedocs-hosted.com/en/latest/howtoguides/enable_livepatch/).

- Use the {ref}`exp-web-dashboard` as your default stream client. If you want to use a custom client, ensure you have set it up securely as described in the {ref}`tut-set-up-stream-client` tutorial.

### 2 - Instances

- Limit the ports and services that you expose over the network. {ref}`ref-network-ports` lists the ports that are exposed externally by default. If your deployment exposes additional ports for communication between components, consider other ways the communication channel can be implemented without exposing more ports.

  Disable services on inactive instances. The ideal scenario is to never expose a service endpoint over the internet. Instead, use a proxy.

  Exposing service endpoints is typically required when the instance needs to communicate with the service. Design your deployment to allow the instance to reach out and communicate with the control plane.

- Do not set the `application.auto_update`, `instance.security_updates`, `container.security_updates` to `false`. These settings will disable automatic updates at the application or the instance level. See {ref}`ref-ams-configuration` for more information.

- When considering the communication between the instance and the stream agent, if your deployment does not use a load balancer, do not disable TLS pinning.
Without a load balancer, the instance is directly communicating with the stream agent. So it is important to keep TLS pinning enabled to ensure that the communication is directly and securely established with the correct stream agent.

- Monitor resources used by instances regularly. See {ref}`howto-monitor-anbox` for detailed steps.

### 3 - AMC

Secure and back up the following folders on the Anbox Management Client (AMC) because they contain the TLS client certificate and key used to access the AMS API:

- `$HOME/snap/amc/current/client`
- `$HOME/snap/anbox-cloud-appliance/current/client`

### 4 - Stream gateway

- Expose endpoints only when required. When doing so, limit [API exposure](https://documentation.ubuntu.com/anbox-cloud/reference/api-reference/gateway-api/) by using a reverse proxy or a web application firewall.
The appliance has a built-in reverse proxy but if you are using the charmed deployment, remember to set up one for the deployment.

These are the endpoints that you may require to expose for specific purposes:
  - `^/1.0/sessions/[a-zA-Z0-9-_:]+/sockets/(slave|adb)[/]?$` - This endpoint is required for streaming
  - `^/1.0/sessions/[a-zA-Z0-9-_:]+/connect$` - This endpoint is required for seamless ADB support

  No other endpoint is required to be exposed over the public network and can be used instead through internal services.

- You can [adjust how strict the API rate limiting](https://charmhub.io/anbox-stream-gateway/configurations#max_http_requests_per_second) must be configured for the gateway API endpoint.
- Rotate authentication tokens used for the gateway API on a regular basis.
- When you share a session with others, do not create ephemeral shares. Instead, create a share with a limited validity and then extend the expiration period, if required.

### 5- TURN/STUN

Disable TURN support if it is not needed. TURN is only needed to handle clients with complicated firewall or NAT configurations. If your users don't require TURN, disable support for it in the coturn charm configuration by setting both [`enable_udp_relay`](https://charmhub.io/coturn/configurations#enable_udp_relay) and [`enable_tcp_relay`](https://charmhub.io/coturn/configurations#enable_tcp_relay) to `false`.

Keep in mind that irrespective of whether you are using STUN/TURN, using a public, externally hosted serve expands the attack surface. Hence consider using the built-in TURN/STUN server provided with the Anbox Cloud deployment for better security.

Alternatively you can also use an externally hosted STUN server and configure it as part of the [Anbox Stream Agent charm configuration](https://charmhub.io/anbox-stream-agent/configurations#extra_stun_servers). TURN is currently not supported to be externally hosted.

## Related topics

- {ref}`exp-security`

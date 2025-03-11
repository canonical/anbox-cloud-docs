(howto-harden)=
# How to harden your deployment

Anbox Cloud is secure by design, however, there are certain aspects of the deployment that you need to harden to ensure security.

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

### 5- TURN/STUN server

If you are using the streaming stack, use STUN server wherever possible and disable TURN.

Keep in mind that irrespective of which server you use, using a public TURN/STUN server expands the attack surface.

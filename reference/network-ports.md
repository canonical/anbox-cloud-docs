(ref-network-ports)=
# Network ports

Anbox Cloud exposes certain network ports for access and communication.

For the charmed Anbox Cloud deployment, these ports are used for communication between components, and to allow accessing the Anbox Cloud interface.

For the Anbox Cloud Appliance, ports are exposed only for accessing the Anbox Cloud interface since all components are installed on the same machine.

## Anbox Cloud

| Service               | Port(s)     | Protocol  | Exposed externally | Required                     | Description                           |
|-----------------------|-------------|-----------|--------------------|------------------------------|---------------------------------------|
| AMS                   | 8444        | TCP       | no                 | yes                          | HTTPS API                             |
| AMS                   | 20002       | TCP       | no                 | no                           | HTTPS Prometheus endpoint             |
| Anbox Cloud Dashboard | 5000        | TCP       | no                 | no                           | HTTPS website                         |
| Anbox Stream Agent    | 443         | TCP       | no                 | yes                          | HTTPS API                             |
| Anbox Stream Gateway  | 4000        | TCP       | no                 | yes                          | HTTPS API                             |
| Anbox Stream Gateway  | 7000        | TCP       | no                 | yes                          | Dqlite HA and API                     |
| Coturn                | 5349        | TCP       | yes                | yes                          | STUN/TURN                             |
| Coturn                | 5349        | UDP       | yes                | yes                          | STUN/TURN                             |
| Coturn                | 50000-51000 | UDP       | yes                | no (unless TURN is required) | TURN relay ports                      |
| etcd                  | 2379        | TCP       | no                 | yes                          | gRPC API                              |
| HAProxy               | 80          | TCP       | yes                | no                           | HTTP (redirects to HTTPS on port 443) |
| HAProxy               | 443         | TCP       | yes                | no                           | Redirects to HTTPS website            |
| LXD                   | 8443        | TCP       | no                 | yes                          | HTTPS API                             |
| LXD                   | 10000-11000 | UDP & TCP | yes                | no                           | Instance service ports                |
| NATS                  | 4222        | TCP       | no                 | yes                          | NATS API                              |

## Anbox Cloud Appliance

| Service               | Port(s)     | Protocol  | Exposed externally | Required | Description                            |
|-----------------------|-------------|-----------|--------------------|----------|----------------------------------------|
| AMS node controller   | 10000-11000 | UDP & TCP | yes                | no       | Instance service ports                 |
| Coturn                | 5349        | UDP       | yes                | no       | STUN/TURN                              |
| Coturn                | 60000-60100 | UDP       | yes                | no       | TURN relay ports                       |
| UI and API            | 443         | TCP       | yes                | yes      | Reverse proxy providing access to UI and subset of API endpoints |
| AMS API               | 8444        | TCP       | no                 | yes      | API endpoint for the AMS service       |
| NATS                  | 4004        | TCP       | no                 | yes      | API endpoint for the [NATS](https://nats.io) message queue |
| Anbox Stream Gateway  | 9031        | TCP       | no                 | yes      | API endpoint for the Anbox Stream Gateway |
| Anbox Stream Agent    | 9033        | TCP       | no                 | yes      | API endpoint for the Anbox Stream Agent |
| Anbox Cloud Dashboard | 5000        | TCP       | no                 | yes      | Endpoint providing access to the UI    |

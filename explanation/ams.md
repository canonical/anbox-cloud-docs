(exp-ams)=
# Anbox Management Service

The Anbox Management Service (AMS) sits at the heart of Anbox Cloud and handles all aspects of the application and instance life cycle. It is responsible for managing instances, applications, addons, updates and more, while simultaneously ensuring high density, performance and fast startup times.

## Interacting with AMS

AMS is usually managed through the command line interface, the Anbox Management Client (AMC), which can run either on the same machine as AMS or on a remote machine.

Since AMS exposes an HTTP interface, any tool can use the [AMS HTTP API](https://canonical.github.io/anbox-cloud.github.com/latest/ams/) to interact with AMS. Both the AMC (when running as a remote client) and the Anbox Application Registry (AAR) use the AMS HTTP API to interact with AMS.

You can also develop your own client by using the {ref}`sec-ams-sdk`.

(sec-security-cert-remote-clients)=
### Security certificates for remote clients

If the AMC is running on the same machine as AMS, it communicates with AMS through a UNIX domain socket, not through HTTP. Therefore, you do not need to worry about security certificates for local clients. However, in case of remote clients, interacting with AMS through HTTP requires a secure and trusted setup for communications, using TLS and [certificates](https://en.wikipedia.org/wiki/X.509).

You can generate self-signed certificates or use certificates signed by a Certificate Authority.

#### Self-signed certificates

Self-signed certificates are easier to set up than CA certificates, but it requires every new self-signed client certificate to be added to AMS manually.

AMC automatically generates a self-signed certificate when it is invoked for the first time. You must add this certificate to AMS before you can use AMC to access AMS remotely.

#### Certificate Authority (CA)

CA certificates are best suited if you have multiple clients connecting to AMS, because you only need to configure AMS to trust a single certificate.

After adding the CA certificate to AMS, the client certificates that are generated from the CA certificate are trusted as well.

```text
                         +-----+
                         | CA  |
           +-------------+--+--+-------------+
           |                |                |
    +------v------+  +------v------+  +------v------+
    | Certificate |  | Certificate |  | Certificate |
    +-------------+  +-------------+  +-------------+

    Trusting a CA trusts all its signed certificates as well
```

### Custom clients

As an alternative to using AMC, you can develop a custom client built around your own needs using the AMS HTTP API.

You can access AMS either by IP or through a UNIX socket. The IP depends on your network, but the UNIX socket will always be located at `/var/snap/ams/common/server/unix.socket` on the machine that hosts AMS.

```{tip}
If your client requires the AMS certificate, you can find it in `/var/snap/ams/common/server/ams.crt`.
```

## Related topics

* {ref}`exp-aar`
* {ref}`howto-access-ams-remote`
* {ref}`ref-ams-configuration`
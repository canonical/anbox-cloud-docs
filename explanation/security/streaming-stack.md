(exp-security-streaming)=
# Streaming

The Anbox Cloud Streaming Stack is based on [WebRTC](https://webrtc.org/). WebRTC forbids unencrypted communication, which enforces a certain security level.

For communication with the Anbox stream gateway, token-based authentication is used. This allows components that need to communicate with the stream gateway to verify their identity, and in return receive a unique access token. During the life of the token, it acts as a means to verify the identity of the services that handle communication between the applications and the gateway.

Of course, the overall streaming security relies on a secure client implementation. This is ensured by Anbox Cloud's web dashboard, but other client implementations might have weaknesses. However, since encryption is a mandatory feature of WebRTC, developers are forced to consider security aspects when implementing a client application.

See [A Study of WebRTC Security](https://webrtc-security.github.io/) for a detailed discussion of security features in WebRTC.

(exp-security-crypto-stream-gateway)=
## Cryptography used by the stream gateway

Anbox Streaming Gateway is using cryptographic technology for:

* TLS transport encryption
* Mutual TLS based authentication
* Token based authentication

### TLS transport encryption

All network endpoints exposed by the Anbox Stream Gateway are secured with TLS using a 4096 bit RSA key. The Anbox Stream Gateway strictly enforces TLS 1.3 or later and does not provide backward compatibility with older TLS versions.

### Mutual TLS based authentication

To exchange messages with the Anbox Stream Agent through the [NATS](https://nats.io/) message queue, the Anbox Stream Gateway uses a CA certificate signed by a 4096 bit RSA key to ensure trust with the NATS server.

### Token based authentication

Users can generate API tokens to authenticate with the HTTP API provided by the Anbox Stream Gateway. For the API tokens, a scope-limited [Macaroon](http://theory.stanford.edu/~ataly/Papers/macaroons.pdf) is used. The token is signed with a [HMAC](https://www.okta.com/identity-101/hmac/) using SHA-256 (HS256) and a 64 byte secret key. The [`macaroon.New`](https://pkg.go.dev/gopkg.in/macaroon.v2@v2.1.0#New) method is used internally to generate the [JWT](https://jwt.io/) token.

### Packages used

* [Go standard library](https://pkg.go.dev/std)
* [`gopkg.in/macaroon.v2`](https://gopkg.in/macaroon.v2)

(sec-security-crypto-stream-agent)=
## Cryptography used by the stream agent

Anbox Streaming Agent is using cryptographic technology for:

* TLS transport encryption
* Mutual TLS based authentication
* Token based authentication

### TLS transport encryption

All network endpoints exposed by the Anbox Stream Agent are secured with TLS using a 4096 bit RSA key. The Anbox Stream Agent strictly enforces TLS 1.3 or better and does not provide backward compatibility with older TLS versions.

### Mutual TLS based authentication

The Anbox Stream Agent uses mutual TLS authentication to establish a trusted TLS communication channel with AMS to call its API. For this it generates a TLS certificate using a 4096 bit RSA key.

In order to exchange messages with the Anbox Stream Gateway through the [NATS](https://nats.io/) message queue, the Anbox Stream Agent uses a CA certificated signed by a 4096 bit RSA key to ensure trust with the NATS server.

### Token based authentication

Individual Anbox instances have access to a limited set of API endpoints exposed by the Anbox Stream Agent to receive commands or exchange WebRTC signaling information with a connecting client. Access is authenticated by a scope-limited [Macaroon](http://theory.stanford.edu/~ataly/Papers/macaroons.pdf) based token. The token is signed with a [HMAC](https://www.okta.com/identity-101/hmac/) using SHA-256 (HS256) and a 64 byte secret key. The [`macaroon.New`](https://pkg.go.dev/gopkg.in/macaroon.v2@v2.1.0#New) method is used internally to generate the JWT token.

For authentication purposes with the [Coturn TURN server](https://github.com/coturn/coturn) the Anbox Stream Agent generates short living authentication tokens signed with a [HMAC](https://www.okta.com/identity-101/hmac/) using SHA-1 and a 64 byte secret key. See [RFC5389](https://datatracker.ietf.org/doc/html/rfc5389#section-15.4) and the [Coturn documentation](https://github.com/coturn/coturn/blob/master/README.turnserver) for more details.

### Packages used

* [Go standard library](https://pkg.go.dev/std)
* [`gopkg.in/macaroon.v2`](https://gopkg.in/macaroon.v2)

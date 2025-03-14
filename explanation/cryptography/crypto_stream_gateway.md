(exp-security-crypto-stream-gateway)=
# Anbox Stream Gateway

Anbox Streaming Gateway is using cryptographic technology for:

* TLS transport encryption
* Mutual TLS based authentication
* Token based authentication

## TLS transport encryption

All network endpoints exposed by the Anbox Stream Gateway are secured with TLS using an 4096 bit RSA key. The Anbox Stream Gateway strictly enforces TLS 1.3 or later and does not provide backward compatibility with older TLS versions.

## Mutual TLS based authentication

To exchange messages with the Anbox Stream Agent through the [NATS](https://nats.io/) message queue, the Anbox Stream Gateway uses a CA certificate signed by a 4096 bit RSA key to ensure trust with the NATS server.

## Token based authentication

Users can generate API tokens to authenticate with the HTTP API provided by the Anbox Stream Gateway. For the API tokens, a scope-limited [Macaroon](http://theory.stanford.edu/~ataly/Papers/macaroons.pdf) is used. The token is signed with a [HMAC](https://www.okta.com/identity-101/hmac/) using SHA-256 (HS256) and a 64 byte secret key. The [`macaroon.New`](https://pkg.go.dev/gopkg.in/macaroon.v2@v2.1.0#New) method is used internally to generate the [JWT](https://jwt.io/) token.

## Packages used

* [Go standard library](https://pkg.go.dev/std)
* [`gopkg.in/macaroon.v2`](https://gopkg.in/macaroon.v2)

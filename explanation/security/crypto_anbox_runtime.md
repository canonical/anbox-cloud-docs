(exp-security-crypto-anbox-runtime)=
# Anbox runtime

The Anbox runtime (see {ref}`howto-anbox-runtime`) is using cryptographic technology for:

* TLS transport encryption
* Token based authentication
* WebRTC

## TLS transport encryption

All HTTP communication Anbox performs over IP connections to external services is using TLS for transport encryption.

When communicating with the HTTPS API of the Anbox Stream Agent, Anbox will either rely on [system CA certificates](https://launchpad.net/ubuntu/+source/ca-certificates) or verify the certificate presented via TLS against a SHA-256 fingerprint of the certificate with which it has been configured. For the fingerprint validation, Anbox will retrieve the remote certificate and use the `X509_digest` method from [OpenSSL](https://launchpad.net/ubuntu/+source/openssl/) to calculate a SHA-256 hash. The hash is then compared against the expected hash. If they don't match, the connection to the Anbox Stream Gateway is canceled by Anbox.

## Token based authentication

Anbox accesses a limited set of API endpoints of the Anbox Management Service (AMS) to submit status information during runtime. Access is authenticated by a scope-limited [JWT](https://jwt.io/) based token. See {ref}`exp-security-crypto-ams` for more details.

As part of the WebRTC connection process, Anbox communicates with the HTTP API endpoints provided by the Anbox Stream Agent. Anbox authenticates itself to the agent by presenting a token (see {ref}`exp-security-crypto-stream-agent`) and validates the TLS certificate of the agent by checking its fingerprint. The fingerprint Anbox uses for the validation check is the SHA-256 hash of the complete ASN.1 DER content (certificate, signature algorithm and signature) of the TLS certificate that the agent uses.

## WebRTC

For streaming of audio, video and other data, the Anbox runtime uses WebRTC as provided by the upstream [WebRTC](https://webrtc.org) project from Google. Unlike the upstream default, the WebRTC build for the Anbox runtime utilizes [OpenSSL](https://launchpad.net/ubuntu/+source/openssl/) instead of Google's [BoringSSL](https://boringssl.googlesource.com/boringssl) for any cryptographic use.

The security model and cryptographic use of WebRTC is described in [RFC8827](https://www.rfc-editor.org/rfc/rfc8827) and use of WebRTC in the Anbox runtime does not deviate from this.

## Packages used

* [Go standard library](https://pkg.go.dev/std)
* [OpenSSL](https://launchpad.net/ubuntu/+source/openssl/)
* [`ca-certificates`](https://launchpad.net/ubuntu/+source/ca-certificates)
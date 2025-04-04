(exp-security-dashboard)=
# Dashboard

The Anbox Cloud Dashboard (dashboard) is using cryptographic technology for:

* TLS transport encryption
* Registration of new users
* User authentication
* Mutual TLS based authentication

## TLS transport encryption

All network endpoints exposed by the dashboard are secured with TLS using an 4096 bit RSA key. The dashboard strictly enforces TLS 1.2 or later and does not provide backward compatibility with older TLS versions.

## Registration of new users

For registering a new user, a token is generated using the [PyJWT](https://github.com/jpadilla/pyjwt) library.

1. The token includes the user's email and the token's validity period as payload data. This `payload` dictionary is passed to the `encode()` function from the PyJWT library.
1. A secret key is used to sign the token. The [HMAC](https://www.okta.com/identity-101/hmac/) SHA-256 algorithm is used in the signing process.
1. The `encode()` function returns a [JWT](https://jwt.io/), which is a string representing the encoded and signed payload data.

The dashboard uses PyJWT to decode the token after it has been presented by the user, verifies its validity and checks its expiration:

1. The token, in the form of a JWT string, is passed to the `decode()` function from the PyJWT library.
1. The secret key is used to verify the token's signature and the expected signing algorithm for the token is [HMAC](https://www.okta.com/identity-101/hmac/) SHA-256.
1. The `decode()` function verifies the token's signature using the secret key and algorithm. If verification is successful, it decodes the token and returns the original payload dictionary.

## User authentication

When authenticating with an external identity provider, the following actions are performed:

Retrieving ID Tokens
  : ID tokens, which contain the user's email and full name, are obtained from the authentication server.

Decoding Unverified Headers
  : Initially, the `get_unverified_header()` function from [`python-jose`](https://github.com/mpdavis/python-jose/) is used to decode the token's unverified headers and extract the key ID.

Fetching and Caching JWKS
  : The JSON Web Key Set (JWKS) is fetched from the JWKS endpoint and is cached. For subsequent requests, the cached JWKS is checked for a key matching the key ID in the token. If the key is not found in the cache, the JWKS is fetched again.

Decoding the Token
  : The `decode()` function from [`python-jose`](https://github.com/mpdavis/python-jose/) is used to decode the token. This process uses the JWKS containing the key ID and verifies the audience.

## Mutual TLS based authentication

The dashboard uses mutual TLS authentication to establish a trusted TLS communication channel with the Anbox management Service (AMS) to communicate with the AMS API. To do this, the dashboard generates a TLS certificate using a 4096 bit RSA key.

## Packages used

* [PyJWT](https://github.com/jpadilla/pyjwt), supplied by [PyPI](https://pypi.org/project/PyJWT/)
* [`python-jose`](https://github.com/mpdavis/python-jose/), supplied by [PyPI](https://pypi.org/project/python-jose/)
* [OpenSSL](https://launchpad.net/ubuntu/+source/openssl/)
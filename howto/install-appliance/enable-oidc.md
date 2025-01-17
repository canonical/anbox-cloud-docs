(howto-appliance-enable-oidc)=
# How to enable custom identity provider support

The Anbox Cloud Appliance has support for custom identity providers for authentication through the use of [OpenID Connect](https://openid.net/developers/discover-openid-and-openid-connect/).

Support for a custom identity provider has to be enabled at initialization by using a preseed configuration. See {ref}`ref-appliance-preseed-config` for more details.

Anbox Cloud uses the [authorization code flow](https://openid.net/specs/openid-connect-core-1_0.html#CodeFlowAuth) to obtain an identity token. No access token is requested in this flow because authorization is handled within the Anbox Cloud services.

In order to allow discovery of the necessary endpoints on the identity provider, it must support the [OpenID Connect Discovery](https://openid.net/specs/openid-connect-discovery-1_0.html) protocol.

The following will show you how to configure an [OpenID Connect](https://openid.net/developers/discover-openid-and-openid-connect/) based identity provider for the Anbox Cloud Appliance.

## Preparation

In order to configure [OpenID Connect](https://openid.net/developers/discover-openid-and-openid-connect/) based authentication, you will need the following from your identity provider:

* The issuer URL
* The client ID
* (Optional) The audience URL, required by some providers. For example, [Auth0](https://auth0.com)

The identity provider is expected to provide the JSON Web Key Set endpoint on `<issuer URL>/.well-known/jwks.json`.

Your identity provider must have `https://<appliance address or <DNS name>/oidc/callback` configured as allowed redirect/callback URL.

## Configure OpenID Connect

It is only possible to configure support for OpenID Connect only when the Anbox Cloud Appliance is being initialized with a preseed (see {ref}`ref-appliance-preseed-config`). The other steps to install the Anbox Cloud Appliance as described in {ref}`tut-installing-appliance` remain the same.

The issuer URL, client ID and optional audience URL are set in the preseed configuration as follows:

```yaml
$ cat preseed.yaml
....
oidc:
  issuer: https://my.auth.com
  client_id: aff32f32ffwfsdfdsfdsg
  # Only if your identity provider requires it
  audience: https://my.auth.com/api/v2
```

With the preseed configuration you can initiate the initialization process by running:

    sudo anbox-cloud-appliance init --preseed < preseed.yaml

Once the initialization has been completed, you can register a new user by running:

    sudo anbox-cloud-appliance dashboard register <email address>

Once the user has been registered by following the printed URL and authenticated with your identity provider, access is granted to the web UI.

## Related topics

* {ref}`tut-installing-appliance`
* {ref}`howto-use-web-dashboard`
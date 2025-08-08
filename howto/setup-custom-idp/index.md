(howto-set-up-idp)=
# Set up a custom identity provider

Anbox Cloud has support for custom identity providers for authentication through [OpenID Connect](https://openid.net/developers/discover-openid-and-openid-connect/). To allow discovery of necessary endpoints, the identity provider must support the [OpenID Connect Discovery](https://openid.net/specs/openid-connect-discovery-1_0.html) protocol.

Anbox Cloud uses the [authorization code flow](https://openid.net/specs/openid-connect-core-1_0.html#CodeFlowAuth) to obtain an identity token. No access token is requested in this flow because authorization is handled within the Anbox Cloud services.

Anbox Cloud also supports authenticating command line clients using [device code flow](https://www.rfc-editor.org/rfc/rfc8628). However, this is an experimental feature and under active development.

```{important}
Authenticating command line clients using OIDC is an experimental feature in 1.27.0. Hence, the interface and the API endpoints may change in future releases.
```

To configure OpenID Connect based authentication, you will need an issuer URL and a client ID from your identity provider. This guide shows you how to get those values with different custom identity providers.

::::{tab-set}
:::{tab-item} Auth0

Open a free account on [Auth0.com](https://auth0.com/) and log in to its web interface.

## 1. Create an application

Select *Applications > Create application*.

For authenticating a web client, create a *Single Page Application* (type of the application). For a command line client, create a *Native* application.

## 2. Configure the application settings

Navigate to the *Settings* tab of your application.

**For authenticating a web client**, add your web client's address to the *Allowed Callback URLs*, followed by `/oidc/callback`. This could be your Anbox Cloud dashboard or a custom web client. For example: `https://example.com:8406/oidc/callback`.You can choose to use an IP address instead of a domain name and `:8406` is the default listening port. This default port might differ for your setup.

To the *Allowed Logout URLs*, add your web client's address, for example, `https://example.com:8406`. Enable *Allow Refresh Token Rotation* and save.

**For authenticating a command line client**, select *Advanced Settings > Grant Types*. Verify if the *Refresh Token* and *Device Code* options are selected and save.

## 3. Copy necessary parameters

Anbox Cloud needs the issuer URL, the client ID and the API audience values to authenticate the identity provider:

- Near the application *Settings* tab, locate the *Domain*. The value of this domain prefixed with `https://` is your issuer URL.
- Copy the *Client ID* from the application settings.
- Select *Applications > APIs* and copy the *API Audience* value.

:::

:::{tab-item} Keycloak

```{note}
This guide assumes that Keycloak is available over HTTPS.
```
## 1. Initial setup
Configure Keycloak for production by following their [documentation](https://www.keycloak.org/server/configuration-production). If you are fine using the development version, download [Keycloak-25.0.4](https://github.com/keycloak/keycloak/releases/download/25.0.4/keycloak-25.0.4.zip), extract the file and run `bin/kc.sh start-dev`. Open *http://localhost:8080/* and create an admin user. Sign in to Keycloak with the admin account.

## 2. Create a realm and a client

Select the *Keycloak* dropdown in the admin console. Create a realm and give it a name, for example, `anbox-cloud-realm`.

Navigate to *Clients > Create client*. Select the client type as *OpenID Connect*. Enter a client ID, for example, `anbox-cloud-client`. Make a note of this client ID before proceeding, you will need this later.

**For authenticating a command line client,**  you will need to select the authentication flow too — Select *OAuth2.0 Device Authorization Grant* in the *Authentication Flow* option.

Leave the default login settings and save. Now, you can proceed to creating a user.

**For authenticating a web client,** you need to add redirect URIs:

In *Valid redirect URIs*, enter your web client's address, followed by `/oidc/callback`. This could be your Anbox Cloud dashboard or a custom web client. For example: `https://example.com:8406/oidc/callback`. You can choose to use an IP address instead of a domain name and `:8406` is the default listening port. This default port might differ for your setup.

In the field for *Valid post logout redirect URIs*, enter your Anbox Cloud dashboard address. For example, `https://example.com:8406`. Save and proceed to adding a client scope.

## 3. Add a client scope (only for a web client)

Navigate to your client (*Clients* > your client name). Select *Client Scopes* and add one.

Select *email*, *profile* and *offline_access* scopes from the list of available scopes.

## 4. Create a user

Navigate to *Users > Create new user*, add a user name and create a user.

On the user detail page, select *Credentials* and *Set password*. Save the new password.

Navigate to *Realm settings > OpenID Endpoint Configuration* and copy the value of the *issuer* key. This is your issuer URL, make a note of it.

:::

:::{tab-item} Ory Hydra

Ory Hydra supports both local user accounts and social login options, including Google, Facebook, Microsoft, GitHub, Apple and others.

Ory Hydra currently does not support authenticating clients using [device code flow](https://www.rfc-editor.org/rfc/rfc8628), hence it is not available to authenticate command line clients. You can use Ory Hydra with a web client like the Anbox Cloud dashboard.

## 1. Create a client

Create a free account on [Ory Hydra](https://www.ory.sh/hydra/). After logging into the Ory Console, navigate to *OAuth 2 > OAuth2 Clients > Create OAuth2 Client*.

Create the client with:
   - *Type*: *Mobile / SPA*
   - *Client Name*: Choose a name, such as `anbox-cloud-ory-client`.
   - *Scope*: Add the scopes `email`, `openid`, and `profile`.
   - *Redirect URIs*: Add your web client address, followed by `/oidc/callback`, for example, `https://example.com:8406/oidc/callback`. You can choose to use an IP address instead of a domain name and `:8406` is the default listening port. This default port might differ for your setup.
   - *Post Logout Redirect URIs*: Add your web client's address, for example, `https://example.com:8406`.

## 2. Copy necessary parameters

On the *OAuth2 Clients* list, find and copy the *ID* for the client you created.

In the Ory Console, navigate to *OAuth 2* > *Overview*. Find and copy the value of the *Issuer URL*.

```{important}
No users exist within ORY by default. New users can use the sign-up link during login. Alternatively, configure Google, Facebook, Microsoft, GitHub, Apple, or another social sign-in provider as described in the [ORY documentation](https://www.ory.sh/docs/kratos/social-signin/overview).
```
:::
::::

## Next Steps

Once you have the issuer URL, client ID, audience API:

For using the appliance with the dashboard (web client), your next step is to {ref}`initialize the appliance with a preseed <howto-configure-oidc>`.

For using the appliance with the command line client or using the charmed deployment, your next step is to {ref}`connect to the remote AMS using the IdP <sec-oidc-idp>`.

```{toctree}
:hidden:

Configure OIDC (Appliance) <configure-oidc>
```

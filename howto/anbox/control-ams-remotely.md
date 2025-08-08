(howto-access-ams-remote)=
# Access AMS remotely

By default, the {term}`Anbox Management Client (AMC)` runs on the same machine as the {term}`Anbox Management Service (AMS)` and connects to it through a UNIX socket.

You can also choose to install AMC on a different machine and configure it to connect to AMS through an HTTPS connection. There are two ways to connect to a remote AMS instance and authenticate over HTTPS:

- Using a trusted client certificate
- Using an identity provider that supports [OpenID Connect](https://openid.net/developers/how-connect-works/)

## Prerequisite: Install AMC

You need the AMC snap to connect to AMS:

    snap install amc


## Use trusted client certificates

If you have installed AMC on a different machine than the AMS, controlling AMS remotely requires trusted security certificates, as a default. To establish trusted security certificates, you can generate self-signed certificates or use certificates signed by a Certificate Authority. See {ref}`sec-security-cert-remote-clients` for more information.

### Self-signed certificates

To generate a self-signed certificate:

Invoke any `amc` command on the client machine, for example:

    amc remote ls

AMC automatically generates a self-signed certificate when invoked for the first time.

Locate the `$HOME/snap/amc/current/client/client.crt` certificate on the client machine and copy it to the machine that runs AMS.

Log on to the machine that runs AMS and configure AMS to trust the new client by adding the client certificate:

   amc config trust add client.crt


### Certificate Authority (CA)

There are different ways to generate a CA certificate and key. For example, use a PKI like [easy-rsa](https://github.com/OpenVPN/easy-rsa).

Copy the generated CA certificate to the machine that runs AMS.

Log on to the machine that runs AMS and configure AMS to trust the CA certificate and all certificates that are based on it

    amc config trust add ca.crt

Using the same method that you used to generate the CA certificate, generate a client key and certificate for each client.

Copy the generated credentials to the client machine:

   * Copy the client certificate to `$HOME/snap/amc/current/client/client.crt`.
   * Copy the client key to `$HOME/snap/amc/current/client/client.key`

### Configure AMC to connect to AMS

When you have the necessary certificates in place, configure AMC to connect to the remote AMS:

    amc remote add <your remote name> https://<IP address of the AMS machine>:8444

```{tip}
If you haven't changed the port AMS is listening on, it's 8444 by default.
```

The command connects to AMS and shows you the fingerprint of the server certificate. If it matches what you expect, acknowledge the fingerprint by typing "yes".

Now, switch to the new remote:

    amc remote set-default <your remote name>

From here on, all invocations of the `amc` command will use the new remote.

(sec-oidc-idp)=
## Use an OpenID Connect identity provider

```{important}
Authenticating command line clients using OIDC is an experimental feature in 1.27.0. Hence, the interface and the API endpoints may change in future releases.
```

To authenticate with AMS through a supported identity provider, you need to first configure the identity provider. Follow the instructions in {ref}`howto-set-up-idp` to configure Auth0 or Keycloak.

### Configure AMS to use OpenID Connect

Log on to the machine that runs AMS and configure AMS to use the identity provider:

```
amc config set oidc.issuer_url '<issuer url configured for the provider>'
amc config set oidc.client_id '<client id configured for the client on the identity provider>'
amc config set oidc.audience '<audience, if configured, for the client>'
```
You would have copied the issuer URL, client ID and audience API values when you finished the identity provider setup.

### Configure AMC to connect to AMS

To configure AMC to connect to the remote AMS:

    amc remote add <your remote name> https://<IP address of the AMS machine>:8444 --auth-type oidc

```{tip}
If you haven't changed the port AMS is listening on, it's 8444 by default.
```

The command connects to AMS and shows you the fingerprint of the server certificate. If it matches what you expect, acknowledge the fingerprint by typing “yes”.

The command will return a URL from your identity provider and ask you to log in:

```
Please visit the following URL to complete authentication:
URL: http://<url returned from provider>/device?user_code=<code returned from the provider>
Code: <code returned from the provider>
```

Complete the authentication with the URL and switch to the new remote by running the following command:

    amc remote set-default <your remote name>

After this step, all invocations of the `amc` command use the new remote.

## Related topics

* {ref}`exp-ams`

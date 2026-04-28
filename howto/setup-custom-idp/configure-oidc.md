(howto-configure-oidc)=
# Configure OIDC for the appliance

It is possible to configure OpenID Connect only when the appliance is initialized with a preseed (see {ref}`ref-appliance-preseed-config`) after the installation.

When you have the issuer URL and client ID, set the values in the preseed configuration:

```{note}
Auth0 additionally requires the audience value.
```

```yaml
$ cat preseed.yaml
....
oidc:
  issuer: https://my.auth.com
  client_id: example_client_id
  audience: https://example.auth0.com/api/v2/ # for Auth0 only
```

To start the initialization process with the preseed configuration, run:

    sudo anbox-cloud-appliance init --preseed < preseed.yaml

When the initialization is complete, create an identity in AMS to provide access to it via OIDC:

    amc auth identity create oidc/<email address>

In addition to creating the user you need to add it to a group to give permissions for access. To make the user an admin run:

    amc auth identity group add <identity id> --groups admin

The user can now login to Anbox Cloud dashboard with the identity created.

The user can also access AMS by running

    amc remote add test https://<address>:8444 --auth-type=oidc

## Related topics

* {ref}`tut-installing-appliance`
* {ref}`howto-use-web-dashboard`

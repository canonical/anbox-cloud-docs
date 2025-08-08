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
dashboard:
  oidc:
    issuer: https://my.auth.com
    client_id: example_client_id
    audience: https://example.auth0.com/api/v2/ # for Auth0 only
```

To start the initialization process with the preseed configuration, run:

    sudo anbox-cloud-appliance init --preseed < preseed.yaml

When the initialization is complete, to register a new user, run:

    sudo anbox-cloud-appliance dashboard register <email address>

This prints a URL to complete the registration. Access that URL and complete the registration. Finally, log in to access the dashboard user interface.

## Related topics

* {ref}`tut-installing-appliance`
* {ref}`howto-use-web-dashboard`
(howto-configure-oidc)=
# Configure OIDC for the appliance

It is possible to configure OpenID Connect only when the appliance is initialized with a preseed (see {ref}`ref-appliance-preseed-config`) after the installation.

When you have the client ID, set the value in the preseed configuration:

```{note}
Auth0 additionally requires the audience value.
```

```yaml
$ cat preseed.yaml
....
oidc:
  client_id: example_client_id
```

To start the initialization process with the preseed configuration, run:

    sudo anbox-cloud-appliance init --preseed < preseed.yaml

When the initialization is complete, to register a new user with the dashboard, run:

    sudo anbox-cloud-appliance dashboard register <email address>

This prints a URL to complete the registration. Access that URL and complete the registration. Finally, log in to access the dashboard user interface.

You can also register the same user with AMS to provide access to it via OIDC:

    amc auth identity create oidc/<email address>

In addition to creating the user you need to add it to a group to give permissions for access. To make the user an admin run:

    amc auth identity group add <identity id> --groups admin

Afterwards the user can access AMS by running

    amc remote add test https://<address>:8444 --auth-type=oidc

## Related topics

* {ref}`tut-installing-appliance`
* {ref}`howto-use-web-dashboard`

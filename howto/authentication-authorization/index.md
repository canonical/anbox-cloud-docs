---
myst:
  html_meta:
    "description": "How to set up and configure authentication and authorization for Anbox Cloud."
---

(howto-manage-auth)=
# Authentication and authorization

Use these guides to set up and configure authentication and authorization:

- {ref}`howto-set-up-idp` with Auth0, Keycloak or Ory Hydra.
- {ref}`howto-configure-oidc` to connect the Anbox Cloud Appliance to your identity provider.
- {ref}`howto-access-ams-remote` using a trusted client certificate or an OIDC identity provider.
- {ref}`howto-auth` to create identities and groups and assign permissions.

## See also

- Explanation: {ref}`exp-auth`
- Reference: {ref}`ref-auth`
- How-to guide: {ref}`howto-set-up-tls` to configure the HTTPS certificate for your appliance.

```{toctree}
:hidden:

set-up-custom-idp
configure-oidc
control-ams-remotely
configure-user-permissions
```

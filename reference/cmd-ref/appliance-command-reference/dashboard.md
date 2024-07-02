---
orphan: true
---
# `dashboard`

The `dashboard` command allows access to the web dashboard and also allows you to manage it. By default, the dashboard is enabled and exposed, but you can disable it. You can also register new users for the web dashboard. See {ref}`sec-register-ubuntu-one-appliance` for more information.

    anbox-cloud-appliance dashboard <subcommand>

## Subcommands

The following subcommands are available:

### `expose`

Enables access to the web dashboard in the load balancer.

    anbox-cloud-appliance dashboard expose

### `register`

Registers a new user for the web dashboard.

    anbox-cloud-appliance dashboard register

### `unexpose`

Disables access to the web dashboard in the load balancer.

    anbox-cloud-appliance dashboard unexpose

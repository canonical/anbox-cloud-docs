The `ams` command provides access to the Anbox Management Service (AMS) through subcommands. It exposes the AMS HTTPS service on the public endpoint of the machine on which the appliance is running. Using this command, you can expose or unexpose AMS through the load balancer.

    anbox-cloud-appliance ams <subcommand>

## Subcommands

The following subcommands are available:

### `expose`

Enables access to AMS in the load balancer.

    anbox-cloud-appliance ams expose

### `unexpose`

Disables access to AMS in the load balancer.

    anbox-cloud-appliance ams unexpose

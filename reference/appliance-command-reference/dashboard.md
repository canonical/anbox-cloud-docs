The `dashboard` command allows access to the web dashboard and also allows you to manage it. By default, the dashboard is enabled and exposed, but you can disable it. You can also register new users for the web dashboard. See [Register an Ubuntu One account in Anbox Cloud Appliance](https://discourse.ubuntu.com/t/web-dashboard/20871#dashboard-access-appliance) for more information.

    anbox-cloud-appliance dashboard <subcommand>

## Subcommands

### `expose`
Enables access to the web dashboard in the load balancer.

    anbox-cloud-appliance dashboard expose

### `register`
Registers a new user for the web dashboard.

    anbox-cloud-appliance dashboard register

### `unexpose`
Disables access to the web dashboard in the load balancer.

    anbox-cloud-appliance dashboard unexpose

(ref-appliance-commands)=
# Appliance command reference

The `anbox-cloud-appliance` is a command line client to manage the appliance and its components.

Use `anbox-cloud-appliance --help` or `anbox-cloud-appliance <command> --help` to display usage information for the tool and its commands.

The following commands are available for the `anbox-cloud-appliance` tool:

| Command | Description|
|---------|------------|
|[`ams`](ams.md)    | Manage access to the Anbox Management Service (AMS)|
|[`dashboard`](dashboard.md)| Manage the web dashboard of appliance|
|[`destroy`](destroy.md) | Destroy the appliance|
|[`gateway`](gateway.md) | Manage the appliance stream gateway|
|[`help`](help.md) | Help about the `anbox-cloud-appliance` tool|
|[`init`](init.md)| Initialise the appliance|
|[`status`](status.md) | Display the current status and version of the appliance|
|[`upgrade`](upgrade.md) | Upgrade the appliance to a newer version|

If you encounter an issue and want to collect debugging information from the appliance, use `anbox-cloud-appliance.buginfo`.

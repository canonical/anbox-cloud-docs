(howto-configure-instance)=
# Configure an instance

AMS allows some configuration options of an instance to be changed. A full list of configuration options is available at {ref}`ref-ams-instance-configuration`

## Show current configuration options

To view the current set configuration options for an instance, you can run

    amc show <instance id or name>

## Set confguration option

Use the `amc set` command to configure instance level options:

    amc set <instance id or name> <name> <value>

For example, to set the `security.delete_protected` option for the instance `test0`:

    amc set test0 security.delete_protected true

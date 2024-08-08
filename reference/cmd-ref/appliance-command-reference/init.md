---
orphan: true
---
# `init`

The `init` command configures and initialises the Anbox Cloud Appliance. This command runs through the initial initialisation process before Anbox Cloud can be used. It provides an interactive configuration dialog which allows you to either accept the defaults or specify custom preferences for configurable aspects of the appliance.

    anbox-cloud-appliance init <options>

See {ref}`sec-initialise-appliance` for more information.

## Options

|Option | Description |
|-------|-------------|
|`--auto`|To enable automatic (non-interactive) mode. Use this option if you want to accept the default options for the appliance.|
|`--preseed`| To enable pre-seed mode, expects YAML config from stdin|
|`--force`|Force run, even if already initialised|

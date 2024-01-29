The `init` command configures and initialises the Anbox Cloud Appliance. This command runs through the initial bootstrap process before Anbox Cloud can be used. It provides an interactive configuration dialog which allows you to either accept the defaults or specify custom preferences for configurable aspects of the appliance. 

    anbox-cloud-appliance init <options>

See [Initialise the appliance](https://discourse.ubuntu.com/t/install-the-anbox-cloud-appliance-on-a-dedicated-machine/22681#initialise-the-appliance-6) for more information.

## Options

|Option | Description |
|-------|-------------|
|`--auto`|To enable automatic (non-interactive) mode. Use this option if you want to accept the default options for the appliance.|
|`--charm-channel <channel>`|To specify the store channel from which Anbox Cloud charms are to be deployed. This is an *advanced* option and used mostly for *development purposes*.|
|`--force-network-bridge`|To force using a local network bridge instead of a FAN overlay network|
|`--image-server-auth <username:password>`|To specify authentication credentials for the Anbox Cloud image server. This is an *advanced* option and used mostly for *development purposes*.|
|`--image-server-url <url>`| To specify the URL of the Anbox Cloud image server. This is an *advanced* option and used mostly for *development purposes*.|
|`--preseed`| To enable pre-seed mode, expects YAML config from stdin|
|`--proxy <server-address>`| To specify the HTTP/HTTPS proxy server to use during installation|
|`--use-existing-gpu-driver`|To indicate that a GPU driver is already installed and ready for use|

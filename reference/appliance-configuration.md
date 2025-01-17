(ref-appliance-configuration)=
# Anbox Cloud Appliance configuration

The Anbox Cloud Appliance provides various configuration items to customize its behavior. Currently set configuration can be seen by running

    sudo anbox-cloud-appliance config show

Available configuration items can be changed by using the following command

    sudo anbox-cloud-appliance config set <key>=<value> ...

The following table lists the available configuration items and their meaning.

| Name<br/>*(Type, Default)* | Description           |
|-----|-----------------------|
| `network.public_address`<br/>*(string, N/A)* | Public address (if behind NAT) of the machine the appliance is running on |
| `network.location`<br/>*(string, N/A)* | DNS name used to access the appliance |
| `core.https_allowed_origin`<br/>*(string, N/A)* | `Access-Control-Allow-Origin` HTTP header value for the reverse proxy of the appliance |
| `core.https_allowed_headers`<br/>*(string, N/A)* | `Access-Control-Allow-Headers` HTTP header value for the reverse proxy of the appliance |
| `core.https_allowed_methods`<br/>*(string, N/A)* | `Access-Control-Allow-Methods` HTTP header value for the reverse proxy of the appliance |
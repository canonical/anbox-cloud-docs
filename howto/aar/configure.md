(howto-configure-aar)=
# Configure

The {term}`Anbox Application Registry (AAR)` uses a certificate-based authentication system that uses TLS server and client certificates to establish a trusted connection between the AAR and the {term}`Anbox Management Service (AMS)`.

## Configuring AAR for the charmed deployment

Use Juju relations to register an instance with the AAR if your deployment uses Anbox Cloud charms.

To register an instance as a client, use the following command:

    juju add-relation aar:client ams:registry-client

To register an instance as a publisher, use the following command:

    juju add-relation aar:publisher ams:registry-publisher

```{tip}
Run `amc config show` to check that the AAR configuration items were changed.
```

### Register units deployed in another model

For `ams` units deployed in another model, you can make use of Juju cross model relations.

Enter the following commands:

    juju switch <model containing aar>
    juju offer aar:client

The second command returns the name of the generated offer, for example, `my-controller/my-model.aar`. Continue with the following commands:

    juju switch <model containing ams>
    juju relate ams <offer name>

## Configuring AAR for the Appliance

If you are using the appliance, you must register the clients manually. Adding clients manually requires access to the machines hosting AMS and the AAR.

Install the snap:

    sudo snap install --channel=<channel> aar

Replace <channel> with a suitable snap version. For example, it could be `1.27/stable`. For a list of all snap versions available, you can run `snap info aar`.

### Establish trust for AAR with AMS

If you have AAR installed on the same machine as the appliance, make the AAR certificate available in the location `/var/snap/anbox-cloud-appliance/common/certs/` so that AMS has access to the AAR.

If you have AAR and the appliance on separate machines, import the AAR certificate into the machine where appliance is installed.

On the machine hosting the AAR, copy the certificate and import it to the appliance machine:

    sudo cp /var/snap/aar/common/certs/server.crt /var/snap/anbox-cloud-appliance/common/certs/aar.crt

Once the certificate is in place, add trust for the AAR:

    sudo amc config trust add /var/snap/anbox-cloud-appliance/common/certs/aar.crt

Verify that the new certificate is listed in the AMS trust store:

    amc config trust list

### Establish trust for AMS with AAR

If you have AAR installed on the same machine as the appliance, make the AMS registry-specific certificate available in the location `/var/snap/anbox-cloud-appliance/common/certs/` so that the AAR can use it to establish trust with AMS.

If you have AAR and the appliance on separate machines, import the AMS registry-specific certificate into the machine where AAR is installed.

Copy the certificate to the machine where AAR is installed:

    sudo cp /var/snap/anbox-cloud-appliance/common/ams/registry/client.crt /var/snap/aar/common/certs/aar.crt

Now, you need to establish the trust for the AMS client with the AAR. Depending on the kind of access required, AMS can act in two different roles, when working with the AAR: a publisher or a client. See {ref}`exp-aar`.

To add AMS as a trusted publisher, run:

    sudo aar trust add client.crt --publisher

To add AMS as a trusted client, run:

    sudo aar trust add client.crt

```{note}
Due to Snap strict confinement and the AAR `sudo` requirement, the command requires the certificates to be located in the root user home directory `/root`. To bypass this requirement, use the following command:

`cat client.crt | sudo aar trust add [--publisher]`
```

### Configure registry endpoint in AMS

Configure the registry endpoint so that AMS can sync applications and new application versions with the AAR:

    amc config set registry.url https://<aar-machine-ip-address>:3000

For AMS to know which certificate to expect from the AAR, find and set the certificate fingerprint:

    amc config trust list
    amc config set registry.fingerprint <fingerprint>

### Configure sync interval in AMS

Set the interval in which AMS checks for new applications to sync with the AAR. By default, the interval is set to one hour. You can change this to a lesser interval.

For example, to configure AMS to check for updates to be synced with the AAR, every five minutes, run:

    amc config set registry.update_interval 5m

### Configure registry mode in AMS

There are three registry modes that you can configure: push, pull and manual.

To configure AMS to push any local applications to the AAR, set the `registry.mode` configuration item to `push`:

    amc config set registry.mode push

The AMS is now configured to push all existing applications and any future applications as well as updates to the AAR.

```{note}
Only published application versions are pushed to the AAR.
```

To configure AMS to pull applications from the AAR, set `registry.mode` to `pull`:

    amc config set registry.mode pull

All existing and future applications are automatically pulled from the AAR.

If you prefer to sync the applications manually, set the registry mode to manual:

    amc config set registry.mode manual

Then, push or pull application updates when needed:

    amc registry push app_name

or

    amc registry pull app_name

### Reboot AAR snap

Finally, reboot the AAR:

    sudo snap restart aar

## Related topics

* {ref}`exp-aar`
* {ref}`howto-revoke-aar`
* [Juju relations](https://canonical-juju.readthedocs-hosted.com/en/latest/user/reference/relation/)
* [Juju cross model relations](https://canonical-juju.readthedocs-hosted.com/en/latest/user/reference/relation/#cross-model/)

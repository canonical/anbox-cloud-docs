By default, the Anbox Management Client (AMC) runs on the same machine as the [Anbox Management Service (AMS)](https://discourse.ubuntu.com/t/about-ams/24321) and connects to it through a UNIX socket.

If you want to control AMS remotely, you can install the AMC on a separate machine and configure it to connect to AMS through a secure HTTP connection.

## Install the AMC on a separate machine

To install the AMC on a machine other than the machine running AMS, you must first install it.

To do so, use the following command:

    snap install amc

## Install a trusted certificate

Controlling AMS remotely requires trusted security certificates. You can generate self-signed certificates or use certificates signed by a Certificate Authority. See [Security certificates for remote clients](https://discourse.ubuntu.com/t/anbox-management-service-ams/24321#security-certificates-for-remote-clients-2) for more information.

### Self-signed certificates

To use a self-signed certificate, complete the following steps:

1. Invoke an `amc` command on the client machine, for example:

        amc remote ls

    To generate a self-signed certificate, you can invoke any `amc` command because AMC automatically generates a self-signed certificate the first time it is invoked.

2. Locate the `$HOME/snap/amc/current/client/client.crt` certificate on the client machine and copy it to the machine that runs AMS.
3. Log on to the machine that runs AMS and configure AMS to trust the new client by adding the client certificate:

   ```
   amc config trust add client.crt
   ```

### Certificate Authority (CA)

To use a CA certificate, complete the following steps:

1. Generate a CA certificate and key. There are different ways of how to do this. For example, you can use a PKI like [easy-rsa](https://github.com/OpenVPN/easy-rsa).
2. Copy the generated CA certificate to the machine that runs AMS.
3. Log on to the machine that runs AMS and configure AMS to trust the CA certificate (and with that, all certificates that are based on it):

        amc config trust add ca.crt
4. For each client, generate a client key and certificate based on the CA certificate. You should use the same method for this as you did in the first step.
5. Copy the generated credentials to the client machine:

   * Copy the client certificate to `$HOME/snap/amc/current/client/client.crt`.
   * Copy the client key to `$HOME/snap/amc/current/client/client.key`

## Expose the AMS HTTPS service

To be able to access AMS remotely, its HTTPS service must be exposed.

If you are running the Anbox Cloud Appliance, you can expose the service with the following command:

    anbox-cloud-appliance ams expose

If you are running a full Anbox Cloud deployment, the service is automatically exposed within the internal subnet. If this is sufficient, you do not need further configuration. If you want to access AMS from a machine that is in a different subnet, use `juju expose` to expose the service (see [How to expose a deployed application](https://juju.is/docs/olm/expose-a-deployed-application) for instructions). Note that if you expose services externally, you should also add a load balancer or proxy to your deployment.

## Configure AMC to connect to AMS

After setting up the security certificates, configure AMC to connect to the remote AMS. To do this, choose a name for the remote and enter the following command:

    amc remote add <your remote name> https://<IP address of the AMS machine>:8444

[note type="information" status="Tip"]If you haven't changed the port AMS is listening on, it's 8444 by default.[/note]

The command connects to AMS and shows you the fingerprint of the server certificate. If it matches what you expect, acknowledge the fingerprint by typing "yes".

Finally, switch to the new remote by running the following command:

    amc remote set-default <your remote name>

All invocations of the `amc` command will from now on use the new remote.

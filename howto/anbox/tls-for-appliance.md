(howto-set-up-tls)=
# Set up TLS for the Anbox Cloud Appliance

The Anbox Cloud Appliance uses a self-signed certificate to provide HTTPS services. If you want to serve the appliance over HTTPS using a valid SSL/TLS certificate, follow the steps in this document to generate and install a valid SSL/TLS certificate on the Anbox Cloud Appliance.

If you run the appliance on AWS, you can choose to use the AWS Certificate Manager. Otherwise, you must manage the certificate yourself manually.

## Prerequisites

Before you start, make sure the following requirements are met:

- The Anbox Cloud Appliance is installed and initialized. See {ref}`howto-install-appliance-aws` and {ref}`sec-initialize-appliance` for instructions.

- A DNS name you can use to point to the machine hosting the Anbox Cloud Appliance

## Manage the certificate manually

To generate and install a certificate yourself, complete the following steps:

### Add a DNS record

Setting up DNS redirection depends on your DNS provider. Refer to the documentation of your provider to create a DNS record pointing to the IP/DNS of the machine where the Anbox Cloud Appliance is running.


(ref-appliance-tls-location)=
### Configure the location

Configure the location for the appliance using the created DNS name by running the following command:

    sudo anbox-cloud-appliance config set network.location=your.dns.name

The change will be automatically applied and will cause all services components of the appliance to restart. If you want to defer the restart to a later point, you can use the `--no-restart` option.

### Generate an SSL certificate

There are many ways to create a valid SSL certificate. One way is to use [Let's Encrypt](https://letsencrypt.org/) to generate a free SSL certificate.

First, connect and SSH into your appliance instance, and install the `certbot` snap:

    sudo snap install --classic certbot

Using `certbot` requires that TCP port 80 is not in use as it will use the port to verify your ownership of the requested DNS name. The Anbox Cloud Appliance only occupies TCP port 443. Please ensure that nothing is listening on the machine on TCP port 80 before you continue.

Then run the following command to generate your certificate:

    sudo certbot certonly --standalone

This command prompts you to enter the domain name for the certificate to be generated. You will see the following message when the certificate is created successfully:

```bash
Successfully received certificate.
Certificate is saved at: /etc/letsencrypt/live/<your domain name>/fullchain.pem
Key is saved at:         /etc/letsencrypt/live/<your domain name>/privkey.pem
This certificate expires on yyyy-MM-dd.
These files will be updated when the certificate renews.
Certbot has set up a scheduled task to automatically renew this certificate in the background.
```

### Install the SSL certificate

Copy the generated certificate to the `/var/snap/anbox-cloud-appliance/common/daemon` directory:

    sudo cp /etc/letsencrypt/live/<your domain name>/fullchain.pem /var/snap/anbox-cloud-appliance/common/daemon/server.crt
    sudo cp /etc/letsencrypt/live/<your domain name>/privkey.pem /var/snap/anbox-cloud-appliance/common/daemon/server.key

Then restart the appliance service to make it load the new key and certificate:

    sudo snap restart anbox-cloud-appliance.daemon

With the certificate installed on the appliance, you now can access the appliance using the created domain name and will be presented with a valid certificate.

### Renew the SSL certificate

The `certbot` snap packages installed on your machine would have already set up a systemd timer that automatically renews your certificates before they expire. However, to get the certificate renewed successfully for the appliance, you can create `post-start` hook for `certbot` which will automatically reconfigure it:

   ```bash
   cat <<EOF | sudo tee /etc/letsencrypt/renewal-hooks/post/001-start-appliance.sh
   #!/bin/bash
   sudo cp /etc/letsencrypt/live/<your domain name>/fullchain.pem /var/snap/anbox-cloud-appliance/common/daemon/server.crt
   sudo cp /etc/letsencrypt/live/<your domain name>/privkey.pem /var/snap/anbox-cloud-appliance/common/daemon/server.key
   sudo snap restart anbox-cloud-appliance.daemon
   EOF
   sudo chmod +x /etc/letsencrypt/renewal-hooks/post/001-start-appliance.sh
   ```

```{note}
The appliance will be restarted when the renewal of the SSL certificate is complete, to let the reverse proxy reload the certificate.
```


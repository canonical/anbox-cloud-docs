(howto-set-up-tls)=
# Set up TLS for the Anbox Cloud Appliance

The Anbox Cloud Appliance uses a self-signed certificate to provide HTTPS services. If you want to serve the appliance over HTTPS using a valid SSL/TLS certificate, follow the steps in this document to generate and install a valid SSL/TLS certificate on the Anbox Cloud Appliance.

```{note}
This document assumes you have the Anbox Cloud Appliance installed. If you haven't, follow the {ref}`tut-installing-appliance` tutorial to do so.
```

If you run the appliance on AWS, you can choose to use the AWS Certificate Manager. Otherwise, you must manage the certificate yourself manually.

## Manage the certificate yourself

To generate and install a certificate yourself, complete the following steps.

### 1. Add a DNS record

Setting up DNS redirection depends on your DNS provider. Refer to the documentation of your provider to create a DNS record pointing to the IP/DNS of the AWS instance where the Anbox Cloud Appliance is running.

### 2. Configure the location

Configure the location for the appliance using the created DNS name:

    sudo snap set anbox-cloud-appliance experimental.location=<your DNS name>

```{note}
This option is experimental. It will be removed in a future release when a better replacement exists.
```

### 3. Generate an SSL certificate

There are many ways to create a valid SSL certificate. One way is to use [Let's Encrypt](https://letsencrypt.org/) to generate a free SSL certificate.

First, connect and SSH into your appliance instance, and install the `certbot` snap:

    sudo snap install --classic certbot

Before generating your certificate using `certbot`, stop the Traefik service from listening on port 80 for the certificate creation:

    sudo snap stop anbox-cloud-appliance.traefik

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

### 4. Install the SSL certificate

Copy the generated certificate to the `/var/snap/anbox-cloud-appliance/common/traefik/tls` directory:

    sudo cp /etc/letsencrypt/live/<your domain name>/fullchain.pem /var/snap/anbox-cloud-appliance/common/traefik/tls/cert.pem
    sudo cp /etc/letsencrypt/live/<your domain name>/privkey.pem   /var/snap/anbox-cloud-appliance/common/traefik/tls/key.pem

Then start the Traefik service:

    sudo snap start anbox-cloud-appliance.traefik

With the certificate installed on the appliance, you now can access the appliance using the created domain name.

### Renew the SSL certificate

The `certbot` snap packages installed on your machine already set up a systemd timer that will automatically renew your certificates before they expire. However, in order to get the certificate renewed successfully for the appliance, you must complete the following steps:

1. Stop the Traefik service to release port 80 right before the certificate is going to be renewed. This can be done through the `pre-hook`:

   ```bash
   cat <<EOF | sudo tee /etc/letsencrypt/renewal-hooks/pre/001-stop-traefik.sh
   #!/bin/bash
   sudo snap stop anbox-cloud-appliance.traefik
   EOF
   sudo chmod +x /etc/letsencrypt/renewal-hooks/pre/001-stop-traefik.sh
   ```

2. Install the certificate right after it has been renewed and start the Traefik service through the `post-hook`:

   ```bash
   cat <<EOF | sudo tee /etc/letsencrypt/renewal-hooks/post/001-start-traefik.sh
   #!/bin/bash
   sudo cp /etc/letsencrypt/live/<your domain name>/fullchain.pem /var/snap/anbox-cloud-appliance/common/traefik/tls/cert.pem
   sudo cp /etc/letsencrypt/live/<your domain name>/privkey.pem   /var/snap/anbox-cloud-appliance/common/traefik/tls/key.pem
   sudo snap start anbox-cloud-appliance.traefik
   EOF
   sudo chmod +x /etc/letsencrypt/renewal-hooks/post/001-start-traefik.sh
   ```

In this way, the SSL certificate auto-renewal is in place.

```{note}
The appliance will face a short downtime during the renewal of the SSL certificate but will come back online once the process is completed.
```

## Use the AWS Certificate Manager

If you run the Anbox Cloud Appliance on AWS, you can use the [AWS Certificate Manager](https://aws.amazon.com/certificate-manager/) to provision and manage your TLS certificate.

Before you start, make sure the following requirements are met:

- You have a domain name for use with the Anbox Cloud Appliance registered, either through Amazon Route 53 (see [Register a new domain](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/domain-register.html) in the Amazon Route 53 documentation) or  through another domain provider.

  ```{note}
  The screenshots in the following instructions use an example domain name that is not owned or controlled by Canonical. Replace it with your own domain name when following the setup instructions.
  ```
- The Anbox Cloud Appliance is installed and initialised. See {ref}`howto-install-appliance-aws` and {ref}`sec-initialise-appliance` for instructions.

Then complete the following steps.

(sec-configure-routing-info-name-servers)=
### 1. Configure routing information and name servers

```{note}
You can skip this step if you registered your domain name through Amazon Route 53.
```

If you want to use a domain name that was not registered through Amazon Route 53, you must manually create a [public hosted zone](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/AboutHZWorkingWith.html) for it, and then make your domain use Amazon Route 53 as its DNS service. A public hosted zone contains routing information for the domain, and Amazon Route 53 uses it to determine to which machine it should route the traffic to your domain.

In the case of the Anbox Cloud Appliance, we want the traffic routed to the AWS load balancer which we will set up later in this guide.

1. To create a public hosted zone, follow the instructions in [Creating a public hosted zone](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/CreatingHostedZone.html) in the Amazon Route 53 documentation.

   The following example shows a public hosted zone for an example domain name. The two DNS records are added automatically after creation:

   ![AWS public hosted zone](https://assets.ubuntu.com/v1/28d5d0ad-manage_tls_public-hosted-zone.png)
1. To change the DNS service for your domain registration, you must specify the custom name servers that Amazon Route 53 allocated for the domain name. You can find them in the "NS" record for your public hosted zone.

   The following example shows the custom name servers for the example domain:

   ![Custom name servers in Amazon Route 53](https://assets.ubuntu.com/v1/2dfee5bd-manage_tls_custom-name-servers.png)

   Go to your domain provider and configure the DNS settings for your domain there. Specify the name servers listed in Amazon Route 53 as the custom name servers.

   The following example shows this configuration for the example domain:

   ![Configure custom name servers for your domain with your domain provider](https://assets.ubuntu.com/v1/433fdfd9-manage_tls_enter-nameservers.png)

### 2. Create a public certificate

To create a public certificate using the AWS Certificate Manager, you must first request a certificate and then validate that you own the domain that the certificate applies to.

1. To request the public certificate, follow the instructions in [Requesting a public certificate](https://docs.aws.amazon.com/acm/latest/userguide/gs-acm-request-public.html) in the AWS Certificate Manager documentation.

   The following example shows a certificate for the example domain name that is pending validation:

   ![Certificate that is pending validation](https://assets.ubuntu.com/v1/5caeac31-manage_tls_cname-record.png)
1. To validate the certificate, follow the instructions in [Validating domain ownership](https://docs.aws.amazon.com/acm/latest/userguide/domain-ownership-validation.html) in the AWS Certificate Manager documentation.

   Since you have a public hosted zone for your domain in Amazon Route 53 (see {ref}`sec-configure-routing-info-name-servers`), you can follow the steps for creating records in Route 53.

DNS propagation usually takes a while. When it completes and the validation is successful, the status of the certificate changes to issued, and it is ready to use.

![Valid certificate in AWS Certification Manager](https://assets.ubuntu.com/v1/b95943aa-manage_tls_certificate-status.png)

### 3. Create a load balancer

To use the Anbox Cloud Appliance through your domain name, AWS must route the HTTPS traffic for your domain to the Anbox Cloud Appliance. To ensure this, you must create a load balancer that listens for traffic and routes it to the appliance.

1. Go to the Load balancers page in the EC2 dashboard.
1. Click **Create load balancer**.
1. Choose `Application Load Balancer` as the load balancer type.
1. For the **Basic configuration**, keep the default options (scheme: internet-facing, IP address type: `IPv4`).
1. For the **Network mapping**, select the appropriate Availability Zones.
1. For the **Security groups**, use a new group with an inbound rule that allows only HTTPS traffic and the default outbound rule that allows all traffic.
1. For **Listeners and routing**, create a listener that will route traffic to the AWS instance that hosts the Anbox Cloud Appliance:

   1. Select `HTTPS` as the protocol.
   1. Click **Create target group**.
   1. Select `Instances` as the target type for the new target group.
   1. Enter a name for the target group.
   1. Select `HTTPS` as the protocol and specify port `443` (this is the destination port to which the traffic coming from the AWS load balancer is routed).
   1. For the remaining settings, leave the default values.
   1. Click **Next** to go to the **Register targets** page.
   1. Select the instance that runs the Anbox Cloud Appliance.
   1. Click **Include as pending below**.
   1. Review the target.

      The following example shows a target for the Anbox Cloud Appliance:

      ![Create a target group for the appliance](https://assets.ubuntu.com/v1/14995bdf-manage_tls_register-targets.png)
   1. Click **Create target group** to finish the target group creation.

1. Back in the **Listeners and routing** sections on the load balancer creation page, select the target group that you just created for the default action.
1. In the **Secure listener settings** section, select the public certificate that you created through the AWS Certificate Manager.

   ![Listener settings](https://assets.ubuntu.com/v1/3308aa3a-manage_tls_listener-settings.png)
1. Check the **Summary**, and if everything looks correct, click **Create load balancer**.

### 4. Direct traffic from your domain to the load balancer

When the load balancer is created, AWS assigns it an automatic DNS name. The following example shows where to find it:

![DNS name of the load balancer](https://assets.ubuntu.com/v1/040220cb-manage_tls_dns-name.png)

You now need to route the traffic that goes to your domain name to the load balancer.

1. Go to the [Route 53](https://console.aws.amazon.com/route53/) console.
1. Select your public hosted zone (which was created automatically if you registered your domain through Amazon Route 53, or which you created earlier in {ref}`sec-configure-routing-info-name-servers`).
1. Create a type `A` DNS record that routes the traffic that from the public hosted zone to the load balancer:

   1. Click **Create Record** and select `Simple routing`.
   1. Click **Define simple record**.
   1. Select `A - Route traffic to an IPv4 address and some AWS resources` as the record type.
   1. For **Value/Route traffic to**, select `Alias to the application and Classic load balancer`, the region where the load balancer is located and the name of the load balancer.

   The following example shows the record creation for the example domain:

   ![Define simple record](https://assets.ubuntu.com/v1/36bcce7f-manage_tls_a-record.png)

1. Click **Define simple record** to create the DNS record for your public hosted zone.

The following example shows the DNS record with type `A` for the example domain:

![DNS records for the public hosted zone](https://assets.ubuntu.com/v1/5a4986bd-manage_tls_dns-records.png)

### 5. Configure the appliance to use the domain name

Finally, configure the Anbox Cloud Appliance to use the domain name that you prepared.

1. Use SSH to connect to the AWS instance where the Anbox Cloud Appliance is running.
1. Run the following command to configure the location of the appliance:

   ```
   sudo snap set anbox-cloud-appliance experimental.location=<domain_name>
   ```
1. Start the `reboot-checker` service to let the core services (for example, the stream gateway) use the new domain name:

   ```
   sudo systemctl start snap.anbox-cloud-appliance.reboot-checker.service
   ```

You can now use the new domain name to access the Anbox Cloud Appliance.

The following example shows the certificate for the example domain:

![Certificate for the domain](https://assets.ubuntu.com/v1/cd4c0316-manage_tls_result.png)

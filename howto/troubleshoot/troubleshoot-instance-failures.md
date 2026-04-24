(howto-ts-instance-failures)=
# Troubleshoot instance failures

The following information should help you in determining issues related to instances.

## Images not available

*Applies to: Anbox Cloud, Anbox Cloud Appliance*

> I completed the installation and initialization process correctly. When I try creating an instance, I don't see any available images.

This issue occurs most likely because the Ubuntu Pro token was not attached before the appliance was initialized for the first time. Even when you attach the Ubuntu Pro token later on, the authentication to sync images from the media server is not set correctly and hence the images are inaccessible.

On the appliance, you can confirm this by running:

    amc config show | grep images.auth

If you are using the charmed deployment, you will need to first `ssh` into the machine:

    juju ssh ams/leader
    amc config show | grep images.auth

If `images.auth` is set to `false`, then the image authentication not being set properly is the issue. To correct the authentication and access images on the appliance, run:

    amc config set images.auth bearer:$(sudo cat /var/lib/ubuntu-advantage/private/machine-token.json | jq -r '.resourceTokens[] | select(.type=="anbox-images").token')

## Instance failed to start

*Applies to: Anbox Cloud, Anbox Cloud Appliance*

> An instance failed to start. Where can I find more information why it failed to start?

If an instance fails to start, its status is set to `error`. Anbox Management Service (AMS) automatically fetches several log files from the instance and makes them available for further inspection. The log files can provide information on why the instance failed to start. The reason for instance failure may not always be simple and easy to resolve because of a number of variable factors, for example, the application that the instance is hosting or any installed addons.

See {ref}`howto-view-instance-logs` for instructions on how to access the instance log files.

## Published application version not found

*Applies to: Anbox Cloud, Anbox Cloud Appliance*

> When launching an instance for an application, I get an error that mentions "published application version not found". Why?

If you launch an instance by only specifying the application ID and the application has no published version yet, you must explicitly specify the version that you want to launch or publish a version of the application. See {ref}`sec-launch-application-instances` and {ref}`sec-publish-app-versions` for more information.

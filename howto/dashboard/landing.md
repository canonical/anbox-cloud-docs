(howto-use-web-dashboard)=
# How to use the web dashboard
The Anbox Cloud Dashboard offers a web GUI that users can use to create, manage and stream applications from their web browser. If you have configured the Anbox Application Registry (AAR), you can also view applications in the registry using the **Registry** button on the main menu. You can use the pre-installed dashboard almost immediately after deploying Anbox Cloud.

## Prerequisites

Before you can log into the dashboard, you must register your Ubuntu One account with the dashboard to authenticate.

### Register an Ubuntu One account in Anbox Cloud

On a regular Anbox Cloud deployment, use the following Juju action to register an Ubuntu One account:

    juju run anbox-cloud-dashboard/0 --wait=5m register-account email=<Ubuntu One email address>

You will see output similar to the following:

```sh
unit-anbox-cloud-dashboard-0:
  UnitId: anbox-cloud-dashboard/0
  id: "157"
  results:
    Stdout: |
      Visit https://10.10.10.10/register?token=eyJ0...-Td7A to create the new user
  status: completed
  timing:
    completed: 2021-02-10 14:04:46 +0000 UTC
    enqueued: 2021-02-10 14:04:44 +0000 UTC
    started: 2021-02-10 14:04:44 +0000 UTC
```
(sec-register-ubuntu-one-appliance)=
### Register an Ubuntu One account in Anbox Cloud Appliance

If you followed the instructions in the {ref}`tut-installing-appliance` tutorial, you already registered your Ubuntu One account.

To add more accounts, use the following command:

    anbox-cloud-appliance dashboard register <Ubuntu One email address>

Accessing the resulting link will create the account and ask you to login via Ubuntu One. You only need to do this step once per user for access to the dashboard.

The generated link is valid for one hour.

## Using the dashboard

To access the dashboard, go to `https://<your-machine-address>/`. The dashboard uses self-signed certificates. You might see a warning from your browser and have to accept the certificates manually.

## Related topics

* {ref}`exp-aar`
* {ref}`exp-web-dashboard`

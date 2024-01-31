The topics in this guide describe some commonly encountered problems with Anbox Cloud and provide instructions for resolving them. If you encounter an issue with Anbox Cloud, check if any of the following scenarios help in resolving your issue.

[note type="information" status="Note"] If the deployment is older than 3 months, you must upgrade Anbox Cloud to the latest version and see if the required fixes are already part of the upgrade. See [How to upgrade Anbox Cloud](https://discourse.ubuntu.com/t/how-to-upgrade-anbox-cloud/17750) for upgrade instructions.[/note]

* [Troubleshoot issues with initial setup](https://discourse.ubuntu.com/t/35704)
* [Troubleshoot instance failures](https://discourse.ubuntu.com/t/35703)
* [Troubleshoot issues with application creation](https://discourse.ubuntu.com/t/35702)
* [Troubleshoot issues with LXD clustering](https://discourse.ubuntu.com/t/35705)
* [Troubleshoot issues with dashboard](https://discourse.ubuntu.com/t/36105)
* [Troubleshoot issues with streaming](https://discourse.ubuntu.com/t/31341)

If you still need help, use any of the following utilities to collect troubleshooting information and report an [issue](https://bugs.launchpad.net/anbox-cloud/+filebug).

[note type="information" status="Note"] The following utilities could be applicable for the regular Anbox Cloud deployed with Juju or for the Anbox Cloud Appliance or both. The *Applies to* tag in each section indicates whether it is applicable to a particular variant. To know more about Anbox Cloud variants, see [Variants](https://discourse.ubuntu.com/t/anbox-cloud/17802#variants-1).[/note]

## Juju crashdump

*Applies to: Anbox Cloud*

If you have the [`juju-crashdump` plugin](https://github.com/juju/juju-crashdump) installed, you can collect troubleshooting information from the deployment model. The Juju crash dump gives you a high level overview of the issue and is the recommended option to provide debugging information when you report an issue with your Anbox Cloud deployment.

A Juju crash dump may include the following debugging information:
* Additional information provided by the Anbox Cloud charms
* Information about any instances that crashed

Use the following command to generate a crash dump:

    juju crashdump -s -a debug-layer 

The Anbox Management Service (AMS) charm implements the `debug-layer` addon which will add a `debug-*.tar.gz` archive to the crash dump for the AMS units. The tarball may contain logs for the instances that are in `error` state in AMS and other information about the Anbox runtime process.

## `anbox-cloud-appliance.buginfo` command

*Applies to: Anbox Cloud Appliance*

Use the `anbox-cloud-appliance.buginfo` command to obtain debugging information for issues with the Anbox Cloud Appliance.

This is the recommended option to provide debugging information when you report an issue with the Anbox Cloud Appliance.

## Anbox Cloud bug report utility

*Applies to: Anbox Cloud, Anbox Cloud Appliance since 1.16.0*

In Anbox Cloud, instances come preinstalled with the `anbox-bug-report` utility, which
collects the log files and other relevant information for a specific instance.
To generate the report and save it to a local file, use `amc exec` on a running
instance:

```
amc exec <instance_id> -- bash -c 'cat "$(anbox-bug-report)"' > "<target_file>"
```

This command builds a zip archive that contains the instance report. It then
saves it to the local `<target_file>`. This process might take a few seconds.

## Stored instance logs

*Applies to: Anbox Cloud, Anbox Cloud Appliance*

If an instance fails to start or a runtime error occurs, AMS collects relevant log files from the instance and makes them available for inspection. 

Use `amc show <instance_id>` command to list the available logs. See [View stored logs](https://discourse.ubuntu.com/t/24329#view-stored-logs-2) for an example of such a stored log.

## Related topics

* [View Anbox Cloud logs](https://discourse.ubuntu.com/t/17771)
* [View instance logs](https://discourse.ubuntu.com/t/24329)

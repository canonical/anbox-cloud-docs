(howto-ts-anbox-cloud)=
# Troubleshoot Anbox Cloud

The following troubleshooting guides describe some commonly encountered problems with Anbox Cloud and provide instructions for resolving them. If you encounter an issue with Anbox Cloud, check if any of the following scenarios help in resolving your issue.

```{toctree}
:titlesonly:

Instance failures <troubleshoot-instance-failures>
Issues with application creation <troubleshoot-application-creation>
Issues with clustering <troubleshoot-cluster-issues>
Issues with initial setup <troubleshoot-initial-setup>
Issues with streaming <troubleshoot-streaming-issues>
Issues with web dashboard <troubleshoot-dashboard-issues>
view-logs
```

```{note}
If the deployment is older than 3 months, you must upgrade Anbox Cloud to the latest version and see if the required fixes are already part of the upgrade. See {ref}`howto-upgrade-anbox-cloud` for upgrade instructions.
```

If you still need help, use any of the following utilities to collect troubleshooting information and report an [issue](https://bugs.launchpad.net/anbox-cloud/+filebug).


The following utilities could be applicable for the charmed Anbox Cloud deployed with Juju or for the Anbox Cloud Appliance or both. The *Applies to* tag in each section indicates whether it is applicable to a particular variant. To know more about Anbox Cloud variants, see {ref}`sec-variants`.

(sec-bug-report)=
## Bug report diagnostic facility

*Applies to: Anbox Cloud, Anbox Cloud Appliance*

Since 1.28.0, you can download a bug report bundle that contains files necessary to troubleshoot issues you may be facing.

This diagnostic facility is available in the Anbox Cloud dashboard from the streaming and the instance details pages. Depending on where you download the bug report from, the files in the download bundle will vary.

When you download the bug report from the *Stream page > Actions > Bug Report* menu, the report gives you logs from the Anbox and Android instances, metrics data from Anbox, the event logs from the WebRTC connection, WebRTC statistics, metadata from the dashboard. These help you diagnose any issues with the stream or your connection.

When you download from the *Instance details page > Bug Report*, the report gives you all the files except the ones related to the WebRTC statistics and connection event logs. This is the bug report you need to download when your instance is in an error state.

## Juju crashdump

*Applies to: Anbox Cloud*

If you have the [`juju-crashdump` plugin](https://github.com/juju/juju-crashdump) installed, you can collect troubleshooting information from the deployment model. The Juju crash dump gives you a high level overview of the issue and is the recommended option to provide debugging information when you report an issue with your Anbox Cloud deployment.

A Juju crash dump may include the following debugging information:
* Additional information provided by the Anbox Cloud charms
* Information about any instances that crashed

Use the following command to generate a crash dump:

    juju-crashdump -s --as-root -a debug-layer

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

Use `amc show <instance_id>` command to list the available logs. See {ref}`howto-view-instance-logs` for information on viewing the instance logs.

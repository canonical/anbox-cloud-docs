(howto-upgrade-appliance)=
# How to Upgrade the Appliance

The upgrade process for the Anbox Cloud Appliance is as simple as updating the snap package to the appropriate channel. Before upgrading the appliance, consider the changes that the new version brings as downgrades are not supported.

If you are on the `latest` track, upgrade to the newest snap version by running:

    sudo snap refresh anbox-cloud-appliance

Automatic updates may install the new version without manual intervention.

For installations on a versioned track (e.g. 1.25), change the track explicitly with:

    sudo snap refresh --channel=1.26/stable anbox-cloud-appliance

After refreshing the snap, the appliance will automatically apply the necessary configuration changes and restart services as needed.

For the host system, run the upgrade script manually. This script performs additional updates, including:

1. Upgrading Anbox Cloud-specific kernel modules.
2. (If a GPU is available) Upgrading GPU driver packages from the Ubuntu archive and applying required tuning settings.

Review the upgrade script by running:

    anbox-cloud-appliance upgrade-node-script

Then execute the script with:

    anbox-cloud-appliance upgrade-node-script | sudo bash -ex

After the script completes, verify the output to determine if a system reboot is necessary.



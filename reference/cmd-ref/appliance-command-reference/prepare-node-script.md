---
orphan: true
---
# `prepare-node-script`

The `prepare-node-script` generates a shell script which needs to be executed outside of the snap execution environment to install additional dependency and adjust system configuration.

Please carefully review the script before execution! It will install additional kernel modules and GPU drivers and apply configuration changes to tune these for Anbox Cloud.

You can show the script by running

    $ anbox-cloud-appliance prepare-node-script

and execute it after reviewing the content by

    $ anbox-cloud-appliance prepare-node-script | sudo bash -ex

Once the script has finished all preparation is completed.

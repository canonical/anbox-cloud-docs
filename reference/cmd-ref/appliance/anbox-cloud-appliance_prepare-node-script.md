## anbox-cloud-appliance prepare-node-script

Generate a shell script to prepare or upgrade a machine for the Anbox Cloud Appliance

### Synopsis

Generate a shell script to prepare or upgrade a machine for the Anbox Cloud Appliance

The command generates a shell script which needs to be executed outside
of the snap execution environment to install additional dependency and
adjust system configuration.

Please carefully review the script before execution! It will install
additional kernel modules and GPU drivers and apply configuration
changes to tune these for Anbox Cloud.

You can show the script by running

  $ anbox-cloud-appliance prepare-node-script

and directly execute it after reviewing the content by

  $ anbox-cloud-appliance prepare-node-script | sudo bash -ex

Once the script has finished all preparation is completed.


```
anbox-cloud-appliance prepare-node-script [flags]
```

### Examples

```
$ anbox-cloud-appliance prepare-node-script
```

### Options

```
      --force-nvidia   Force including NVIDIA GPU driver installation steps even if no GPU is detected
  -h, --help           help for prepare-node-script
```

### SEE ALSO

* [anbox-cloud-appliance](anbox-cloud-appliance.md)	 - Anbox Cloud Appliance, bringing Android at scale to any cloud


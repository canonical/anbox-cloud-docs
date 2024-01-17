The `destroy` command deletes the deployment that the Anbox Cloud Appliance has created on a machine. If you want to uninstall the Anbox Cloud Appliance, you must first run this command before you uninstall the snap.

    anbox-cloud-appliance destroy <options>

[note type="caution" status="Warning"]This command resets the Anbox Cloud Appliance and destroys all data. Execution of the command cannot be stopped or reverted. Hence, before destroying a deployment, ensure to backup all necessary data.[/note]

## Options

`--force` to force the destroy process on non interactive terminals
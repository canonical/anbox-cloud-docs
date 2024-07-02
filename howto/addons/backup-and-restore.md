(howto-backup-restore-example)=
# Example: Back up data
When an instance is stopped, all the data and logs produced during the runtime are lost. To avoid this, you can use hooks to back up and restore any type of data you want.

## Back up data

In this example, we create a backup hook that uploads logs onto a cloud storage if Android terminated with an error.

Add the following `post-stop` hook to a new or existing addon:
```bash
#!/bin/sh -ex

# Don't upload logs if no error happened
if [ "$ANBOX_EXIT_CODE" = 0 ]; then
  exit 0
fi

FILE_NAME=container-logs.tar.bz2
(cd /var/lib/anbox/logs; tar cvjf ../"${FILE_NAME}" *)
# Upload the tarball to a public or private cloud storage service
curl -i -X POST --data-binary @"${FILE_NAME}" <cloud_storage_upload_url>
```

## Restore data

In this example, we create a hook that restores some user application data.

Add the following `pre-start` hook to a new or existing addon:
```bash
#!/bin/sh -ex

# Download the tarball from a public or private cloud storage service
if curl -o app-data.tar.bz2 <cloud_storage_download_url> ; then
  tar xvjf app-data.tar.bz2 -C /var/lib/anbox/data/data/com.foo.bar
fi
```

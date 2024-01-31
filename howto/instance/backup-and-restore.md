Backup and restoration of application data can be achieved easily with the `aam`  (Anbox Application Manager) utility helper installed in the image. The `aam` can bundle any necessary application data together into a tarball file or extract the tarball file to a particular application folder according to the specified package name.

## Back up application data

See the following script for an example for backing up your data:

```bash
 #!/bin/sh -ex
aam backup com.canonical.candy
TARBALL_FILE=$(basename $(find ./ -name *.tar.bz2))
 # Upload the tarball to public or private cloud storage service
curl -i -X POST --data-binary @"${TARBALL_FILE}" <cloud_storage_upload_url>
```
Running this script in an [addon post-stop hook](https://discourse.ubuntu.com/t/example-back-up-data/25289) will back up the user data of a particular application with `aam` and upload the resulting tarball file to the cloud storage service when an instance is stopped.

If [`boot-package`](https://discourse.ubuntu.com/t/application-manifest/24197) is specified in the application manifest file, you can also back up the boot application data simply with the flag `--boot-package`.

    aam backup --boot-package


`aam` will automatically query the boot package name from the instance and back up the relevant application data. As result `aam` will create a tarball file with the name `<package name>.tar.bz2`.

## Restore application data

The application data can be restored with the following [pre-start hook](https://discourse.ubuntu.com/t/example-back-up-data/25289#restore-data-2) when an instance is up and running:

```bash
#!/bin/sh -ex
# Download the tarball from public or private cloud storage service
if curl -o app-data.tar.bz2 <cloud_storage_download_url> ; then
  aam restore -p app-data.tar.bz2 com.canonical.candy
fi
```

Or by relying on the boot package of the instance:

    aam restore -p app-data.tar.bz2 --boot-package

## Filter data to be backed up

Sometimes, not every piece of data is useful (for example, cache), and backing up the entire application data takes a long time and occupies more disk space if the application data is large. `aam` supports two filters to back up files that match wildcard patterns:

 Filter      |  Description
-------------|--------------------------------------------------------------------
`include`    | Include files in resulting tarball with a wildcard
`exclude`    | Exclude files in resulting tarball with a wildcard

Please refer to the pattern syntax [here](https://golang.org/pkg/path/filepath/#Match).

For example, with the following filters:

```bash
aam backup com.canonical.candy \
   --include=/data/data/com.canonical.candy/cache/*.db \
   --include=/data/data/com.canonical.candy/new_level/fixture* \
   --exclude=/sdcard/Android/data/com.canonical.candy/user_data/*.jpeg \
   --exclude=/data/data/com.canonical.candy/new_level/*.cfg
```

The resulting tarball file will include the following files:

- Files with `db` suffix below the folder `/data/data/com.canonical.candy/cache`
- Files with `fixture` prefix below the folder `/data/data/com.canonical.candy/new_level`

And exclude the following files:

* Files with `jpeg` suffix below the folder `/sdcard/Android/data/com.canonical.candy/user_data`
* Files with `cfg` suffix below the folder `/data/data/com.canonical.candy/new_level`

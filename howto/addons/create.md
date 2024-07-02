(howto-create-addons)=
# How to create an addon

To create or update an addon, you need a specific file structure for the directory containing your addon files. In the directory where you created your addon files, also create the following:

- A file named `manifest.yaml`. See {ref}`ref-addon-manifest` to learn about valid keys in an addon manifest file.
- A directory named `hooks`. This directory must contain at least one executable file with a valid hook name.

Other files in the addon directory are bundled with the addon. They can be accessed in a hook by using the `$ADDON_DIR` environment variable. See {ref}`sec-env-variables` for more information.

For example:

```bash
cat "$ADDON_DIR"/public_key.pem >> ~/.ssh/authorized_keys
```

To create an addon, you must provide the Anbox Management Client (AMC) with either of the following:
* The addon directory
* A tarball containing the required addon file structure
* A zip archive containing the required addon file structure
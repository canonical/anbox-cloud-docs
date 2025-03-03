(howto-addons)=
# How to manage addons

In Anbox Cloud, addons can be used to customize images that are used for instances. See {ref}`exp-addons` and {ref}`ref-addon-manifest` to learn about addons in detail.

You can use addons to, for example:
- Enable SSH access for automation tools (see {ref}`howto-create-addon`)
- Set up user-specific data when starting an application (see {ref}`howto-backup-restore-example`)
- Install additional tools in the instance (see {ref}`howto-install-tools-example`)
- Back up data when the instance is stopping (see {ref}`howto-backup-restore-example`)
- Configure the Android system before running the application (see {ref}`howto-customize-android-example`)
- Provide support for other platforms (see {ref}`howto-emulate-platforms-example`)

If you have used addons before Anbox Cloud 1.12, see {ref}`howto-migrate-addons` to update your addons to use the new hooks.

```{toctree}
:hidden:


Create an addon <create-addon>
Enable an addon globally <enable-addons-globally>
Migrate addons <migrate-addon>
Update addons <update-addon>
Examples <examples>
```

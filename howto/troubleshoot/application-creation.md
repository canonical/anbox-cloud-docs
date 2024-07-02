(howto-ts-application-creation-issues)=
# Troubleshoot issues with application creation

You might encounter the following issues when creating an application.

## Application manifest

*Applies to: Anbox Cloud, Anbox Cloud Appliance*

> Is there an automatic way to create a manifest for an application?

No. The application manifest describes necessary metadata on top of the APK, which AMS needs. You can simplify the manifest to only contain the `name` and `instance-type` fields or the `name` and `resources` fields, but you will lose a lot of control about how your application is being executed.

## No such file or directory

*Applies to: Anbox Cloud, Anbox Cloud Appliance*

> When creating an application, I get an error that there is “no such file or directory”. Why?

Due to Snap strict confinement, the directory, the tarball file, or the zip archive file must be located in the home directory. There is no workaround for this requirement. The same requirement applies to addon creation.
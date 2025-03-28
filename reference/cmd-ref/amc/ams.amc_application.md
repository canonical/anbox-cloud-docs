## ams.amc application

Manage applications

### Synopsis

Manage applications.

Applications are the centrepiece of Anbox Cloud.

An application usually encapsulates one Android application and manages it
within the cluster.
The application installs the supplied APK to make it available to users.
Applications can be updated, pushed to a central registry and more.
See https://documentation.ubuntu.com/anbox-cloud/en/latest/explanation/applications/ for more information.

Android applications must go through a bootstrap process before they can
run on Anbox Cloud. This bootstrap process helps to improve the performance
and decrease the boot times.

Applications are versioned. Every time you update an application, its version
number is incremented. Application versions are not automatically published.
While you can launch an unpublished application, it is recommended to do so
only for testing purposes.

Once ready for use, you can publish a specific version. It will then be used
for any container launched for the application.


### Options

```
  -h, --help   help for application
```

### SEE ALSO

* [ams.amc](ams.amc.md)	 - Anbox Management Client
* [ams.amc application create](ams.amc_application_create.md)	 - Create an application
* [ams.amc application delete](ams.amc_application_delete.md)	 - Delete an application
* [ams.amc application list](ams.amc_application_list.md)	 - List created applications
* [ams.amc application publish](ams.amc_application_publish.md)	 - Mark an application version as published
* [ams.amc application revoke](ams.amc_application_revoke.md)	 - Revoke a published application version
* [ams.amc application set](ams.amc_application_set.md)	 - Update fields for an application
* [ams.amc application show](ams.amc_application_show.md)	 - Show information about a specific application
* [ams.amc application unset](ams.amc_application_unset.md)	 - Reset an application field
* [ams.amc application update](ams.amc_application_update.md)	 - Update an existing application


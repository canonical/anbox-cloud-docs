The following information should help you in determining why your instance failed.

## More information on instance failures

*Applies to: Anbox Cloud, Anbox Cloud Appliance*

> An instance failed to start. Where can I find more information why it failed to start?

If an instance fails to start, its status is set to `error`. Anbox Management Service (AMS) automatically fetches several log files from the instance and makes them available for further inspection. The log files can provide information on why the instance failed to start. The reason for instance failure may not always be simple and easy to resolve because of a number of variable factors, for example, the application that the instance is hosting or any installed addons.

See [How to view the instance logs](https://discourse.ubuntu.com/t/24329) for instructions on how to access the instance log files.

## Published application version not found

*Applies to: Anbox Cloud, Anbox Cloud Appliance*

> When launching an instance for an application, I get an error that mentions "published application version not found". Why?

If you launch an instance by only specifying the application ID and the application has no published version yet, you must explicitly specify the version that you want to launch or publish a version of the application. See [How to launch application instances](https://discourse.ubuntu.com/t/24327#launch-application-instances-1) and [How to publish application versions](https://discourse.ubuntu.com/t/update-an-application/24201#publish-application-versions-1) for more information.
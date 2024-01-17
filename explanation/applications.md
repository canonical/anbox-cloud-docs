Applications are one of the main objects managed by Anbox Management Service (AMS). A single application encapsulates one Android APK ([Android Package Kit](https://en.wikipedia.org/wiki/Android_application_package)) and manages it within the cluster. It takes care of installing the supplied APK and making it available to users. AMS also manages updates to existing applications, which includes allowing the operator to test new uploaded versions before making them available to any users.

## Application requirements
To run on the Anbox Cloud platform, applications must fulfil the following requirements:

* The application **SHOULD NOT** download any additional resources on regular startup to contribute to short startup times. If additional resources need to be downloaded, this can be done during the application bootstrap phase.
* The application **MUST NOT** require the **Google Play services** to be available as Anbox Cloud does not include them.

If your application fulfils these requirements but you are still having issues running it on Anbox Cloud, file a [bug report](https://bugs.launchpad.net/indore-extern/+filebug).

<a name="bootstrap"></a>
## Bootstrap process

When [creating an application](https://discourse.ubuntu.com/t/create-an-application/24198) from a directory, a tarball, or a zip archive, AMS will perform a bootstrap process, which builds the application and synchronises it across all LXD nodes in the cluster. There are major benefits that the bootstrap process provides:

  * It enables AMS to launch an instance for an application without installing the APK every time.
  * It dramatically speeds up the startup time of a regular instance.

Furthermore, an application is synchronised within the LXD cluster, which enables AMS to continue to work when nodes are being removed from the cluster through [scaling down](https://discourse.ubuntu.com/t/scale-down-a-lxd-cluster/24323) or lost from the cluster unexpectedly.

A temporary base instance is created and used for bootstrapping during the application creation. For example, you might see the following output for `amc ls` right after creating an application:

```bash
+----------------------+-------------+------+----------+------+---------------+-----------+
|          ID          | APPLICATION | TYPE |  STATUS  | NODE |    ADDRESS    | ENDPOINTS |
+----------------------+-------------+------+----------+------+---------------+-----------+
| bq78a3oj1qm02cebmof0 |    candy    | base | prepared | lxd0 | 192.168.100.2 |           |
+----------------------+-------------+------+----------+------+---------------+-----------+
```

In general, the bootstrap process goes through the following steps in order:

1. Configure the network interface and gateway.
2. Apply any pending Ubuntu system security updates.
3. Install [addons](https://discourse.ubuntu.com/t/addons/25293) listed in the application manifest file.
4. Run the `pre-start` hook provided by each addon listed in the application manifest.
5. Launch the Android container.
6. Install the APK provided by the application.
7. Grant the application permissions as requested in the application manifest.
8. Install the extra data as listed in the application manifest.
9. Execute the `post-start` hook provided by each addon listed in the application manifest.

![Application bootstrap process|571x653](https://assets.ubuntu.com/v1/7eed04fd-application-bootstrap.png)

The bootstrap process fails if one or more of the following situations happen:

* If one of the steps in the bootstrap process fails, AMS will interrupt the bootstrap process and hence the entire process fails. As a result, the status of the base instance will be set to `error` and the application status is set to `error` as well.

* An application crash or ANR upon APK installation causes the bootstrap process to terminate abnormally and the application status is set to `error`.

* The bootstrap process is limited to a maximum duration of 15 minutes. If it takes longer, the bootstrap process is aborted and the instance status is set to `error`.

When a base instance runs into an `error` status, you can find the issue by checking the error message with `amc show <instance ID>`:

```bash
id: bq78a3oj1qm02cebmof0
name: ams-bq78a3oj1qm02cebmof0
status: error
node: lxd0
created_at: 2019-08-09T02:11:33Z
application:
    id: bq6ktjgj1qm027q585kg
network:
    address: ""
    public_address: ""
    services: []
stored_logs:
- container.log
- system.log
- android.log
error_message: 'Failed to install application: com.foo.bar: Failed to extract native libraries, res=-113'
config: {}
```

Alternatively, [check the instance logs](https://discourse.ubuntu.com/t/24329) to troubleshoot problems in an instance.

When the application bootstrap succeeds, the base instance is automatically removed and the status of the application changes to `ready` indicating that the application is ready to use.

## Related information
* [Application manifest](https://discourse.ubuntu.com/t/application-manifest/24197)
* [How to create an application](https://discourse.ubuntu.com/t/create-an-application/24198)
* [How to wait for an application](https://discourse.ubuntu.com/t/wait-for-an-application/24202)
* [How to update an application](https://discourse.ubuntu.com/t/update-an-application/24201)
* [How to configure available resources](https://discourse.ubuntu.com/t/configure-available-resources/24960)
* [How to delete an application](https://discourse.ubuntu.com/t/delete-an-application/24199)
* [How to list applications](https://discourse.ubuntu.com/t/list-applications/24200)
* [How to test your application](https://discourse.ubuntu.com/t/usecase-application-testing/17775)
* [How to create a virtual device](https://discourse.ubuntu.com/t/virtual-devices/19069)

## Session with an Error status

*Applies to: Anbox Cloud, Anbox Cloud Appliance*

On the **Sessions** page, you could see a session with an **Error** status when there are not enough resources to start a streaming session. 

![Session with an Error status|690x440](https://assets.ubuntu.com/v1/43e5fac7-session-error.png)

Try the following actions:
* Verify if you have [sufficient resources](https://discourse.ubuntu.com/t/capacity-planning/28717) for instance/application creation.
* Check if all the nodes are in [`unschedulable`](https://discourse.ubuntu.com/t/ams-configuration/20872) mode.

## Session does not start

*Applies to: Anbox Cloud, Anbox Cloud Appliance*

A session does not start and the session details page displays the following error:

![Session does not start|690x440](https://assets.ubuntu.com/v1/4658bad5-session-does-not-start.png)

[Check the instance logs](https://discourse.ubuntu.com/t/24329) to find reasons for the session failure.


## Instances(s) in Error status

*Applies to: Anbox Cloud, Anbox Cloud Appliance*

The **Instances** list page shows instances with Error status.

![Instance in Error status|690x440](https://assets.ubuntu.com/v1/62cc57f1-instance-list-error.png)

An instance can end up with an error status due to various reasons. It may not always be simple and easy to resolve this because of the variable factors involved, for example, the application that the instance is hosting or any installed addons.

Click on the corresponding **INSTANCE ID** and check the instance details page for any possible error messages. The instance details page has an **Error Message** field that could be useful.

![Instance details page|690x440](https://assets.ubuntu.com/v1/590c9eea-instance-details-error.png)

The **Error Message field** can give you a starting point for identifying the issue. Some reasons for an instance to go into error status could be:
* Insufficient resources. Refer [Capacity planning](https://discourse.ubuntu.com/t/capacity-planning/28717).
* Occasionally, access to Ubuntu archives could be a problem when creating an application. As an immediate workaround, you could disable the security update by running `amc config set instance.security_updates false` or explicitly set `amc config set instance.api_mirror <mirror_address>` to configure an instance to use a different APT mirror. See [AMS configuration](https://discourse.ubuntu.com/t/ams-configuration/20872) for more details.
 
If the reason for the instance failure is not obvious from the **Error Message**, check the **Logs** tab for more information.

## Logs unavailable for an instance

*Applies to: Anbox Cloud, Anbox Cloud Appliance*

![Instance logs unavailable|690x440](https://assets.ubuntu.com/v1/9b3d4959-logs-unavailable-for-instance.png)

Logs are unavailable for an instance when:
* The instance is not in error status.
* Occasionally, the instance could have ended up with an error status due to insufficient resources but there are no log files because the application bootstrap process succeeded.

Normally, the logs are available if the instance is in an error state. If the instance is in the error state and yet there are no logs available, [check if you have enough resources](https://discourse.ubuntu.com/t/capacity-planning/28717).

## Terminal is unavailable for an instance

*Applies to: Anbox Cloud, Anbox Cloud Appliance*

![Terminal unavailable for instance|690x440](https://assets.ubuntu.com/v1/3c745aa3-terminal-unavailable-for-instance.png)

Terminal is not available if the instance has any other status apart from **running** and **started**.
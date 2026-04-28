(howto-ts-web-dashboard)=
# Troubleshoot issues while using the web dashboard

You might encounter the following issues when using the dashboard.

## Error while streaming

*Applies to: Anbox Cloud, Anbox Cloud Appliance*

Streaming can fail when there are not enough resources to start a streaming session.

Try the following actions:

- Verify if you have sufficient resources for instance/application creation. See {ref}`exp-capacity-planning` for more information.
- Check if all the nodes are in `unschedulable` mode. See {ref}`sec-node-configuration` for more information.

## Session does not start

*Applies to: Anbox Cloud, Anbox Cloud Appliance*

A session does not start and the session details page displays the following error:

    Anbox stream failed
    failed to communicate with the signaler: There was an error with the websocket, check debug console for more information

See {ref}`howto-view-instance-logs` to find reasons for the session failure.

## Instances(s) in Error status

*Applies to: Anbox Cloud, Anbox Cloud Appliance*

The *Instances* page of the dashboard shows instances with *Error* status.

An instance can end up with an error status due to various reasons. It may not always be simple and easy to resolve this because of the variable factors involved, for example, the application that the instance is hosting or any installed addons.

The error message tooltip can give you a starting point for identifying the issue. Some reasons for an instance to go into error status could be:

- Insufficient resources. Refer to {ref}`exp-capacity-planning`.
- Occasionally, access to Ubuntu archives could be a problem when creating an application. As an immediate workaround, you could disable the security update by running `amc config set instance.security_updates false` or explicitly set `amc config set instance.api_mirror <mirror_address>` to configure an instance to use a different APT mirror. See {ref}`ref-ams-configuration` for more details.

If the reason for the instance failure is not obvious from the error message, check the *Logs* tab for more information.

## Logs unavailable for an instance

*Applies to: Anbox Cloud, Anbox Cloud Appliance*

Logs are unavailable for an instance when:

- The instance is not in error status.
- Occasionally, the instance could have ended up with an error status due to insufficient resources but there are no log files because the application bootstrap process succeeded.

Normally, the logs are available if the instance is in an error state. If the instance is in the error state and yet there are no logs available, check if you have enough resources. See {ref}`exp-capacity-planning` for more information.

## Terminal is unavailable for an instance

*Applies to: Anbox Cloud, Anbox Cloud Appliance*

Terminal is not available if the instance has any other status apart from *running* and *started*.

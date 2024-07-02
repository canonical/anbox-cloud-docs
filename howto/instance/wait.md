(howto-wait-for-instance)=
# How to wait for an instance

When launching an instance, the instance should not be considered started until it reaches the running state. Sometimes if you want to interact with the instance (with the `amc shell` command, for example), you must wait until the instance reaches a `running` status.

The `amc wait` command allows to wait for an instance to reach a specific condition. If the condition is not satisfied within the specified time (five minutes by default), a timeout error will be returned by AMS.

The supported conditions for an instance are as follows:

Name            |  Value
----------------|------------
`app`           |  Application name or ID
`type`          |  Type of the instance, possible values: "base", "regular"
`node`          |  Node on which the instance runs
`status`        |  instance status, possible values: "created", "prepared", "started", "stopped", "running", "error", "deleted", "unknown"

For example, to wait for the instance to reach state `running`:

    amc wait -c status=running bdpaqaqhmss611ruq6kg

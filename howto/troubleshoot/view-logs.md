(howto-ts-view-logs)=
# How to view logs

There are two types of logs that help you understand what is happening in your Anbox Cloud installation:

- Logs for the applications that you are running, on a cluster or node level. See {ref}`howto-view-instance-logs` for more information.
- Infrastructure logs for the deployment. These logs differ depending on whether you run the charmed Anbox Cloud deployment or the Anbox Cloud Appliance. See the following sections for more information.

## View logs for Anbox Cloud

The Anbox Cloud deployment has centralized logging set up as default. Each unit in your cluster automatically sends logging information to the controller based on the current [logging level](#logging-level). You can use the Juju command line to easily inspect these logs and to change the logging level.

To view the logs from the current controller and model, simply run:

    juju debug-log

The default behavior is to show the last 10 entries and to tail the log (so you will need to terminate the command with `Ctrl-C`).

The output is in the following form:

    <entity> <timestamp> <log-level> <module>[:<line-no>] <message>

For example, a typical line of output might read:

    unit-ams-0: 18:04:11 INFO juju.cmd running jujud [2.4.2 gc go1.10]

The entity is the unit, machine or application the message originates from (in this case `ams/0`). It can be very useful to filter the output based on the entity or log level, and the debug-log command has many options.

For a full description, run the command `juju help debug-log` or see the Juju documentation.

### View historical logs

To view the last 100 entries and tail the log, use the following command:

    juju debug-log -n 100

To show the last 20 entries and exit:

    juju debug-log -n 20 --no-tail

To replay the log from the very beginning, but filter to logs from `ams/0`:

    juju debug-log --replay --include=ams/0

### View logs live

It is also possible to view logs directly on the running machine, if needed. A user with SSH access can connect to the relevant machine and find the logs for all the units running on that machine in the directory `/var/logs/juju`. The `juju ssh` command can be used for this, and you can connect to the relevant machine using a unit identifier. So for example, to look at the logs on the machine running the first unit of `ams`, log on to the machine with `juju ssh ams/0` and run the following command:

    ls /var/logs/juju/

The result should show something similar to:

    machine-1.log  machine-lock.log  unit-ams-node-controller-0.log unit-ams-0.log

Note that the logs from other units (in this case `ams-node-controller`) running on this machine can also be found here.

### Check logging level

You can check the current logging level by running the following command:

    juju model-config logging-config

This will result in output similar to:

    <root>=WARNING;unit=DEBUG

This is the default for any Juju model. It indicates that the machine log level is set to `WARNING` and the unit logging level is set to `DEBUG`. As all the software components of your Anbox cluster run in units, these logs are likely to be useful for diagnosing issues with software.

The logging levels, from most verbose to least verbose, are as follows:

* `TRACE`
* `DEBUG`
* `INFO`
* `WARNING`
* `ERROR`

The logging level can be set like this:

    juju model-config logging-config="<root>=WARNING;unit=TRACE"

This command sets the logging level for all units to `TRACE`.

Do not leave the logging level at `TRACE` for longer than you need. Verbose logging not only consumes network bandwidth but also fills up the database on the controller.

## View logs for the Anbox Cloud Appliance

The Anbox Cloud Appliance is deployed on one machine, so all relevant logs are located on that machine.

If you encounter any problems, check the following logs:

- The system log of the host machine
- `/var/lib/anbox-cloud-appliance/common/logs/bootstrap.log` for installation issues
- `/var/lib/anbox-cloud-appliance/common/logs/upgrade.log` for upgrade issues
- The output of the `anbox-cloud-appliance.buginfo` command

## Aggregate logs

When monitoring your deployment, it is a good idea to centralize all logs in a log aggregator to spot issues early.
Below is a non-exhaustive list of useful log files as well as which machine they can be found on.

| Log file location/command                                                                                                             | Machine                                                                                                                             | Description                                                         |
|---------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------|
| `/var/snap/lxd/common/lxd/logs/ams-*/console.log`                                                                                     | Any LXD node                                                                                                                        | LXD logs for a specific instance                                   |
| `journalctl -u anbox.service`                                                                                                         | Within an AMS instance (accessible from an addon or an agent installed in the instance), or by running `amc logs <id>`            | Anbox logs                                                          |
| `/var/lib/anbox/logs`                                                                                                                 | Within an AMS instance (accessible from an addon or an agent installed in the instance)                                           | instance-related logs for a single instance                       |
| `/var/lib/anbox/data/logs`                                                                                                            | Within an AMS instance (accessible from an addon or an agent installed in the instance), or by running `amc logs <id> -t android` | Android-related logs for a single instance                         |
| `/var/log/syslog`, `journalctl -u snap.ams.ams.service`, `snap logs -n all ams`                                                       | On any machine hosting AMS (e.g. `ams/0`)                                                                                           | Logs for the AMS daemon                                             |
| `/var/log/syslog`, `journalctl -u snap.anbox-stream-agent.anbox-stream-agent.service`, `snap logs -n all anbox-stream-agent`          | On any machine hosting the Anbox Stream Agent (e.g. `anbox-stream-agent/0`)                                                         | Logs for the Anbox Stream Agent daemon                              |
| `/var/log/syslog`, `journalctl -u snap.anbox-stream-agent.anbox-stream-gateway.service`, `snap logs -n all anbox-stream-gateway`      | On any machine hosting the Anbox Stream Gateway (e.g. `anbox-stream-gateway/0`)                                                     | Logs for the Anbox Stream Gateway daemon                            |
| `/var/log/syslog`, `journalctl -u snap.anbox-cloud-dashboard.anbox-cloud-dashboard.service`, `snap logs -n all anbox-cloud-dashboard` | On any machine hosting the Anbox Cloud web dashboard (e.g. `anbox-cloud-dashboard/0`)                                               | Logs for the web dashboard                                          |
| `/var/log/syslog`, `journalctl -u snap.nats.server.service`, `snap logs -n all nats`                                                  | On any machine hosting NATS (e.g. `nats/0`)                                                                                         | Logs for the NATS communication queue                               |
| `/var/log/syslog`, `journalctl -u snap.etcd.etcd.service`, `snap logs -n all etcd`                                                    | On any machine hosting etcd (e.g. `etcd/0`)                                                                                         | Logs for the etcd database (useful when AMS operations are failing) |
| `/var/log/juju/*`, `juju debug-log`                                                                                                   | Any machine managed by Juju and on the machine hosting the controller for `juju debug-log`                                          | Juju logs of all units hosted on the machine                        |

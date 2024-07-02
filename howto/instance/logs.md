(howto-view-instance-logs)=
# How to view the instance logs

You can view the Anbox and the Android system logs while an instance is running, or check the collected logs if an instance fails.
```{note}
AMS does not support runtime log collection. Logs are currently only being collected from an instance that failed to start or had an error at runtime.
```

## View runtime logs

While an instance is running, you can use the `amc` command to access both the Anbox and the Android system logs. The following command shows the system log:

    amc logs -t <log type> <instance_id>

As `<log type>`, specify either `anbox` for the Anbox system log or `android` for the Android one. If you don't specify the log type, the Anbox system log is displayed by default.

To follow the log and get automatic updates for new entries, add the `-f` argument:

    amc logs -t anbox -f <instance_id>

This will show the logs and update the output whenever new entries are added.

(sec-view-stored-logs)=
## View stored logs

If an instance fails to start or a runtime error occurs, AMS collects relevant log files from the instance and makes them available for inspection.

Available logs can be listed with the `amc show <instance_id>` command:

```bash
id: bh03th0j1qm6416q0v30
name: ams-bh03th0j1qm6416q0v30
status: error
node: lxd0
created_at: 1970-01-01T00:00:00Z
application:
  id: bh03tgoj1qm6416q0v2g
network:
  address: 192.168.100.2
  public_address: 10.226.4.63
  services: []
stored_logs:
- container.log
- system.log
- android.log
error_message: 'Failed to install application com.canonical.candy: exit status 1'
```

The instance in this example failed to install the application as indicated by the `error_message` field. There are three log files being stored which can be shown with the `amc show-log` command (for example, `amc show-log bh03th0j1qm6416q0v30 system.log`):

```bash
-- Logs begin at Thu 2019-01-17 08:37:56 UTC, end at Thu 2019-01-17 08:38:58 UTC. --
Jan 17 08:37:56 ams-bh03th0j1qm6416q0v30 systemd-journald[38]: Journal started
Jan 17 08:37:56 ams-bh03th0j1qm6416q0v30 systemd-journald[38]: Runtime journal (/run/log/journal/2c8dee797148423b8f8987009ee28eab) is 8.0M, max 99.6M, 91.6M free.
Jan 17 08:37:56 ams-bh03th0j1qm6416q0v30 systemd[1]: Starting Flush Journal to Persistent Storage...
....
Jan 17 08:38:57 ams-bh03th0j1qm6416q0v30 acc[607]: 2019/01/17 08:38:57 Extracting application package ...
Jan 17 08:38:58 ams-bh03th0j1qm6416q0v30 acc[607]: 2019/01/17 08:38:58 Waiting for Android container
Jan 17 08:38:58 ams-bh03th0j1qm6416q0v30 acc[607]: 2019/01/17 08:38:58 Installing application com.canonical.candy from app.apk ...
```

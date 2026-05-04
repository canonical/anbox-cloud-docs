(howto-access-instance)=
# Access an instance

In some cases, it might be necessary to access an individual instance for debugging reasons.
You can do this on the command line with the `amc` command.

## Access an instance with `amc`

The `amc` command provides simple shell access to any instance managed by AMS. To access a specific instance you only need its ID:

    amc shell <id>

This command opens a bash shell inside the instance. To access the nested Android container, use the `anbox-shell` command inside the new shell. If you combined the `anbox-shell` command with `amc exec`, you can get direct access to the Android container:

    amc exec <id> -- anbox-shell

```{note}
`anbox-shell` is available only for images with containerized Android (`jammy:*`). For images with virtualized Android (`resolute:*-cf:*`), connect to the Android shell through ADB:

    adb connect <instance_ip>:6520
    adb shell

See {ref}`tut-getting-started-virtualized-android` for details.
```

If you only want to watch the Android log output, use the following command:

    amc exec <id> -- anbox-shell logcat

`amc shell` and `amc exec` open various possibilities for automation use cases. See the help output of the commands for further details.

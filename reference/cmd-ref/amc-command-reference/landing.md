(ref-amc-commands)=
# AMC command reference

The Anbox Management Client (AMC) is a command line utility offered by Anbox Cloud that interacts with the Anbox Management Service (AMS).

Use `amc --help` or `amc <command> --help` to display usage information for the tool and its commands. The following commands are available for use with `amc`:

| Command | Description|
|---------|------------|
|[`addon`](addon.md)    | Manage addons |
|[`application`](application.md) | Manage applications |
|[`benchmark`](benchmark.md) | Benchmark your Anbox Cloud deployment |
|[`completion`](completion.md) | Generate the auto completion script for the specified shell |
|[`config`](config.md) | Manage AMS configuration |
|[`delete`](delete.md) | Delete an instance |
|[`exec`](exec.md) | Execute a command inside an instance |
|[`help`](help.md) | Help for a command |
|[`image`](image.md) | Manage images |
|[`info`](info.md) | Provide information about connected AMS service |
|[`init`](init.md) | Initialise an instance |
|[`launch`](launch.md) | Launch an instance |
|[`list`](list.md) | List instances |
|[`logs`](logs.md) | View runtime logs of an instance |
|[`node`](node.md) | Manage nodes |
|[`remote`](remote.md) | Interact with remote AMS daemons |
|[`shell`](shell.md) | Open a shell inside a running instance |
|[`show`](show.md) | Display information about an instance |
|[`show-log`](show-log.md) | Display a particular instance's log file |
|[`start`](start.md) | Start an existing instance |
|[`stop`](stop.md) | Stop a running instance |
|[`wait`](wait.md) | Wait for an instance to reach a specific condition |

## Options

You can use the following options or flags with the `amc` utility:

| Option | Description |
|--------|-------------|
|`-h`, `--help` | Display help for the `amc` utility |
|`-v`, `--version` | Display version of the AMS |

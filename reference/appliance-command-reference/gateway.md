The `gateway` command allows and manages access to the HTTP API of the stream gateway. If the HTTP API is exposed (which is the default), authenticated clients can connect to it.

    anbox-cloud-appliance gateway <subcommand>

## Subcommands

### `account`
Manages accounts to access the Anbox stream gateway.

    anbox-cloud-appliance gateway account <subcommand>

The `account` command can be used with two subcommands - `create` and `delete`:

The `account create` command creates an account to access the Anbox stream gateway.

This command creates an account with the given <account-name> and returns a token which you can use for accessing the Anbox Stream Gateway HTTP API directly or through the Anbox Stream SDK. See [How to access the stream gateway](https://discourse.ubuntu.com/t/managing-stream-gateway-access/17784) for more information.

    anbox-cloud-appliance gateway account create <account-name>

The `account delete` command deletes the specified account and removes access to the Anbox stream gateway for the specified account.

    anbox-cloud-appliance gateway account delete <account-name>

### `expose`
Enables access to the stream gateway in the load balancer.

    anbox-cloud-appliance gateway expose

### `unexpose`
Disables access to the stream gateway in the load balancer.

    anbox-cloud-appliance gateway unexpose

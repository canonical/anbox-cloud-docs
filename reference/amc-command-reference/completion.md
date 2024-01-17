The `completion` command allows you to generate the auto completion script for the specified shell.

    amc completion <subcommand>

## Subcommands

### `bash`
Generate the auto completion script for `bash`. This script depends on and requires the `bash-completion` package to be installed.

    amc completion bash --no-descriptions

where `--no-descriptions` disables completion descriptions.

To load completions in your current shell session, use:

    source <(amc completion bash)

To load completions for every new session, execute the following once and start a new shell for the setup to take effect:

For Linux,

    amc completion bash > /etc/bash_completion.d/amc

For macOS,

    amc completion bash > $(brew --prefix)/etc/bash_completion.d/amc

### `fish`
Generate the auto completion script for `fish`.

    amc completion fish --no-descriptions

where `--no-descriptions` disables completion descriptions.

To load completions in your current shell session, use:

    amc completion fish | source

To load completions for every new session, execute the following once and start a new shell for the set to take effect:

    amc completion fish > ~/.config/fish/completions/amc.fish

### `powershell`
Generate the auto completion script for `powershell`.

    amc completion powershell --no-descriptions

where `--no-descriptions` disables completion descriptions.

To load completions in your current shell session, use:

    amc completion powershell | Out-String | Invoke-Expression

To load completions for every new session, add the output of the above command
to your powershell profile.

### `zsh`
Generate the auto completion script for `zsh`.

    amc completion zsh --no-descriptions

where `--no-descriptions` disables completion descriptions.

If shell completion is not already enabled in your environment, enable it by running the following command:

    echo "autoload -U compinit; compinit" >> ~/.zshrc

To load completions in your current shell session:

    source <(amc completion zsh)

To load completions for every new session, execute the following once and start a new shell for the setup to take effect:

For Linux,

    amc completion zsh > "${fpath[1]}/_amc"

For macOS,

    amc completion zsh > $(brew --prefix)/share/zsh/site-functions/_amc

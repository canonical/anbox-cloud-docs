# aar completion zsh

Generate the autocompletion script for the zsh shell.

If shell completion is not already enabled in your environment you will need
to enable it.  You can execute the following once:

	echo "autoload -U compinit; compinit" >> ~/.zshrc

To load completions in your current shell session:

	source <(aar completion zsh)

To load completions for every new session, execute once:

For Linux

	aar completion zsh > "${fpath[1]}/_aar"

For macOS,

	aar completion zsh > $(brew --prefix)/share/zsh/site-functions/_aar

You will need to start a new shell for this setup to take effect.

## Usage

    aar completion zsh [flags]

## Flags

```
-h, --help              help for zsh
    --no-descriptions   disable completion descriptions
```

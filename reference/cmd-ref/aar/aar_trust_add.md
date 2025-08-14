## aar trust add

Register a client certificate.

If a filename is provided, make sure your certificates is placed within /root'.

Example:

    sudo aar trust add /root/client.crt

If no argument is provided, AAR will read the standard input, allowing the use of pipes and redirections.

Example:

    cat client.crt | sudo aar trust add

## Usage

    aar trust add [path to certificate] [flags]

## Flags

```
  -h, --help        help for add
  -p, --publisher   Register client as publisher
  -q, --quiet       Don't print warning when running in non-interactive mode
```

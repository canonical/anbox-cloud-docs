## ams.amc addon update

Update an existing addon

```
ams.amc addon update <name> <addon_path> [flags]
```

### Examples

```
$ tree addon
addon/
├── hooks
│   └── install
└── manifest.yaml

$ amc addon update foo addon/

```

### Options

```
  -h, --help             help for update
  -t, --timeout string   Maximum time to wait for the operation to complete (default "5m")
```

### SEE ALSO

* [ams.amc addon](ams.amc_addon.md)	 - Manage addons


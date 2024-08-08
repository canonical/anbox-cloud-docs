(ref-appliance-preseed-config)=
# Anbox Cloud Appliance preseed configuration format

The Anbox Cloud Appliance supports a `--preseed` command line flag for its `init` command that makes it possible to fully configure it in a non-interactive way.

For example, starting from a clean installation of the Anbox Cloud Appliance, the preseed configuration can be provided in the following way:

    cat << EO | sudo anbox-cloud-appliance init --preseed
    network:
      listen-address: 192.168.11.4
    lxd:
      storage-pool: my-pool
      project: anbox-cloud
    ams:
      api:
        allowed-uid: [0, 1000]
    EOF

## Configuration format

The following shows a complete example of the preseed configuration with all available keys and a description.

```yaml
network:
  # An IP address all services the appliance deploys will listen on.
  listen-address: 192.168.11.4
  # The IP address the appliance is accessible on when running behind NAT
  public-address: 192.168.11.4
  # The DNS name the appliance is accessible on when running behind NAT
  public-location: foo.bar
lxd:
  # Specifies the path to a storage disk. This can be used to ask the
  # appliance to create a new storage pool based on the specified
  # storage disk. The option is mutually exclusive to StorageSize
  storage-disk: /dev/sdc
  # The size in bytes of a new storage pool to create with the name
  # specified in `storage-pool`. The option is mutually exclusive to
  # `storage-disk`
  storage-size: 343413411
  # Specifies the name of an existing LXD storage pool to use. If not
  # specified the appliance will automatically select a suitable
  # storage pool if available. If `storage-disk` or `storage-size`
  # are specified this will describe the name of the storage pool to
  # create
  storage-pool: local
  # The name of a to be created LXD project the appliance will use. If
  # not specified the default "anbox-cloud" name will be used.
  project: anbox-cloud
ams:
  api:
    allowed-uids: [0, 1000]
```
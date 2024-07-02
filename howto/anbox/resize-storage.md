(howto-resize-lxd-storage)=
# How to resize LXD storage

Resizing the LXD storage pool that Anbox Cloud uses is not recommended. Before you deploy Anbox Cloud, you should analyse and plan the capacity you need, so that you can size the storage that you need correctly right from the start. See {ref}`exp-capacity-planning` for detailed information.

However, if you run into a situation where you need to grow the LXD storage pool, try the following workarounds depending on your setup.

- **Loop-backed storage pool**

  If you use a loop file for your LXD storage, follow the instructions for ZFS in [Resize a storage pool](https://documentation.ubuntu.com/lxd/en/latest/howto/storage_pools/#resize-a-storage-pool) in the LXD documentation.

  After resizing the storage pool, you must restart AMS.
- **Dedicated block device**

  You cannot resize a dedicated block device. Instead, replace the block device with a bigger one. Once you replace the block device, you must redeploy the cluster node.
- **EBS volume**

  While it is generally [possible to resize an EBS volume](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/requesting-ebs-volume-modifications.html), it is usually easier to replace the cluster node with a new one that has a bigger EBS volume.

# Instances

Anbox Cloud uses secure and isolated system instances supplied by [LXD](https://ubuntu.com/lxd). LXD provides a high degree of flexibility when setting up instances - you get to decide the level of security for your requirements. See [Security](https://documentation.ubuntu.com/lxd/en/latest/security/) in the LXD documentation for more information about how a LXD setup can be secured.

```{tip}
Using virtual machines to host Android containers provides better workload isolation. 
```

## Unprivileged instances

```{note}
This section is particularly applicable for container based instances because a virtual machine is unprivileged by nature.
```

Many instance managers use privileged instances, which means that the instances have root privileges on the host system, including access to all devices. This is a security risk, because attackers could gain control over the host system.

Anbox Cloud uses unprivileged LXD instances only, which fully isolates the instances and ensures that they cannot gain root privileges. In addition, the Android container that runs inside the LXD instance also runs as an unprivileged instance. This method isolates the Android container twice, with the result that if the encapsulation of either the LXD instance or the Android container should fail, the system would still be protected.

```{caution}
While instances are fully isolated, all instances currently use the same GPU resources. As a result, any instance that is launched with GPU support could take all GPU resources in a DDoS-like attack, which would prevent other instances from starting.

Monitoring how the GPU resources are used for different applications and ensuring that you are running trusted workloads can provide insulation against DDoS-like attacks.

See {ref}`sec-gpu-slots` for more information.
```
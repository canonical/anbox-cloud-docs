(exp-rendering-graphics)=
# Rendering graphical output

Anbox Cloud can adapt to your rendering needs by adjusting its behavior depending on the availability of a GPU and the presence of the `--enable-graphics` flag when you launch an instance.

    amc launch --enable-graphics my-application

The use of the `--enable-graphics` flag when you launch an instance decides whether Anbox Cloud renders a graphical output.

When this flag is set, if there is a GPU available, Anbox Cloud renders graphical output using the GPU. If there is no GPU available, it uses software rendering to render the graphical output.

However, if you do not use the `--enable-graphics` flag when launching an instance, Anbox Cloud does not provide any graphical output.

Now your environment may or may not include a GPU. If Anbox Cloud detects a GPU device during deployment, it adjusts itself to use the GPU. AMS configures each LXD instance to pass through a GPU device from the host. Every instance that owns a GPU slot will have access to the GPU. For NVIDIA GPUs, LXD uses the [NVIDIA container runtime](https://github.com/NVIDIA/nvidia-container-runtime) to make the GPU driver of the host available to the instance.

```{important}
Anbox Cloud currently does not support GPU provisioning for instances that are virtual machines and not containers. This feature is planned for a future release.
```

To use container instances with a GPU,

- Configure the number of available GPU slots on the node. This decides how many instances can run on a given node because GPUs have limited sharing capacity among multiple instances. See {ref}`sec-gpu-slots` for detailed information.
- Check the list of supported GPUs ({ref}`sec-supported-gpus`) to see if Anbox Cloud has support for a driver for your GPU device. If a GPU driver is available inside the instance, there are no further differences in how to use it in comparison to a regular environment. If no GPU driver is available, you must provide it through an {ref}`addon <exp-addons>`.
- Launch your instance with the `--enable-graphics` flag.

If your environment does not have a GPU, Anbox Cloud uses software rendering.

To use instances without a GPU and still render graphical output,

- Change the {ref}`sec-application-manifest-resources` of the application to not require a GPU. This tells Anbox Cloud that no GPU should be used.
- Launch your instance with the `--enable-graphics` flag. The presence of this flag when there is no GPU tells Anbox Cloud to use software rendering.

## Related topics

* {ref}`ref-rendering-resources`
* {ref}`exp-rendering-architecture`

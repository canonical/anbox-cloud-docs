(ref-rendering-resources)=
# Supported rendering resources

This guide lists various supported GPU vendors, drivers, platforms, APIs and discuss the rendering pipelines used for different GPUs.

```{important}
Currently Anbox Cloud does not support GPU for virtual machines.
```

(sec-supported-gpus)=
## Supported GPU vendors and GPU models

Being a cloud solution, Anbox Cloud is optimised for GPUs that are designed for a data centre. We currently support the following GPU vendors:

* NVIDIA
* Intel
* AMD

Mixing GPUs from different vendors is not supported.

Concrete support for the individual GPU depends on the platform being using for Anbox Cloud. The included `webrtc` platform currently supports the following GPUs:

| Vendor | Supported Generations        | Render | Hardware video encode  |
|--------|------------------------------|--------|------------------------|
| AMD    | RDNA, RDNA2, RDNA3           | Yes    | No                     |
| NVIDIA | Turing, Ampere, Ada Lovelace | Yes    | Yes                    |
| Intel  | Gen9, Gen11, Gen12           | Yes    | No                     |

For GPUs on which Anbox Cloud doesn't support hardware video encoding, a software-based video encoding fallback is available.

Anbox Cloud is extensively tested using NVIDIA GPUs and occasionally, on Intel and AMD GPUs. However, if you want to use a different GPU vendor, you can customise and configure Anbox Cloud for the GPU vendor of your choice using the Anbox Platform SDK. See {ref}`sec-platform-sdk` for more information.

## Supported GPU drivers

For NVIDIA GPUs, Anbox Cloud uses the [Enterprise Ready Driver (ERD) from NVIDIA](https://help.ubuntu.com/community/NvidiaDriversInstallation) for Linux as available in Ubuntu.

For AMD GPUs, Anbox Cloud uses the [Mesa radv](https://docs.mesa3d.org/drivers/radv.html) driver and for Intel GPUs, the [Mesa anv](https://docs.mesa3d.org/drivers/anv.html) driver.

See {ref}`ref-component-versions` to refer to the actual version supported for any particular Anbox Cloud release.

(sec-supported-platforms)=
## Supported platforms

Anbox Cloud can make use of different [platforms](https://canonical.github.io/anbox-cloud.github.com/latest/anbox-platform-sdk/) to customise its behaviour and currently supports 3 platforms.

| Name     	| Behaviour                                                                                                                                            	|
|----------	|-----------------------------------------------------------------------------------------------------------------------------------------------------	|
| `null`   	|  A headless-GL platform. No rendering is performed. No audio input/output. Useful for functional tests. It's used by default if no platform is specified when launching an instance.                                                                       	|
| `webrtc` 	| Full-featured WebRTC based streaming platform. Includes driver and integration for AMD and NVIDIA GPUs as well as LLVMpipe based software rendering if no GPU is detected.  Support audio input/output. |
| `swrast` 	| (DEPRECATED) Software Rasterization platform. A LLVMpipe based software rendering platform. Useful for visual tests. No audio input/output.    |

For rendering, you can use the `swrast` or the `null` platforms depending on your requirements.

`swrast` is a software rasterization platform, which is a rendering implementation of the Mesa driver with support for LLVMpipe. It can be utilised for use cases that require a visual output without a GPU. The rendering pipe for the `swrast` or `null` platform is not different than the one for the `webrtc` platform with NVIDIA GPU support except that it is irrespective of any available GPUs. To know more about this implementation, see [LLVMpipe](https://docs.mesa3d.org/drivers/llvmpipe.html).

`null` is an OpenGL headless platform that makes use of the rendering backend of the [Almost Native Graphics Layer Engine (ANGLE)](https://chromium.googlesource.com/angle/angle) and can be used when you do not need a graphic output, such as, automation testing. It does not perform software rendering and does not produce any graphic output. Hence, the overhead on the CPU when using `null` platform is significantly low which makes it a good candidate for all use cases where a graphic output is not necessary.

The `webrtc` platform is used by Anbox to provide graphical output. It supports all GPUs supported by Anbox Cloud in addition to software rendering. It is used when an instance is launched with `--enable-graphics`, or via the Anbox Stream Gateway.

## Supported APIs

| API        | Version | Supported GPUs     |
|------------|---------|--------------------|
| EGL        | 1.5     | AMD, Intel, NVIDIA |
| OpenGL ES  | 3.2     | AMD, Intel, NVIDIA |
| Vulkan     | 1.3     | AMD, Intel, NVIDIA |

Support for API extensions on all supported GPUs depends on the availability of such extensions from the used driver.

The following OpenGL ES extensions are known to be unsupported by all used GPU drivers:

* [`GL_EXT_shader_framebuffer_fetch`](https://registry.khronos.org/OpenGL/extensions/EXT/EXT_shader_framebuffer_fetch.txt)
* [`GL_EXT_shader_framebuffer_fetch_non_coherent`](https://registry.khronos.org/OpenGL/extensions/EXT/EXT_shader_framebuffer_fetch.txt)

## Related topics

* {ref}`exp-rendering-architecture`
* {ref}`exp-platforms`

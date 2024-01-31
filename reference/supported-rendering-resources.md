This guide lists various supported GPU vendors, drivers, platforms, APIs and discuss the rendering pipelines used for different GPUs.

[note type="information" status="Important"]Currently Anbox Cloud does not support GPU for virtual machines.[/note]

## Supported GPU vendors and GPU models

Being a cloud solution, Anbox Cloud is optimised for GPUs that are designed for a data centre. We currently support the following GPU vendors:

* NVIDIA
* Intel
* AMD

Do not mix GPUs from different vendors in a single deployment.

Concrete support for the individual GPU depends on the platform being using for Anbox Cloud. The included `webrtc` platform currently supports the following GPUs:

| Vendor | Model                 | Render | Hardware video encoder |
|--------|-----------------------|--------|-----------------------|
| AMD    | WX5100, WX4100        | Yes    | No                    |
| NVIDIA | Quadro, Tesla, Ampere | Yes    | Yes                   |

For GPUs on which Anbox Cloud doesn't support hardware video encoding, a software-based video encoding fallback is available.

Anbox Cloud is extensively tested using NVIDIA GPUs and occasionally, on Intel and AMD GPUs. However, if you want to use a different GPU vendor, you can customise and configure Anbox Cloud for the GPU vendor of your choice using the [Anbox Platform SDK](https://discourse.ubuntu.com/t/17844).

## Supported GPU drivers

For NVIDIA GPUs, Anbox Cloud uses the [Enterprise Ready Driver (ERD) from NVIDIA](https://help.ubuntu.com/community/NvidiaDriversInstallation) for Linux as available in Ubuntu.
For AMD and Intel GPUs, Anbox Cloud uses the [Mesa driver](https://www.mesa3d.org/).

See [Component versions](https://discourse.ubuntu.com/t/21413) to refer to the actual version supported for any particular Anbox Cloud release.

## Supported platforms

Anbox Cloud can make use of different [platforms](https://anbox-cloud.github.io/latest/anbox-platform-sdk/) to customise its behaviour and currently supports 3 platforms.

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

For NVIDIA GPUs Anbox Cloud uses [OpenGL ES 3.2](https://www.khronos.org/opengles/) and [EGL 1.5](https://www.khronos.org/egl/) graphical interfaces. For Intel and AMD GPUs, Anbox Cloud uses [Vulkan 1.3](https://vulkan.org/).

## Related information

* [Rendering architecture](https://discourse.ubuntu.com/t/rendering-architecture/35129)
* [Configuring the Anbox Cloud platforms](https://discourse.ubuntu.com/t/anbox-platforms/18733)

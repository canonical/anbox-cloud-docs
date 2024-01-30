The rendering pipeline of Anbox Cloud can vary depending on the GPU used. This guide explains in detail, the rendering architecture of Anbox Cloud while discussing the different rendering pipeline models.

## Overview

For NVIDIA GPUs, Anbox Cloud driver stacks currently have a native OpenGL ES driver. For AMD and Intel GPUs, an OpenGL ES or EGL driver is layered on top of the Vulkan API. Since Vulkan API provides better GPU management at a lower level than OpenGL ES or EGL, this approach is beneficial and preferred by many users.

To have a better understanding of the rendering architecture of Anbox Cloud, it is important to understand what the Android framework offers in terms of rendering. In Android, applications interact with the SurfaceFlinger which is the system compositor that is responsible for composing a frame together from all the outputs rendered by different applications. The frame is then submitted to the hardware composer which renders the frames on a screen. For more information on Android graphics components and how they work, see https://source.android.com/docs/core/graphics. 

## Rendering pipeline

Anbox Cloud has two rendering pipeline models - one for NVIDIA and the other for Intel and AMD. However, irrespective of the GPU that you use, the path of a frame typically looks like this: Android application > SurfaceFlinger > Hardware composer > Anbox Cloud > Display on screen or send it to streaming component.

For communication between the hardware composer module on the Android side and Anbox runtime, we use the Wayland protocol. So Anbox Cloud really functions as a compositor for Android i.e., the hardware composer module receives frames from the SurfaceFlinger and notifies Anbox runtime using Wayland. The Anbox runtime then submits the frame towards its output, which is either the screen or the streaming component.

### For NVIDIA

![Anbox Cloud NVIDIA pipeline|690x440](https://assets.ubuntu.com/v1/c277dade-NVIDIA_pipeline_updated.png)

For NVIDIA, as we cannot use the NVIDIA driver inside the Android container because of compatibility issues, we use the Enterprise Ready NVIDIA driver that is available on every Ubuntu installation. Instead, we have an Anbox Cloud GPU driver which is a standard OpenGL ES or EGL driver that receives the API calls and converts them to remote procedure calls to the NVIDIA driver. The actual rendering and actions on the NVIDIA driver happens on the Anbox runtime side inside the Ubuntu instance and not in the Android space.

In terms of performance, this could be perceived to have some transmission overhead when compared to the rendering on Intel and AMD GPUs. However, Anbox Cloud is optimised to keep this overhead minimal and the additional overhead due to the transmission of OpenGL ES calls from the Android space to Anbox runtime is not significant enough to affect most use cases.

### For Intel and AMD

![Anbox Cloud Intel and AMD pipeline|690x440](https://assets.ubuntu.com/v1/9d189689-Intel_AMD_pipeline_updated.png)

For AMD and Intel GPUs, Anbox Cloud uses Vulkan as API in the Android space and we use ANGLE on top of Vulkan to circumvent OpenGL ES and EGL. Since the Mesa driver (vendor GPU driver) is available directly in the Android space, we do not have the overhead of the remote procedure call implementation as in the pipeline for NVIDIA. 

## Related information

* [Supported rendering resources](https://discourse.ubuntu.com/t/37322)
* [SurfaceFlinger](https://source.android.com/docs/core/graphics/surfaceflinger-windowmanager)
* [Wayland](https://wayland.freedesktop.org/)


(howto-increase-instance-density)=
# Increase instance density

In an Anbox Cloud deployment with NVIDIA GPUs, launching multiple GPU-based Anbox instances or performing {ref}`howto-run-benchmarks` may reveal a limit on the number of running instances. Although [NVIDIA-SMI](https://developer.nvidia.com/system-management-interface) shows low GPU memory usage and utilization, launching additional instances can result in the following errors when [viewing instance logs](/howto/troubleshoot/view-logs.md):


    anbox-starter[698]: I0826 00:57:18.131316 787 vk_context.cpp:267] Using Vulkan device: NVIDIA T4G (driver 570.632.64 api 1.4.303)
    anbox-starter[698]: E0826 00:57:18.168112 787 vk_context.cpp:345] Failed to create Vulkan device: VK_ERROR_INITIALIZATION_FAILED
    anbox-starter[698]: E0826 00:57:18.177026 787 base_gpu_implementation.cpp:57] Failed to create Vulkan context


or

    anbox-starter[700]: E0826 00:56:48.728224 789 cuda_helpers.cpp:22] Failed to initialize CUDA: no CUDA-capable device is detected
    anbox[700]: Failed to create platform webrtc
    anbox[700]: Failed to create the platform: webrtc


This error is typically caused by the NVIDIA kernel module parameter `RMIncreaseRsvdMemorySizeMB`, which defaults to 256MB in Anbox Cloud deployments. This reserved memory can be exhausted when launching many GPU instances, even though the GPU still has available VRAM. Tuning this parameter from **256MB to 1024MB** enables more GPU instances to run in the deployment.

```{note}
The optimal value for `RMIncreaseRsvdMemorySizeMB` depends on the GPU model and its VRAM. Increasing this parameter to 1024MB may allow more GPU instances to launch, but it also reduces the amount of VRAM available for rendering or video encoding per Anbox instance. Therefore, you may need to adjust this value carefully to balance instance density and per-instance performance.
```

1. Unload NVIDIA Kernel Modules

        sudo rmmod nvidia_drm nvidia_modeset nvidia_uvm nvidia

1. Update NVIDIA kernel module parameter

        sudo sed -i 's/RMIncreaseRsvdMemorySizeMB=256/RMIncreaseRsvdMemorySizeMB=1024/' /etc/modprobe.d/anbox-nvidia.conf

1. Reload NVIDIA Modules

        sudo modprobe nvidia_drm nvidia_modeset nvidia_uvm nvidia

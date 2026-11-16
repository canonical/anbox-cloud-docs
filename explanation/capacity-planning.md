---
myst:
  html_meta:
    "description": "Explanation of capacity planning for Anbox Cloud, with guidance on estimating resources based on user load."
---

(exp-capacity-planning)=
# Capacity planning

When planning your Anbox Cloud deployment, you should start by estimating how much capacity you need, how many instances you expect to run at the same time and what resources each instance needs. Based on this estimate, you can then size your deployment and figure out how many cluster nodes you need and what resources they should have.

When estimating capacity, consider the following questions to better understand your requirements:

- Instance resources:
  * How much CPU, memory and disk space does each instance require?
  * Does every instance need dedicated access to the CPU and memory, or can the capacity be shared between several instances?
  * Does each instance require GPU resources, and if so, how many GPU slots does it require?

- Streaming:
  * Is streaming enabled?
  * Does the instance use hardware- or software-based video encoding?
  * If the instance uses hardware-based encoding, how much GPU capacity is needed?
  * What frame rate and resolution do your instances need?
  * For virtualized Android, how many displays does each instance have?

- Demand:
  * How many instances will be running simultaneously?
  * What would be the impact of not being able to serve all users?
  * What is the impact if the deployment reaches capacity and cannot start additional instances?


## Instance resources

Each instance is allocated a number of vCPU cores, an amount of RAM, an amount of disk space and, optionally, a number of GPU slots. The source of these values depends on how the instance is configured:

- Instances launched from {ref}`application <exp-applications>` use the application's {ref}`resource preset <exp-resources-presets>` or the {ref}`sec-application-manifest-resources` defined in its manifest by default. This is true for containerized Android only.
- Instances launched from images use the resources you specify at launch, with the `--cpus`, `--memory`, `--disk-size` and `--gpu-slots` options of `amc launch`. This applies for both containerized and virtualized Android.

AMS internally summarizes the amount of resources used by instances on a single machine and disallows launching additional instances when all resources are used (see {ref}`sec-over-committing` for how to allow a higher resource usage). In such cases, you will see the following error message when trying to launch a new instance:

    no suitable node to satisfy instance requirements available

This error also appears when no node in the cluster supports the requested instance type, for example launching a Cuttlefish instance when nested virtualization is unavailable across all cluster nodes (see {ref}`exp-android-execution-models`).

To help you diagnose why no node could satisfy the request, AMS appends the specific reason to the error message, such as unsupported instance types:

    no suitable node to satisfy instance requirements available (instance type: vm not supported)

Otherwise, the message lists why each evaluated node failed to meet the resource requirements, for example:

    no suitable node to satisfy instance requirements available (node0: cpu: available 2 < required 4)

The reported resources can include CPU, memory, disk space, GPU (including GPU type and slots), depending on what the instance requested and which of them the available nodes cannot satisfy. You could use this information together with the guidance in this page to determine whether you need to free up resources, add more nodes, or adjust your instance's resource allocation.

If an instance stops with an error, its disk space is preserved for inspection. Other resources are released. Therefore, if you have many instances with `error` status, you might run out of disk space.

### Containerized Android

Instances with containerized Android can be launched from an application or directly from an image. They use GPU-accelerated rendering when a GPU is assigned and software rendering otherwise.

For instances launched from applications, the video encoder configuration in the application manifest determines whether GPU resources are required for encoding. See {ref}`sec-application-manifest-video-encoder`.

For the minimum resources per instance, see {ref}`ref-feature-support-by-image-type`.

### Virtualized Android

Instances with virtualized Android are launched directly from an image. They require higher minimum resources than instances with containerized Android, as well as KVM on the host. AMS rejects an instance whose CPU, memory or disk space is below the minimum. For the minimum resources per instance, see {ref}`ref-feature-support-by-image-type`.

These instances use the instance's GPU for accelerated rendering when it has an NVIDIA GPU. Without a GPU, they use software rendering.

#### Multi-display instances

Multi-display ({ref}`exp-multi-display`) is supported only for instances with virtualized Android.

Each additional active display increases CPU and memory usage, because each display has its own rendering and video encoding pipeline.

When estimating resources for a multi-display instance, consider:

- The number of displays.
- The resolution and frame rate of each display.
- Instance density per LXD node decreases as display count increases. Account for this in cluster sizing.

Additional displays can increase the resources required by each instance and reduce the number of instances that a node can host.

(sec-gpu-slots)=
## GPU slots

An additional aspect to take into account when planning your resources is the number of required GPU slots.

GPUs have limited capacity that can be shared among multiple instances, and GPU slots are a way to fine-tune how many instances can run on a given node. In a cluster setup, you define the number of available GPU slots for each node (see {ref}`sec-config-gpu-slots` for instructions).

To determine the best number of GPU slots for a specific GPU model, consider the following aspects:

- The memory that the GPU provides
- The memory that an instance uses
- The number of parallel encoding pipelines that the GPU offers

Each node has a configured number of GPU slots. When AMS launches an instance that requests GPU slots, it reserves that number of slots on the selected node until the instance is terminated.

AMS can place an instance on a node only if that node has enough available GPU slots to satisfy the request. Instances that do not require GPU resources can still be placed on a node when no GPU slots are available.

For instances launched from applications, the video encoder type determines whether a GPU is required: `gpu` requires an available GPU, while `software` and `gpu-preferred` do not. See {ref}`sec-application-manifest-video-encoder` for more information.

```{important}
GPU slots are used to share GPUs among instances, but they do not impose limits on GPU usage. Therefore, increasing the number of required GPU slots for an application or an instance does not guarantee that more GPU resources are allocated to it. For example, an intensive game that is configured to use one GPU slot might consume more GPU resources than a simple photo gallery app that is configured to use five GPU slots.

A {ref}`default number <sec-node-configuration>` of GPU slots and GPU encoder slots are configured depending on the GPU used but this value can be changed. The main purpose of GPU slots is to control the number of instances that are launched on a node that has a GPU installed, which reduces contention for GPU resources.
```

(sec-over-committing)=
## Over-committing resources

If the unused resources on a cluster node don't suffice to launch an instance with its defined resource requirements, the instance cannot be launched. This behavior is very restrictive, and in many cases unnecessary.

Usually, an instance doesn't use its dedicated vCPU cores and memory at 100% all the time. Therefore, AMS allows over-committing available resources. By default, AMS uses a CPU allocation rate of `4` and a memory allocation rate of `2`, which means that it allows four times the number of vCPU cores and twice the amount of RAM per node. See {ref}`sec-config-allocation-rates` for instructions on how to define the allocation rates for a node.

For example, consider an application that has a resource preset of 2 vCPU cores and 3 GB of memory, and you have a node with 8 CPU cores and 16 GB of memory. Without over-commitment, you could only launch four instances before you run out of resources on the node. However, with a CPU allocation rate of `4` and a memory allocation rate of `2` (the default), the available resources on the node change to `4 * 8 physical CPU cores = 32 vCPU cores` and `2 * 16 GB memory = 32 GB memory`, which will allow up to ten instances on the node.

The CPU allocation rate depends on the type of application and the amount of resources it requires. For applications that are not CPU-intensive, a higher allocation rate makes sense while for applications that are very CPU-intensive, a lower allocation rate is suitable.

## Application requirements

To realistically estimate the required capacity for your deployment, you must consider the type of application that you're running and the expected usage behavior.

You should run benchmarks to test your application performance and fine-tune the best node and application configuration. See {ref}`howto-run-benchmarks`.

Also consider whether your instances use a hardware or software video encoder for video encoding, and the frame rate and resolution they require.

Another aspect is, of course, the number of users expected and hence, the number of instances that will be running simultaneously. If you expect the usage to be rather consistent, you might not need to plan for huge peaks in load. On the other hand, you must also consider the impact if your cluster runs out of resources and it is not possible anymore to start more instances.

## An example calculation

Let's consider an instance with 4 vCPU cores, 3 GB of RAM, 3 GB of disk space and 1 GPU slot. The workload is quite CPU-intensive, which means you should not over-commit resources by a large margin. You expect an average of 100 instances running at the same time, with peaks up to 200.

We now want to determine the capacity that is needed for the overall deployment. This capacity can be either for a single machine (which is rather unlikely for the given requirements) or for a cluster with multiple nodes.

Without over-commitment, you would require the following resources to fulfill the average demand of 100 instances:

- vCPU cores: `100 * 4 = 400`
- RAM: `100 * 3 GB = 300 GB`
- Disk space: `100 * 3 GB = 300 GB`
- GPU slots: `100 * 1 = 100`

With a CPU allocation rate of 2, you can bring the requirement of 400 vCPU cores down to 200 cores. With a CPU allocation rate of 4, the requirement would be further reduced to 100. With a memory allocation rate of 2, you can bring the memory requirement down to 150 GB. With over-committing, the numbers now look like the following:

- vCPU cores: `100 * 4 = 400` or with CPU allocation rate 2: `200`
- RAM: `100 * 3 GB = 300 GB` or with memory allocation rate 2: `150 GB`
- Disk space: `100 * 3 GB = 300 GB`
- GPU slots: `100 * 1 = 100`

The current calculation does not take into account that there might be peaks of up to 200 simultaneous instances. To cover all peaks, you would require the following resources:

- vCPU cores: `200 * 4 = 800` or with CPU allocation rate 2: `400`
- RAM: `200 * 3 GB = 600 GB` or with memory allocation rate 2: `300 GB`
- Disk space: `200 * 3 GB = 600 GB`
- GPU slots: `200 * 1 = 200`

To avoid your cluster running out of resources even at peak loads, you must size it accordingly (or dynamically scale it up and down). If the impact of not being able to provide additional instances at peak loads is rather low, you could compromise on the following factors:

- Use a higher CPU and/or memory allocation rate, which might decrease performance at peak loads.
- Configure your cluster nodes to use more GPU slots per GPU, which might decrease video quality.
- Reduce the resource allocation per instance (for example, using `--cpus`, `--memory` or `--disk-size` when launching instances). The impact depends on the workload, and allocations must still meet the minimum requirements for the Android execution model.
- Base your estimate on a lower maximum number of instances (for example, 150 instances), which will lead to your cluster running out of resources before the peak load is reached.

## Related topics

- {ref}`exp-clustering`
- {ref}`ref-application-manifest`
- {ref}`ref-feature-support-by-image-type`
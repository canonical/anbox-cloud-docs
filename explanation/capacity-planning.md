(exp-capacity-planning)=
# Capacity planning

When planning your Anbox Cloud deployment, you should start by estimating how much capacity you need, to be able to provide your application to your users and how many users (translating to the number of Android containers) you expect. Based on this estimate, you can then size your deployment and figure out how many cluster nodes you need and what resources they should have.

When estimating capacity, consider the following questions to better understand your requirements:

* Application resources:
    - How much CPU, memory and disk space does your application need?
    - Will the application use hardware- or software-based video encoding?
    - If the application uses hardware-based encoding, how much GPU capacity is needed?
* CPU and memory:
    - Does every instance need dedicated access to the CPU and memory, or can the capacity be shared between several instances?
* Application:
    - What type of application are you running?
    - What frame rate and what resolution does your application need?
    - How many instances will be running simultaneously?
    - What would be the impact of not being able to serve all users?

## Application resources

A default resource preset will be set for every application. A resource preset specifies the resources that are available to the application:

- The number of vCPU cores
- The amount of RAM
- The amount of disk space
- The number of GPU slots

Depending on the resources that your application requires, if the {ref}`default resource preset <exp-resources-presets>` does not suit, you can choose suitable {ref}`sec-application-manifest-resources` that fit your application.

When an instance for an application is launched, it takes the specified amount of resources. AMS internally summarizes the amount of resources used by instances on a single machine and disallows launching additional instances when all resources are used (see {ref}`sec-over-committing` for how to allow a higher resource usage). In such cases, you will see the following error message when trying to launch a new instance:

    No suitable node to satisfy instance requirement available

If an instance stops with an error, its disk space is preserved for inspection. Other resources are released. Therefore, if you have many instances with `error` status, you might run out of disk space.

(sec-gpu-slots)=
### GPU slots

An additional aspect to take into account when planning your resources is the number of required GPU slots.

```{note}
Currently, Anbox Cloud does not have GPU support for virtual machines. This feature is planned for a future release.
```

GPUs have limited capacity that can be shared among multiple instances, and GPU slots are a way to fine-tune how many instances can run on a given node. In a cluster setup, you define the number of available GPU slots for each node (see {ref}`sec-config-gpu-slots` for instructions).

To determine the best number of GPU slots for a specific GPU model, consider the following aspects:

- The memory that the GPU provides
- The memory that an instance uses
- The number of parallel encoding pipelines that the GPU offers

When you launch an instance for an application, AMS reserves the number of GPU slots defined for the application on the node where it is launched. These GPU slots are marked as unavailable until the instance is terminated. If no GPU slots are available on the node, instances that require a GPU (with video encoder type as `gpu`) will not be launched on it. Instances that don't require a GPU (with video encoder type as `software` or `gpu-preferred`) can still be launched. See {ref}`sec-application-manifest-video-encoder` for more information on video encoder types.

```{important}
GPU slots are used to share GPUs among instances, but they do not impose limits on GPU usage. Therefore, increasing the number of required GPU slots for an application does not guarantee that more GPU resources are allocated to the corresponding application instances. For example, an intensive game that is configured to use one GPU slot might consume more GPU resources than a simple photo gallery app that is configured to use five GPU slots.

The main purpose of GPU slots is to control the number of instances that are launched on a node that has a GPU installed, which reduces contention for GPU resources.
```
(sec-over-committing)=
## Over-committing resources

If the unused resources on a cluster node don't suffice to launch an instance for an application with its defined resource requirements, the instance cannot be launched. This behavior is very restrictive, and in many cases unnecessary.

Usually, an instance doesn't use its dedicated vCPU cores and memory at 100% all the time. Therefore, AMS allows over-committing available resources. By default, AMS uses a CPU allocation rate of `4` and a memory allocation rate of `2`, which means that it allows four times the number of vCPU cores and twice the amount of RAM per node. See {ref}`sec-config-allocation-rates` for instructions on how to define the allocation rates for a node.

For example, consider an application that has a resource preset of 2 vCPU cores and 3 GB of memory, and you have a node with 8 CPU cores and 16 GB of memory. Without over-commitment, you could only launch four instances before you run out of resources on the node. However, with a CPU allocation rate of `4` and a memory allocation rate of `2` (the default), the available resources on the node change to `4 * 8 physical CPU cores = 32 vCPU cores` and `2 * 16 GB memory = 32 GB memory`, which will allow up to ten instances on the node.

The CPU allocation rate depends on the type of application and the amount of resources it requires. For applications that are not CPU-intensive, a higher allocation rate makes sense while for applications that are very CPU-intensive, a lower allocation rate is suitable.

## Application requirements

To realistically estimate the required capacity for your deployment, you must consider the type of application that you're running and the expected usage behavior.

You should run benchmarks to test your application performance and fine-tune the best node and application configuration. See {ref}`howto-run-benchmarks`.

Also consider whether your instances use a hardware or software video encoder for video encoding, and the frame rate and resolution they require.

Another aspect is, of course, the number of users expected and hence, the number of instances that will be running simultaneously. If you expect the usage to be rather consistent, you might not need to plan for huge peaks in load. On the other hand, you must also consider the impact if your cluster runs out of resources and it is not possible anymore to start more instances.

## An example calculation

Let's consider an application that has a resource preset of 4 vCPU cores, 3 GB of RAM, 3 GB of disk space and 1 GPU slot. The application is quite CPU-intensive, which means you should not over-commit resources by a large margin. You expect an average of 100 instances running at the same time, with peaks up to 200.

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
- Tweak the resource preset for your application to give less resources to each instance. The impact of doing this depends very much on your application.
- Base your estimate on a lower maximum number of instances (for example, 150 instances), which will lead to your cluster running out of resources before the peak load is reached.

## Related topics

* {ref}`exp-clustering`
* {ref}`ref-application-manifest`
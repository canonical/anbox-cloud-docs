(exp-resources-presets)=
# Resources and resource presets

Resource presets denote the resources available to an instance. Anbox Cloud uses some default resource presets if there are no custom resource requirements specified.

For a container instance, the default resource preset is:

```yaml
name: my-application
resources:
  cpus: 2
  memory: 3GB
  disk-size: 3GB
```
For a virtual machine instance, the default resource preset is:

```yaml
name: my-application
resources:
  cpus: 2
  memory: 3GB
  disk-size: 15GB
```

If your application requires different resources than the default, specify the required resources in the application manifest to override some or all of default resource preset options.

In addition to the `cpus`, `memory` and the `disk-size` requirements, if your application requires a custom number of GPU slots, change the `gpu-slots` value for the `resources` attribute in the application manifest.

## Related topics

* {ref}`ref-application-manifest`

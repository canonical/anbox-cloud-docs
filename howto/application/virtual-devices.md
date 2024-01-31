In addition to running individual Android apps, Anbox Cloud allows you to stream the whole Android experience. The following sections describe how to set up such a virtual Android device experience.

## Set up an application for the virtual device

To create a virtual device, you must first set up a basic application. This application will not contain an APK and will therefore start directly into the Android system launcher and provide the full Android experience.

A very simple application manifest for such an application looks like this:

```yaml
name: vdev
resources:
  cpus: 2
  memory: 3GB
  disk-size: 3GB
```

If you want to use a GPU for instances created for your new `vdev` application, include `gpu-slots` as a resource requirement in the application manifest.

```yaml
name: vdev-gpu
resources:
  cpus: 2
  memory: 3GB
  disk-size: 5GB
  gpu-slots: 3
```

## Optionally extend the application

If you want to install additional applications that you want to offer as part of the default virtual device, you can extend the application with [hooks](https://discourse.ubuntu.com/t/hooks/28555). For example, you could replace the standard Android launcher with a custom one or change the system locale.

See [How to extend an application](https://discourse.ubuntu.com/t/extand-an-application/28554) for instructions.

## Create the application

Once the configuration is in place, create the application in AMS:

    amc application create vdev

After creating the application, you can stream it through the UI of the Anbox Stream Gateway (see [Get started with Anbox Cloud (web dashboard)](https://discourse.ubuntu.com/t/getting-started-with-anbox-cloud-web-dashboard/24958) for more details) or your own custom client application built with the [Anbox Streaming SDK](https://discourse.ubuntu.com/t/anbox-cloud-sdks/17844#anbox-cloud-streaming-sdk-8).

![Virtual device|690x662,100%](https://assets.ubuntu.com/v1/4cc5a115-application_virtual-device.png)

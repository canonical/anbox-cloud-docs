(howto-create-virtual-device)=
# How to create a virtual Android device

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

If you want to install additional applications that you want to offer as part of the default virtual device, you can extend the application with {ref}`ref-hooks`. For example, you could replace the standard Android launcher with a custom one or change the system locale.

See {ref}`howto-extend-application` for instructions on extending your application.

## Create the application

Once the configuration is in place, create the application in AMS:

    amc application create vdev

After creating the application, you can stream it through the UI of the Anbox Stream Gateway (see {ref}`tut-getting-started-dashboard`) or your own custom client application built with the Streaming SDK (see {ref}`sec-streaming-sdk`).

![Virtual device|690x662,100%](https://assets.ubuntu.com/v1/4cc5a115-application_virtual-device.png)

(tut-aaos)=
# Get started with an AAOS application

This tutorial guides you through basic operations that you can do with an application based on an Android Automotive OS (AAOS) image. 

In this tutorial, we will be focusing on the following tasks:
- Creating an application using an AAOS image.
- Streaming the application you created with a specific screen resolution.
- Setting the temperature of the automotive using the Vehicle Hardware Abstraction Layer (VHAL) controls.

## Prerequisites
We will use the appliance dashboard to perform the tasks for this tutorial. So if you haven’t installed the Anbox Cloud Appliance yet, you must do that first.

Follow the installation instructions available at {ref}`tut-installing-appliance` to install and initialise the appliance. Proceed with the tutorial when you can access the appliance dashboard.

## Create an AAOS-based application

We need an application to work with, so let's create one first.

In the *Applications* screen, add an application (**Add Application**).

Now, let's enter the values required for creating the application:
- *Application type*: `Automotive`

    This indicates that the application is for automotive systems.
- *Application name*: `my-app`
- *Resource-type*: `a4.3`

    The default value of a4.3 is sufficient for this tutorial. Resource type indicates a {ref}`pre-defined set of resources <sec-application-manifest-instance-type>` that will be made available for your application.
- *Create the image in a*: `Container`

    Your choice of whether to create the associated image in a container or a virtual machine.
- *Image*: `jammy:aaos13:amd64`

    The image name will indicate what kind of image it is, for example, `jammy:aaos13:amd64` is an AAOS image based on Ubuntu Jammy 22.04 for the amd64 architecture.

Confirm with *Add application* and wait till the *Applications* list screen shows that your application is ready.

## Stream the application with a specific screen resolution

In the *Sessions* screen, create a session to view the application (**Create session**).

Select the application that you created earlier.

Any of the *Screen resolution* options listed for the application will work but to set a custom resolution, select *Custom* from the drop-down and set the following values:
```
Width = 2304
Height = 3072
```
The screen resolutions for AAOS (automotive) applications will be different from those of the AOSP (mobile) applications because the target devices are different.

It is important to understand that higher screen resolutions consume more resources.

Select a desired *Frame rate*, for example, 60.

Confirm with *Create session*.

## Set automotive temperature using the VHAL panel

The dashboard uses self-signed certificates. Before the stream starts, you might see a warning from your browser to accept the certificates manually. You will see the Android UI streaming once you accept the certificate and reload the page.

The controls on the right help you set specific automotive properties.

Now, let's try setting the temperature of the automotive:

- Open the HVAC panel (fan icon in the navigation bar at the bottom).
- Select *All VHAL properties* on the right.
- Search for *HVAC_TEMPERATURE_DISPLAY_UNITS*. This indicates the unit of temperature.

    By default, the HVAC panel displays the temperature in Fahrenheit while the VHAL properties show values in Celsius. To avoid confusion, let's switch the HVAC panel display to Celsius.

    Update the value from 49 to 50.
- Now, search for *HVAC_TEMPERATURE_SET*.
- Modify the temperatures for *Area 1* and *Area 2*.
- **Save** to see your temperature updates reflect on the HVAC panel.

## Learn more

Learn about the various [supported system properties in the VHAL](https://source.android.com/docs/automotive/vhal/system-properties).

You can also use the {ref}`Anbox HTTP API <sec-anbox-https-api-vhal>` to adjust the properties using the CLI.

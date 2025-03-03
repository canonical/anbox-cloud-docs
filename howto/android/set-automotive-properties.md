(howto-set-automotive-properties)=
# How to set automotive properties using VHAL

This how-to guide explains the steps of how to set the automotive properties when using an AAOS application.

> Watch the [video tutorial](https://www.youtube.com/watch?v=irx2ylMalos).

## Prerequisites

- Install and initialize Anbox Cloud. Register with the dashboard and log in with your Ubuntu SSO account. {ref}`tut-installing-appliance` shows how to get this step done.
- Create an automotive application and stream it. {ref}`tut-create-virtual-device` shows how to create an application. Remember to choose *Automotive* as your application type.

## Set values using the VHAL panel

Now, you are streaming the AAOS application. The controls on the right help you set specific automotive properties.

Now, try setting the temperature of the automotive:

1. Open the HVAC panel (fan icon in the navigation bar at the bottom).
1. Select *All VHAL properties* on the right.
1. Search for *HVAC_TEMPERATURE_DISPLAY_UNITS* which indicates the unit of temperature.
1. By default, the HVAC panel displays the temperature in Fahrenheit while the VHAL properties show values in Celsius. To switch the HVAC panel display to Celsius, update the value from 49 to 50.
1. Now, search for *HVAC_TEMPERATURE_SET*. Modify the temperatures for *Area 1* and *Area 2* and *Save*.

You can learn more about the various [supported system properties in the VHAL](https://source.android.com/docs/automotive/vhal/system-properties) and try changing them.

You can also use the {ref}`Anbox HTTP API <sec-anbox-https-api-vhal>` to adjust the properties using the CLI.

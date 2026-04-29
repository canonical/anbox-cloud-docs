(howto-set-automotive-properties)=
# Set automotive properties using VHAL

This guide demonstrates how automotive application developers can test their features in automotive infotainment systems, using Anbox Cloud, without requiring the vehicle hardware.

**A video version of this guide is also available:**

```{raw} html
<iframe width="640" height="360"
        src="https://www.youtube.com/embed/irx2ylMalos"
        title="Set automotive properties using VHAL"
        frameborder="0"
        allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture"
        allowfullscreen>
</iframe>
```

## Prerequisites

Install and initialize Anbox Cloud. Register with the dashboard and log in with your Ubuntu SSO account. Follow {ref}`tut-installing-appliance` to do this in the appliance.

You need an automotive instance that you can stream. {ref}`tut-create-virtual-device` shows how to create an instance. Remember to choose *Automotive* as your instance type.

## Change an automotive property

When you have an AAOS instance streaming, you can adjust the automotive properties using the dashboard or the API.

<!-- vale Canonical.000-US-spellcheck = NO -->
::::{tab-set}
:::{tab-item} API
:sync: api
<!-- vale Canonical.000-US-spellcheck = YES -->

You can adjust the automotive properties with the {ref}`Anbox HTTP API <sec-anbox-https-api-vhal>`.

Inside the instance terminal, install `curl` to send HTTP requests using the API:

        sudo apt update
        sudo apt install curl

Install `jq` so that you can parse JSON responses better:

        sudo apt install jq

Check the value set for the temperature property currently and observe the response:

        curl -s -X GET --unix-socket /run/user/1000/anbox/sockets/api.unix s/1.0/vhal/358614275/49 | jq .

The output could look like:

```
{
  "metadata": {
    "value": {
      "area_id": 49,
      "float_values": [
        16
      ],
      "prop": 358614275,
      "status": 0,
      "timestamp": 0
    }
  },
  "status": "Success",
  "status_code": 200,
  "type": "sync"
}
```

Try changing the temperature property:

```
curl -s -X PUT --unix-socket /run/user/1000/anbox/sockets/api.unix s/1.0/vhal \
  -d '{
    "prop_id": 358614275,
    "area_id": 49,
    "float_values": [22.5]
  }'
```

Now if you try the `GET` query again, you should be able to see your changes reflected.

:::

:::{tab-item} Dashboard
:sync: dashboard

The dashboard has a HVAC panel with which you can control the automotive properties.

For example, try setting the temperature property:

Open the HVAC panel (fan icon in the navigation bar at the bottom).

Select *All VHAL properties* on the right.

Search for *HVAC_TEMPERATURE_DISPLAY_UNITS* which indicates the unit of temperature.

By default, the HVAC panel displays the temperature in Fahrenheit while the VHAL properties show values in Celsius. To switch the HVAC panel display to Celsius, update the value from 49 to 50.

Now, search for *HVAC_TEMPERATURE_SET*. Modify the temperatures for *Area 1* and *Area 2* and *Save*.

:::
::::

To change other supported system properties in the VHAL, see [Android documentation](https://source.android.com/docs/automotive/vhal/system-properties).

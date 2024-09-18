(ref-api)=
# API reference

Anbox Cloud includes various APIs to help you build solutions with it. This page provides an overview of the available APIs and their uses.

All these APIs except for the {ref}`anbox-https-api` have an auto-generated Open API specification describing its API endpoints.

## AMS HTTP API

The AMS services provide an HTTP based API to help you manage all of its objects. Internally the `amc` client uses the same API to perform its operation.

## Anbox HTTP API

The Anbox runtime inside each instance managed by the AMS provides an HTTP API over a UNIX domain socket that helps interacting with various functionalities offered by Anbox. This includes the injection of position or sensor events into Android, among other things.

You can find the API specification at {ref}`anbox-https-api`.

## Anbox Stream Gateway API

The Anbox Stream Gateway service provides an API endpoint to help you to manage streaming sessions.

```{toctree}
:hidden:

ams-api
anbox-https-api
Anbox Platform API<https://canonical.github.io/anbox-cloud.github.com/latest/anbox-platform-sdk/>
gateway-api
```

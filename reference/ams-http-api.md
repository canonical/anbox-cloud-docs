All the communications between AMS and its clients happen using a  RESTful API over HTTP which is then encapsulated over either TLS for  remote operations or a Unix socket for local operations

Not all REST API endpoints require authentication:

* GET to `/` is allowed for everyone
* GET to `/1.0` is allowed for everyone
* GET to `/1.0/version` is allowed for everyone

Some endpoints require an additional authentication token to ensure that the requester is authorised to access the resource:

* GET to `/1.0/artifacts`
* PATCH to `/1.0/containers/<name>`


## API versioning

The details of a version of the API can be retrieved using `GET /<version>`.
For example `GET /1.0`

The reason for a major API bump is if the API breaks backward compatibility.

Feature additions done without breaking backward compatibility only result in addition to `api_extensions` which can be used by the client to check if a given feature is supported by the server.

## Return values

There are three standard return types:

 * Standard return value
 * Background operation
 * Error

### Standard return value

For a standard synchronous operation, the following dict is returned:

```json
{
    "type": "sync",
    "status": "Success",
    "status_code": 200,
    "metadata": {}                          # Extra resource/action specific metadata
}
```

HTTP code must be 200.

### Background operation

When a request results in a background operation, the HTTP code is set to 202 (Accepted)
and the Location HTTP header is set to the operation URL.

The body is a dict with the following structure:

```json
{
    "type": "async",
    "status": "OK",
    "status_code": 100,
    "operation": "/1.0/containers/<id>",                    # URL to the background operation
    "metadata": {}                                          # Operation metadata (see below)
}
```

The operation metadata structure looks like:

```json
{
    "id": "c6832c58-0867-467e-b245-2962d6527876",           # UUID of the operation
    "class": "task",                                        # Class of the operation (task, web socket or token)
    "created_at": "2018-04-02T16:49:36.341463206+02:00",    # When the operation was created
    "updated_at": "2018-04-02T16:49:36.341463206+02:00",    # Last time the operation was updated
    "status": "Running",                                    # String version of the operation's status
    "status_code": 103,                                     # Integer version of the operation's status (use this rather than status)
    "resources": {                                          # Dictionary of resource types (container, snapshots, images) and affected resources
      "containers": [
        "/1.0/containers/3apqo5te"
      ]
    },
    "metadata": null,                                       # Metadata specific to the operation in question (in this case, nothing)
    "may_cancel": false,                                    # Whether the operation can be canceled (DELETE over REST)
    "err": ""                                               # The error string should the operation have failed
}
```

The body is mostly provided as a user friendly way of seeing what's going on without having to pull the target operation, all information in the body can also be retrieved from the background operation URL.

### Error

There are various situations in which something may immediately go wrong, in those cases, the following return value is used:

```json
{
    "type": "error",
    "error": "Failure",
    "error_code": 400,
    "metadata": {}                      # More details about the error
}
```

HTTP code must be one of 400, 401, 403, 404, 409, 412 or 500.

## Status codes

The AMS REST API often has to return status information, be that the reason for an error, the current state of an operation or the state of the various resources it exports.

To make it simple to debug, all of those are always doubled. There is a numeric representation of the state which is guaranteed never to change and can be relied on by API clients. Then there is a text version meant to make it easier for people manually using the API to figure out what's happening.

In most cases, those will be called status and `status_code`, the former being the user friendly string representation and the latter the fixed numeric value.

The codes are always 3 digits, with the following ranges:

 * 100 to 199: resource state (started, stopped, ready, ...)
 * 200 to 399: positive action result
 * 400 to 599: negative action result
 * 600 to 999: future use

### List of current status codes

Code  | Meaning
---|------
100   | Operation created
101   | Started
102   | Stopped
103   | Running
104   | Cancelling
105   | Pending
106   | Starting
107   | Stopping
108   | Aborting
109   | Freezing
110   | Frozen
111   | Thawed
200   | Success
400   | Failure
401   | Cancelled

## Recursion

To optimise queries of large lists, recursion is implemented for collections. A `recursion` argument can be passed to a GET query against a collection.

The default value is 0 which means that collection member URLs are returned. Setting it to 1 will have those URLs be replaced by the object they point to (typically a dict).

Recursion is implemented by simply replacing any pointer to a job (URL) by the object itself.

## Async operations

Any operation which may take more than a second to be done must be done in the background, returning a background operation ID to the client.

The client will then be able to either poll for a status update or wait for a notification using the long-poll API.

## Notifications

A web-socket based API is available for notifications, different notification types exist to limit the traffic going to the client.

It's recommended that the client always subscribes to the operations notification type before triggering remote operations so that it doesn't have to then poll for their status.

## PUT vs PATCH

The AMS API supports both PUT and PATCH to modify existing objects.

PUT replaces the entire object with a new definition, it's typically called after the current object state was retrieved through GET.

To avoid race conditions, the ETag header should be read from the GET response and sent as If-Match for the PUT request. This will cause AMS to fail the request if the object was modified between GET and PUT.

PATCH can be used to modify a single field inside an object by only specifying the property that you want to change. To unset a key, setting it to empty will usually do the trick, but there are cases where PATCH won't work and PUT needs to be used instead.

## Authorisation

Some operation may require a token to be included in the HTTP Authorisation header like this:

 * `Authorization: bearer <token>`

No matter if the request is already authenticated using a trusted certificate. If the token is not valid, the request is rejected by the server. This ensures that only authorised clients can access those endpoints.

## File upload

Some operations require uploading a payload. To prevent the difficulties of handling multipart requests, another solution has been taken: A unique file is uploaded and its bytes are included in the body of the request. Some metadata associated with the file is included in extra HTTP headers:

 * X-AMS-Fingerprint: fingerprint of the payload being added
 * X-AMS-Request: metadata for the payload. This is a JSON, specific for the operation.

## API structure

 * [`/`](heading--#)
 * [`/1.0`](#heading--10)
 * [`/1.0/addons`](#heading--10addons)
   * [`/1.0/addons/<id or name>`](#heading--10addonsname)
   * [`/1.0/addons/<id or name>/<version>`](#heading--10addonsnameversion)
 * [`/1.0/applications`](#heading--10applications)
     * [`/1.0/applications/<id or name>`](#heading--10applicationsname)
       * [`/1.0/applications/<id or name>/manifest`](#heading--10applicationsnamemanifest)
       * [`/1.0/applications/<id or name>/<version>`](#heading--10applicationsnameversion)
       * [`/1.0/applications/<id or name>/<version>/manifest`](#heading--10applicationsnameversionmanifest)
  * [`/1.0/certificates`](#heading--10certificates)
     * [`/1.0/certificates/<fingerprint>`](#heading--10certificatesid)
   * [`/1.0/config`](#heading--10config)
   * [`/1.0/containers`](#heading--10containers)
     * [`/1.0/containers/<id>`](#heading--10containersid)
       * [`/1.0/containers/<id>/logs`](#heading--10containersidlogs)
       * [`/1.0/containers/<id>/logs/<name>`](#heading--10containersidlogsname)
   * [`/1.0/events`](#heading--10events)
   * [`/1.0/images`](#heading--10images)
     * [`/1.0/images/<id or name >`](#heading--10images)
       * [`/1.0/images/<id or name>/<version>`](#heading--10imagesidversion)
   * [`/1.0/nodes`](#heading--10nodes)
     * [`/1.0/nodes/<name>`](#heading--10nodesname)
   * [`/1.0/operations`](#heading--10operations)
     * [`/1.0/operations/<uuid>`](#heading--10operationsuuid)
       * [`/1.0/operations/<uuid>/wait`](#heading--10operationsuuidwait)
       * [`/1.0/operations/<uuid>/websocket`](#heading--10operationsuuidwebsocket)
   * [`/1.0/tasks`](#heading--10tasks)
   * [`/1.0/version`](#heading--10version)

## API details
<a name="heading--10"></a>
### `/1.0/`
#### GET
 * Description: Server configuration
 * Authentication: guest, untrusted or trusted
 * Operation: sync
 * Cancellable: no

Example:
```bash
curl -s -X GET --insecure --cert client.crt --key client.key <AMS_SERVICE_URL>/1.0
```

Output (if trusted):

```json
{
  "type": "sync",
  "status": "Success",
  "status_code": 200,
  "operation": "",
  "error_code": 0,
  "error": "",
  "metadata": {
    "api_extensions": [],                           // List of API extensions added after the API was marked stable
    "api_status": "stable",                         // API implementation status (one of, development, stable or deprecated)
    "api_version": "1.0",                           // The API version as a string
    "auth": "trusted",                              // Authentication state, one of "guest", "untrusted" or "trusted"
    "auth_methods": [                               // Authentication method
      "2waySSL"
    ]
  }
}
```

<a name="heading--10addons"></a>
### `/1.0/addons`
#### GET
 * Description: List of addons
 * Authentication: trusted
 * Operation: sync
 * Cancellable: no

Example:
```bash
curl -s -X GET --insecure --cert client.crt --key client.key <AMS_SERVICE_URL>/1.0/addons
```

Output:

```json
{
  "type": "sync",
  "status": "Success",
  "status_code": 200,
  "operation": "",
  "error_code": 0,
  "error": "",
  "metadata": [
    "/1.0/addons/foo",
    "/1.0/addons/bar"
  ]
}
```

#### POST
 * Description: Create a new addon
 * Authentication: trusted
 * Operation: async
 * Cancellable: no

In the HTTP payload upload case, the following headers may be set by the client:

* `Content-Type:`: application/octet-stream (mandatory field)
* `X-AMS-Request`: JSON format metadata (mandatory field)
* `X-AMS-Fingerprint:`: SHA-256 (if set, the uploaded payload must match)

For an addon upload, the `X-AMS-Request` header is comprised of:

```json
{
    "name": "my-addon"
}
```

The payload to upload must be a tarball compressed with bzip2 or a zip archive. Also, it must contain a `manifest.yaml` which declares the basic addon information and at least an install hook for the creation. For the layout of the addon and supported syntax, please refer to [How to use addons](https://discourse.ubuntu.com/t/managing-addons/17759) for more details.

Example:
```bash
curl -s --header "Content-Type: application/octet-stream"  --header 'X-AMS-Request: {"name": "my-addon"}' -X POST --insecure --cert client.crt --key client.key --data-binary @addon.tar.bz2 <AMS_SERVICE_URL>/1.0/addons
```

Output:

```json
{
  "type": "async",
  "status": "Operation created",
  "status_code": 100,
  "operation": "1.0/operations/603055f6-5cc6-4668-9f2d-28d8bce64024",
  "error_code": 0,
  "error": "",
  "metadata": {
    "id": "603055f6-5cc6-4668-9f2d-28d8bce64024",
    "class": "task",
    "description": "Creating addon",
    "created_at": "2018-07-21T03:02:22.091350247Z",
    "updated_at": "2018-07-21T03:02:22.091350247Z",
    "status": "Running",
    "status_code": 103,
    "resources": {
      "addons": [
        "/1.0/addons/my-addon"
      ]
    },
    "metadata": null,
    "may_cancel": true,
    "err": "",
    "server_address": ""
  }
}
```

To monitor the status of an addon upload operation, please refer to [`/1.0/operations`](#heading--10operations)

<a name="heading--10addonsname"></a>
### `/1.0/addons/<id or name>`
#### GET
 * Description: Retrieve information about an addon
 * Authentication: trusted
 * Operation: sync
 * Cancellable: no

Example:
```bash
curl -s -X GET --insecure --cert client.crt --key client.key <AMS_SERVICE_URL>/1.0/addons/my-addon
```

Output:

```json
{
  "type": "sync",
  "status": "Success",
  "status_code": 200,
  "operation": "",
  "error_code": 0,
  "error": "",
  "metadata": {
    "name": "my-addon",
    "versions": [                 // List of versions
      {
        "version": 0,             // Version number
        "fingerprint":  "60d8af000f50527f83f30673586329717384d7243858fd6216a8eeb488802d4a",  // SHA-256 fingerprint
        "size": 283,              // Size in bytes
        "created_at": 1611716542  // Seconds since Jan 01 1970. (UTC)
      }
    ],
    "used_by": null               // List of applications to use this addon
  }
}
```

#### DELETE
 * Description: Delete an addon
 * Authentication: trusted
 * Operation: async
 * Cancellable: no

Example:
```bash
curl -s -X DELETE --insecure --cert client.crt --key client.key <AMS_SERVICE_URL>/1.0/addons/my-addon
```

Output:

```json
{
  "type": "async",
  "status": "Operation created",
  "status_code": 100,
  "operation": "1.0/operations/0cb31170-c2af-429b-97bc-016c94daf6a2",
  "error_code": 0,
  "error": "",
  "metadata": {
    "id": "0cb31170-c2af-429b-97bc-016c94daf6a2",
    "class": "task",
    "description": "Deleting addon",
    "created_at": "2018-07-27T03:26:46.696046272Z",
    "updated_at": "2018-07-27T03:26:46.696046272Z",
    "status": "Running",
    "status_code": 103,
    "resources": {
      "addons": [
        "/1.0/addons/my-addon"
      ]
    },
    "metadata": null,
    "may_cancel": true,
    "err": "",
    "server_address": ""
  }
}
```
To monitor the status of an addon deletion operation, please refer to [`/1.0/operations`](#heading--10operations)

#### PATCH (ETag supported)
 * Description: Update addon metadata and creates a new addon version for it
 * Authentication: trusted
 * Operation: async
 * Cancellable: no

In the HTTP addon update case, the following headers may be set by the client:

* `Content-Type:`: application/octet-stream (mandatory field)
* `X-AMS-Request`: JSON format metadata (mandatory field)
* `X-AMS-Fingerprint:`: SHA-256 (if set, the uploaded payload must match)

For an addon patch, the `X-AMS-Request` header is comprised of an empty JSON object

```json
{}
```

Example
```bash
curl -s --header "Content-Type: application/octet-stream"  --header 'X-AMS-Request: {}' -X PATCH --insecure --cert client.crt --key client.key --data-binary @addon.tar.bz2 <AMS_SERVICE_URL>/1.0/addons/my-addon
```

Output:

```json
{
  "type": "async",
  "status": "Operation created",
  "status_code": 100,
  "operation": "1.0/operations/7022c28e-ed5b-484a-9bb2-43706b01e229",
  "error_code": 0,
  "error": "",
  "metadata": {
    "id": "7022c28e-ed5b-484a-9bb2-43706b01e229",
    "class": "task",
    "description": "Updating addon",
    "created_at": "2018-07-27T03:46:31.431217757Z",
    "updated_at": "2018-07-27T03:46:31.431217757Z",
    "status": "Running",
    "status_code": 103,
    "resources": {
      "addons": [
        "/1.0/addons/my-addon"
      ]
    },
    "metadata": null,
    "may_cancel": true,
    "err": "",
    "server_address": ""
  }
}
```

To monitor the status of an addon update operation, please refer to [`/1.0/operations`](#heading--10operations)

<a name="heading--10addonsnameversion"></a>
### `/1.0/addons/<id or name>/<version>`
#### DELETE
 * Description: Delete specific version of an addon
 * Authentication: trusted
 * Operation: async
 * Cancellable: no

Example
```bash
curl -s -X DELETE --insecure --cert client.crt --key client.key <AMS_SERVICE_URL>/1.0/addons/my-addon/1
```

Output:

```json
{
  "type": "async",
  "status": "Operation created",
  "status_code": 100,
  "operation": "1.0/operations/bc20dcd5-6e8c-4feb-b3f0-cb8d2fd7238a",
  "error_code": 0,
  "error": "",
  "metadata": {
    "id": "bc20dcd5-6e8c-4feb-b3f0-cb8d2fd7238a",
    "class": "task",
    "description": "Deleting addon version",
    "created_at": "2018-07-27T03:55:58.005511611Z",
    "updated_at": "2018-07-27T03:55:58.005511611Z",
    "status": "Running",
    "status_code": 103,
    "resources": {
      "addons": [
        "/1.0/addons/my-addon"
      ]
    },
    "metadata": null,
    "may_cancel": true,
    "err": "",
    "server_address": ""
  }
}
```

To monitor the status of an addon version deletion operation, please refer to [`/1.0/operations`](#heading--10operations)

<a name="heading--10applications"></a>
### `/1.0/applications`
#### GET
 * Description: List of applications
 * Authentication: trusted
 * Operation: sync
 * Cancellable: no

Example
```bash
curl -s -X GET --insecure --cert client.crt --key client.key <AMS_SERVICE_URL>/1.0/applications
```

Output:

```json
{
  "type": "sync",
  "status": "Success",
  "status_code": 200,
  "operation": "",
  "error_code": 0,
  "error": "",
  "metadata": [
    "/1.0/applications/c08fr0gj1qm443dtn870"
  ]
}
```

#### POST
 * Description: Create a new application
 * Authentication: trusted
 * Operation: async
 * Cancellable: no

In the HTTP application upload case, the following headers may be set by the client:

* `Content-Type:`: application/octet-stream (mandatory field)
* `X-AMS-Fingerprint:`: SHA-256 (if set, the uploaded payload must match)

The payload to upload must be a tarball compressed with bzip2 or a zip archive. Also it must contain a `manifest.yaml` which declares the basic application information for the creation. For the layout of the application and supported syntax, see [How to create an application](https://discourse.ubuntu.com/t/create-an-application/24198) for more details.

To support the following syntax in the application `manifest.yaml`, the server requires a corresponding extension

Syntax in manifest            |   Extension
----------------|------------------------------------
watchdog |  `application_watchdog_settings`
resources |  `application_resource_customization`
services    |  `application_services_configuration`
version     |  `application_manifest_version`
video-encoder | `application_gpu_encoder`

Example
```bash
curl -s -X POST --header "Content-Type: application/octet-stream" --insecure --cert client.crt --key client.key --data-binary @app.tar.bz2 <AMS_SERVICE_URL>/1.0/applications
```

Output:

```json
{
  "type": "async",
  "status": "Operation created",
  "status_code": 100,
  "operation": "1.0/operations/d1cb8d8f-1471-40d7-9b1a-3c222afbde53",
  "error_code": 0,
  "error": "",
  "metadata": {
    "id": "d1cb8d8f-1471-40d7-9b1a-3c222afbde53",
    "class": "task",
    "description": "Creating application",
    "created_at": "2018-07-27T05:43:30.66261346Z",
    "updated_at": "2018-07-27T05:43:30.66261346Z",
    "status": "Running",
    "status_code": 103,
    "resources": {
      "applications": [
        "/1.0/applications/c08fr0gj1qm443dtn870"
      ]
    },
    "metadata": null,
    "may_cancel": true,
    "err": "",
    "server_address": ""
  }
}
```

To monitor the status of an application  creation operation, please refer to [`/1.0/operations`](#heading--10operations)

<a name="heading--10applicationsname"></a>
### `/1.0/applications/<id or name>`
#### GET
 * Description: Retrieve information about an application
 * Authentication: trusted
 * Operation: sync
 * Cancellable: no

Example
```bash
curl -s -X GET --insecure --cert client.crt --key client.key <AMS_SERVICE_URL>/1.0/applications/my-app
```

Output:

```json
{
  "type": "sync",
  "status": "Success",
  "status_code": 200,
  "operation": "",
  "error_code": 0,
  "error": "",
  "metadata": {
    "id": "c08fr0gj1qm443dtn870",
    "name": "my-app",
    "status_code": 2,
    "status": "ready",        // Application status
    "instance_type": "a4.3",  // Instance type
    "boot_package": "com.lolo.io.onelist",  // Boot application
    "parent_image_id": "btavtegj1qm58qg7ru50",
    "published": true,
    "versions": [             // List of all versions
      {
        "number": 0,
        "manifest_version": "",
        "parent_image_id": "btavtegj1qm58qg7ru50",   // Base image the application is created from
        "parent_image_version": 0,                   // Base image version
        "status_code": 3,
        "status": "active",                          // Application status
        "published": true,                           // Publication status
        "created_at": 1532150640,
        "boot_activity": "",                         // Boot activity on application start
        "required_permissions": null,                // Required Android application permissions
        "addons": [],                                // Attached addons
        "extra_data": {},                            // Extra data to be installed on application creation
        "error_message": "",
        "video_encoder": "gpu-preferred",            // Video encoder settings
        "watchdog": {                                // Watchdog settings
          "disabled": false,
          "allowed-packages": null
        }
      }
    ],
    "addons": [],
    "created_at": 1532150640,
    "immutable": false,
    "tags": null,
    "resources": {        // Application resources
      "gpu-slots": -1
    },
    "abi": "x86_64",      // Application ABI
    "inhibit_auto_updates": false  // Application automatically update configuration
  }
}
```

#### PATCH (ETag supported)
 * Description: Update existing application
 * Authentication: trusted
 * Operation: sync
 * Cancellable: no

An application can be updated with either a new package or specific fields.
The `Content-Type` header of HTTP patch request is different when uploading
an application in either way.

Update methods            |  Content-Type
----------------|------------------------------------
With a new package |  `application/octet-stream`
With specified fields        |  `application/json`

An application package can be uploaded with a bzip2 compressed payload if the former method is taken.

Example
```bash
curl -s --header "Content-Type: application/octet-stream" -X PATCH --insecure --cert client.crt --key client.key --data-binary @app_1.tar.bz2 <AMS_SERVICE_URL>/1.0/applications/my-app
```

Output:
```json
{
  "type": "async",
  "status": "Operation created",
  "status_code": 100,
  "operation": "1.0/operations/e1dc826e-8627-4225-94b1-808ac0e40bfb",
  "error_code": 0,
  "error": "",
  "metadata": {
    "id": "e1dc826e-8627-4225-94b1-808ac0e40bfb",
    "class": "task",
    "description": "Updating application",
    "created_at": "2018-07-27T06:18:33.157030462Z",
    "updated_at": "2018-07-27T06:18:33.157030462Z",
    "status": "Running",
    "status_code": 103,
    "resources": {
      "applications": [
        "/1.0/applications/my-app"
      ]
    },
    "metadata": null,
    "may_cancel": true,
    "err": "",
    "server_address": ""
  }
}
```

For the specific field update case, a JSON format payload is accepted.

```json
{
    "tags": [ "game" ],
    "instance-type": "a4.3"
}
```

Example
```bash
curl -s --header "Content-Type: application/json" -X PATCH --insecure --cert client.crt --key client.key --data "$payload" <AMS_SERVICE_URL>/1.0/applications/my-app
```

To monitor the status of an application update operation, please refer to [`/1.0/operations`](#heading--10operations)

The following fields can be modified when updating an application. Changing some of those fields will lead to creating another application version.

Supported update field            |   Will create a new application version
----------------|------------------------------------
image |  no
instance-type        |  no
tags | no
addons | no
resources | no
inhibit_auto_updates | no
services | yes
watchdog |yes
boot_activity | yes
required_permissions | yes
video_encoder | yes
manifest_version | yes

To use those fields that would create a new application version on application update, the server requires `application_partial_updates` extension.

#### DELETE
 * Description: Remove an application
 * Authentication: trusted
 * Operation: async
 * Cancellable: no

In the HTTP application removal case, a JSON format payload input is required from the client:

```Payload
{
    "force": false // (boolean) Forcibly remove the application
}
```

Example
```bash
curl -s -X DELETE --insecure --cert client.crt --key client.key --data "$payload" <AMS_SERVICE_URL>/1.0/applications/my-app
```

Output:

```json
{
  "type": "async",
  "status": "Operation created",
  "status_code": 100,
  "operation": "1.0/operations/d0792e48-a65b-4dcd-87d3-90597f84f964",
  "error_code": 0,
  "error": "",
  "metadata": {
    "id": "d0792e48-a65b-4dcd-87d3-90597f84f964",
    "class": "task",
    "description": "Deleting application",
    "created_at": "2018-07-27T06:36:04.370952371Z",
    "updated_at": "2018-07-27T06:36:04.370952371Z",
    "status": "Running",
    "status_code": 103,
    "resources": {
      "applications": [
        "/1.0/applications/my-app"
      ]
    },
    "metadata": null,
    "may_cancel": true,
    "err": "",
    "server_address": ""
  }
}
```

To monitor the status of an application removal operation, please refer to [`/1.0/operations`](#heading--10operations)

<a name="heading--10applicationsnameversion"></a>
### `/1.0/applications/<id or name>/<version>`

#### GET
 * Description: Export an application version image
 * Authentication: trusted
 * Operation: sync
 * Cancellable: no
 * Extension: application_image_export

Example:
```bash
curl -s -X GET --insecure --cert client.crt --key client.key <AMS_SERVICE_URL>/1.0/applications/my-app --output app-version.tar
```
As a result, an application image that contains a piece of `metadata.yaml` and RootFS will be generated

#### DELETE
 * Description: Removes an application version
 * Authentication: trusted
 * Operation: async
 * Cancellable: no

In the HTTP application version removal case, a JSON format payload input is required from client:

```json
{
    "force": false // (boolean) Forcibly remove the application version
}
```

Example:
```bash
curl -s -X DELETE --insecure --cert client.crt --key client.key --data "$payload" \<AMS_SERVICE_URL>/1.0/applications/my-app/1
```

Output:

```json
{
  "type": "async",
  "status": "Operation created",
  "status_code": 100,
  "operation": "1.0/operations/e0d15285-cef5-4263-bcc4-f1a737a5018e",
  "error_code": 0,
  "error": "",
  "metadata": {
    "id": "e0d15285-cef5-4263-bcc4-f1a737a5018e",
    "class": "task",
    "description": "Delete application version",
    "created_at": "2018-07-27T07:17:08.222268495Z",
    "updated_at": "2018-07-27T07:17:08.222268495Z",
    "status": "Running",
    "status_code": 103,
    "resources": {
      "applications": [
        "/1.0/applications/my-app",
        "/1.0/applications/1"
      ]
    },
    "metadata": null,
    "may_cancel": true,
    "err": "",
    "server_address": ""
  }
}
```

To monitor the status of an application version removal operation, please refer to [`/1.0/operations`](#heading--10operations)

#### PATCH
 * Description: Publish/unpublish an application version
 * Authentication: trusted
 * Operation: async
 * Cancellable: no

In the HTTP application version update case, a JSON format payload input is required from the client:

```json
{
    "published": true  // (boolean) Toggle application publication status
}
```

Example:
```bash
curl -s -X PATCH --insecure --cert client.crt --key client.key --data "$payload" \<AMS_SERVICE_URL>/1.0/applications/my-app/1
```

Output:
```json
{
  "type": "async",
  "status": "Operation created",
  "status_code": 100,
  "operation": "1.0/operations/157aa633-2cf1-41d6-a8a6-92ecc1830e32",
  "error_code": 0,
  "error": "",
  "metadata": {
    "id": "157aa633-2cf1-41d6-a8a6-92ecc1830e32",
    "class": "task",
    "description": "Updating application version",
    "created_at": "2018-07-27T07:35:31.289933915Z",
    "updated_at": "2018-07-27T07:35:31.289933915Z",
    "status": "Running",
    "status_code": 103,
    "resources": {
      "applications": [
        "/1.0/applications/my-app"
      ]
    },
    "metadata": null,
    "may_cancel": true,
    "err": "",
    "server_address": ""
  }
}
```
To monitor the status of an application version update operation, please refer to [`/1.0/operations`](#heading--10operations)

<a name="heading--10applicationsnamemanifest"></a>
### `/1.0/applications/<id or name>/manifest`

#### GET
 * Description: Get latest application manifest file
 * Authentication: trusted
 * Operation: sync
 * Cancellable: no

Example:
```bash
curl -s -X GET --insecure --cert client.crt --key client.key <AMS_SERVICE_URL>/1.0/applications/my-app/manifest
```

Output:
```yaml
name: my-app
image: Android10
instance-type: a4.3
boot-package: com.lolo.io.onelist
video-encoder: gpu-preferred
watchdog:
  disabled: false
  allowed-packages: []
abi: x86_64
```
The use of this API requires the `application_manifest_download` extension is supported by the server.

<a name="heading--10applicationsnamemanifestmanifest"></a>
### `/1.0/applications/<id or name>/<version>/manifest`

#### GET
 * Description: Get one specific application version manifest file
 * Authentication: trusted
 * Operation: sync
 * Cancellable: no

Example:
```bash
curl -s -X GET --insecure --cert client.crt --key client.key <AMS_SERVICE_URL>/1.0/applications/my-app/0/manifest
```

Output:
```yaml
name: my-app
image: Android10
instance-type: a4.3
boot-package: com.lolo.io.onelist
video-encoder: gpu-preferred
watchdog:
  disabled: false
  allowed-packages: []
abi: x86_64
```
The use of this API requires the `application_manifest_download` extension is supported by the server.

<a name="heading--10certificates"></a>
### `/1.0/certificates`
#### GET
 * Description: List of trusted client certificates
 * Authentication: trusted
 * Operation: sync
 * Cancellable: no

Example:
```bash
curl -s -X GET --insecure --cert client.crt --key client.key <AMS_SERVICE_URL>/1.0/certificates
```

Output:

```json
{
  "type": "sync",
  "status": "Success",
  "status_code": 200,
  "operation": "",
  "error_code": 0,
  "error": "",
  "metadata": [
   "/1.0/certificates/<fingerprint>",
   ]
}
```

#### POST
 * Description: Registers a new client certificate as trusted
 * Authentication: trusted
 * Operation: sync
 * Cancellable: no

In the HTTP certificate removal case, a JSON format payload is required sent by the client:

```json
{
    "certificate": "MIIFUTCCAzmgAw...xjKoUEEQOzJ9",  # Base64 certificate content without header and footer
    "trust-password": "aahhdjiks9",                  # Only needed if not using an already trusted client
                                                     # certificate in the SSL request or using the local unix socket
}
```

Example:
```bash
curl -s -X POST --insecure --cert client.crt --key client.key --data "$payload" <AMS_SERVICE_URL>/1.0/certificates
```

Output:

```json
{
  "type": "sync",
  "status": "Success",
  "status_code": 200,
  "operation": "",
  "error_code": 0,
  "error": "",
  "metadata": null
}
```

<a name="heading--10certificatesid"></a>
### `/1.0/certificates/<fingerprint>`
#### GET
 * Description: Retrieve information about a stored certificate
 * Authentication: trusted
 * Operation: sync
 * Cancellable: no

Example:
```bash
curl -s -X GET --insecure --cert client.crt --key client.key <AMS_SERVICE_URL>/1.0/certificates/<fingerprint>
```

Output:

```json
{
    "certificate": "-----BEGIN CERTIFICATE-----
MIIFUTCCAzmgAw
...
xjKoUEEQOzJ9
-----END CERTIFICATE-----",  # Base64 certificate content, including header and footer
    "fingerprint": "<fingerprint>"
}
```

#### DELETE
 * Description: Remove specified certificate from the trusted store
 * Authentication: trusted
 * Operation: async
 * Cancellable: no

Example:
```bash
curl -s -X DELETE --insecure --cert client.crt --key client.key <AMS_SERVICE_URL>/1.0/certificates/<fingerprint>
```

Output:
```json
{
  "type": "async",
  "status": "Operation created",
  "status_code": 100,
  "operation": "1.0/operations/469f1838-3f10-43cb-97e4-41f49627cf36",
  "error_code": 0,
  "error": "",
  "metadata": {
    "id": "469f1838-3f10-43cb-97e4-41f49627cf36",
    "class": "task",
    "description": "Deleting certificate",
    "created_at": "2018-07-27T12:30:54.65841646Z",
    "updated_at": "2018-07-27T12:30:54.65841646Z",
    "status": "Running",
    "status_code": 103,
    "resources": {
      "certificates": [
        "/1.0/certificates/<fingerprint>"
      ]
    },
    "metadata": null,
    "may_cancel": true,
    "err": "",
    "server_address": ""
  }
}
```

To monitor the status of a certificate removal operation, please refer to [`/1.0/operations`](#heading--10operations)

<a name="heading--10config"></a>
### `/1.0/config`
#### GET
 * Description: Retrieve list of all configuration items
 * Authentication: trusted
 * Operation: sync
 * Cancellable: no

Example:
```bash
curl -s -X GET --insecure --cert client.crt --key client.key <AMS_SERVICE_URL>/1.0/config
```
Output:

```json
{
  "type": "sync",
  "status": "Success",
  "status_code": 200,
  "operation": "",
  "error_code": 0,
  "error": "",
  "metadata": {
    "config": {
      "application.addons": "",          // (comma separated list) Addons that will be attached to every application
      "application.auto_publish": true,  // (true/false) Auto publish application when they are created
      "application.default_abi": "",     // Default application ABI, would be an ABI with cluster compatible if unset
      "application.max_published_versions": 3,  // (number) Limit the number of stored application versions
      "container.default_platform": "",  // (string) Default platform to launch containers with. The `null` platform will be used if unset
      "container.features": "",          // Features to apply when launching a container
      "container.security_updates": false,  // Apply security updates when boostraping an applicaiton
      "core.proxy_http": "",             // HTTP proxy for AMS service
      "core.proxy_https": "",            // HTTPS proxy for AMS service
      "core.proxy_ignore_hosts": "",     // Hosts to be ignored in the network proxy
      "core.trust_password": true,       // Password to be used by the untrusted client to talk to AMS
      "gpu.allocation_mode": "all",      // GPU allocation mode, optional values: "one" or "all"
      "gpu.type": "none",                // GPU type, optional values: "none", "nvidia", "intel" or "amd"
      "images.allow_insecure": false,    // (true/false) Allow an insecure image server
      "images.auth": true,               // Authentication token for security purpose, `true` implies an auth token has been set, vice versa.
      "images.update_interval": "5m",    // (time) Frequency of updates from image server
      "images.url": "https://images.anbox-cloud.io/stable/", // (string) URL for image server
      "images.version_lockstep": "true", // Prevent images of new minor releases to be pulled by AMS
      "registry.filter": "",             // (comma separated list) Filter out applications without matching tags
      "registry.fingerprint": <fingerprint>, // (string) Fingerprint of registry certificate
      "registry.mode": "pull",           // (pull/push/manual) Whether AMS should act as a client or publisher automatically synchronizing applications with AAR, or manually doing so. Please refer to https://anbox-cloud.io/docs/explanation/aar for all details.
      "registry.update_interval": "5s",  // (time) Frequency of updates from registry
      "registry.url": "https://127.0.0.1:3000", // (string) URL of Anbox Application Registry
      "scheduler.strategy": "spread"     // (spread|binpack) Container allocation schedule strategery
    }
  }
}
```

#### PATCH
 * Description: Modify one specific configuration item
 * Authentication: trusted
 * Operation: async
 * Cancellable: no

In the HTTP configuration modification case, a JSON format payload is required sent by the client:

```json

{
"name": "application.auto_publish",
"value": "false"
}
```

Example:
```bash
curl -s -X PATCH --insecure --cert client.crt --key client.key --data "$payload" <AMS_SERVICE_URL>/1.0/config
```
Output:

```json
{
  "type": "async",
  "status": "Operation created",
  "status_code": 100,
  "operation": "1.0/operations/5f2b3817-ada1-43d3-9ed0-0c9ed3a4a20e",
  "error_code": 0,
  "error": "",
  "metadata": {
    "id": "5f2b3817-ada1-43d3-9ed0-0c9ed3a4a20e",
    "class": "task",
    "description": "Applying configuration",
    "created_at": "2018-07-27T12:59:14.889009796Z",
    "updated_at": "2018-07-27T12:59:14.889009796Z",
    "status": "Running",
    "status_code": 103,
    "resources": null,
    "metadata": null,
    "may_cancel": true,
    "err": "",
    "server_address": ""
  }
}
```

To monitor the status of a configuration modification operation, please refer to [`/1.0/operations`](#heading--10operations)


<a name="heading--10containers"></a>
### `/1.0/containers`
#### GET
 * Description: Retrieve list of all available containers
 * Authentication: trusted
 * Operation: sync
 * Cancellable: no

Example:
```bash
curl -s -X GET --insecure --cert client.crt --key client.key <AMS_SERVICE_URL>/1.0/containers
```

Output:

```json
{
  "type": "sync",
  "status": "Success",
  "status_code": 200,
  "operation": "",
  "error_code": 0,
  "error": "",
  "metadata": [
     "/1.0/containers/c00i2s0j1qm4f18jdkfg"
  ]
}
```

#### POST
 * Description: Launch a new container
 * Authentication: trusted
 * Operation: async
 * Cancellable: no

In the HTTP container launch case, a JSON format payload is required sent by the client:
Payload:

 * Payload to launch a container from an application
```json
{
    "app_id": "my-app",                       # (string | mandatory) Identifier or name of the application this container belongs to.
    "app_version": 0,                         # (number | optional) Version of the application this container uses.
    "user_data": "",                          # (string | optional) Additional data to be put into the container when bootstrapped.
    "node": "lxd1",                           # (string | optional) Lxd node to use for the container to launch
    "services": [                             # (array | optional) List of services the container provides
        {
            "name": "ssh",                    # (string) Name of service
            "port": 22,                       # (number) Network port the service listens on
            "protocols": ["tcp"],             # (array) Network protocol the services uses (udp, tcp)
            "expose": false                   # (boolean) to expose the service on the public endpoint or false to keep it on the private one
        }
    ],
    "disk_size": 5368709120,                  # (number | optional) Number of bytes disk size to be assigned for the container.
    "cpu": 2,                                 # (number | optional) Number of CPU cores to be assigned for the container,
    "memory": 4294965097,                     # (number | optional) Number of bytes memory to be assigned for the container.
    "gpu_slots": 0,                           # (number | optional) Number of GPU slots to be allocated for the container to use
    "config": {                               # (struct | optional) Config parameters included in created container
        "platform": "null",                   # (string | optional) Platform name, optional value: "null", "swrast", "webrtc". Please refer to https://anbox-cloud.io/docs/reference/anbox-platforms for all details of each platform
        "boot_package": "com.my.app",         # (string | optional) Boot package
        "boot_activity": "com.my.app.Activity",   # (string | optional)  Boot acitivty
        "metrics_server": "influxdb:192.168.100.8:8095,raw",    # (string | optional) Metrics server
        "disable_watchdog": false             # (boolean | optional) Toggle watchdog settings
    }
}
```

* Payload to launch a container from an image
```json
{
    "image_id": "Android_10",                 # (string | mandatory) Identifier or name of the application this container belongs to.
    "instance_type": "a4.3",                  # (string | mandatory)  Instance type to use for the container. Please refer to https://anbox-cloud.io/docs/manage/instance-types-reference for all available instance types.
    "image_version": 0,                       # (number | optional) Version of the image this container uses.
    "user_data": "",                          # (string | optional) Additional data to be put into the container when bootstrapped.
    "node": "lxd1",                           # (string | optional) Lxd node to use for the container to launch
    "services": [                             # (array | optional) List of services the container provides
        {
            "name": "ssh",                    # (string) Name of service
            "port": 22,                       # (number) Network port the service listens on
            "protocols": ["tcp"],             # (array) Network protocol the services uses (udp, tcp)
            "expose": false                   # (boolean) to expose the service on the public endpoint or false to keep it on the private one
        }
    ],
    "disk_size": 5368709120,                  # (number | optional) Number of bytes disk size to be assigned for the container.
    "cpu": 2,                                 # (number | optional) Number of CPU cores to be assigned for the container,
    "memory": 4294965097,                     # (number | optional) Number of bytes memory to be assigned for the container.
    "gpu_slots": 0,                           # (number | optional) Number of GPU slots to be allocated for the container to use
    "config": {                               # (struct | optional) Config parameters included in created container
        "platform": "null",                    # (string | optional) Platform name, optional value: "null", "swrast", "webrtc". Please refer to https://anbox-cloud.io/docs/reference/anbox-platforms for all details of each platform
        "boot_package": "com.my.app",         # (string | optional) Boot package
        "boot_activity": "com.my.app.Activity",   # (string | optional)  Boot acitivty
        "metrics_server": "influxdb:192.168.100.8:8095,raw"    # (string | optional) Metrics server
    }
}
```

Example:
```bash
curl -s -X POST --insecure --cert client.crt --key client.key --data "$payload" <AMS_SERVICE_URL>/1.0/containers
```

Output:
```json
{
  "type": "async",
  "status": "Operation created",
  "status_code": 100,
  "operation": "1.0/operations/84767004-de24-4f57-86c3-a0c765487c08",
  "error_code": 0,
  "error": "",
  "metadata": {
    "id": "84767004-de24-4f57-86c3-a0c765487c08",
    "class": "task",
    "description": "Creating container",
    "created_at": "2018-07-27T16:06:44.331686878Z",
    "updated_at": "2018-07-27T16:06:44.331686878Z",
    "status": "Running",
    "status_code": 103,
    "resources": {
      "containers": [
        "/1.0/containers/c08ov50j1qm6t2783d7g"
      ]
    },
    "metadata": null,
    "may_cancel": true,
    "err": "",
    "server_address": ""
  }
}
```
To monitor the status of a container creation operation, please refer to [`/1.0/operations`](#heading--10operations)

<a name="heading--10containersid"></a>
### `/1.0/containers/<id>`
#### GET
 * Description: Container information
 * Authentication: trusted
 * Operation: sync
 * Cancellable: no

Example:
```bash
curl -s -X GET --insecure --cert client.crt --key client.key <AMS_SERVICE_URL>/1.0/containers/<container_id>
```

Output:

```json
{
  "type": "sync",
  "status": "Success",
  "status_code": 200,
  "operation": "",
  "error_code": 0,
  "error": "",
  "metadata": {
    "id": "c08p730j1qm6t2783da0",
    "name": "ams-c08p730j1qm6t2783da0",
    "type": "regular",
    "status_code": 4,
    "status": "running",
    "node": "lxd1",
    "app_id": "",
    "app_version": 0,
    "image_id": "btc5bugj1qm4a9s22580",
    "image_version": 0,
    "created_at": 1611764620,
    "address": "192.168.100.3",
    "public_address": "10.226.4.52",
    "services": [
      {
        "port": 22,
        "node_port": 10000,
        "protocols": [
          "tcp"
        ],
        "expose": false,
        "name": "ssh"
      }
    ],
    "stored_logs": null,
    "error_message": "",
    "config": {
      "platform": "null",
      "boot_package": "com.my.app",
      "boot_activity": "com.my.app.Activity",
      "metrics_server": "influxdb:192.168.100.8:8095,raw"
    },
    "resources": {
      "memory": "4GB"
    },
    "architecture": "x86_64"
  }
}
```

#### DELETE
 * Description: remove the container
 * Authentication: trusted
 * Operation: async
 * Cancellable: no

Example:
```bash
curl -s -X DELETE --insecure --cert client.crt --key client.key <AMS_SERVICE_URL>/1.0/containers/<container_id>
```

Output:
```json
{
  "type": "async",
  "status": "Operation created",
  "status_code": 100,
  "operation": "1.0/operations/07ca938d-4d80-47a7-ad1f-18bbaa61ffdc",
  "error_code": 0,
  "error": "",
  "metadata": {
    "id": "07ca938d-4d80-47a7-ad1f-18bbaa61ffdc",
    "class": "task",
    "description": "Deleting container",
    "created_at": "2018-07-28T04:44:24.03707954Z",
    "updated_at": "2018-07-28T04:44:24.03707954Z",
    "status": "Running",
    "status_code": 103,
    "resources": {
      "containers": [
        "/1.0/containers/c08p730j1qm6t2783da0"
      ]
    },
    "metadata": null,
    "may_cancel": true,
    "err": "",
    "server_address": ""
  }
}
```
To monitor the status of a container removal operation, please refer to [`/1.0/operations`](#heading--10operations)

<a name="heading--10containersidlogs"></a>
### `/1.0/containers/<id>/logs`
#### GET
 * Description: List of container logs
 * Authentication: trusted
 * Operation: sync
 * Cancellable: no

Example:
```bash
curl -s -X GET --insecure --cert client.crt --key client.key <AMS_SERVICE_URL>/1.0/containers/c00hvbgj1qm4f18jdkb0/logs
```

Output:
```
{
  "type": "sync",
  "status": "Success",
  "status_code": 200,
  "operation": "",
  "error_code": 0,
  "error": "",
  "metadata": [
    "/1.0/containers/c00hvbgj1qm4f18jdkb0/logs/android.log",
    "/1.0/containers/c00hvbgj1qm4f18jdkb0/logs/console.log",
    "/1.0/containers/c00hvbgj1qm4f18jdkb0/logs/container.log",
    "/1.0/containers/c00hvbgj1qm4f18jdkb0/logs/system.log"
  ]
}
```

<a name="heading--10containersidlogsname"></a>
### `/1.0/containers/<id>/logs/<name>`
#### GET
 * Description: Retrieves a stored log file for a container
 * Authentication: trusted
 * Operation: sync
 * Cancellable: no

Example:
```bash
curl -s -X GET --insecure --cert client.crt --key client.key <AMS_SERVICE_URL>/1.0/containers/c00hvbgj1qm4f18jdkb0/logs/android.log
```

Output:
```
--------- beginning of main
01-28 07:22:44.573     5     5 I         : debuggerd: starting
--------- beginning of system
01-28 07:22:44.578     7     7 I vold    : Vold 3.0 (the awakening) firing up
01-28 07:22:44.578     7     7 V vold    : Detected support for: ext4 vfat
...
```

<a name="heading--10events"></a>
### `/1.0/events`
This URL isn't a real REST API endpoint, instead of doing a GET query on it
will upgrade the connection to a web socket on which notifications will
be sent.

#### GET
 * Description: web socket upgrade
 * Authentication: trusted
 * Operation: sync
 * Cancellable: no

URL parameter | Description  |  Optional values
----------------|-------------------|-----------------
type |   comma separated list of notifications to subscribe to (defaults to all) | `operation`, `logging`, `lifecycle`

The notification types are:

 * `operation` - notification about creation, updates and termination of all background operations
 * `logging` - every log entry from the server
 * `lifecycle` - container life cycle events

As a result,  this API call upgrades the connection to a web socket on which notifications will be sent.

This never returns. Each notification is sent as a separate JSON dict, for example:

```json
{
  "metadata": {                                 // Event metadata
    "class": "task",
    "created_at": "2017-07-28T05:02:22.92201407Z",
    "description": "Deleting container",
    "err": "",
    "id": "bc85137b-b20d-470a-a6ea-daa9a2b8506a",
    "may_cancel": false,
    "metadata": null,
    "resources": {
      "containers": [
        "/1.0/containers/c0946voj1qm6t2783db0"
      ]
    },
    "server_address": "",
    "status": "Success",
    "status_code": 200,
    "updated_at": "2017-07-28T05:02:22.92201407Z"
  },
  "timestamp": "2017-07-28T05:02:22.92201407Z",  // Current timestamp
  "type": "operation"                            // Notification type
}
```

<a name="heading--10images"></a>
### `/1.0/images`
#### GET
 * Description: List available images
 * Authentication: trusted
 * Operation: sync
 * Cancellable: no

Example:
```bash
curl -s -X GET --insecure --cert client.crt --key client.key <AMS_SERVICE_URL>/1.0/images
```

Return value:

```json
{
  "type": "sync",
  "status": "Success",
  "status_code": 200,
  "operation": "",
  "error_code": 0,
  "error": "",
  "metadata": [
    "/1.0/images/btavtegj1qm58qg7ru50"
  ]
}
```

#### POST
 * Description: Registers a new image
 * Authentication: trusted
 * Operation: async
 * Cancellable: no

In the HTTP payload upload case, the following headers may be set by the client:

* `Content-Type:`: application/octet-stream (mandatory field)
* `X-AMS-Request`: JSON format metadata (mandatory field)
* `X-AMS-Fingerprint:`: SHA-256 (if set, the uploaded payload must match)

For an image upload, the `X-AMS-Request` header is comprised of:

```
{
    "name": "my-image",  // (string) Image name
    "default": false     // (boolean) Whether the default image to be used by AMS
}
```

The payload to upload must be a tarball compressed with gzip, bzip2 or xz. It must contain a piece of `metadata.yaml` and RootFS for image registration.

Example:
```bash
curl -s --header "Content-Type: application/octet-stream" --header 'X-AMS-Request: {"name": "my-image", "default": false}' -X POST --insecure --cert client.crt --key client.key --data-binary @my-image.tar.xz <AMS_SERVICE_URL>/1.0/images
```

Output:
```json
{
  "type": "async",
  "status": "Operation created",
  "status_code": 100,
  "operation": "1.0/operations/dcdc6eb7-324c-4034-8d86-9f658c5dd696",
  "error_code": 0,
  "error": "",
  "metadata": {
    "id": "dcdc6eb7-324c-4034-8d86-9f658c5dd696",
    "class": "task",
    "description": "Adding image",
    "created_at": "2018-07-28T07:48:01.449542378Z",
    "updated_at": "2018-07-28T07:48:01.449542378Z",
    "status": "Running",
    "status_code": 103,
    "resources": {
      "images": [
        "/1.0/images/c096oc8j1qm30f20g2sg"
      ]
    },
    "metadata": null,
    "may_cancel": true,
    "err": "",
    "server_address": ""
  }
}
```
To monitor the status of an image registration operation, please refer to [`/1.0/operations`](#heading--10operations)

<a name="heading--10imagesid"></a>
### `/1.0/images/<id or name>`
#### GET
 * Description: Load image information
 * Authentication: trusted
 * Operation: sync
 * Cancellable: no

Example:
```bash
curl -s -X GET --insecure --cert client.crt --key client.key <AMS_SERVICE_URL>/1.0/images/my-image
```

Output:

```json
{
  "type": "sync",
  "status": "Success",
  "status_code": 200,
  "operation": "",
  "error_code": 0,
  "error": "",
  "metadata": {
    "id": "btbfutoj1qm45810otr0",
    "name": "my-image",
    "versions": [
      {
        "version": 0,
        "fingerprint": "0791cfc011f67c60b7bd0f852ddb686b79fa46083d9d43ef9845c9235c67b261",
        "size": 529887868,
        "created_at": 1610641117,
        "status_code": 3,
        "status": "active",
        "remote_id": ""
      }
    ],
    "status_code": 3,
    "status": "active",
    "used_by": null,
    "immutable": true,
    "default": false,
    "architecture": "x86_64"
  }
}
```

#### PATCH (ETag supported)
 * Description: Updates an existing image
 * Authentication: trusted
 * Operation: sync
 * Cancellable: no

An image can be updated with either a new package or specific fields.
The `Content-Type` header of HTTP patch request is different when uploading
an image in either way.

|Update methods|Content-Type|
| --- | --- |
|With a new package|`application/octet-stream`|
|With specified fields|`application/json`|

An image package can be uploaded with one of the supported compress format payload(gzip, bzip2 or xz) if the former approach is taken. And X-AMS-Request header is comprised of as follows in this case:

```json
{
    "name": "my-image",  // (string) Image name
    "default": false     // (boolean) Default image setting
}
```

Example:
```bash
curl -s --header "Content-Type: application/octet-stream"  --header 'X-AMS-Request: {"name": "my-image", "default": false}' -X PATCH --insecure --cert client.crt --key client.key --data-binary @my-image.tar.bz2 <AMS_SERVICE_URL>/1.0/images/my-image
```

Output:
```json
{
  "type": "async",
  "status": "Operation created",
  "status_code": 100,
  "operation": "1.0/operations/882795ad-6876-46b2-8f32-8226f4b22912",
  "error_code": 0,
  "error": "",
  "metadata": {
    "id": "882795ad-6876-46b2-8f32-8226f4b22912",
    "class": "task",
    "description": "Updating image",
    "created_at": "2018-07-28T08:23:14.253985803Z",
    "updated_at": "2018-07-28T08:23:14.253985803Z",
    "status": "Running",
    "status_code": 103,
    "resources": {
      "images": [
        "/1.0/images/my-image"
      ]
    },
    "metadata": null,
    "may_cancel": true,
    "err": "",
    "server_address": ""
  }
}
```
As a result, a new image version will be generated.

To update an image with a specified field, a JSON format payload is accepted.

```json
{
     "default": true     // (boolean) Default image setting
}
```
URL parameter | Description  |  Optional values
----------------|-------------------|-----------------
type |   comma separated list of notifications to subscribe to (defaults to all) | `operation`, `logging`, `lifecycle`
Example:
```bash
curl -s --header "Content-Type: application/json"  -X PATCH --insecure --cert client.crt --key client.key --data "$payload" <AMS_SERVICE_URL>/1.0/images/my-image
```

When updating an image with the above field, no new image version will be generated.

To monitor the status of an image update operation, please refer to [`/1.0/operations`](#heading--10operations)

#### DELETE
 * Description: Remove an existing image
 * Authentication: trusted
 * Operation: async
 * Cancellable: no

In the HTTP image removal case, a JSON format payload input is required from the client:

```Payload
{
    "force": false // (boolean) Forcibly remove the image
}
```

Example:
```bash
curl -s -X DELETE --insecure --cert client.crt --key client.key --data "$payload" <AMS_SERVICE_URL>/1.0/images/my-image
```

Output:
```json
`{
  "type": "async",
  "status": "Operation created",
  "status_code": 100,
  "operation": "1.0/operations/5485e9ea-bd57-48f1-af0d-761056c7d4e0",
  "error_code": 0,
  "error": "",
  "metadata": {
    "id": "5485e9ea-bd57-48f1-af0d-761056c7d4e0",
    "class": "task",
    "description": "Deleting image",
    "created_at": "2018-07-28T10:29:16.26129557Z",
    "updated_at": "2018-07-28T10:29:16.26129557Z",
    "status": "Running",
    "status_code": 103,
    "resources": {
      "images": [
        "/1.0/images/c098kfgj1qm5ivqf9ktg"
      ]
    },
    "metadata": null,
    "may_cancel": true,
    "err": "",
    "server_address": ""
  }
}
```
To monitor the status of an image removal operation, please refer to [`/1.0/operations`](#heading--10operations)

<a name="heading--10imagesidversion"></a>
### `/1.0/images/<id or name>/<version>`
#### DELETE
 * Description: Deletes a single version of an image
 * Authentication: trusted
 * Operation: async
 * Cancellable: no

Example:
```bash
curl -s -X DELETE --insecure --cert client.crt --key client.key <AMS_SERVICE_URL>/1.0/images/my-image/2
```

Output:
```json
{
  "type": "async",
  "status": "Operation created",
  "status_code": 100,
  "operation": "1.0/operations/412e428d-7468-454b-aef8-b29540d1960d",
  "error_code": 0,
  "error": "",
  "metadata": {
    "id": "412e428d-7468-454b-aef8-b29540d1960d",
    "class": "task",
    "description": "Deleting image version",
    "created_at": "2018-07-28T10:18:55.938675833Z",
    "updated_at": "2018-07-28T10:18:55.938675833Z",
    "status": "Running",
    "status_code": 103,
    "resources": {
      "images": [
        "/1.0/images/my-image"
      ]
    },
    "metadata": null,
    "may_cancel": true,
    "err": "",
    "server_address": ""
  }
}
```
To monitor the status of an image version removal operation, please refer to [`/1.0/operations`](#heading--10operations)

<a name="heading--10nodes"></a>
### `/1.0/nodes`
#### GET
 * Description: List available nodes
 * Authentication: trusted
 * Operation: sync
 * Cancellable: no

Example:
```bash
curl -s -X GET --insecure --cert client.crt --key client.key <AMS_SERVICE_URL>/1.0/nodes
```

Output:

```json
{
  "type": "sync",
  "status": "Success",
  "status_code": 200,
  "operation": "",
  "error_code": 0,
  "error": "",
  "metadata": [
    {
      "name": "lxd1",
      "address": "10.226.4.52",
      "public_address": "10.226.4.52",
      "network_bridge_mtu": 1500,
      "cpus": 2,
      "cpu_allocation_rate": 4,
      "memory": "3GB",
      "memory_allocation_rate": 2,
      "status_code": 4,
      "status": "online",
      "is_master": true,
      "disk_size": "21GB",
      "gpu_slots": 0,
      "gpu_encoder_slots": 0,
      "tags": [],
      "unschedulable": false,
      "architecture": "x86_64",
      "storage_pool": "ams0",
      "managed": true
    }
  ]
}
```

#### POST
 * Description: Add a LXD node to the cluster
 * Authentication: trusted
 * Operation: async
 * Cancellable: no

In the HTTP node registration case, a JSON format payload input is required from the client:

```json
{
    "name": "lxd2",                       // (string | mandatory) Name to the LXD node to be added to AMS
    "address": "172.31.23.150",           // (string | mandatory) LXD node address
    "public_address": "34.250.180.153",   // (string | optional) LXD node public address
    "trust_password": "foobar",           // (string | optional) Trust password for the remote LXD node
    "network_bridge_mtu": 1500,           // (number | optional) MTU of the network bridge configured for LXD
    "storage_device": "/dev/sda",         // (string | optional) Storage device LXD node should use
    "cpus": 32                            // (number | optional) (number | optional) Number of CPU cores used by LXD node
    "cpu_allocation_rate": 4,             // (number | optional) Factor of CPU overcommitment. Overcommitting resources allow to run more containers per node
    "memory": "256GB",                    // (string | optional) Memory used by LXD node
    "memory_allocation_rate": 2,          // (number | optional) Factor of memory overcommitment. Similar to cpu-allocation rate
    "gpu_slots": 10,                      // (number | optional) Slots on the GPU available to containers
    "gpu_encoder_slots": 10,              // (number | optional) Slots on the GPU encoders available to containers
    "tags": [],                           // (array | optional) User defined tags
    "unmanaged": false,                   // (boolean | optional) Expect node to be already clustered
    "storage_pool": "",                   // (string | optional) Existing LXD storage pool to use
    "network_name": "amsbr0",             // (string | optional) Name of the network device to create on the LXD cluster. Default to "amsbr0" if unet
    "network_subnet": "192.168.100.1/24"  // (string | optional) Network subnet for the network device on the node. Default to  "192.168.100.1/24" if unset
}
```

Example:
```bash
curl -s -X POST --insecure --cert client.crt --key client.key --data "$payload" <AMS_SERVICE_URL>/1.0/nodes
```

Output:
```json
{
  "type": "async",
  "status": "Operation created",
  "status_code": 100,
  "operation": "1.0/operations/2215b63c-9f2b-4665-bf34-6fe8dbcbe4b5",
  "error_code": 0,
  "error": "",
  "metadata": {
    "id": "2215b63c-9f2b-4665-bf34-6fe8dbcbe4b5",
    "class": "task",
    "description": "Creating node",
    "created_at": "2018-07-28T11:51:13.261045632Z",
    "updated_at": "2018-07-28T11:51:13.261045632Z",
    "status": "Running",
    "status_code": 103,
    "resources": {
      "nodes": [
        "/1.0/nodes/lxd2"
      ]
    },
    "metadata": null,
    "may_cancel": true,
    "err": "",
    "server_address": ""
  }
}
```
To monitor the status of an LXD node registration operation, please refer to [`/1.0/operations`](#heading--10operations)

<a name="heading--10nodesname"></a>
### `/1.0/nodes/<name>`
#### GET
 * Description: Load node information
 * Authentication: trusted
 * Operation: sync
 * Cancellable: no

Example:
```bash
curl -s -X GET --insecure --cert client.crt --key client.key <AMS_SERVICE_URL>/1.0/nodes/lxd1
```
Output:

```json
{
  "type": "sync",
  "status": "Success",
  "status_code": 200,
  "operation": "",
  "error_code": 0,
  "error": "",
  "metadata": {
    "name": "lxd1",
    "address": "10.226.4.52",
    "public_address": "10.226.4.52",
    "network_bridge_mtu": 1500,
    "cpus": 2,
    "cpu_allocation_rate": 4,
    "memory": "3GB",
    "memory_allocation_rate": 2,
    "status_code": 4,
    "status": "online",
    "is_master": false,
    "disk_size": "21GB",
    "gpu_slots": 0,
    "gpu_encoder_slots": 0,
    "tags": [],
    "unschedulable": false,
    "architecture": "x86_64",
    "storage_pool": "ams0",
    "managed": true
  }
}
```

#### PATCH (ETag supported)
 * Description: Update node configuration
 * Authentication: trusted
 * Operation: sync
 * Cancellable: no

In the HTTP node update case, a JSON format payload input is required from the client:

Supported update field            |   Description
-----------------|------------------------------------
`public_address` |  (string) LXD node public address
`cpus`        |  (number) Number of CPU cores used by LXD node
`cpu_allocation_rate` |  (number) Factor of CPU overcommitment. Overcommitting resources allow to run more containers per node
`memory` | (string) Memory used by LXD node
`memory_allocation_rate` | Factor of memory overcommitment.
`gpu_slots` | (number) Slots on the GPU available to containers
`gpu_encoder_slots` | (number) Slots on the GPU encoders available to containers
`tags` | (string) User defined tags
`unschedulable` | (Boolean) Whether this LXD node is schedulable by AMS.

A sample payload as follows:

```json
{
  "cpu_allocation_rate": 4,
  "memory_allocation_rate": 2
}
```

Example:
```bash
curl -s -X PATCH --insecure --cert client.crt --key client.key --data "$payload"<AMS_SERVICE_URL>/1.0/nodes/lxd0
``

Output:

```json
{
  "type": "async",
  "status": "Operation created",
  "status_code": 100,
  "operation": "1.0/operations/a6124977-72c2-4daa-b349-8e31e12dfd37",
  "error_code": 0,
  "error": "",
  "metadata": {
    "id": "a6124977-72c2-4daa-b349-8e31e12dfd37",
    "class": "task",
    "description": "Updating node lxd1",
    "created_at": "2018-07-28T13:04:04.701576609Z",
    "updated_at": "2018-07-28T13:04:04.701576609Z",
    "status": "Running",
    "status_code": 103,
    "resources": {
      "nodes": [
        "/1.0/nodes/lxd1"
      ]
    },
    "metadata": null,
    "may_cancel": true,
    "err": "",
    "server_address": ""
  }
}
```
To monitor the status of an LXD node update operation, please refer to [`/1.0/operations`](#heading--10operations)

#### DELETE
 * Description: Remove the node from the cluster
 * Authentication: trusted
 * Operation: async
 * Cancellable: no

In the HTTP node removal case, a JSON format payload input is required from the client:

```json
{
    "force": false,          // (boolean) Forcibly remove the node
    "keep_in_cluster": false // (boolean) Whether to remove the node from LXD cluster as well
}
```

Example:
```bash
curl -s -X DELETE --insecure --cert client.crt --key client.key --data "$payload"<AMS_SERVICE_URL>/1.0/nodes/lxd0
```

Output:
```json
{
  "type": "async",
  "status": "Operation created",
  "status_code": 100,
  "operation": "1.0/operations/cc43bc37-330a-4696-b3f4-b7639b05ae8a",
  "error_code": 0,
  "error": "",
  "metadata": {
    "id": "cc43bc37-330a-4696-b3f4-b7639b05ae8a",
    "class": "task",
    "description": "Deleting node",
    "created_at": "2018-07-28T10:56:18.912988425Z",
    "updated_at": "2018-07-28T10:56:18.912988425Z",
    "status": "Running",
    "status_code": 103,
    "resources": {
      "nodes": [
        "/1.0/nodes/lxd0"
      ]
    },
    "metadata": null,
    "may_cancel": true,
    "err": "",
    "server_address": ""
  }
}
```
To monitor the status of a LXD node removal operation, please refer to [`/1.0/operations`](#heading--10operations)

<a name="heading--10operations"></a>
### `/1.0/operations`
#### GET
 * Description: list of operations
 * Authentication: trusted
 * Operation: sync
 * Return: list of URLs for operations that are currently going on/queued

Example:
```bash
curl -s -X GET --insecure --cert client.crt --key client.key <AMS_SERVICE_URL>/1.0/operations
```

Output:
```json
{
  "type": "sync",
  "status": "Success",
  "status_code": 200,
  "operation": "",
  "error_code": 0,
  "error": "",
  "metadata": {
    "success": [
      "1.0/operations/5d2a6807-7c8a-48eb-94c7-e07dd75119ce"
    ]
  }
}
```

<a name="heading--10operationsuuid"></a>
### `/1.0/operations/<uuid>`
#### GET
 * Description: Load operation information. If the service is deployed as
a cluster of several instances, the operation is held in one of them. In
case the request reaches a different instance of the one holding the
operation, the information is taken internally from the right one.
 * Authentication: trusted
 * Operation: sync
 * Cancellable: no

For example, when changing the publication status of an application by issuing
```bash
payload='{"published": false}'
operation=$(curl -s -X PATCH --insecure --cert client.crt --key client.key --data "$payload"  <AMS_SERVICE_URL>/1.0/applications/my-app/0 | jq -r .operation)
```

To monitor the operation status
```bash
curl -s -X GET --insecure --cert client.crt --key client.key <AMS_SERVICE_URL>/$operation | jq .

{
  "type": "sync",
  "status": "Success",
  "status_code": 200,
  "operation": "",
  "error_code": 0,
  "error": "",
  "metadata": {
    "id": "0db09aee-3de9-4250-b707-0a3a90fd39c6",
    "class": "task",
    "description": "Updating application version",
    "created_at": "2018-07-28T13:25:35.186064229Z",
    "updated_at": "2018-07-28T13:25:35.186064229Z",
    "status": "Success",
    "status_code": 200,
    "resources": {
      "applications": [
        "/1.0/applications/my-app"
      ]
    },
    "metadata": null,
    "may_cancel": false,
    "err": "",
    "server_address": ""
  }
}
```

#### DELETE
 * Description: Cancel an operation. Calling this will change the state of cancellable API to "cancelling" rather than actually removing the entry. If the service is deployed as a cluster of several instances, the operation is held in one of them. In case the request reaches a different instance of the one holding the
operation, the information is taken internally from the right one.
 * Authentication: trusted
 * Operation: sync
 * Cancellable: no

For example, to cancel an operation of an application creation
```bash
operation=$(curl -s --header "Content-Type: application/octet-stream" -X POST
--insecure --cert client.crt --key client.key  --data-binary @my-app.tar.bz2
        <AMS_SERVICE_URL>/1.0/applications | jq -r .operation)

curl -s -X DELETE --insecure --cert client.crt --key client.key <AMS_SERVICE_URL>/$operation| jq .
```

Output:
```json
{
  "type": "sync",
  "status": "Success",
  "status_code": 200,
  "operation": "",
  "error_code": 0,
  "error": "",
  "metadata": {}
}
```

HTTP code for this should be 202 (Accepted).

<a name="heading--10operationsuuidwait"></a>
### `/1.0/operations/<uuid>/wait`
#### GET
 * Description: Wait until an operation reaches a final status
 * Authentication: trusted
 * Operation: sync
 * Cancellable: yes

URL parameter | Description
----------------|-------------------
timeout |   The amount of time (In second) when wait operation reaches timed out.  If the value is assigned to `-1`, it means the operation will wait infinitely until the monitored operation reaches a final status.

For example, to wait for the process of an application creation to be done
```bash
operation=$(curl -s --header "Content-Type: application/octet-stream" -X POST
--insecure --cert client.crt --key client.key  --data-binary @my-app.tar.bz2
        <AMS_SERVICE_URL>/1.0/applications | jq -r .operation)

curl -s -X GET \
        --insecure --cert ~/trust-client/client.crt --key ~/trust-client/client.key \
        <AMS_SERVICE_URL>/$operation/wait | jq .
```

Output:
```json
{
  "type": "sync",
  "status": "Success",
  "status_code": 200,
  "operation": "",
  "error_code": 0,
  "error": "",
  "metadata": {
    "id": "fbe40515-7948-41c8-8668-e815db8916f8",
    "class": "task",
    "description": "Creating application",
    "created_at": "2018-07-28T13:39:49.736209814Z",
    "updated_at": "2018-07-28T13:39:49.736209814Z",
    "status": "Success",
    "status_code": 200,
    "resources": {
      "applications": [
        "/1.0/applications/c09bt98j1qm1as2tvn00"
      ]
    },
    "metadata": null,
    "may_cancel": false,
    "err": "",
    "server_address": ""
  }
}
```

<a name="heading--10operationsuuidwebsocket"></a>
### `/1.0/operations/<uuid>/websocket`
#### GET (`?secret=SECRET`)
 * Description: This connection is upgraded into a web socket connection
   speaking the protocol defined by the operation type. For example, in the
   case of an exec operation, the web socket is the bidirectional pipe for
   stdin/stdout/stderr to flow to and from the process inside the container.
   In the case of migration, it will be the primary interface over which the
   migration information is communicated. The secret here is the one that was
   provided when the operation was created. Guests are allowed to connect
   provided they have the right secret.
 * Authentication: guest or trusted
 * Operation: sync
 * Cancellable: no

<a name="heading--10tasks"></a>
### `/1.0/tasks`
#### GET
 * Description: List of available tasks
 * Authentication: trusted
 * Operation: sync
 * Cancellable: no

Example:
```bash
curl -s -X GET --insecure --cert client.crt --key client.key <AMS_SERVICE_URL>/1.0/tasks
```

 Output:

```json
{
  "type": "sync",
  "status": "Success",
  "status_code": 200,
  "operation": "",
  "error_code": 0,
  "error": "",
  "metadata": [
    {
      "id": "c055dl0j1qm027422feg",
      "status": "running",
      "object_id": "c055dl0j1qm027422fe0",
      "object_type": "container"
    }
  ]
}
```

<a name="heading--10version"></a>
### `/1.0/version`
#### GET
 * Description: Load status information about the service
 * Authentication: guest
 * Operation: Sync
 * Cancellable: no

Example:
```bash
curl -s -X GET --insecure --cert client.crt --key client.key <AMS_SERVICE_URL>/1.0/version
```

Output:

```json
{
  "type": "sync",
  "status": "Success",
  "status_code": 200,
  "operation": "",
  "error_code": 0,
  "error": "",
  "metadata": {
    "version": "1.7.3"
  }
}
```

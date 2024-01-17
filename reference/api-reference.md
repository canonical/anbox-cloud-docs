All communication between AMS and its clients happen using a RESTful API over HTTP. This API is encapsulated over either TLS (for remote operations) or a Unix socket (for local operations).

## APIs and their structure
Anbox Cloud provides the following APIs:

* AMS HTTP API
* Anbox Cloud HTTP API
* Stream Gateway API
* Anbox Platform SDK API

All these APIs except for the [Anbox Cloud HTTP API](https://discourse.ubuntu.com/t/anbox-http-api/17819) have an auto-generated specification describing its API endpoints.

## Authentication

Not all REST API endpoints require authentication, for example, the following API calls are allowed for everyone:

* `GET /`
* `GET /1.0`
* `GET /1.0/version`

Some endpoints require an additional authentication token to ensure that the requester is authorised to access the resource, for example:

* `GET /1.0/artifacts`
* `PATCH /1.0/instances/<name>`

## API versioning
The details of a version of the API can be retrieved using `GET /<version>`. For example, `GET /1.0`.

If an API version is bumped to a major version, it indicates that backward compatibility is affected.

Feature additions done without breaking backward compatibility only result in additions to `api_extensions` which can be used by the client to check if a given feature is supported by the server.

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
    "metadata": {}
}
```

HTTP response status code is 200.

### Background operation
When a request results in a background operation, the HTTP code is set to 202 (Accepted) and the Location HTTP header is set to the operation URL.

The response body is a dict with the following structure:

```json
{
    "type": "async",
    "status": "OK",
    "status_code": 100,
    "operation": "/1.0/containers/<id>",
    "metadata": {}
}
```

The operation metadata structure looks like:

```json
{
    "id": "c6832c58-0867-467e-b245-2962d6527876",
    "class": "task",
    "created_at": "2018-04-02T16:49:36.341463206+02:00",
    "updated_at": "2018-04-02T16:49:36.341463206+02:00",
    "status": "Running",    
    "status_code": 103,                        
    "resources": {                                  
      "containers": [
        "/1.0/containers/3apqo5te"
      ]
    },
    "metadata": null,                          
    "may_cancel": false,                       
    "err": ""                                    
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
    "metadata": {}           
}
```

HTTP response status code is one of 400, 401, 403, 404, 409, 412 or 500.

## Status codes
The REST API often has to return status information, which could be the reason for an error, the current state of an operation or the state of the various resources it exports.

To make it simple to debug, there are two ways in which such information is represented - a numeric representation of the state which is guaranteed never to change and can be relied on by API clients and a text version so that it is easier for people manually using the API to understand better. In most cases, those will be called `status` and `status_code`, the former being the user friendly string representation and the latter being the fixed numeric value.

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
Any operation which take more than a second must be done in the background, returning a background operation ID to the client. With this ID, the client is able to either poll for a status update or wait for a notification using the long-poll API.

## Notifications
A web-socket based API is available for notifications. Different notification types exist to limit the traffic going to the client. It is recommended that the client always subscribes to the *operations* notification type before triggering remote operations so that it doesn't have to continually poll for their status.

## PUT vs PATCH
PUT and PATCH APIs are supported to modify existing objects.

PUT replaces the entire object with a new definition, it's typically called after the current object state was retrieved through GET.

To avoid race conditions, the ETag header should be read from the GET response and sent as If-Match for the PUT request. Doing so makes the request fail if the object was modified between GET and PUT.

PATCH can be used to modify a single field inside an object by only specifying the property that you want to change. To unset a key, setting it to empty will usually do the trick, but there are cases where PATCH won't work and PUT needs to be used instead.

## Authorisation
Some operation may require a token to be included in the HTTP Authorisation header even if the request is already authenticated using a trusted certificate. If the token is not valid, the request is rejected by the server. This ensures that only authorised clients can access those endpoints.

    Authorization: bearer <token>

## File upload
Some operations require uploading a payload. To prevent the difficulties of handling multipart requests, a unique file is uploaded and its bytes are included in the body of the request. The following metadata associated with the file is included in extra HTTP headers:

 * X-AMS-Fingerprint: Fingerprint of the payload being added
 * X-AMS-Request: Metadata for the payload. This is a JSON, specific for the operation.

## Instances and Containers
The documentation shows paths such as `/1.0/instances/...`, which were introduced with Anbox Cloud version 1.20.0. Older releases that supported only containers and not virtual machines supply the exact same API at `/1.0/containers/...`.

Although deprecated, the `1.0/containers/...` API is still available for backward compatibility.

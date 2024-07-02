(howto-access-stream-gateway)=
# How to access the stream gateway

Similar to the Anbox Management Service (AMS), the stream gateway exposes its API over an HTTP interface. Clients can be anything from the Anbox Cloud web dashboard to any custom client that you develop.

## Access the stream gateway

### Prerequisites

To access the stream gateway,
* The gateway's HTTP API must be exposed. This is the default configuration.
* All calls to the stream gateway must be authenticated. Authentication takes the form of a single token per client that you must embed in your requests. A token is associated to a *service account*, has a limited lifetime, and can be revoked at any time.

### Creating a token

An internal HTTP API is exposed for managing client tokens. This API is only accessible via a Unix domain socket which resides at `/var/snap/anbox-stream-gateway/common/service/unix.socket` by default.
For convenience, the stream gateway has a built-in client designed to communicate to that API.

If you are running a full Anbox Cloud deployment, use the following command to create a token:

    anbox-stream-gateway account create my-client

If you are running the Anbox Cloud Appliance, use the following command:

    anbox-cloud-appliance gateway account create my-client

### Using the token

When making requests to the stream gateway API, you can either place the token in the request HTTP headers or in the query parameters.

**Request headers**

```bash
curl -X GET https://20.234.75.29:4000/1.0/sessions \
    -H 'authorization:macaroon root=AgEUYW5ib3...QSyzaA_GHLYQ'
```

**Query parameters**

```bash
curl -X GET https://20.234.75.29:4000/1.0/sessions?api_token=AgEUYW5ib3...QSyzaA_GHLYQ
```

```{note}
- The Anbox Stream SDK handles the token automatically for all its requests.
- The token does not get renewed automatically. If it expires, create a new token.
```

### Deleting a token

If you are running a full Anbox Cloud deployment, use the following command to delete a token:

    anbox-stream-gateway account delete my-client

If you are running the Anbox Cloud Appliance, use the following command:

    anbox-cloud-appliance gateway account delete my-client

Type `anbox-stream-gateway --help` to list all commands.

## Related topics

* {ref}`exp-application-streaming`
* {ref}`exp-ams`
* {ref}`tut-set-up-stream-client`
* {ref}`sec-streaming-sdk`

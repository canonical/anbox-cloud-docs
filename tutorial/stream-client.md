(tut-set-up-stream-client)=

# Set up a stream client

This tutorial guides you through the process of setting up a web-based streaming client using the Anbox Cloud streaming stack. The connection between the stream client and the server uses WebRTC backed by WebSockets that enable the real time communications required for streaming. To know more about the WebRTC configuration, see {ref}`ref-webrtc`.

For security reasons, there are limits on what APIs are exposed through the reverse proxy configured by the appliance. The API provided by the Anbox Stream Gateway is typically meant to be used in service-to-service communication and not on public endpoints. If you want to use the API from a client application, you should use a proxy service that communicates with the Anbox Stream Gateway and also provides the user with an authentication method specific to your service. We will see how to set this up in this tutorial.

## Preparation

Complete the following preparatory steps:

### Install the Anbox Cloud Appliance

We need the Anbox Cloud streaming stack to be deployed already to set up a streaming client. So let's get the streaming stack ready by installing the Anbox Cloud Appliance. Follow the instructions in the {ref}`tut-installing-appliance` until initializing the appliance. When you have installed and initialized the appliance, let's proceed to the next step.

(sec-create-access-token)=
### Create an access token

To access the HTTP API of the Anbox Cloud stream gateway, an access token is required. Each access token is associated with a service account.

On the machine where Anbox Cloud Appliance is installed, create the service account by running the following command:

    sudo anbox-cloud-appliance.gateway account create streaming-tutorial

The output of this command provides the access token. Make a note of this token to use when you make a request to the stream gateway API.

See {ref}`howto-access-stream-gateway` for more information on creating, using and deleting the access token.

### Create an Android Instance

Create a streaming enabled Android instance:

    arch="$(dpkg-architecture -q DEB_HOST_ARCH)"
    amc launch --enable-streaming --raw --name a13 jammy:android13:"$arch"

### Determine session ID of the Android instance

For the next step, we need the session ID which AMS assigned to the instance. So let's get that using the following command:

    amc ls --filter name=a13 --format=csv | cut -d, -f6 | awk -F"session=" '{ print $2 }'

## Implement the stream client

Now that we have everything ready, let's create a directory to set up the stream client:

    mkdir -p stream-client/{templates,static}

We will be using [Flask](https://flask.palletsprojects.com/en/stable/) for the purpose of this tutorial. First, let us create a `requirements.txt` file inside `stream-client` with the following code:

```
flask==3.0.3
requests==2.32.3
pyopenssl==24.2.1
```

Create a `service.py` file inside `stream-client` with the following code:

```python
import os
import os.path
import secrets

from flask import Flask, jsonify, render_template, request
from requests import Session
from functools import wraps
from typing import *


class GatewayAPI:
    def __init__(self, base_url, session, token, verify):
        self.base_url = base_url
        self.session = session
        self.token = token
        self.verify = verify

    def make_request(
        self,
        method,
        path,
        headers,
        data,
    ):
        uri = f"{self.base_url}{path}"

        headers["Authorization"] = f"macaroon root={self.token}"
        headers["Content-Type"] = "application/json"

        return self.session.request(
            method, uri, json=data, headers=headers, verify=self.verify
        )

    def join_session(self, session_id, data):
        uri = f"/1.0/sessions/{session_id}/join"
        return self.make_request(
            "POST",
            uri,
            data=data,
            headers={"Content-Type": "application/json"},
        ).json()

app = Flask(__name__)

gateway_api_url = os.getenv("GATEWAY_URL")
gateway_api_token = os.getenv("GATEWAY_API_TOKEN")
gateway_server_cert = os.getenv("GATEWAY_SERVER_CERT") or False
gateway_enabled = bool(gateway_api_url and gateway_api_token)

auth_user = os.getenv("AUTH_USER") or "anbox"
auth_password = os.getenv("AUTH_PASSWORD") or secrets.token_urlsafe(16)

print(f"You can login with username {auth_user} and password {auth_password}")

gateway = GatewayAPI(gateway_api_url, Session(), gateway_api_token, gateway_server_cert)


def render_error_response(msg, code):
    response = {"error_msg": msg}
    return jsonify(response), code


def check_auth(username, password):
    return username == auth_user and password == auth_password


def login_required(f):
    @wraps(f)
    def wrapped_view(**kwargs):
        auth = request.authorization
        if not (auth and check_auth(auth.username, auth.password)):
            return (
                "Unauthorized",
                401,
                {"WWW-Authenticate": 'Basic realm="Login Required"'},
            )
        return f(**kwargs)

    return wrapped_view


@app.route("/1.0/sessions/<session_id>/join", methods=["POST"])
@login_required
def api_1_0_sessions_join_post(session_id):
    if not gateway_enabled:
        return render_error_response("no gateway connected", 503)

    request_data = {"disconnect_clients": True}
    response = gateway.join_session(session_id, request_data)

    if "status_code" not in response or response["status_code"] != 200:
        return render_error_response("failed to join session", 500)

    return jsonify(response), 200


@app.route("/<session_id>")
@login_required
def stream_session(session_id=None):
    return render_template("stream.html", session_id=session_id)


@app.route("/")
@login_required
def index():
    return "Welcome to the Anbox Cloud Stream SDK tutorial!"
```

Create a `stream.html` file inside `stream-client/templates` with the following code:

```html
<!doctype html>
<html>
  <head>
    <title>Anbox Streaming SDK - Tutorial</title>
    <script type="module" src="static/anbox-stream-sdk.js"></script>
    <style>
      html,
      body,
      #anbox-stream {
        height: 100%;
        margin: 0;
        width: 100%;
      }
    </style>
  </head>

  <body>
    <div id="anbox-stream"></div>
    <script>
      const sessionId = "{{ session_id }}";
      class Connector {
        async connect() {
          var url = `${window.location.origin}/1.0/sessions/${sessionId}/join`;
          const rawResponse = await fetch(url, { method: "POST" });
          if (rawResponse === undefined || rawResponse.status !== 200)
            throw new Error("failed to join session");

          const jsonResponse = await rawResponse.json();
          if (jsonResponse === undefined || jsonResponse.status !== "success")
            throw new Error(jsonResponse.error ?? "Failed to parse the response object");

          return {
            id: jsonResponse.metadata.id,
            websocket: jsonResponse.metadata.url,
            stunServers: jsonResponse.metadata.stun_servers,
          };
        }

        disconnect() {}
      }
      window.onload = () => {
        const connector = new Connector();
        const stream = new AnboxStream({
          connector: connector,
          targetElement: "anbox-stream",
          enableStats: false,
          stream: {
            audio: true,
            video: true,
          },
        });
        stream.connect();
      };
    </script>
  </body>
</html>
```

Next, let's make a copy of the Anbox Stream Gateway server to allow the service to validate it:

    # We use cat here to ensure gateway.crt has the users permissions
    sudo cat /var/snap/anbox-cloud-appliance/common/gateway/server.crt > gateway.crt

As a final step, download a copy of the Anbox streaming SDK and place it inside `stream-client/static`

    curl -o stream-client/static/anbox-stream-sdk.js \
        https://raw.githubusercontent.com/canonical/anbox-streaming-sdk/refs/heads/main/js/anbox-stream-sdk.js

## Run the stream client

To run the stream client, let's set up a virtual environment for Python to install necessary dependencies.

Assuming that you are working on a fresh installation of Ubuntu, let's start by installing the `venv` module:

    cd stream-client
    sudo apt install -y python3.12-venv

Next, let's create and activate the virtual environment and use `pip` to install all the required dependencies:

    python3 -m venv .venv
    . .venv/bin/activate
    pip3 install -r requirements.txt

To run the stream client service application, we need to set the necessary environment variables and execute the service via flask.

When installing and initializing the appliance, we would have configured the private IP address of the machine running the appliance. The gateway API is accessible on the local listen address of the appliance on port `9031/tcp`. So that's the IP address and port we use in the GATEWAY_URL.

For the `GATEWAY_API_TOKEN`, use the access token you noted earlier in {ref}`sec-create-access-token`.

    addr="$(sudo anbox-cloud-appliance config show | yq -r .network.listen_address)"
    export GATEWAY_URL=https://"$addr":9031
    export GATEWAY_API_TOKEN=<access-token>
    export GATEWAY_SERVER_CERT="$PWD"/gateway.crt
    FLASK_APP=service.py python3 -m flask run --cert=adhoc -h "$addr" -p 8080

This will start the service and make it accessible at `https://<appliance_private_ip>:8080` and print out a username and password needed to access the site.

```{note}
This example uses a Flask server with a spontaneous certificate. Note that this implementation is used only for demonstration purposes in this tutorial and is not recommended for production deployments. For better ways to deploy to production, see the [Flask documentation](https://flask.palletsprojects.com/en/stable/deploying/).
```

To view the stream of the instance we created earlier, you can access `https://<appliance_private_ip>:8080/<session_id>` in your browser. Remember to use the session ID of the Android instance we retrieved earlier in place of `<session_id>` and for credentials, use `anbox` as username and the password that the example printed.

Remember that to access the stream URL, you will be required to accept both the spontaneous certificate for the server and also the certificate from `https://<appliance_private_ip>`.

You have now successfully set up a web client that you can use for streaming your applications.

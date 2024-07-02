(tut-set-up-stream-client)=
# Set up a stream client

This tutorial guides you through the process of setting up a web-based streaming client using the Anbox Cloud streaming stack. The connection between the stream client and the server uses WebRTC backed by web sockets which enable the real time communications required for streaming. To know more about the WebRTC configuration, see {ref}`ref-webrtc`.

## Preparation

Complete the following preparatory steps:

### Install the Anbox Cloud Appliance

We need the Anbox Cloud streaming stack to be deployed already to set up a streaming client. So let's get the streaming stack ready by installing the Anbox Cloud Appliance. Follow the instructions in the {ref}`tut-installing-appliance` tutorial until you finish initialising the Appliance.

### Create an access token

To access the HTTP API of the Anbox Cloud stream gateway, an access token is required. Each access token is associated with a service account.

On the machine where Anbox Cloud Appliance is installed, create the service account by running the following command:

    anbox-cloud-appliance gateway account create test

The output of this command provides the access token. Make a note of this token to use when you make a request to the stream gateway API.

See {ref}`howto-access-stream-gateway` for more information on creating, using and deleting the access token.

### Download the Anbox Cloud streaming SDK

Download the {ref}`sec-streaming-sdk` from GitHub:

    git clone https://github.com/canonical/anbox-streaming-sdk.git

### Create an application

Follow the instructions in {ref}`howto-create-application` and create an application. You can create any application, the application type does not matter.

## Set up the stream client

Create a directory to set up the stream client:

    sudo mkdir -p /srv/stream-client

Create a `demo.html` file inside `/srv/stream-client`:

```{important}
The inline comments in the following code provide pointers to replace certain values with your corresponding values. For example, you will be required to replace the values of `url`, `authToken`, `app` in the following example with your values.
```

```html
<!DOCTYPE html>
<html>
<head>
    <meta content="text/html;charset=utf-8" http-equiv="Content-Type">
    <meta content="utf-8" http-equiv="encoding">
    <title>Anbox Streaming SDK Example</title>
</head>
<body>
    <script type="module">
        // Replace <path_to_stream_sdk> with the filepath of the SDK downloaded earlier
    import {AnboxStream, AnboxStreamGatewayConnector} from '<path_to_stream_sdk>/js/anbox-stream-sdk.js';

    const connector = new AnboxStreamGatewayConnector({
        // Replace 'https://gateway.url.net' with the host IP address or domain name
        url: 'https://gateway.url.net',
        // Use the access token created earlier as 'YOUR_AUTH_TOKEN'
        authToken: 'YOUR_AUTH_TOKEN',
        session: {
            // Run `amc list` to see a list of all applications
            // Replace `com.foo.bar` with your application name
            app: "com.foo.bar",
        },
        // Adjust the display resolution and frame rate for the
        // Android container as per your requirements
        screen: {
            width: 1280,
            height: 720,
            fps: 25,
        }
    });
    // The AnboxStream class takes care of the WebRTC signaling process
    // as well as the web browser integration
    let stream = new AnboxStream({
        connector: connector,
        // targetElement is the ID of the HTML element where the SDK can attach the video
        targetElement: "anbox-stream",
        controls: {
            keyboard: true
        },
        // Register callbacks to be notified at specific points in the stream life cycle.
        callbacks: {
            error: error => {
                console.log("AnboxStream failed: ", error);
            }
        }
    });
    stream.connect();
    </script>
    <!--To display the video element correctly,
        always specify both the height and the width attributes-->
    <div id="anbox-stream" style="width: 100vw; height: 100vh;"></div>
</body>
```
If you experience any streaming issues, you can turn on debug information by adding the following option to the `AnboxStream`:

    experimental: {
       debug: true,
    }

See {ref}`howto-ts-streaming-issues` for common issues related to streaming.

## Create and enable the stream UI service

Create `stream-ui.service` with the following content:
```service
[Unit]
Description=Simple Anbox Cloud Stream Client

[Service]
WorkingDirectory=/srv/stream-client
ExecStart=/usr/bin/python3 -m http.server -b 127.0.0.1 8080

[Install]
WantedBy=multi-user.target
```

Run the following commands to install and start the service:
```bash
# Install the service file
sudo cp stream-ui.service /etc/systemd/system/
# Reload systemd
sudo systemctl daemon-reload
# Enable and start the service
sudo systemctl enable --now stream-ui.service
```
## Generate the HTTP basic authentication credentials

Use the `htpasswd` tool to generate a user/password combination:
```
apt install -y apache2-utils
htpasswd -n <your user name>
```

Enter your desired password when prompted.

## Add a middleware definition

The appliance uses Traefik as the reverse proxy for routing incoming requests and you need to add a middleware definition for the stream client to the Traefik configuration.

Create `stream-ui.yaml` under `/var/snap/anbox-cloud-appliance/common/traefik/conf/` with the following content for Traefik to redirect requests to the service. 

```yaml
http:
  routers:
    to-stream-ui-demo:
      entryPoints: ["websecure"]
      rule: "PathPrefix(`/demo/`)"
      service: stream-ui-demo
      priority: 110
      tls: {}
      middlewares: ["ratelimiter", "strip-demo-prefix", "demo-auth"]
  middlewares:
    strip-demo-prefix:
      stripPrefix:
        prefixes:
          - "/demo"
        forceSlash: false
    demo-auth:
      basicAuth:
        users:
        # Replace 'demo' with the user name and
        # 'foobar' with the password generated for HTTP basic 
        # authentication earlier with the 'htpasswd' tool
        - "demo:foobar"
  services:
    stream-ui-demo:
      loadBalancer:
        servers:
          - url: http://127.0.0.1:8080
```

Set the right permissions for the `stream-ui.yaml`:

    chmod 0600 /var/snap/anbox-cloud-appliance/common/traefik/conf/stream-ui.yaml

With HTTP basic authentication configured, users will be asked to enter the credentials to access the site. Restart Traefik for the configuration changes to take effect:

    sudo snap restart anbox-cloud-appliance.traefik

Now you can go to `https://<ip>/demo/`, enter the HTTP basic authentication credentials and view the web-based streaming client.

## Related topics

* [WebRTC](https://webrtc.org/)
* [Traefik](https://traefik.io/)
* [Adding Basic Authentication for Traefik](https://doc.traefik.io/traefik/v2.0/middlewares/basicauth/)

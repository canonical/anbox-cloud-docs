(howto-ts-streaming-issues)=
# Troubleshoot streaming issues

Debugging issues that occur when streaming your application can be tricky. The following instructions give you some pointers on how to start tracking down streaming issues.

First of all, check the error message that occurs. Unfortunately, it is often hard to determine why a connection fails, which is why the error message does not always give a clear indication of the source of the error. Typical errors are covered though, so in these cases, the error message should give you an idea on where to look.

If the error message does not help, check the WebRTC debug information. You can find this information in your browser:

- In Google Chrome, go to `chrome://webrtc-internals/`.
- In Mozilla Firefox, go to `about:webrtc`.

You can create a dump of the debug information by expanding the **Create Dump** section (in Chrome) or clicking **Save Page** (in Firefox).

Analyse the dump to find the source of the error, or provide it to Anbox Cloud's support team for help.

## Streaming does not start

If streaming does not start, there is usually a connection problem.

If you are using the web dashboard and, for example, creating an application works as expected, the connection problem is not that the web dashboard cannot reach Anbox Cloud. Most likely, there are some security rules in place that prevent WebRTC from establishing a connection. In this case, check your firewall configuration and VPN setup.

In the WebRTC logs, check whether the connection was established.

![Screen capture (Chrome) showing that the connection was established](https://assets.ubuntu.com/v1/f80697ef-stream_webrtc-connected.png)
*(Screen capture taken in Chrome)*
<br/>

If the connection could not be established, check the table of ICE candidates. The ICE state of the different candidates should help you identify where the problem lies.

![Screen capture (Firefox) showing ICE stats and candidates](https://assets.ubuntu.com/v1/4bc262ee-stream_webrtc-candidates.png)
*(Screen capture taken in Firefox)*

If you are still not able to get the streaming to start, check if it is a problem with the public IP address configuration. Run the following command:

    sudo anbox-cloud-appliance internal generate-cloud-info

In the output, verify if the public address and location of the cloud is displayed correctly. Verify if the public address is reachable.

The public location is typically a DNS name for the public address of the instance. If there is no DNS name, the public location must match the public address.

If you want to override the public address or location, try running the following commands:

```
sudo snap set anbox-cloud-appliance experimental.public-address=x.x.x.x experimental.location=foo.bar
sudo snap restart anbox-cloud-appliance.reboot-checker
```

Note that these values will be configured but running the `sudo anbox-cloud-appliance internal generate-cloud-info` command again will not reflect these changes. To check if the correct public address is now applied, run:

    amc node ls

Try launching a new session now.

## Streaming works badly and stalls

If streaming starts, but keeps stalling and the quality is bad, the reason is usually a bad network connection. The connection can be established, but something is going wrong when transferring packets.

In this case, check the WebRTC log to see if there is a high packet loss, and if so, in what situations it occurs. Most likely it is due to a bad network connection between the web dashboard (or your client application) and Anbox Cloud.

See {ref}`sec-client-devices` for more information.

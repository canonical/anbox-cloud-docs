---
html_meta:
  description: Security notices. This page contains information about security vulnerabilities
    found and fixed in Anbox Cloud. For information about our security policy, see.
---
(ref-security-notices)=
# Security notices

This page contains information about security vulnerabilities found and fixed in Anbox Cloud.

For information about our security policy, see {ref}`ref-security-policy`.

(sec-CVE-2024-8287)=
## CVE-2024-8287

### Impacted versions

This vulnerability affects Anbox Cloud versions 1.17.0 through 1.23.0. It was fixed as part of the 1.23.1 release.

### Details

The Anbox Stream Agent provides configuration to the Anbox instance which includes an API endpoint and information on how to connect to the provided API endpoint. This information also includes a fingerprint of the TLS certificate that the agent uses for its API endpoint to allow Anbox to verify and establish trust. The stream agent has a mutual TLS authenticated connection for API access with the Anbox Management Service (AMS) and thereby, it provides the configuration through the AMS API.

When the stream agent triggers the launch of a new instance via the AMS API, it hands the configuration as a JSON document to the AMS. The AMS then uses the LXD API over a mutually authenticated TLS connection to LXD and LXD puts it into the `/var/lib/anbox/userdata` path within the instance.

When the AMS starts the instance via the LXD API, the Anbox instance reads the configuration from `/var/lib/anbox/userdata` on startup and connects to the API endpoints provided by the stream agent. There are two endpoints that Anbox connects to - one for WebRTC signaling and one for receiving control information. Only the signaling endpoint is affected by this issue. The control API endpoint is correctly verified with the provided fingerprint.

This issue has led Anbox to not validate the certificate presented by the stream agent against the fingerprint configured within `/var/lib/anbox/userdata` but instead to accept the certificate without validation.

### Impact

Exploiting this issue requires access to internal components and configuration. The stream agent is running within the internal network. It provides the exact API endpoint address via the `/var/lib/anbox/userdata` configuration file through the AMS to the instance without an attacker being able to tamper the endpoint address.

Anbox will not make use of the signaling endpoint unless being instructed to do so via the control API endpoint. So an attacker would need to be able to have access to the internal network and hijack outgoing connections from the Anbox instance and redirect to a malicious service component.

This situation is unlikely and only possible after an attacker has already gained access to the internal network. In the unlikely event of an attacker having access to the internal network and having control over outgoing connections from Anbox, the WebRTC signaling information will be available to the attacker and thereby the attacker will be able to interact with the Anbox instance.

### Upgrade instructions

The issue can be fixed by upgrading your deployment to 1.23.1 or later release of Anbox Cloud. See {ref}`howto-upgrade-anbox-cloud` and {ref}`howto-upgrade-appliance` for instructions on how to update your Anbox Cloud deployment.

### References

- [CVE-2024-8287](https://www.cve.org/CVERecord?id=CVE-2024-8287)
- [LP 2077570](https://bugs.launchpad.net/anbox-cloud/+bug/2077570)
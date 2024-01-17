The Anbox Application Registry (AAR) provides a central repository for applications created on Anbox Cloud. Using an AAR is very useful for larger deployments involving multiple regions, in order to keep applications in sync.

<a name="aar-roles"></a>
## How AAR works

You can configure the Anbox Management Service (AMS) to regularly poll an AAR and import any new application versions found there. When a new application version is found, AMS starts to import it. Once done, AMS makes it available for use.

An imported application is immutable and cannot be changed other than through the AAR itself. If an application is removed from the AAR, it is removed from AMS on the next update as well.

AMS can act in two different roles, `publisher` or `client` when working with an AAR. A single AMS instance can act either as a publisher or as a client, but not both.

* `publisher`:

    The `publisher` role allows both read and write access to the AAR. AMS instances registered as publishers act in `push` mode and are meant to push new applications and their updates to the AAR so that they can be consumed by regular read-only clients.

    We recommend that you have one `publisher` per architecture, for example, one for `amd64` and one for `arm64`. The publishers should not be used to host regular instances but only to manage applications. Regular users should be directed to AMS instances acting as clients.

* `client`:

    The `client` role allows only read access to the AAR. AMS instances registered as clients consume the applications pushed by the publishers.

## Related information

* [How to deploy an AAR](https://discourse.ubuntu.com/t/installation-application-registry/17749)
* [How to configure an AAR](https://discourse.ubuntu.com/t/configure-an-aar/24319)
* [How to revoke an AAR client](https://discourse.ubuntu.com/t/revoke-an-aar-client/24320)

(reference)=
# Reference

The reference guides in this section provide additional information about using Anbox Cloud, release information, available configuration options, performance metrics and benchmarks.

## Releases and versions

Learn about Anbox Cloud releases, the product roadmap, deprecations, supported product versions and component versions.

* {ref}`ref-release-notes`
* {ref}`ref-deprecation-notes`
* {ref}`ref-component-versions`

## Usage

Understand the difference aspects of using Anbox Cloud such as requirements, supported features, provided SDKs, images, APIs, available network ports for communication, extending Anbox Cloud through addons and hooks.

* {ref}`ref-requirements`
* {ref}`Anbox Cloud images <ref-provided-images>`
* {ref}`ref-rendering-resources`
* {ref}`ref-codecs`
* {ref}`ref-android-features`
* {ref}`AOSP vs AAOS images <ref-aosp-aaos>`
* {ref}`ref-sdks`
* {ref}`ref-network-ports`
* {ref}`ref-addon-manifest`
* {ref}`ref-hooks`

## Configuration

Know the configuration options that can be defined for various components of Anbox Cloud.

* {ref}`Appliance preseed configuration <ref-appliance-preseed-config>`
* {ref}`ref-ams-configuration`
* {ref}`Appliance configuration <ref-appliance-configuration>`
* {ref}`ref-application-manifest`
* {ref}`ref-feature-flags`
* {ref}`ref-webrtc`

## API reference

Learn about the APIs provided by Anbox cloud.

* {ref}`ref-api`
  - [AMS HTTP API](https://documentation.ubuntu.com/anbox-cloud/en/latest/reference/api-reference/ams-api/)
  - [Anbox HTTPS API](https://documentation.ubuntu.com/anbox-cloud/en/latest/reference/api-reference/anbox-https-api/)
  - [Anbox Platform API](https://canonical.github.io/anbox-cloud.github.com/latest/anbox-platform-sdk/)
  - [Stream Gateway API](https://documentation.ubuntu.com/anbox-cloud/en/latest/reference/api-reference/gateway-api/)


## Command reference

Learn about the commands and their usage for the Anbox Management Client (AMC) and the Anbox Cloud Appliance.

* [AMC commands](./cmd-ref/amc/ams.amc.md)
* [Appliance commands](./cmd-ref/appliance/anbox-cloud-appliance.md)

## Performance

Learn about the available metrics and benchmarks for measuring performance.

* {ref}`ref-prometheus-metrics`
* {ref}`ref-performance-benchmarks`

## Security

Learn about our security policies and about the fixes we have provided for vulnerabilities.

* {ref}`ref-security-notices`
* {ref}`ref-security-policy`

## Other

* {ref}`ref-license-information`
* {ref}`ref-glossary`

Also check out the {ref}`tutorials` for step-by-step instructions that help you get familiar with Anbox Cloud, the {ref}`how-to-guides` for instructions on how to achieve specific goals when using Anbox Cloud and the {ref}`explanation` section for background information.

```{toctree}
:hidden:

addon-manifest
ams-configuration
Anbox Cloud images <provided-images>
appliance-preseed
appliance-configuration
sdks
api-reference/landing.md
application-manifest
cmd-ref/landing.md
component-versions
charm-configuration
deprecation-notices
feature-flags
glossary
hooks
license-information
network-ports
perf-benchmarks
prometheus
release-notes/release-notes.md
requirements
roadmap
security-notices
security-policy
android-features
Supported features <anbox-features>
supported-rendering-resources
supported-versions
supported-codecs
webrtc-streamer
```

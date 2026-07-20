---
myst:
  html_meta:
    "description": "Reference documentation for Anbox Cloud, covering configuration, requirements, APIs, SDKs, and release notes."
---

(reference)=
# Reference

The reference guides in this section provide additional information about using Anbox Cloud, release information, available configuration options, performance metrics and benchmarks.

## Releases and versions

Anbox Cloud releases, the product roadmap, deprecations, supported product versions and component versions.

- {ref}`ref-release-notes`
- {ref}`ref-deprecation-notes`
- {ref}`ref-component-versions`

## Usage

Reference information about Anbox Cloud requirements, supported features, SDKs, images, APIs, network ports, addons, and hooks.

- {ref}`ref-requirements`
- {ref}`Anbox Cloud images <ref-provided-images>`
- {ref}`ref-feature-support-by-image-type`
- {ref}`ref-rendering-resources`
- {ref}`ref-codecs`
- {ref}`ref-android-features`
- {ref}`ref-compatibility-considerations`
- {ref}`AOSP vs AAOS images <ref-aosp-aaos>`
- {ref}`ref-sdks`
- {ref}`ref-network-ports`
- {ref}`ref-addon-manifest`
- {ref}`ref-hooks`
- {ref}`ref-stream-page-actions`

## Authorization

Authorization entitlements and permissions at the global and resource levels.

- {ref}`ref-auth`

## Configuration

Configuration options defined for various components of Anbox Cloud.

- {ref}`Appliance preseed configuration <ref-appliance-preseed-config>`
- {ref}`ref-ams-configuration`
- {ref}`ref-ams-instance-configuration`
- {ref}`Appliance configuration <ref-appliance-configuration>`
- {ref}`ref-application-manifest`
- {ref}`ref-feature-flags`
- {ref}`ref-webrtc`
- {ref}`ref-charm-configuration`

## API reference

APIs for management, runtime control, and streaming.

- {ref}`ref-api`
  * [AMS HTTP API](/reference/api-reference/ams-api.md)
  * {ref}`Anbox HTTPS API <anbox-https-api>`
  * [Anbox Platform API](https://canonical.github.io/anbox-cloud.github.com/latest/anbox-platform-sdk/)
  * [Stream Gateway API](/reference/api-reference/gateway-api.md)

## Command reference

CLI reference for the Anbox Management Client (AMC), the Anbox Cloud Appliance, and AAR.

- [AMC commands](./cmd-ref/amc/ams.amc.md)
- [Appliance commands](./cmd-ref/appliance/anbox-cloud-appliance.md)
- [AAR commands](./cmd-ref/aar/aar.md)

## Performance

Performance metrics, benchmarks, and monitoring data.

- {ref}`ref-prometheus-metrics`
- {ref}`ref-performance-benchmarks`

## Security

Security policies and fixes for reported vulnerabilities.

- {ref}`ref-security-notices`
- {ref}`ref-security-policy`

## Other

- {ref}`ref-license-information`
- {ref}`ref-glossary`

If you are new to Anbox Cloud, start with the {ref}`tutorials` for step-by-step instructions.
For operational tasks, see the {ref}`how-to-guides`.
For background information and concepts, refer to {ref}`explanation`.

```{toctree}
:hidden:

addon-manifest
ams-configuration
ams-instance-configuration
Anbox Cloud images <provided-images>
feature-support-by-image-type
appliance-preseed
appliance-configuration
auth
sdks
api-reference/index.md
application-manifest
cmd-ref/index.md
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
security-notices
security-policy
stream-page-actions
android-features
compatibility-considerations
Supported features <anbox-features>
supported-rendering-resources
supported-codecs
webrtc-streamer
```

(reference)=
# Reference

The reference guides in this section provide additional information about using Anbox Cloud, release information, available configuration options, performance metrics and benchmarks.

## Releases and versions

Learn about Anbox Cloud releases, release roadmap, supported product versions and component versions.

| Guides | Description  |
|--|--|
| {ref}`ref-roadmap` | Information about general release cycle, currently supported version and future releases |
| {ref}`ref-release-notes` | Release notes for all versions of Anbox Cloud |
| {ref}`ref-component-versions` | Version information about different components of Anbox Cloud for each release |
| {ref}`ref-supported-versions` | Information about supported Anbox Cloud versions and professional support |

## Usage

Understand the difference aspects of using Anbox Cloud such as requirements, supported Android features, provided SDKs, images, APIs, available network ports for communication, extending Anbox Cloud through addons and hooks.

| Guides | Description  |
|--|--|
| {ref}`ref-requirements`| Hardware and software requirements to use Anbox Cloud |
| {ref}`ref-provided-images`| A list of official images that Anbox Cloud provides |
| {ref}`ref-rendering-resources`| A list of supported GPU vendors, drivers, platforms, APIs etc. |
| {ref}`ref-codecs`| A list of supported video codecs |
| {ref}`ref-android-features`| Overview of Android features and which of them are supported by Anbox Cloud |
| {ref}`ref-api`| APIs that Anbox Cloud provides |
| {ref}`ref-sdks`| Overview of the SDKs that Anbox Cloud provides to facilitate integrating and extending the solution |
| {ref}`ref-network-ports`| A list of network ports that Anbox Cloud exposes for each service |
| {ref}`ref-addon-manifest`| List of keys in the addon manifest |
| {ref}`ref-hooks`| Information about hooks for addons or applications and related environment variables |

## Configuration

Know the configuration options that can be defined for various components of Anbox Cloud.

| Guides | Description |
|--|--|
| {ref}`ref-appliance-preseed-config`| The Anbox Cloud Appliance preseed configuration format |
| {ref}`ref-ams-configuration`| Configuration options for Anbox Management Service (AMS) |
| {ref}`ref-application-manifest`| A list of attributes that can be specified in the application manifest |
| {ref}`ref-webrtc`| Configuration details for the WebRTC streamer |

## Command reference

Learn about the commands and their usage for the Anbox Management Client (AMC) and the Anbox Cloud Appliance.

| Guides | Description |
|--|--|
| {ref}`ref-amc-commands`| Commands and their usage when using the AMC |
| {ref}`ref-appliance-commands`| Commands and their usage when using the appliance |

## Performance

Learn about the available metrics and benchmarks for measuring performance.
| Guides | Description |
|--|--|
| {ref}`ref-prometheus-metrics`| Performance metrics that Anbox Cloud provides |
| {ref}`ref-performance-benchmarks`| Benchmarks for the performance that you can achieve with different versions and configurations of Anbox Cloud |

## Other

| Guides | Description |
|--|--|
| {ref}`ref-license-information`| Information on where to find the licenses of components used by Anbox Cloud |
| {ref}`ref-glossary`| Useful terminology for working with Anbox Cloud |

Also check out the {ref}`tutorials` for step-by-step instructions that help you get familiar with Anbox Cloud, the {ref}`how-to-guides` for instructions on how to achieve specific goals when using Anbox Cloud and the {ref}`explanation` section for background information.

```{toctree}
:hidden:

addon-manifest
ams-configuration
Anbox Cloud images <provided-images>
appliance-preseed
sdks
api-reference
application-manifest
cmd-ref/landing.md
component-versions
deprecation-notices
glossary
hooks
license-information
network-ports
perf-benchmarks
prometheus
release-notes/release-notes.md
requirements
roadmap
android-features
Supported features <anbox-features>
supported-rendering-resources
supported-versions
supported-codecs
webrtc-streamer
```
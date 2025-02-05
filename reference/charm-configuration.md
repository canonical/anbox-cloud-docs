(ref-charm-configuration)=
# Charm Configuration

Since the release of Anbox Cloud 1.25.0, Anbox Cloud Charms have been updated to support the latest Ops Framework used by Juju.
This document lists all the resulting changes to the configuration and actions of various Anbox Cloud charms.

## [AMS](https://charmhub.io/ams)

Name          | Value type | Status |
--------------|------------|-------------------------|
`storage_device` | string     |  Removed since 1.25.0 |
`nagios_context` | string     | Removed since 1.25.0 |
`nagios_servicegroups` | string | Removed since 1.25.0 |
`extra_packages` | strings | Removed since 1.25.0 |
`package_status` | string   | Removed since 1.25.0 |
`install_sources` | string | Removed since 1.25.0 |
`install_keys` | string   | Removed since 1.25.0 |
`ua_source` | string   | Removed since 1.25.0 |
`ua_source_key` | string   | Removed since 1.25.0 |
`ua_use_staging` | string   | Removed since 1.25.0 |
`public_interface` | string   | Removed since 1.25.0 |
`snap_revision` | string   | Added since 1.25.0 |

## [AMS-LXD](https://charmhub.io/ams-lxd)

Name          | Value type | Status |
--------------|------------|-------------------------|
`enable_manual_upgrades` | string     |  Removed since 1.25.0 |
`shiftfs_enabled` | string     | Removed since 1.25.0 |
`subnet_prefix_length` | string     | Removed since 1.25.0 |
`extra_packages` | strings | Removed since 1.25.0 |
`package_status` | string   | Removed since 1.25.0 |
`install_sources` | string | Removed since 1.25.0 |
`install_keys` | string   | Removed since 1.25.0 |
`ua_source` | string   | Removed since 1.25.0 |
`ua_source_key` | string   | Removed since 1.25.0 |
`ua_use_staging` | string   | Removed since 1.25.0 |
`public_interface` | string   | Removed since 1.25.0 |
`snapd_refresh` | string   | Removed since 1.25.0 |


## [Anbox Stream Gateway](https://charmhub.io./anbox-stream-gateway)

Name          | Value type | Status |
--------------|------------|-------------------------|
`enable_dev_ui` | string     |  Removed since 1.25.0 |
`nagios_context` | string     | Removed since 1.25.0 |
`nagios_servicegroups` | string | Removed since 1.25.0 |
`tls_cert_path` | strings | Removed since 1.25.0 |
`tls_key_path` | string   | Removed since 1.25.0 |
`prometheus_tls_cert_path` | string | Removed since 1.25.0 |
`prometheus_tls_key_path` | string   | Removed since 1.25.0 |
`prometheus_metrics_path` | string   | Removed since 1.25.0 |
`ua_source` | string   | Removed since 1.25.0 |
`ua_source_key` | string   | Removed since 1.25.0 |
`ua_use_staging` | string   | Removed since 1.25.0 |
`public_interface` | string   | Removed since 1.25.0 |
`snap_revision` | string   | Added since 1.25.0 |

## [Anbox Stream Agent](https://charmhub.io/anbox-stream-agent)

Name          | Value type | Status |
--------------|------------|-------------------------|
`nagios_context` | string     | Removed since 1.25.0 |
`nagios_servicegroups` | string | Removed since 1.25.0 |
`ua_source` | string   | Removed since 1.25.0 |
`ua_source_key` | string   | Removed since 1.25.0 |
`ua_use_staging` | string   | Removed since 1.25.0 |
`public_interface` | string   | Removed since 1.25.0 |
`snap_revision` | string   | Added since 1.25.0 |

## [Anbox Application Registry (AAR)](https://charmhub.io/aar)

Name          | Value type | Status |
--------------|------------|-------------------------|
`nagios_context` | string     | Removed since 1.25.0 |
`nagios_servicegroups` | string | Removed since 1.25.0 |
`ua_source` | string   | Removed since 1.25.0 |
`ua_source_key` | string   | Removed since 1.25.0 |
`ua_use_staging` | string   | Removed since 1.25.0 |
`public_interface` | string   | Removed since 1.25.0 |
`snap_revision` | string   | Added since 1.25.0 |

## Updates to Charm actions

| Action          | Charm | Change | Notes |
|---------------|------------|-------------------------| ----- |
| `debug` | All charms | Removed | - |
| `clear-notifications` | AMS-LXD | Removed | This action has been superseded by a combination of `upgrade-machine` and `upgrade-cluster` actions. |
| `upgrade` | AMS-LXD | Removed | This action has been superseded by a combination of `upgrade-machine` and `upgrade-cluster` actions. |
| `upgrade-gpu-drivers` | AMS-LXD | Removed | This action has been superseded by a combination of `upgrade-machine` and `upgrade-cluster` actions. |
| `upgrade-cluster` | AMS-LXD | Added | Upgrade cluster wide properties like snap updates for LXD. |
| `upgrade-machine` | AMS-LXD | Added | Upgrade node specific properties like kernel module and GPU driver updates.|
| `upgrade-info` | AMS-LXD | Changed | Output changed for the AMS-LXD charm. |

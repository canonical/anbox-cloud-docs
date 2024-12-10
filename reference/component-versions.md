(ref-component-versions)=
# Component versions

This documents the versions of the different components for each Anbox Cloud release.

Not all components are updated with each release. When components are not updated, they are marked with `n/a` below.

## 1.24.1

### Charms

#### Ubuntu 22.04

| Name | Channel | Revision |
|----------|--------------|--------------|
| `anbox-cloud-dashboard` | `1.24/stable` | 601 |
| `ams-node-controller` (Deprecated) | `1.24/stable` | 610 |
| `coturn` | `1.24/stable` | 601 |
| `ams` | `1.24/stable` | 737 |
| `anbox-stream-gateway`  | `1.24/stable` |  692 |
| `ams-lxd` | `1.24/stable` | 652  |
| `anbox-stream-agent` | `1.24/stable` | 685 |
| `aar` | `1.24/stable` |  723 |
| `nats` | `latest/stable` | 9 (AMD64), 11 (ARM64) |

### Bundles

| Name | Channel | Revision |
|----------|--------------|--------------|
| `anbox-cloud` | `1.24/stable` | 554 |
| `anbox-cloud-core` | `1.24/stable` | 566 |

### Snaps

| Name |  Channel | Version |
|----------|--------------|---------|
| `ams`    | `1.24/stable` | `1.24.1-f58845a77`  |
| `aar`    | `1.24/stable` | `1.24.1-f58845a77`  |
| `anbox-cloud-dashboard` | `1.24/stable` | `1.24.1-f58845a77`  |
| `anbox-stream-agent` | `1.24/stable` | `1.24.1-f58845a77`  |
| `anbox-stream-gateway` | `1.24/stable` |  `1.24.1-f58845a77` |
| `anbox-cloud-appliance` | `1.24/stable` | `1.24.1-f58845a77`  |
| `nats` | `latest/stable` | `1.24.1-f58845a77` |

### Anbox images

The following Anbox images are available in two variants: one based on a container and one based on a virtual machine.

| Name | Version |
|----------|--------------|
| `jammy:android14:amd64` |  |
| `jammy:android14:arm64` |  |
| `jammy:android13:amd64` |  |
| `jammy:android13:arm64` |  |
| `jammy:android12:amd64` |  |
| `jammy:android12:arm64` |  |
| `jammy:aaos13:amd64`    |  |
| `jammy:aaos13:arm64`    |  |
| `jammy:aaos14:amd64`    |  |
| `jammy:aaos14:arm64`    |  |


## 1.23.3

The following Anbox images are the only artefacts released for this patch.

```{note}
There are no VM images for ARM64.
```

| Name | Version |
|----------|--------------|
| `jammy:android13:amd64` | `1.23.3-20241128155118.git5e43037d8` |
| `jammy:android13:arm64` | `1.23.3-20241128155118.git5e43037d8` |
| `jammy:android12:amd64` | `1.23.3-20241128155118.git5e43037d8` |
| `jammy:android12:arm64` | `1.23.3-20241128155118.git5e43037d8` |
| `jammy:aaos13:amd64`    | `1.23.3-20241128155118.git5e43037d8` |
| `jammy:aaos13:arm64`    | `1.23.3-20241128155118.git5e43037d8` |


## 1.24.0

### Charms

#### Ubuntu 22.04

| Name | Channel | Revision |
|----------|--------------|--------------|
| `anbox-cloud-dashboard` | `1.24/stable` | 575 |
| `ams-node-controller` (Deprecated) | `1.24/stable` | 585 |
| `coturn` | `1.24/stable` | 576 |
| `ams` | `1.24/stable` | 679 |
| `anbox-stream-gateway`  | `1.24/stable` |  635 |
| `ams-lxd` | `1.24/stable` | 595  |
| `anbox-stream-agent` | `1.24/stable` | 629 |
| `anbox-cloud-nfs` | `latest/stable` | 41 |
| `aar` | `1.24/stable` |  663 |
| `nats` | `latest/stable` | 9 (AMD64), 11 (ARM64) |

### Bundles

| Name | Channel | Revision |
|----------|--------------|--------------|
| `anbox-cloud` | `1.24/stable` | 501 |
| `anbox-cloud-core` | `1.24/stable` | 513 |

### Snaps

| Name |  Channel | Version |
|----------|--------------|---------|
| `ams`    | `1.24/stable` | `1.24.0-599f42a84`  |
| `aar`    | `1.24/stable` | `1.24.0-599f42a84`  |
| `anbox-cloud-dashboard` | `1.24/stable` | `1.24.0-599f42a84`  |
| `anbox-stream-agent` | `1.24/stable` | `1.24.0-599f42a84`  |
| `anbox-stream-gateway` | `1.24/stable` |  `1.24.0-599f42a84` |
| `anbox-cloud-appliance` | `1.24/stable` | `1.24.0-599f42a84`  |
| `nats` | `latest/stable` | `1.24.0-599f42a84` |

### Anbox images

The following Anbox images are available in two variants: one based on a container and one based on a virtual machine.

| Name | Version |
|----------|--------------|
| `jammy:android14:amd64` |  `1.24.0-20241108182702.gitcd2d0650b` |
| `jammy:android14:arm64` |  `1.24.0-20241108182702.gitcd2d0650b` |
| `jammy:android13:amd64` |  `1.24.0-20241108182702.gitcd2d0650b` |
| `jammy:android13:arm64` |  `1.24.0-20241108182702.gitcd2d0650b` |
| `jammy:android12:amd64` |  `1.24.0-20241108182702.gitcd2d0650b` |
| `jammy:android12:arm64` |  `1.24.0-20241108182702.gitcd2d0650b` |
| `jammy:aaos13:amd64`    |  `1.24.0-20241108182702.gitcd2d0650b` |
| `jammy:aaos13:arm64`    |  `1.24.0-20241108182702.gitcd2d0650b` |
| `jammy:aaos14:amd64`    |  `1.24.0-20241108182702.gitcd2d0650b` |
| `jammy:aaos14:arm64`    |  `1.24.0-20241108182702.gitcd2d0650b` |

## 1.23.2

### Charms

#### Ubuntu 22.04

| Name | Channel | Revision |
|----------|--------------|--------------|
| `anbox-cloud-dashboard` | `1.23/stable` | 545 |
| `ams-node-controller` (Deprecated) | `1.23/stable` | 554 |
| `coturn` | `1.23/stable` | 547 |
| `ams` | `1.23/stable` | 619 |
| `anbox-stream-gateway`  | `1.23/stable` | 573 |
| `ams-lxd` | `1.23/stable` | 566 |
| `anbox-stream-agent` | `1.23/stable` | 568 |
| `aar` | `1.23/stable` | 600 |
| `nats` | `latest/stable` | 9 (AMD64), 11 (ARM64) |


#### Ubuntu 20.04 (Deprecated)

| Name | Channel | Revision |
|----------|--------------|--------------|
| `anbox-cloud-dashboard` | `1.23/stable` | 544 |
| `ams-node-controller` (Deprecated) | `1.23/stable` | 553 |
| `coturn` | `1.23/stable` | 546 |
| `ams` | `1.23/stable` | 618 |
| `anbox-stream-gateway`  | `1.23/stable` | 572 |
| `ams-lxd` | `1.23/stable` | 565 |
| `anbox-stream-agent` | `1.23/stable` | 567 |
| `aar` | `1.23/stable` | 599 |
| `nats` | `latest/stable` | 10 (AMD64), 12 (ARM64) |

### Bundles

| Name | Channel | Revision |
|----------|--------------|--------------|
| `anbox-cloud` | `1.23/stable` | 442|
| `anbox-cloud-core` | `1.23/stable` | 451 |

### Snaps

| Name |  Channel | Version |
|----------|--------------|---------|
| `ams`    | `1.23/stable` | `1.23.2-047136ecf` |
| `aar`    | `1.23/stable` | `1.23.2-047136ecf` |
| `amc`    | `latest/stable` | `1.23.2-047136ecf` |
| `ams-node-controller` (Deprecated) | `1.23/stable` | `1.23.2-047136ecf` |
| `anbox-cloud-dashboard` | `1.23/stable` | `1.23.2-047136ecf` |
| `anbox-stream-agent` | `1.23/stable` | `1.23.2-047136ecf` |
| `anbox-stream-gateway` | `1.23/stable` | `1.23.2-047136ecf` |
| `anbox-connect` | `latest/stable` | `1.23.2-047136ecf` |
| `anbox-cloud-appliance` | `1.23/stable` | `1.23.2-047136ecf` |

### Anbox images

The following Anbox images are available in two variants: one based on a container and one based on a virtual machine.

| Name | Version |
|----------|--------------|
| `jammy:android13:amd64` | `1.23.2-20241012130214.git273ce8dc2` |
| `jammy:android13:arm64` | `1.23.2-20241012130214.git273ce8dc2` |
| `jammy:android12:amd64` | `1.23.2-20241012130214.git273ce8dc2` |
| `jammy:android12:arm64` | `1.23.2-20241012130214.git273ce8dc2` |
| `jammy:aaos13:amd64`    | `1.23.2-20241012130214.git273ce8dc2` |
| `jammy:aaos13:arm64`    | `1.23.2-20241012130214.git273ce8dc2` |

## 1.23.1

### Charms

#### Ubuntu 22.04

| Name | Channel | Revision |
|----------|--------------|--------------|
| `anbox-cloud-dashboard` | `1.23/stable` | 515 |
| `ams-node-controller` (Deprecated) | `1.23/stable` | 524 |
| `coturn` | `1.23/stable` | 517 |
| `ams` | `1.23/stable` | 547 |
| `anbox-stream-gateway`  | `1.23/stable` | 533 |
| `ams-lxd` | `1.23/stable` | 520 |
| `anbox-stream-agent` | `1.23/stable` | 528 |
| `nats` | `latest/stable` | 9 (AMD64), 11 (ARM64) |


#### Ubuntu 20.04 (Deprecated)

| Name | Channel | Revision |
|----------|--------------|--------------|
| `anbox-cloud-dashboard` | `1.23/stable` | 514 |
| `ams-node-controller` (Deprecated) | `1.23/stable` | 523 |
| `coturn` | `1.23/stable` | 516 |
| `ams` | `1.23/stable` | 546 |
| `anbox-stream-gateway` | `1.23/stable` | 532 |
| `ams-lxd` | `1.23/stable` | 519 |
| `anbox-stream-agent` | `1.23/stable` | 527 |
| `nats` | `latest/stable` | 10 (AMD64), 12 (ARM64) |

### Bundles

| Name | Channel | Revision |
|----------|--------------|--------------|
| `anbox-cloud` | `1.23/stable` | 356|
| `anbox-cloud-core` | `1.23/stable` | 365 |

### Snaps

| Name |  Channel | Version |
|----------|--------------|---------|
| `ams`    | `1.23/stable` | `1.23.1-2eb71a49d` |
| `aar`    | `1.23/stable` | `1.23.1-2eb71a49d` |
| `amc`    | `latest/stable` | `1.23.1-2eb71a49d` |
| `ams-node-controller` (Deprecated) | `1.23/stable` | `1.23.1-2eb71a49d` |
| `anbox-cloud-dashboard` | `1.23/stable` | `1.23.1-2eb71a49d` |
| `anbox-stream-agent` | `1.23/stable` | `1.23.1-2eb71a49d` |
| `anbox-stream-gateway` | `1.23/stable` | `1.23.1-2eb71a49d` |
| `anbox-connect` | `latest/stable` | `1.23.1-2eb71a49d` |
| `anbox-cloud-appliance` | `1.23/stable` | `1.23.1-2eb71a49d` |

### Anbox images

The following Anbox images are available in two variants: one based on a container and one based on a virtual machine.

| Name | Version |
|----------|--------------|
| `jammy:android13:amd64` | `1.23.1-20240909122006.gitbfce81154` |
| `jammy:android13:arm64` | `1.23.1-20240909122006.gitbfce81154` |
| `jammy:android12:amd64` | `1.23.1-20240909122006.gitbfce81154` |
| `jammy:android12:arm64` | `1.23.1-20240909122006.gitbfce81154` |
| `jammy:aaos13:amd64`    | `1.23.1-20240909122006.gitbfce81154` |
| `jammy:aaos13:arm64`    | `1.23.1-20240909122006.gitbfce81154` |

## 1.23.0

### Charms

#### Ubuntu 22.04

| Name | Channel | Revision |
|----------|--------------|--------------|
| `anbox-cloud-dashboard` | `1.23/stable` | 449 |
| `ams-node-controller` (Deprecated) | `1.23/stable` | 457 |
| `coturn` | `1.23/stable` | 451 |
| `ams` | `1.23/stable` | 481 |
| `anbox-stream-gateway` | `1.23/stable` | 467 |
| `ams-lxd` | `1.23/stable` | 454 |
| `anbox-stream-agent` | `1.23/stable` | 462 |
| `nats` | `latest/stable` | 9 (AMD64), 11 (ARM64) |

#### Ubuntu 20.04 (Deprecated)

| Name | Channel | Revision |
|----------|--------------|--------------|
| `anbox-cloud-dashboard` | `1.23/stable` | 448 |
| `ams-node-controller` (Deprecated) | `1.23/stable` | 456 |
| `coturn` | `1.23/stable` | 450 |
| `ams` | `1.23/stable` | 480 |
| `anbox-stream-gateway` | `1.23/stable` | 466 |
| `ams-lxd` | `1.23/stable` | 454 |
| `anbox-stream-agent` | `1.23/stable` | 461 |
| `nats` | `latest/stable` | 10 (AMD64), 12 (ARM64) |

### Bundles

| Name | Channel | Revision |
|----------|--------------|--------------|
| `anbox-cloud` | `1.23/stable` | 242|
| `anbox-cloud-core` | `1.23/stable` | 251 |

### Snaps

| Name |  Channel | Version |
|----------|--------------|---------|
| `ams`    | `1.23/stable` | `1.23.0-b66df9d8c` |
| `aar`    | `1.23/stable` | `1.23.0-b66df9d8c` |
| `amc`    | `latest/stable` | `1.23.0-b66df9d8c` |
| `ams-node-controller` (Deprecated) | `1.23/stable` | `1.23.0-b66df9d8c` |
| `anbox-cloud-dashboard` | `1.23/stable` | `1.23.0-b66df9d8c` |
| `anbox-stream-agent` | `1.23/stable` | `1.23.0-b66df9d8c` |
| `anbox-stream-gateway` | `1.23/stable` | `1.23.0-b66df9d8c` |
| `anbox-connect` | `latest/stable` | `1.23.0-b66df9d8c` |
| `anbox-cloud-appliance` | `1.23/stable` | `1.23.0-b66df9d8c` |

### Anbox images

The following Anbox images are available in two variants: one based on a container and one based on a virtual machine.

| Name | Version |
|----------|--------------|
| `jammy:android13:amd64` | `1.23.0-20240809080136.4a6ba963a` |
| `jammy:android13:arm64` | `1.23.0-20240809080136.4a6ba963a` |
| `jammy:android12:amd64` | `1.23.0-20240809080136.4a6ba963a` |
| `jammy:android12:arm64` | `1.23.0-20240809080136.4a6ba963a` |
| `jammy:aaos13:amd64`    | `1.23.0-20240809080136.4a6ba963a` |
| `jammy:aaos13:arm64`    | `1.23.0-20240809080136.4a6ba963a` |

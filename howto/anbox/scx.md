(howto-scx)=
# Use userspace schedulers (experimental)

*since 1.30.0*

Since Linux v6.12, the kernel supports running a different scheduler than its internal [EEVDF scheduler](https://docs.kernel.org/scheduler/sched-eevdf.html). This allows for experimenting with different scheduling algorithms. See [the `sched-ext/scx` repository](https://github.com/sched-ext/scx) for more information.

```{important}
Using a userspace scheduler is experimental and may not improve performance; it could alter it in unexpected ways. Use these schedulers only after thorough benchmarking with representative workloads, as described in this guide.
```

## Prerequisites

The following are required:
- Ubuntu 24.04 LTS or newer with the latest HWE kernel. See [Ubuntu kernel life cycle](https://ubuntu.com/kernel/lifecycle) for more information.
- An existing Anbox Cloud deployment.

## Possible effects

The kernel guarantees stability when using a custom userspace scheduler and will ensure no task starvation. However, each scheduler makes different scheduling and placement decisions, which can affect latency, throughput, task placement, and other key metrics in ways that depend heavily on your specific workloads and hardware.

Only thorough testing can identify whether a custom scheduler is the right fit for your deployment.

## Guidelines

Before starting to use any userspace schedulers, implement the following process:

1. Define a set of metrics that you want to optimize.
1. Create a reproducible benchmarking apparatus with representative workloads.
1. Make sure to conduct extensive testing with the base scheduler, to define a baseline for performance.
1. Once your metrics and benchmarks are reliable and well-tested, and you are sure that they represent actual usage that you want to optimize, collect data on a single target system. Ensure that you have a good control over the hardware and software stack.
1. Run your benchmarks using a custom userspace scheduler (as described in the sections below) on the same target system and compare your key metrics with your baseline.

## Usage with Anbox Cloud

Anbox Cloud bundles a subset of the `sched-ext` schedulers with the ams-node-controller snap:
- [`scx_flash`](https://github.com/sched-ext/scx/tree/v1.0.20/scheds/rust/scx_flash)
- [`scx_lavd`](https://github.com/sched-ext/scx/tree/v1.0.20/scheds/rust/scx_lavd)
- [`scx_rustland`](https://github.com/sched-ext/scx/tree/v1.0.20/scheds/rust/scx_rustland)

These schedulers are designed for latency-sensitive tasks and are particularly well-suited for streaming and frame generation workloads. See the linked repository for details on each.

To access these schedulers, the `ams-node-controller` snap must be installed on an Anbox Cloud node in devmode.

```{caution}
Support for `sched_ext` confinement in snapd is not yet available. Until it is, devmode is required to run userspace schedulers in Anbox Cloud.

Installing a snap in devmode disables all security confinement. See [snap confinement](https://documentation.ubuntu.com/security/security-features/privilege-restriction/snap-confinement/#devmode) for more information.
```

```bash
# Delete the ams-node-controller first if it's installed to enable devmode
sudo snap remove ams-node-controller
sudo snap install ams-node-controller --channel=<channel> --devmode
```

Then, to start a userspace scheduler, run the binaries directly with elevated privileges. For example, to start `scx_flash`:

```bash
sudo /snap/ams-node-controller/current/bin/scx_flash
```

Stop the scheduler with Ctrl+C, which reverts to the default kernel scheduler.

## Run a scheduler as a system service

To run a scheduler as a system service, first create a unit file. For `scx_flash`, store it in `/etc/systemd/system/scx-flash.service` on the target node:

```systemd
[Unit]
Description=SCX Flash Userspace Scheduler
After=snapd.seeded.service
Requires=snapd.seeded.service
StartLimitIntervalSec=60
StartLimitBurst=3

[Service]
ExecStart=/snap/ams-node-controller/current/bin/scx_flash
Restart=on-failure

[Install]
WantedBy=multi-user.target
```

Then, enable and start the unit:

```bash
sudo systemctl daemon-reload
sudo systemctl enable --now scx-flash
```

The scheduler will migrate all existing processes on the node gradually. If you start the scheduler on a node with already existing instances, allow it some time to settle before running benchmarks. Alternatively, start the scheduler before launching instances to avoid the migration period entirely.

To check that the scheduler runs as expected, confirm that it is registered with the kernel by reading `/sys/kernel/sched_ext/state` and verifying the file contains `enabled`. Also check the unit status and its logs:

```bash
sudo systemctl status scx-flash
sudo journalctl -u scx-flash -f
```

If you need to use a different scheduler, or go back to the kernel's internal scheduler, disable and stop the unit:

```bash
sudo systemctl disable --now scx-flash
```

## Related topics

- {ref}`howto-run-benchmarks`

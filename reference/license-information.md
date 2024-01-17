The copyright and license information of Anbox Cloud can be found within the container or the virtual machine at `/usr/share/doc/anbox/copyright`.

Anbox Cloud is built using multiple open source software components. This guide lists those components and where to find their license information.

| Software components | Where to find their licenses |
|--|--|
| LXD images | Within the LXD image, <br/>`/usr/share/licenses` and `/usr/share/doc/*/copyright`. |
| Android | In the LXD image instance, <br/> `/var/lib/anbox/android-system/system/etc/NOTICE.xml.gz` |
| Snaps | `/snap/<SNAP_NAME>/current/` </br>Replace <SNAP_NAME> with the name of the Snap.|
| Charms | In the instance where the charm is deployed, `/<path/to/charm>/COPYRIGHT` <br/> Replace `<path/to/charm>` with the path where the charm is deployed. Usually, the charm is deployed in `/var/lib/juju/agents/unit-*/charm`. |

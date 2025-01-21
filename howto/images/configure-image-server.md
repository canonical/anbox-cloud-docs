(howto-configure-image-server)=
# How to configure an image server

  The Canonical image server provides different Anbox Cloud images that are updated regularly. AMS automatically synchronizes new image versions in regular intervals and updates your applications to use these new versions. The images on the image server are updated for important security updates or bug fixes, and with every release of Anbox Cloud.

Access to the image server is automatically configured as part of your Ubuntu Pro subscription during the charm deployment. No further manual steps are necessary.

AMS will automatically start importing the images available on the image server. The `images.update_interval` configuration option allows to customize how often AMS looks for new images. You can set it to a desired interval with the following command:

    amc config set images.update_interval 5m

You can see the synchronized images with the `amc image list` command:

```bash
+----------------------+------------------------+--------+----------+--------------+---------+
|          ID          |          NAME          | STATUS | VERSIONS | ARCHITECTURE | DEFAULT |
+----------------------+------------------------+--------+----------+--------------+---------+
| cgrqjd6k9eqlsruefcng | jammy:android13:arm64  | active | 1        | aarch64      | true    |
+----------------------+------------------------+--------+----------+--------------+---------+
| cgrqjnmk9eqlsruefco0 | jammy:android12:arm64  | active | 1        | aarch64      | false   |
+----------------------+------------------------+--------+----------+--------------+---------+
| cgrqk2uk9eqlsruefcog | jammy:android11:arm64  | active | 1        | aarch64      | false   |
+----------------------+------------------------+--------+----------+--------------+---------+
```

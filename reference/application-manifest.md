An application manifest defines the various attributes of an application.

The available attributes are listed in the following table:

Name          | Value type | Description | Status |
--------------|------------|-------------------------|----|
`name`          | string     | Verbose name of the application. The following special characters are not allowed: `< > : " / \ \| ? *`, as well as space | Supported |
`version`       | string     | Version to encode with the application. Maximum length is 50 characters. | Supported |
`instance-type` | string     | Instance type that all [instances](https://discourse.ubuntu.com/t/26204#instance) created for the application will use. [Jump to details](#instance-type) | Deprecated since 1.20 |
`required-permissions` | array of strings | List of permissions to automatically grant to the application. See [Android Permissions](https://developer.android.com/guide/topics/permissions/overview) for a list of available permissions. If `[*]` was given, all required runtime permissions for the application will be granted on application installation. | Supported |
`image` (optional) | string     | Name or ID of an image to be used for the application. The default image is used if empty. [Jump to details](#image) | Supported |
`addons` (optional) | array      | List of addons to be installed during the application bootstrap process. | Supported |
`tags` (optional) | array      | List of tags to be associated with the application. | Supported |
`boot-package` (optional) | string     | Package to launch once the system has booted (default: package name retrieved from the APK if APK file is present). | Supported |
`boot-activity` (optional) | string     | Activity of boot package to launch once the system has booted (default: main activity as defined in the application manifest). | Supported |
`video-encoder` (optional) | string     | Video encoder to be used by an instance launched from the application  (default: `gpu-preferred`). Possible values are: `gpu`, `gpu-preferred`, `software`. [Jump to details](#video-encoder) | Supported |
`watchdog` (optional)    | map        | Watchdog settings to be configured on application installation. [Jump to details](#watchdog)| Supported |
`services` (optional)    | array      | Services to be provided from the installed application. [Jump to details](#services) | Supported |
`resources` (optional)   | map        | Resources to be allocated on application installation. [Jump to details](#resources) | Supported |
`extra-data` (optional)  | array      | List of additional data to be installed on application installation. [Jump to details](#extra-data) | Supported |
`hooks` (optional) | object | Hooks settings to be configured on application installation. [Jump to details](#hooks) | Supported |
`bootstrap` (optional) | object | Application bootstrap settings to be configured on application installation. [Jump to details](#bootstrap)| Supported |
`features` (optional) | array | List of feature flags to be defined for instances created from the application. | Supported |
`node-selector` (optional) | array | List of selectors which will limit what node an instance for the application can be scheduled on. [Jump to details](#node-selector) | Supported |

<a name="instance-type"></a>
## Instance type
[note type="information" Status="Note"] The `instance-type` attribute is deprecated since 1.20. For any application, a default set of resources will be chosen. If you wish to set specific resources to your application, use the [`resources` attribute](#resources) to do so. [/note]

Similar to other clouds, Anbox Cloud describes the amount of resources that are available to a single instance with an *instance type*. An instance type is a name that is mapped to a set of resources. This allows to have an easy abstraction when referring to resource requirements of instances or particular applications.

Anbox Cloud offers the following instance types:

Name  | vCPU cores | RAM   | Disk size | GPU slots |
------|------------|-------|-----------|-----------|
a2.3  | 2          | 3 GB  | 3 GB      |  0        |
a4.3  | 4          | 3 GB  | 3 GB      |  0        |
a6.3  | 6          | 3 GB  | 3 GB      |  0        |
a8.3  | 8          | 3 GB  | 3 GB      |  0        |
a10.3 | 10         | 3 GB  | 3 GB      |  0        |
g2.3  | 2          | 3 GB  | 3 GB      |  1        |
g4.3  | 4          | 3 GB  | 3 GB      |  1        |
g6.3  | 6          | 3 GB  | 3 GB      |  1        |
g8.3  | 8          | 3 GB  | 3 GB      |  1        |
g10.3 | 10         | 3 GB  | 3 GB      |  1        |

<a name="image"></a>
## Image

The `image` attribute defines which image the application is based on. If left empty, your application is based on the default image. See [How to manage images](https://discourse.ubuntu.com/t/managing-images/17758) for more details on this. Available images on your installation can be listed with the following command:

    amc image list

<a name="node-selector"></a>
## Node selector

The `node-selector` attribute allows specifying a list of selectors to limit the LXD nodes on which an instance for the application can be scheduled. AMS will match the selector against the [tags](https://discourse.ubuntu.com/t/how-to-configure-cluster-nodes/28716#configure-tags) specified for each node.

The following manifest specifies a node selector that instructs the AMS to schedule only those instances having the tags `foo` and `bar`, onto a node:

```
name: candy
instance-type: a4.3
node-selector: [foo, bar]
```

<a name="video-encoder"></a>
## Video encoder
A video encoder type can be specified through the `video-encoder` field in the manifest file when creating an application, so that an instance launched from the application can use a GPU or software video encoder according to different scenarios. Virtual machines do not have GPU support and hence will use software video encoding.

Name                     |  Description
-------------------------|-------------------------
`gpu`                      |  A GPU-based video encoder
`gpu-preferred`  |  A GPU-based video encoder if GPU slots are not used up, otherwise, fall back to use a software-based video encoder
`software`            |  A software-based video encoder

When `gpu` video encoder is specified in the manifest, AMS can fail to create an application if:
 - All GPU slots are used up by running instances.
 - There is no GPU support across the entire LXD cluster.

<a name="watchdog"></a>
## Watchdog

The `watchdog` attribute includes the following field definitions:

Name                     | Value type | Description
-------------------------|------------|-------------------------
`disabled`               | Boolean    | Toggle application watchdog on or off (default: false)
`allowed-packages`       | array of strings | Besides the boot package, list of packages to be allowed to display in the foreground

When an instance is launched, Anbox enables an application watchdog by default for the installed package unless it's disabled explicitly with:

```yaml
name: candy
instance-type: a4.3
image: default
watchdog:
  disabled: true
```

If one of the following scenarios occurs, the watchdog will be triggered. The instance will be terminated and ends up with `error` status.

- The application crashes or an [ANR](https://developer.android.com/topic/performance/vitals/anr) is triggered.
- The application is not in the foreground when an application which is not listed in `allowed-packages` was brought to the foreground and gained the focus.
- The boot package or activity is invalid.
- One of the `allowed-packages` is invalid.

The rules forbid launching another activity, not part of the installed package or listed allowed packages. Launching activities of the same package is allowed.

Supplying `['*']` to the `allowed-packages` when the watchdog is enabled allows any application to be displayed in the foreground without triggering a watchdog.

<a name="services"></a>
## Services

An instance launched from the installed application can expose `services` you want to make accessible from outside the instance. You must define the following properties for each service:

Name           | Value type | Description
---------------|------------|-------------------------
`name`         | string     | Name of service
`port`         | integer    | Port number to be exposed by the service
`protocols`    | array of strings | Protocols to be used by the service (Possible values are: `tcp`, `udp`)
`expose`       | Boolean    | Expose service to be accessible externally or internally

<a name="resources"></a>
## Resources

Anbox Cloud provides a set of [instance types](#instance-type) that define the resources available to an instance. For example, if you start an instance for an application that uses the instance type `a4.3`, the instance is assigned 4 vCPU cores, 3 GB of RAM and 3 GB of disk space.

If your application requires resources that do not correspond to any of the provided instance types, you can use the `resources` directive to override some or all of the predefined resources.

Name           | Value type | Minimum value  | Description
---------------|------------|----------------|-------------------------
`cpus`         | integer    |     1          | Number of vCPU cores
`memory`       | string     |     3 GB       | Memory to be assigned to the application
`disk-size`    | string     |     3 GB       | Disk size to be assigned to the application
`gpu-slots`(optional) | integer |     0      | Number of GPU slots to be assigned to the application

If all required fields (`cpus`/`memory`/`disk-size`) of `resources` are supplied in the application manifest, the `instance-type` field is no longer needed. Even if the `instance-type` field is provided, it will be overridden by the requirements in the `resources` fields upon application installation.

See [How to configure available resources](https://discourse.ubuntu.com/t/24960) for more information.

<a name="extra-data"></a>
## Extra data

Some Android applications which contain large program assets such as graphics or media files use so-called [OBB](https://developer.android.com/google/play/expansion-files) files to store additional data. These data files are separated from the APK and saved onto the external or internal SD card of an Android device. The `extra-data` field can be used in this case to install an APK with separated OBB files or any other additional data into the Android system.

Each item of `extra-data` should be declared as follows:

```yaml
<name>:
    target: <target-path>
    owner:  <uid>:<gid> # optional
    permissions: <file-permission> # optional
```

The fields have the following purpose:

Name                     | Value type | Description
-------------------------|------------|-------------------------
`name`                   | string     | Name of file or directory to be installed into the Android file system
`target-path`            | string     | Target location for the file or directory
`owner` (optional)       | string     | Owner assigned to the target file or directory in the Android file system
`permissions` (optional) | string     | Permissions assigned to the target file or directory in the Android file system

`permissions` represents [Linux file permissions](https://en.wikipedia.org/wiki/File_system_permissions) in octal notation.

It's recommended to let Anbox choose the right values for `owner` and `permissions` instead of manually providing them. If `owner` and `permissions` are not specified, the following default values will be used:

Name          | App data installation directory | Type | Value
--------------|---------------------------------|------|--------
|`owner`       | SD card      | File | `package_uid:sdcard_rw`
|              | SD card      | Dir  | `package_uid:sdcard_rw`
|              | system data | File | `package_uid:package_gid`
|             | system data | Dir  | `package_uid:package_gid`
|`permissions` | SD card      | File | 0660
|              | SD card      | Dir  | 0771
|              | system data | File | 0660
|              | system data | Dir  | boot package folder -> 0700, nested folders of boot package folder -> 0770

Each item (file or folder) declared in the `extra-data` field of the manifest YAML file should be placed in a directory called `extra-data`.

For security reasons, the target location of the files and directories listed in the `extra-data` section is restricted to a few specific locations in the Android file system. These are:

* `/sdcard/Android/obb/<apk-package-name>`
* `/sdcard/Android/data/<apk-package-name>`
* `/data/app/<apk-package-name>`
* `/data/data/<apk-package-name>`

The manifest and extra data in our example are placed next to the application package, which must be named `app.apk`:

```bash
.
├── app.apk
├── extra-data
│   ├── com.canonical.candy.obb
│   └── game-data-folder
│       └── data.bin
└── manifest.yaml
```
<a name="hooks"></a>
## Hooks

Hooks allow you to run custom scripts when a certain event is triggered in the life cycle of an instance. See [Hooks](https://discourse.ubuntu.com/t/hooks/28555) for more details about the usage of hooks in an application.

<a name="bootstrap"></a>
## Bootstrap

An application bootstrap can be fine-tuned through the `bootstrap` field.

The `bootstrap` attribute includes the following field definitions:

Name                  | Value type | Description
----------------------|------------|-------------------------
`keep`                |  array     | Contents under the [APP_DIR](https://discourse.ubuntu.com/t/hooks/28555#env-variables) directory to be preserved in the application image after the bootstrap is finished. Wildcard patterns are supported. See [pattern syntax](https://golang.org/pkg/path/filepath/#Match) for more details.

To minimise the application size, most contents under the `APP_DIR` directory are removed when the application bootstrap is finished. By default, only the metadata content is preserved. If a hook requires any other files under the `APP_DIR` directory during the regular instance runtime, you must include them in the application image.

```yaml
name: my-application
instance-type: a4.3
bootstrap:
  keep:
    - 'apks/*.apk'
    - 'scripts'
```

This will include the `scripts` folder and all APK files under the `apks` folder in the application image when the bootstrap is done, so that they are available to use during the regular instance runtime.

Because it contains metadata, the `manifest.yaml` file and the `hooks` directory (if present) are not removed when the application bootstrap is finished and are always kept in the application image even if they are not explicitly defined in the `keep` list under the `bootstrap` attribute.

The following table lists the valid keys in an addon manifest:

| Name                  | Type         | Description    | Allowed values  |
|-----------------------|--------------|----------------|-----------------|
| `name`                | string       | Name of the addon. Can be used to reference the addon.| All characters except for the following: `< > : " / \ \| ? *`, as well as space. |
| `description`         | string       | Description of the addon.   |   Any character     |
| `provides.abi-support`| string array | Tells AMS that this addon adds support for the given architecture even if the application doesn't support it natively. Use this when your addon brings instruction translation or provides libraries for other architectures. | `arm64-v8a`, `armeabi-v7a`, `armeabi` |
| `hooks.timeout`| string | Execution timeout for each hook that is included in an addon. By default, the timeout is set to 5 minutes. It can be extended to up to 15 minutes. Configure this option if a hook takes longer than 5 minutes to finish. | `10m` |

## Related information

* [Addons](https://discourse.ubuntu.com/t/38727)
* [Tutorial: Create an addon](https://discourse.ubuntu.com/t/creating-an-addon/25284)
* [How to use addons](https://discourse.ubuntu.com/t/managing-addons/17759)
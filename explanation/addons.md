(exp-addons)=
# Addons

Addons provide a way to extend and customize images in Anbox Cloud. Once you have created addons, you can create hooks for them that are triggered based on events in the life cycle of an instance. You can create addons independently and later attach it to individual applications.

## Best practices while using addons

Addons must be created with careful consideration to not affect performance adversely. A good addon is light-weight and targeted for the necessary applications.

Here are some good practices to consider when creating addons:

### Keep addons light

Addons are executed synchronously. Any addon that performs long-running operations (for example, downloading large files, installing packages on regular instances or querying unresponsive services) will delay an application from starting.

```{tip}
Use the `INSTANCE_TYPE` environment variable to run only on the specified instance type. Doing so runs the code in your hooks only when necessary.
```

### Use global addons sparingly

Addons that are enabled for all applications can be useful, but they can add up quickly because whenever a global addon gets updated, a new application version is created. So if you use a global addon and that addon gets updated often, the disk capacity fills up fast.

Try to attach addons to individual applications unless you need a global addon. See {ref}`howto-enable-addons-globally` for more information.

### Clean up your addons

For base instances, if your addon needs additional tools and dependencies during its installation, make sure you remove them afterwards (as part of the `post-stop` hook). This will make your application image lighter and all instances launched from it will start faster.


## Related topics

* {ref}`exp-instances`
* {ref}`tut-create-addon`
* {ref}`howto-addons`
* {ref}`ref-hooks`



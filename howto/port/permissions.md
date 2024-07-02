(howto-grant-runtime-permissions)=
# How to grant runtime permissions

An Anbox Cloud application cannot automatically grant runtime permissions to the app it runs upon creation. Therefore, you must specify the permissions that are required to run the Android app in the application manifest of the Anbox Cloud application. When creating the application in AMS, Anbox Cloud will then grant the specified permissions.

To list all required runtime permissions of an Android app, use [AAPT2](https://developer.android.com/studio/command-line/aapt2):

    aapt2 dump permissions <path_to_APK>

Add the required permissions to the top-level key `required-permissions` in the application manifest. For example:

```yaml
...
required-permissions:
  - android.permission.WRITE_EXTERNAL_STORAGE
  - android.permission.READ_EXTERNAL_STORAGE
  - android.permission.INTERNET
...
```

You can also grant all runtime permissions to an application in the following way:

```yaml
...
required-permissions:  ['*']
...
```

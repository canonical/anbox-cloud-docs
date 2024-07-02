(howto-update-addons)=
# How to update addons

You can update an existing addon with a new version by using the following command:

```bash
amc addon update foo ./foo-addon
```
```{note}
Due to Snap strict confinement, the addon must be located in your home directory.
```

AMS will update the addon and create a new version for all applications that use this addon in the background. If the addon you are updating is used by many applications, you might experience increased load on your cluster while AMS updates many applications simultaneously.

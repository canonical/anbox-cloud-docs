# Android

The images that Anbox Cloud provides are based on different Android versions. They are updated with security patches monthly, based on the upstream security tags. You can find detailed information on the security patches that have been included (or considered to be included but found unrelated) in the [Android Security Bulletins](https://source.android.com/docs/security/bulletin). The relevant security bulletin for each Anbox Cloud release is linked in the {ref}`ref-release-notes`.

See [Android Security Features](https://source.android.com/docs/security/features) in the Android documentation for an overview of security-related features that Android provides. Anbox Cloud supports some of these features, but not all of them. Some of the features rely on hardware that is not available in a virtual system, and others interfere with the Ubuntu security features.

The following table shows which Android security features are supported in Anbox Cloud.

| Security feature                           | Supported in Anbox Cloud |
|--------------------------------------------|:------------------------:|
| App sandbox                                | ✓                        |
| App signing                                | ✓                        |
| Authentication                             | -                        |
| Biometrics                                 | -                        |
| Encryption                                 | -                        |
| Keystore                                   | ✓                        |
| Security-Enhanced Linux (SELinux)          | -                        |
| Trusty Trusted Execution Environment (TEE) | -                        |
| Verified Boot                              | -                        |

## Security-Enhanced Linux (SELinux)

Currently, Anbox Cloud disables SELinux in Android. The reason for this is that SELinux conflicts with AppArmor, which is by default enabled in LXD. Anbox Cloud utilizes the security features provided by LXD and therefore relies on AppArmor instead of SELinux.

In future releases, it might be possible to run AppArmor and SELinux in parallel. In this case, the decision to disable SELinux will be reconsidered.
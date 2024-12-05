(exp-aaos)=
# Android Automotive OS(AAOS)

Since the 1.21.0 release, in addition to providing images based on the Android Open Source Project (AOSP), Anbox Cloud also offers images based on the [Android Automotive OS (AAOS)](https://source.android.com/docs/automotive/start/what_automotive). These images help run Android in automotive infotainment systems at scale.

```{important}
* The Anbox Cloud AAOS images are based on Android Automotive and *not* Android Auto. For understanding the differences between the two, see upstream documentation on [Android Automotive and Android Auto](https://source.android.com/docs/automotive/start/what_automotive#android-automotive-android-auto).
```

The [Vehicle Abstraction Layer (VHAL)](https://source.android.com/docs/automotive/vhal) enables Android Automotive to communicate with and control the different vehicle hardware controls.

Until the 1.24.0 release, if you created your own VHAL implementation by following the [our instructions for customising the Anbox VHAL](https://documentation.ubuntu.com/anbox-cloud/en/latest/howto/android/custom-vhal/) and loaded it as an addon during the Android runtime, vehicle properties and configurations were not visible on the Anbox Cloud dashboard. With the 1.24.0 release, Anbox Cloud has introduced a VHAL adapter that acts as a bridge between the Anbox runtime and the VHAL implementation for data transmission. The Anbox VHAL adapter processes messages sent from the Anbox runtime, performs operations against the VHAL implementation(such as retrieving a list of property configurations), and sends the results back to the Anbox runtime. As a result, vehicle properties and configurations are now visible on the Anbox Cloud dashboard for the third-party VHAL implementations.

However, if a third-party VHAL implementation is loaded during Android runtime, on the Anbox Cloud Dashboard, some vehicle property values may still not be accessible while others may not be editable on the Anbox Cloud dashboard, due to [permission controls](https://source.android.com/docs/automotive/vhal/previous/properties#vehicle-props) that categorise vehicle properties as read-only, write-only, or read-write.

Anbox Cloud offers an [Anbox-specific VHAL HIDL interface](https://github.com/canonical/vendor_canonical_interfaces). By using this HIDL, the VHAL implementation allows the Anbox VHAL adapter to modify non-writable and access non-readable vehicle property values without encountering permission issues. See the {ref}`how-to guide <howto-integrate-hidl>` on instructions for setting this up with your VHAL implementation.

## Related topics

* {ref}`ref-aosp-aaos`

(howto-integrate-hidl)=
# How to integrate Anbox HIDL interface with a custom VHAL implementation

The Anbox HIDL interface is used in the default Anbox VHAL implementation. This document guides you through the steps for setting up and integrating the Anbox HIDL interface with your custom VHAL implementation.

Due to the technical requirements of this procedure, this document assumes familiarity with AOSP development on your part. 

If you are looking for a replacement of the default VHAL implementation with a custom one, see {ref}`replace the Anbox VHAL <howto-replace-anbox-vhal>`.

## Prerequisites

To use and integrate the [Anbox VHAL interface](https://github.com/canonical/vendor_canonical_interfaces/tree/main/vehicle) with a VHAL implementation, the VHAL implementation must be built against Android 14. Hence, you should have downloaded the Android 14 source to perform the following steps. If you don't have this ready, follow the instructions in the [official documentation](https://source.android.com/docs/setup/download).

## Steps

1. Add a new remote definition named `github` to `.repo/manifests/manifest.xml` file.

    ```xml
       <remote name="aosp"
          fetch=".."
          review="https://android-review.googlesource.com/" />

       <remote name="github"
          fetch="https://github.com/canonical/" />
    ```

1. Add a new project named `vendor_canonical_interfaces` to the newly added remote and set it to use the `main` branch.

    ```xml
       <project path="vendor/canonical/interfaces"
                name="vendor_canonical_interfaces"
                remote="github"
                revision="main" />
    ```

1. Sync the project with the remote.

        repo sync vendor_canonical_interfaces

1. In the VHAL implementation, create a VHAL manifest fragment named `vendor.canonical.interfaces.vehicle@1.0.xml`.

    ```xml
       <manifest version="1.0" type="device">
           <hal format="hidl">
               <name>vendor.canonical.interfaces.vehicle</name>
               <transport>hwbinder</transport>
               <fqname>@1.0::IVehicle/default</fqname>
           </hal>
       </manifest>
    ```

   Place the VHAL manifest fragment file in the same folder as the `Android.bp` file that declares the VHAL service, and include the Anbox VHAL manifest fragment in the VHAL service declaration within the `Android.bp` file. Additionally, add the HIDL module as a shared library that the VHAL service links to in the `Android.bp` file.

       cc_binary {
           name: "vendor.<company>.vehicle@<version>-service",
           vintf_fragments: [
               ...
               "vendor.canonical.interfaces.vehicle@1.0.xml",
           ],
           shared_libs: [
               ...
               "vendor.canonical.interfaces.vehicle@1.0",
           ],
           ...
       }

1. Let's consider an [example](https://github.com/canonical/vendor_canonical_interfaces/tree/main/vehicle/1.0/default) that implements the `IVehicle` interface.

    ```cpp
        Return<void> VHalService::get(
            const VehiclePropValue& requestedPropValue, IVehicle::get_cb _hidl_cb) {
          uid_t uid = android::IPCThreadState::self()->getCallingUid();
          if (uid != AID_VEHICLE_NETWORK) {
            _hidl_cb(StatusCode::ACCESS_DENIED, kEmptyValue);
            return Void();
          }

          // NOTE: a VHAL implementation must allow access to non-readable vehicle properties.
          return Void();
        }

        Return<StatusCode> VHalService::set(const VehiclePropValue& value) {
          uid_t uid = android::IPCThreadState::self()->getCallingUid();
          if (uid != AID_VEHICLE_NETWORK)
            return StatusCode::ACCESS_DENIED;

          // NOTE: a VHAL implementation must allow modification of non-writable vehicle properties.
          return StatusCode::NOT_AVAILABLE;
        }
    ```

   Note that you must implement your own access control methods to vehicle properties to ensure secure access. When implementing, this translates to each function having a security mechanism that disallows access to vehicle properties for anything except the authorized `AID_VEHICLE_NETWORK` process.

1. Instantiate the VHAL service that implements the interface and register it as a binder service in the VHAL implementation.

    ```cpp
        #include <VHalService.h>

        int main(int /* argc */, char* /* argv */[]) {
            ...
            ...
            configureRpcThreadpool(4, true);
            auto vendor_vhal_service = std::make_unique<VHalService>();
            status_t status = vendor_vhal_service->registerAsService();
            if (status != OK) {
                return 1;
            }
            joinRpcThreadpool();
            return 1;
        }
    ```

Now, [build](https://source.android.com/docs/setup/build/building) the VHAL module.

Follow the instructions in {ref}`replacing the Anbox VHAL <howto-replace-anbox-vhal>` and load it as an addon during the Android runtime. Once registered, the service can be accessed by the Anbox VHAL adapter.
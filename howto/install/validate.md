Anbox Cloud includes a test suite which allows the validation of an Anbox Cloud deployment. It comes with various tests covering different features of Anbox Cloud and can be used to ensure everything works as expected.

The validation tests currently cover the following areas of an Anbox Cloud deployment:

* AMS
   * Instance creation and deletion in different configurations
   * Expected images are present
   * Configuration is setup as expected
* Anbox Stream Gateway API
  * Session creation and deletion
  * Stress testing
* Streaming
  * Stream selected applications in different configurations from Anbox Cloud while ensuring performance is as expected

## Install Validation Tests

The validation tests are packaged as a snap and are distributed via the Canonical snap store. You can install them via

    snap install anbox-cloud-tests

## Configure the Validation Tests

To run the validation tests, you must generate a configuration file for it first. The tests include an interactive generator that you can use to generate the configuration file. Run the following command:

    anbox-cloud-tests -generate-config

The generator will then guide you through the configuration:

```bash
Do you want to test AMS? [default=yes]
What is the address of AMS? https://1.2.3.4:8444
Generating TLS certificate and key for AMS ...
NOTE: You have to register the certificate generated manually with
 AMS. See https://anbox-cloud.io/docs/manage/managing-ams-access for
 details
Do you want to test the Anbox Stream Gateway? [default=yes]
What is the location of the Anbox Stream Gateway? https://2.3.4.5
Which API token should the tests use to talk with the gateway? xxxx
Is the TLS certificate used by the gateway self signed? [default=yes]
Which application should be used to test the gateway? my-test-app
Do you want to test streaming from your Anbox Cloud deployment? [default=yes]
Which application should be used to test the streaming? my-test-app
Please save the following configuration to a separate file:
services:
    ams:
        url: https://1.2.3.4:8444
        tls:
            key: |
                ...
            certificate: |
                ...
    gateway:
        location: https://2.3.4.5
        auth-token: xxxx
        allow-insecure: true
suites:
    gateway:
        application: my-test-app
    streaming:
        application: my-test-app
        supported-modes:
            - width: 1280
              height: 720
              fps: 30
            - width: 1280
              height: 720
              fps: 60
            - width: 1280
              height: 720
              fps: 25
        execution-time: 5m
        allowed-fps-stddev: 5
        dump-path: ""
    ams:
        supported-architectures:
            - arm64
            - x86_64
        platforms:
            - none
            - swrast
            - webrtc
        instance-types:
            - a2.3
            - a4.3
        gpu-type: none
```

As mentioned by the command you have to store the printed configuration to a file so it can be used by the tests later on. Also you need to register the generated TLS certificate for the AMS tests with AMS. See [How to control AMS remotely](https://discourse.ubuntu.com/t/managing-ams-access/17774) for more details on how to do that.

Depending on your deployment you can further customise the generated configuration. For example may your deployment only support a single architecture for the instances. For that make sure the `suites.ams.supported-architectures` field is set to the right list of architectures.

If you have support for real GPUs set the `suites.ams.gpu-type` item to the right GPU type (supported values are: `nvidia`, `amd`, `intel`, `none`) and add GPU based instance types (see [Instance types](https://discourse.ubuntu.com/t/application-manifest/24197#instance-type-1) for more details) to the `suites.ams.instance-types`.

## Run the Validation Tests

You can run the validation tests with the following command:

    anbox-cloud-tests -config config.yaml -ginkgo.v

If you want to focus on a specific subset of the tests you can specify a focus for the tests:

    anbox-cloud-tests -config config.yaml -ginkgo.v -ginkgo.focus=streaming

The following focus areas are available

* `streaming`
* `gateway`
* `ams`

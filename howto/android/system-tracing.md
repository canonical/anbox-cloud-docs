This guide describes how to enable system tracing in Android using Anbox Cloud. 

## Enable Android System Tracing

1. To enable Android system tracing, add the `android.enable_tracing` flag into the feature file. In the Android container, run:

   ```bash
   echo "android.enable_tracing" >> /var/lib/anbox/features
    ```
 2. Specify the category you want to trace in the Android system using the `debug.atrace.tags.enableflags` system property. The supported categories are defined in [trace.h](https://cs.android.com/android/platform/superproject/main/+/main:system/core/libcutils/include/cutils/trace.h;l=50?q=ATRACE_TAG_INPUT). 
 
    For instance, to enable the graphics category, add the following to the `/var/lib/anbox/android.json` file:

    ```json
      {
        "hardware": "ranchu",
        "api_level": 31,
        "properties": [ "debug.atrace.tags.enableflags=2" ]
      }
    ```
 3. Launch an Anbox session and initiate tracing via the HTTP endpoint. This will not only trace the Anbox session but also capture events aggregated under the category specified in the above system property.: 

    ```bash
    curl --unix-socket /run/user/1000/anbox/sockets/api.unix --request POST --data '{"enable":true}' s/1.0/tracing
      ```   
     After your desired tracing time, stop the tracing:
    ```bash
    curl --unix-socket /run/user/1000/anbox/sockets/api.unix --request POST --data '{"enable":false}' s/1.0/tracing
      ```   
      The resulting trace file is available in the response once tracing is disabled. The trace file should look similar to:

   ```json
	  {
	    "metadata": {
	      "path": "/var/lib/anbox/traces/anbox_884277.0"
	     },
	    "status": "Success",
	    "status_code": 200,
	    "type": "sync"
	  }
 ```


4. Pull the trace file from the Android container:
    ```bash
    lxc file pull <container>/var/lib/anbox/traces/anbox_884277.0 ./
      ```   
      Load the trace file into the [Perfetto UI](https://ui.perfetto.dev/) for visualisation.
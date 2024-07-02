(howto-run-benchmarks)=
# How to run benchmarks

Anbox Cloud provides tools for benchmarking different aspects of your deployment. These tools enable you to put Anbox Cloud under load and use the results to evaluate the performance for a well-defined workload.

See {ref}`ref-performance-benchmarks` for an overview of results that you can expect for selected hardware configurations.

```{important}
Benchmarks provide useful information only if you run them with an application and workload that reflects your real-life scenario. For example, if you run the benchmark with an Android app that just sits idle and does not constantly refresh the screen by itself, you will get a low FPS number. This number does not reflect the real scenario though, because in reality, your users actually use the app and thus cause a higher workload.
```

## Run instance benchmarks

The `amc` command line utility provides a `benchmark` subcommand to run benchmarks on an Anbox Cloud deployment. It measures the time instances take to start up and their average FPS (frames per second) rate.

The results you get depend on the resources of the machines that host the instances. In addition, latency between the different nodes and the AMS services can impact the results

Check the help output to see all available arguments and their purpose:

    amc benchmark -h

The benchmark command launches the specified number of instances on the Anbox `null` platform (see {ref}`exp-platforms`) with the following default display specification:

 | Display spec            | Value |
 | ----------------------- | ----- |
 | Display width           | 1280  |
 | Display height          | 720   |
 | FPS                     | 60    |
 | Display density         | 160   |

You can configure a different display specification through the `--userdata` parameter when running the benchmark. The required format for the parameter varies based on the different platforms:

| Platform              | Required format of user data          | Example                                                   |
| --------------------- | ------------------------------------  | --------------------------------------------------------  |
| `null`                | Comma-separated values                | <display_width>,<display_height>,<display_fps>,<display_density>  |
| `swrast`              | Comma-separated values                | <display_width>,<display_height>,<display_fps>,<display_density>  |
| `webrtc`              | JSON-based                            | {<br>"display_width": <display_width>,<br>"display_height": <display_height>,<br>"display_density": <display_density>,<br>"fps": <display_fps>,<br>"render_only": true<br> } |

```{note}
If you're running a benchmark against the `webrtc` platform, make sure to specify `"render_only": true` to launch the instances in render-only mode. Otherwise, the instance creation will fail, because the `amc benchmark` command doesn't interact with the stream gateway for the benchmark execution.
```

### Example

This example demonstrates running benchmarks for containers. You can do the same for virtual machines following the same commands and procedure.
The following command launches 15 containers for the application with ID `bh2q90vo3v1lt1ft4mlg`:

    amc benchmark --fps --network-address=172.31.4.11 --num-containers=15 --containers-per-second=0.1 bh2q90vo3v1lt1ft4mlg

The output for this command could look like this:

```bash
2019/01/21 11:11:49 Test environment:
2019/01/21 11:11:49   AMS version: 1.7
2019/01/21 11:11:49   Available nodes:
2019/01/21 11:11:49     lxd0 (CPU: 48, Memory: 185GB)
2019/01/21 11:11:49
2019/01/21 11:11:49 Launching 15 containers for application bh2q90vo3v1lt1ft4mlg with 0.1 containers per second
2019/01/21 11:11:49
2019/01/21 11:11:59 Launching container for application bh2q90vo3v1lt1ft4mlg ...
2019/01/21 11:12:05 Started container bh2qhvvo3v1lt1ft4ndg
2019/01/21 11:12:09 Launching container for application bh2q90vo3v1lt1ft4mlg ...
2019/01/21 11:12:15 Started container bh2qi2fo3v1lt1ft4neg
2019/01/21 11:12:19 Launching container for application bh2q90vo3v1lt1ft4mlg ...
2019/01/21 11:12:25 Started container bh2qi4vo3v1lt1ft4nfg
2019/01/21 11:12:29 Launching container for application bh2q90vo3v1lt1ft4mlg ...
2019/01/21 11:12:35 Started container bh2qi7fo3v1lt1ft4ngg
2019/01/21 11:12:39 Launching container for application bh2q90vo3v1lt1ft4mlg ...
2019/01/21 11:12:45 Started container bh2qi9vo3v1lt1ft4nhg
2019/01/21 11:12:49 Launching container for application bh2q90vo3v1lt1ft4mlg ...
2019/01/21 11:12:55 Started container bh2qicfo3v1lt1ft4nig
2019/01/21 11:12:59 Launching container for application bh2q90vo3v1lt1ft4mlg ...
2019/01/21 11:13:05 Started container bh2qievo3v1lt1ft4njg
2019/01/21 11:13:09 Launching container for application bh2q90vo3v1lt1ft4mlg ...
2019/01/21 11:13:15 Started container bh2qihfo3v1lt1ft4nkg
2019/01/21 11:13:19 Launching container for application bh2q90vo3v1lt1ft4mlg ...
2019/01/21 11:13:25 Started container bh2qijvo3v1lt1ft4nlg
2019/01/21 11:13:29 Launching container for application bh2q90vo3v1lt1ft4mlg ...
2019/01/21 11:13:35 Started container bh2qimfo3v1lt1ft4nmg
2019/01/21 11:13:39 Launching container for application bh2q90vo3v1lt1ft4mlg ...
2019/01/21 11:13:45 Started container bh2qiovo3v1lt1ft4nng
2019/01/21 11:13:49 Launching container for application bh2q90vo3v1lt1ft4mlg ...
2019/01/21 11:13:55 Started container bh2qirfo3v1lt1ft4nog
2019/01/21 11:13:59 Launching container for application bh2q90vo3v1lt1ft4mlg ...
2019/01/21 11:14:05 Started container bh2qitvo3v1lt1ft4npg
2019/01/21 11:14:09 Launching container for application bh2q90vo3v1lt1ft4mlg ...
2019/01/21 11:14:15 Started container bh2qj0fo3v1lt1ft4nqg
2019/01/21 11:14:19 Launching container for application bh2q90vo3v1lt1ft4mlg ...
2019/01/21 11:14:25 Started container bh2qj2vo3v1lt1ft4nrg
2019/01/21 11:14:25 Done starting all containers. Measuring container statistics for 1m0s ...
2019/01/21 11:15:25 Removing all containers ...
2019/01/21 11:15:25 Removing container bh2qi2fo3v1lt1ft4neg ...
2019/01/21 11:15:25 Removing container bh2qi7fo3v1lt1ft4ngg ...
2019/01/21 11:15:25 Removing container bh2qitvo3v1lt1ft4npg ...
2019/01/21 11:15:25 Removing container bh2qievo3v1lt1ft4njg ...
2019/01/21 11:15:25 Removing container bh2qj2vo3v1lt1ft4nrg ...
2019/01/21 11:15:25 Removing container bh2qj0fo3v1lt1ft4nqg ...
2019/01/21 11:15:25 Removing container bh2qicfo3v1lt1ft4nig ...
2019/01/21 11:15:25 Removing container bh2qihfo3v1lt1ft4nkg ...
2019/01/21 11:15:25 Removing container bh2qijvo3v1lt1ft4nlg ...
2019/01/21 11:15:25 Removing container bh2qimfo3v1lt1ft4nmg ...
2019/01/21 11:15:25 Removing container bh2qiovo3v1lt1ft4nng ...
2019/01/21 11:15:25 Removing container bh2qi4vo3v1lt1ft4nfg ...
2019/01/21 11:15:25 Removing container bh2qirfo3v1lt1ft4nog ...
2019/01/21 11:15:25 Removing container bh2qhvvo3v1lt1ft4ndg ...
2019/01/21 11:15:25 Removing container bh2qi9vo3v1lt1ft4nhg ...
2019/01/21 11:15:39 Containers boot time measurement:
2019/01/21 11:15:39   Launching all 15 containers took 2m36.560310342s
2019/01/21 11:15:39   Out of 15 containers 0 failed to launch
2019/01/21 11:15:39   Average container launch time: 6.149119411s
2019/01/21 11:15:39   Max container launch time: 6.576302043s
2019/01/21 11:15:39   Min container launch time: 5.911184959s
2019/01/21 11:15:39   Android system failed to boot in the following containers:
2019/01/21 11:15:39     None
2019/01/21 11:15:39 Containers statistics:
2019/01/21 11:15:39   FPS avg 58 min 52 max 64 for 15 containers
2019/01/21 11:15:39   Containers below run at low FPS(<30):
2019/01/21 11:15:39     None
```

## Run stream benchmarks

A benchmark for streaming requires more automation than just starting instances. Therefore, Anbox Cloud provides a dedicated benchmark tool for this purpose. The tool automates the following tasks:

- Create a streaming session
- Receive the video/audio stream
- Collect various statistics
- Optional: Dump the received stream to a local file

The benchmark tool is provided through the `anbox-cloud-tests` snap. Use the following command to install it:

    snap install anbox-cloud-tests

Check the help output to see all available arguments and their purpose:

    anbox-cloud-tests.benchmark -h

To run the benchmark, you must provide an authentication token for the Anbox Stream Gateway. See {ref}`howto-access-stream-gateway` if you haven't already created an authentication token.

If your Anbox Stream Gateway is behind a self-signed TLS certificate, you must specify the `--insecure-tls` option.

By default, the results are printed out as text. Alternatively, you can change the output format to JSON with `--format=json` and save the results to a file with the `--report-path=/path/to/report.json` option.

### Example

The following command runs the benchmark against an existing Anbox Cloud deployment:

    anbox-cloud-tests.benchmark \
      --screen-width=1280 \
      --screen-height=720 \
      --screen-fps=60 \
      --stream-dump-path=/path/to/stream/dump/output \
      --application=my-application \
      --url=<https:// URL of the Anbox Stream Gateway> \
      --auth-token=<valid auth token for the Anbox Stream Gateway> \

The output for this command could look like this:

```bash
I0104 13:03:09.860428 556511 benchmark.cpp:165] Created new session bvpg7vbmend4td6moir0 in region cloud-0 for application bombsquad-stress-nvc
I0104 13:03:10.188585 556626 websocket_client.cpp:32] Successfully connected to websocket
I0104 13:03:10.228832 556626 benchmark.cpp:273] Established connection with stream gateway at https://10.229.100.14
I0104 13:03:10.247896 556626 fake_video_decoder_factory.cpp:149] Adding decoding support for H264
I0104 13:03:10.247918 556626 fake_video_decoder_factory.cpp:161] Adding decoding support for VP8
I0104 13:03:10.309556 556626 peer_connection.cpp:233] Using the following STUN/TURN servers:
I0104 13:03:10.309569 556626 peer_connection.cpp:236] stun:stun.l.google.com:19302
I0104 13:03:10.309572 556626 peer_connection.cpp:236] turn:10.229.100.15:5349
I0104 13:03:10.362562 556626 benchmark.cpp:319] Creating offer to establish connection with the other peer
I0104 13:03:10.378496 556637 peer_connection.cpp:866] Adjusted bitrate for all video and audio encodings on our RTP senders
I0104 13:03:10.378552 556637 benchmark.cpp:370] Offer was created, sharing with the other side
I0104 13:03:38.232844 556637 peer_connection.cpp:746] New stream stream_id added
I0104 13:03:38.820360 556637 benchmark.cpp:396] Connection with other peer is established (took 29s)
I0104 13:03:38.820413 556637 benchmark.cpp:181] Using 10s as sample interval
I0104 13:03:38.820453 556637 main.cpp:165] Connected, starting execution timeout of 1min
I0104 13:03:38.925285 556626 websocket_client.cpp:67] Websocket connection was closed
I0104 13:03:39.048584 556637 peer_connection.cpp:759] New data channel control added
E0104 13:03:40.437090 557770 fake_video_decoder_factory.cpp:63] Failed to create video dumper
I0104 13:03:40.437153 557770 fake_video_decoder_factory.cpp:65] Initialized video decoder for codec H264
I0104 13:04:39.508816 556511 main.cpp:200] Finished benchmark, generating report ...
+-----------------------------------------------------------------------------------------------------------------------------------------------------+
|             Connection |                Average |                    Min |                    Max |                 Stddev |                  Count |
+-----------------------------------------------------------------------------------------------------------------------------------------------------+
|   Round trip time (ms) |                 103.40 |                 101.00 |                 107.00 |                   2.94 |                   5.00 |
|     Bandwidth (Mbit/s) |                   0.00 |                   0.00 |                   0.00 |                   0.00 |                   5.00 |
+-----------------------------------------------------------------------------------------------------------------------------------------------------+
|                  Video |                Average |                    Min |                    Max |                 Stddev |                  Count |
+-----------------------------------------------------------------------------------------------------------------------------------------------------+
|    Bandwidth (Mbit/s)  |                  10.55 |                   9.08 |                  11.88 |                   0.95 |                   5.00 |
|      Frames per second |                  66.00 |                  62.00 |                  69.00 |                   3.29 |                   5.00 |
|        Frames received |                 621.20 |                 619.00 |                 623.00 |                   1.47 |                   5.00 |
|         Frames decoded |                 621.40 |                 617.00 |                 623.00 |                   2.24 |                   5.00 |
|         Frames dropped |                   0.00 |                   0.00 |                   0.00 |                   0.00 |                   5.00 |
|           Freeze count |                   0.00 |                   0.00 |                   0.00 |                   0.00 |                   5.00 |
|            Pause count |                   0.00 |                   0.00 |                   0.00 |                   0.00 |                   5.00 |
|     Key frames decoded |                   4.80 |                   4.00 |                   5.00 |                   0.40 |                   5.00 |
+-----------------------------------------------------------------------------------------------------------------------------------------------------+
Sample interval is 10 seconds
Benchmark ran for 1 minutes
```

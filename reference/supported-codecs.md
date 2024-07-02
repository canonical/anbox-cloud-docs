(ref-codecs)=
# Supported video codecs

Anbox Cloud combines both software and hardware video encoding in order to utilise available resources in the best possible way. Hardware video encoders usually have limited capacity of how many simultaneous video streams they can encode for low latency scenarios. For example, the NVIDIA T4 can encode 37 video streams at 720p and 30 frames per second (see "[Turing H.264 Video Encoding Speed and Quality](https://devblogs.nvidia.com/turing-h264-video-encoding-speed-and-quality/)" for more details). Depending on the CPU platform used, additional compute capacity might be available to support additional sessions via software encoding.

Not all codecs are supported by one or more of the supported GPU models, neither are they performing suitably for low latency. Hence, the list of supported video codecs is limited.

The supported video codecs are:

 * H.264 - The use of H.264 requires a license from the [MPEG LA](https://www.mpegla.com/). Ensure you have the rights to stream H.264 encoded video content to your users.
 * AV1 - Depending on the GPU model used in the deployment, AV1 hardware encoding is the default preference over H.264 on supported GPUs, such as NVIDIA Ada Lovelace Architecture-based GPUs like L4. Otherwise, it will fallback to AV1 software encoding.
 * VP8

Anbox Cloud currently supports the Opus audio codec.

Availability of additional codecs depends on them being supported by the GPU vendors in their hardware encoding solutions or if a viable software encoding solution exists. See {ref}`ref-roadmap` for future versions of Anbox Cloud and planned features.

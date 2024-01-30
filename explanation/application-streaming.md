This guide covers the usage of the Streaming Stack and assumes that you know [how to get access to the Stream Gateway API](https://discourse.ubuntu.com/t/access-the-stream-gateway/17784).

## Streaming Stack Overview

The Streaming Stack is based on [WebRTC](https://webrtc.org/) and integrates with GPUs from different vendors to enable low latency video encoding mandatory for any real time streaming use case. It is highly customisable but requires some functional understanding.

Each component of the stack plays a specific role:

| Gateway                                                                                                                                                             | Agent                                                                                                                         | NATS                                                  | Coturn                                                                                  |
|---------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------|-------------------------------------------------------------------------|
| Provides the initial place where a client and an instance can start a peer to peer discussion. These 'chat rooms' are called sessions and are central to the rest of the stack. | A middleware between the Gateway and Anbox Management Service (AMS). It secures access to AMS, launches instances, relays status information and more. | A messaging queue to allow components to communicate. | A STUN/TURN server needed for WebRTC to work behind NATS and firewalls. |

The following illustration shows how the Streaming Stack components interact with each other when creating a new streaming session:

![Streaming stack sequence|2400x1350](https://assets.ubuntu.com/v1/e38476fe-application_streaming-stack.png)

## Streaming an Application

WebRTC is a peer to peer protocol, but clients must first find each other through a central server. The server does not need to know about the content of the messages between the clients, it only has to forward the messages from one peer to another.

The Stream Gateway exists to enable clients find each other through sessions.Sessions contain user data, application information and more, but most importantly, they provide an entry point for both the client and the instance to start the signalling process. Signalling is a process by which both peers exchange messages and establish optimal codecs, network routes and content types.

### 1. Creating the session

A session is created by calling the Gateway API at `POST /1.0/sessions`. The returned object contains information about the created session as well as a web socket `url` that is necessary to start the signalling process.

### 2. Starting the signalling process

The following is an overview of the signalling process:

 1. The instance creates an offer containing the desired streams (video, audio, binary) as well as codec information.
 2. The client replies to that offer by accepting or refusing it.
 3. Now both peers have agreed on a media type, but do not yet know how to communicate with each other. Remember that, so far, all communication is happening through a web socket on the Gateway.
 4. The peers use the [ICE protocol](https://developer.mozilla.org/en-US/docs/Web/API/WebRTC_API/Signaling_and_video_calling) and interact with STUN/TURN servers to establish an optimal path.
 5. Each network path is bundled in an `ICE candidate`. There are usually multiple ICE candidates per peer and both sides negotiate the best candidate pair.
 6. Both peers agree on the best network path (`ICE candidate`) and start the actual streaming. At this point, they stop communicating through the Gateway web socket and communicate directly with each other.

Details about messages exchanged between the client and the instance are not covered in this guide, but you can find more information on [Mozilla Developer Network](https://developer.mozilla.org/en-US/docs/Web/API/WebRTC_API/Signaling_and_video_calling).

### 3. Establishing the stream

When optimal ICE candidates have been selected and codec capabilities have been agreed upon, the actual tracks are sent. These tracks can be either video, audio or binary. The binary data channel can be useful to send arbitrary data-like controls.

The streams can then be consumed to display the final content.

## Related information

* [Installing Streaming Stack](https://discourse.ubuntu.com/t/installation-quickstart/17744#deploy-anbox-cloud)
* [Signalling](https://www.html5rocks.com/en/tutorials/webrtc/infrastructure/)
* [Supported codecs](https://discourse.ubuntu.com/t/37323)

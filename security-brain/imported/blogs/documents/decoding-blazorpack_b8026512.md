---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2023-02-22_decoding-blazorpack.md
original_filename: 2023-02-22_decoding-blazorpack.md
title: Decoding BlazorPack
category: documents
detected_topics:
- supply-chain
- oauth
- idor
- command-injection
- automation-abuse
- api-security
tags:
- imported
- documents
- supply-chain
- oauth
- idor
- command-injection
- automation-abuse
- api-security
language: en
raw_sha256: b80265129aa89d6fa1f265f59fd9eee636eb95ee831010bf118ffbdfbde6dc74
text_sha256: 3ff403c38c179394f640959df2700fce26f22af36bb591175ae6502f41a9ecc5
ingested_at: '2026-06-28T07:32:18Z'
sensitivity: unknown
redactions_applied: false
---

# Decoding BlazorPack

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2023-02-22_decoding-blazorpack.md
- Source Type: markdown
- Detected Topics: supply-chain, oauth, idor, command-injection, automation-abuse, api-security
- Ingested At: 2026-06-28T07:32:18Z
- Redactions Applied: False
- Raw SHA256: `b80265129aa89d6fa1f265f59fd9eee636eb95ee831010bf118ffbdfbde6dc74`
- Text SHA256: `3ff403c38c179394f640959df2700fce26f22af36bb591175ae6502f41a9ecc5`


## Content

---
title: "Decoding BlazorPack"
page_title: "SensePost | Decoding BlazorPack"
url: "https://sensepost.com/blog/2023/decoding-blazorpack/"
final_url: "https://sensepost.com/blog/2023/decoding-blazorpack/"
authors: ["Rogan Dawes (@RoganDawes)"]
bugs: ["Websockets"]
publication_date: "2023-02-22"
added_date: "2023-03-02"
source: "pentester.land/writeups.json"
original_index: 1488
---

TL;DR: I couldn’t make a custom BlazorPack editor work in Burp, so I used Mallet instead. From an indecipherable binary mess to this, in about [100 lines](https://github.com/sensepost/mallet/blob/master/scripts/ServerSideBlazorUpgradeHandler.groovy):

[![](/img/pages/blog/2023/decoding-blazorpack/49cb2a0e6d465d9455d54b86599259a6.png)](/img/pages/blog/2023/decoding-blazorpack/6cb7020055d66bb82721f0915fa64274.png)Decoded BlazorPack messages

For details on how to do this yourself, even for other protocols, read on!

On a recent assessment, [Marianka](https://twitter.com/mariankabotes) ran into a website using BlazorPack. As Microsoft describes it: “Today’s modern apps are expected to deliver up-to-date information without hitting a refresh button. Add real-time functionality to your dashboards, maps, games and more.”

The initial login used Office365 credentials, via OAuth, downloaded some resources, then transitioned to WebSockets for the rest of the application. After a quick JSON-formatted protocol negotiation, the remainder of the communication was in a binary format, making it really difficult to try to tamper with it, or even to understand what was really going on.

[![](/img/pages/blog/2023/decoding-blazorpack/1419da4746b4e035369bce0dd10831cc.png)](/img/pages/blog/2023/decoding-blazorpack/1419da4746b4e035369bce0dd10831cc.png)Burp view of BlazorPack websockets traffic (note the 4096-byte packets!)

It turns out that there are two versions/implementations of [Blazor](https://dotnet.microsoft.com/en-us/apps/aspnet/web-apps/blazor), client-side and server-side. The client-side version transfers a large WebAssembly blob from the server, which then interacts with the server using a series of HTTP requests. The server-side version actually keeps the application state on the server, and simply sends a presentation layer down to the browser. Having done that, all user interaction (clicks, keystrokes, etc) gets sent back to the server over WebSockets, and the server then sends new rendering instructions back to the browser. We were dealing with this server-side implementation of Blazor.

(You can find a demo site using the server-side approach [here](https://blazor.syncfusion.com/demos/), which can be used to walk through the rest of this blog post.)

Now, while you can sometimes change individual bytes in a binary payload, without too much risk of breaking it horribly, actually figuring out which bytes do what can be quite a task. Ideally, we’d like to figure out how to decode this binary stream into something (somewhat) more comprehensible, and then how to re-encode any changes that we make.

A bit of research turned up the DotNet source code for the [blazorpack protocol](https://github.com/dotnet/aspnetcore/tree/main/src/Components/Server/src/BlazorPack), part of the Microsoft DotNet repository on GitHub. From there I could see that the binary protocol was constructed using a Protobuf-style varint representing the length of the message, with the indicated number of bytes following being a [MessagePack](https://msgpack.org)-encoded blob.

My initial thought was to use BurpSuite’s extension API to make a Editor that would decode the various WebSocket frames, and present them in a readable form, perhaps JSON encoded for easy tampering. However, I was stumped almost immediately when I realised that the WebSocket frames shown by Burp were a maximum of 4096 bytes each, but the actual message could be far larger than that, spread over several frames. From what I could see, Burp had no support for aggregating multiple WebSocket frames (Continuation Frames) into a single entity, and so any attempt to decode a message that was spread over multiple frames would be doomed to fail. Perhaps PortSwigger could consider adding this to BurpSuite. (This post was written before PortSwigger announced their new API, but from what I can see of the Montoya API, aggregating WebSocket frames is still not supported. It would also be nice to see whether a WebSocket frame is Text or Binary, but I digress!)

Of course, this was not the end of the road! [Mallet](https://github.com/sensepost/mallet) is a tool that I have been working on for several years, aimed at exactly this problem – proxying and intercepting arbitrary protocols!

To solve this problem, we’d need to put a few building blocks in place first. Mallet already had support for HTTP (1.0 and 1.1), as well as WebSockets. It also had support for decoding and encoding JSON-formatted messages – needed for the initial handshake. Of course, you could simply assume that the protocol negotiation proceeded as expected, and skip the first request and response before starting the BlazorPack decoding, but for completeness, actually handling the JSON messages would probably be good.

And then finally, we’d need a ProtobufVarint32FrameDecoder, that will break up the stream into actual message-sized chunks, by reading the preceding Varint32, and then that many bytes following. Fortunately, Netty already has [that](https://netty.io/4.1/api/io/netty/handler/codec/protobuf/ProtobufVarint32FrameDecoder.html), along with the corresponding [FrameEncoder](https://netty.io/4.1/api/io/netty/handler/codec/protobuf/ProtobufVarint32LengthFieldPrepender.html). That just left decoding the MessagePack format itself.

My first approach was to use the MessagePack java implementation, and simply wrap it in a couple of Netty classes, to convert the Netty way of doing things to the MessagePack way. Unfortunately, I ran into the first problem that a round trip of bytes to decoded Object, and back again resulted in a differently encoded output. Trying to make sense of the MessagePack library implementation, so that I could understand where the difference had crept in, also had me scratching my head in frustration. It seemed far more complicated than it needed to be!

I then decided to try implement my own MessagePack decoder and encoder, directly from the [specification](https://github.com/msgpack/msgpack/blob/master/spec.md). It couldn’t be *that* hard, could it?

Famous last words, normally! But in this case, a few hundred lines of code in two classes later, I was decoding and encoding, round tripping back to the exact same input byte array! Fantastic!

This is a great advantage of the Netty framework, and its philosophy. While the MessagePack library needed to cater for decoding in a streaming form, adding chunk after chunk, the Netty approach of knowing up front how many bytes to read before trying to decode simplified the decoder immensely! Not having to be able to record exactly where you are in the object tree, so that you can restart from that point, cuts out an enormous amount of complexity.

(I did decide to skip a few of the more esoteric MessagePack protocol extension features, though, so it isn’t an entirely complete MessagePack implementation, I’m afraid!)

And unfortunately, after getting it all set up in a pipeline, it turned out that I was doing something wrong in my encoding or decoding, and Blazor was reporting errors about “no object ID: 9”, and similar. I made a test suite, with a variety of object types and values, but all that did was confirm that I was decoding things the same way that I was encoding them! I even made use of the “official” Messagepack java implementation to convert the objects to serialised bytes, pass those through my codec, confirm that the decoded object was the same as the original test object, and that the re-encoded bytes were the same as those generated by the official library.

Eventually, still not knowing exactly what data type I was processing incorrectly, I realised that I had been using an older version of the MessagePack-Java library, because it had been renamed at some point to messagepack-core! Tearing out my own implementation, I wrapped the latest version of messagepack-java into a Netty codec, and we were in business! Everything was working, and no errors were being reported!

To give you an idea of what the codec ended up looking like, and how much effort it was to integrate, this is the MessagePackCodec. The Decoder is wrapping a Netty ByteBuf containing the data with an InputStream, then using the library to read the objects from it. (I did have to fight a bit with the Groovy scripting engine, which was invoking the wrong method for some reason!). The Encoder simply invokes the MessagePack library to serialize the Object to a byte array, and then writes that into a Netty ByteBuf. And finally, the Codec simply combines the two into a single class.

[![](/img/pages/blog/2023/decoding-blazorpack/db37258550660860f4ea178edfd3cbc2.png)](/img/pages/blog/2023/decoding-blazorpack/2a686f8473f7d498f59e731d3955c365.png)The MessagePackCodec implementation, which simply aggregates the Decoder and Encoder

So, the Mallet processing pipeline looks like this, from client to proxy:

[![](/img/pages/blog/2023/decoding-blazorpack/6f2996119077726d5e7597ff1761ee28.png)](/img/pages/blog/2023/decoding-blazorpack/6f2996119077726d5e7597ff1761ee28.png)[Mallet graph for BlazorPack (client to proxy section)](https://github.com/sensepost/mallet/blob/master/examples/messagepack.mxe)

  * A SOCKS handler to figure out where the connection is going to.
  * An SSLSniffHandler to determine whether the connection is encrypted or not. This provides a branching capability, so that the necessary SSL handlers can be added to those connections.
  * An HttpServerCodec, to decode the incoming bytes into HTTP Request objects, and encode HTTP Response objects to bytes.
  * An HttpObjectAggregator, to combine chunked HTTP Content objects into a single entity.
  * A WebSocketServerUpgradeHandler, to manage the WebSocket upgrade negotiation, and remove the HTTP codec when the negotiation completes.
  * A Groovy ScriptHandler, to install the ProtobufVarInt FrameCodec, and the MessagePackCodec once the WebSocket connection has been negotiated.
  * The Intercept handler, that allows us to see and tamper with the messages.

And then effectively the same on the outbound/upstream connection, just with Client implementations of the SSL and HTTP codecs instead of Server implementations. The full graph is available in the [Mallet examples](https://github.com/sensepost/mallet/blob/master/examples/messagepack.mxe).

Note that the non-SSL branch does not have the BlazorPack handlers. This was created purely in case any non-HTTP resources were requested.

[![](/img/pages/blog/2023/decoding-blazorpack/2f7df8c051768df02d0a9c93335ebb6c.png)](/img/pages/blog/2023/decoding-blazorpack/0dd982340a61a342ac807dd5ac9fff68.png)Mallet showing the initial HTTP request, performing the WebSocket Upgrade.

In the above image, we can see the connection being established, SOCKS negotiation, SSL negotiation, and then the initial HTTP request and response, performing the WebSocket upgrade handshake.

[![](/img/pages/blog/2023/decoding-blazorpack/e6fc88b6ce846ef5cb4d462774e1c774.png)](/img/pages/blog/2023/decoding-blazorpack/e5f54390dbfcd2df0709d6ab31bd40cc.png)Initial WebSocket BlazorPack negotiation messages (one text, one binary)

After the WebSocket channel is established, we can see the initial text frame with a JSON message in it, followed by what is apparently an acknowledgement message (in a binary frame).

Finally, the BlazorPack handlers are added to the pipeline, and the encoded binary messages can be deserialised into representative Java objects. Note that the Mallet Reflection editor allows us to drill down into the individual Objects that are decoded. At this point, we can start trying to understand how this protocol actually works, and look for any possible vulnerabilities.

[![](/img/pages/blog/2023/decoding-blazorpack/49cb2a0e6d465d9455d54b86599259a6.png)](/img/pages/blog/2023/decoding-blazorpack/6cb7020055d66bb82721f0915fa64274.png)Mallet Connection view, with a BlazorPack message selected

For reference, here is an example of the Groovy ScriptHandler that was used to skip the first two WebSocket messages, before installing the Blazor protocol interpreters. (The full script is available in the Mallet GitHub repo, linked under the image.) The same script was used both on the client-to-proxy pipeline, and on the proxy-to-server pipeline.

[![](/img/pages/blog/2023/decoding-blazorpack/3dad4dbec938277a2f6758333e5b5e34.png)](/img/pages/blog/2023/decoding-blazorpack/4455029c3d77e04b2290e8725f09c496.png)[ServerSideBlazorUpgradeHandler.groovy](https://github.com/sensepost/mallet/blob/master/scripts/ServerSideBlazorUpgradeHandler.groovy)

The basic approach was to increment a state variable until we get to the point where the initial handshake has been completed, then just forward messages back and forth. The one remaining wrinkle was dealing with the WebSocket close frame that either end might send. If we see one, we should just close the channel. And we only need to worry about closing one channel. Mallet will see that, and close the other one for us.

One last detail to note is that we need to unwrap the BinaryWebSocketFrames to get just the raw bytes, and rewrap them again on the way back. This is implemented using another small script, BinaryWebSocketFrameCodec.groovy, shown below.

[![](/img/pages/blog/2023/decoding-blazorpack/dadc147b03b17f5bef826a3c1d2766b7.png)](/img/pages/blog/2023/decoding-blazorpack/7442d3a32bcc43b901b555c62682dcb3.png)[BinaryWebSocketFrameCodec.groovy](https://github.com/sensepost/mallet/blob/master/scripts/BinaryWebSocketFrameCodec.groovy)

As you can see, it is very simple! Note: The necessary import statements have been omitted for brevity, but are available by clicking the link above.

In the interests of easy development, the MessagePackCodec was implemented in the same script as the BlazorPack UpgradeHandler. The ScriptHandlers are even specifically designed to make this easy, as they will reload the script from disk if given a filename, every time a new connection is made (and therefore a new ScriptHandler instance is created). Mallet has also been updated to automatically load libraries from the `./libext/` directory on startup (and there is a reload button if you update the libraries after startup too!) So if you are looking at a new protocol, drop any existing libraries into the `libext` directory, write a bit of Groovy (or other scripting language of your choice! Jython, JavaScript and other JSR-223 engines should all work!) and hack up a quick script to make the changes you need! Of course, for proper integration in your IDE, you may want to add those libraries to the pom.xml and have everything automatically included.

And this ultimately is the power that Netty brings to this arena. A powerful, clean API that makes it very easy to compose small, self-contained handlers, that do one thing only, but do it well. My sincere thanks to the authors and contributors of the Netty project!

Footnote: These were the artifacts used to decode the MessagePack frames, available from the Maven repositories:

  * com.fasterxml.jackson.core:jackson-databind version [2.8.11.1,)
  * org.msgpack:msgpack-core version 0.9.0
  * org.msgpack:jackson-dataformat-msgpack version 0.9.0

If you use the site suggested above for testing this, please make sure that your SOCKS proxy configuration in your browser is set up for remote DNS resolution. cdn.syncfusion.com will not negotiate a TLS connection if the correct SNI name is not provided, which is the case when only the IP address is available. Ask me how I know this!

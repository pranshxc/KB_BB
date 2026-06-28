---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2018-12-03_remotely-hijacking-zoom-clients.md
original_filename: 2018-12-03_remotely-hijacking-zoom-clients.md
title: Remotely Hijacking Zoom Clients
category: documents
detected_topics:
- access-control
- command-injection
- rate-limit
- automation-abuse
- business-logic
- api-security
tags:
- imported
- documents
- access-control
- command-injection
- rate-limit
- automation-abuse
- business-logic
- api-security
language: en
raw_sha256: ff9d19e2ea32b9d66b4638a30d608a0f8a3c492341cd7b397709485b0cd16ce7
text_sha256: a55f16870d7a34d5c9d634674ab6a90cfbb0c7a46d318b725c24f4152294437b
ingested_at: '2026-06-28T07:31:58Z'
sensitivity: unknown
redactions_applied: false
---

# Remotely Hijacking Zoom Clients

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2018-12-03_remotely-hijacking-zoom-clients.md
- Source Type: markdown
- Detected Topics: access-control, command-injection, rate-limit, automation-abuse, business-logic, api-security
- Ingested At: 2026-06-28T07:31:58Z
- Redactions Applied: False
- Raw SHA256: `ff9d19e2ea32b9d66b4638a30d608a0f8a3c492341cd7b397709485b0cd16ce7`
- Text SHA256: `a55f16870d7a34d5c9d634674ab6a90cfbb0c7a46d318b725c24f4152294437b`


## Content

---
title: "Remotely Hijacking Zoom Clients"
url: "https://medium.com/tenable-techblog/remotely-exploiting-zoom-meetings-5a811342ba1d"
authors: ["David Wells"]
programs: ["Zoom"]
bugs: ["Logic flaw"]
publication_date: "2018-12-03"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 5551
scraped_via: "browseros"
---

# Remotely Hijacking Zoom Clients

Remotely Hijacking Zoom Clients
David Wells
10 min read
·
Dec 3, 2018

--

2

--

Hello Everyone,

I would like to walkthrough a severe logic flaw vulnerability found in Zoom’s Desktop Conferencing Application. This logic flaw (CVE-2018–15715) affects Zoom clients for MacOS, Linux, and Windows and allows an attacker (doesn’t even have to be meeting attendee) to hijack various components of a live meeting such as forcefully enable desktop control permissions and send keystrokes to meeting attendees sharing their screen. Zoom has released an update for MacOS and Windows and users of Zoom should make sure they are running the most up-to-date version.

Press enter or click to view image in full size
Desktop Control Authorization Bypassed and Keystrokes Sent to Remote Attendee

This vulnerability affects more than just desktop controls as we will see later on, and allows an attacker to manipulate a variety of restricted meeting controls. I will be using the Windows Zoom client as an example to walkthrough how this bug works.

Messaging System

One of the key parts of this vulnerability lies in Zoom’s messaging system.

Zoom’s client contains 4 message pumps (3 only actually appear to be used) located in Util.dll which are responsible for processing and dispatching incoming messages to various Zoom components to carry out functions.

Zoom Message Pumps

This messaging system is the typical inter-thread messaging system that you may find in large applications. In this case, the messaging system is proprietary and uses Zoom message class (msg_db_t) for message objects. The Zoom message class is very simple, having this general structure:

class msg_db_t : public ssb_allocator {
msg_db* prev;
msg_db* next;
BYTE* dataBegin;
BYTE* dataEnd;
DWORD rw_lock;
};

During a meeting, when a Zoom client needs meeting status updated or is receiving packets that are part of an audio/visual stream, a msg_db_t object is constructed and and posted to the appropriate msg_queue, in which the message pump for that queue will process and dispatch the object to the appropriate message handler in Zoom’s application which will then carry out the desired action/update.

Debugging and tracking messages through this was quite a challenge, as stepping into a message posting system and tracking where the pump reads it is like finding a needle in haystack…where the haystack is being shot out of a fire hose. This is where hardware breakpoints (and some IDA debug scripting) helped greatly, as it allowed me to break when specific messages were being read off the queue, so I could easily trace execution flow from message creation to the actual pump processing the message. Now that I have explained a bit of what Zoom’s internal messaging is about, let’s move onto how networking is involved in all of this.

Zoom Networking Basics

When a Zoom client starts/joins a meeting, it will reach out to a Zoom server over TCP to officially notify that a “meeting is starting/being joined.” This allows the Zoom server to then notify appropriate attendees (“hey meeting member has joined / started meeting”), setup UDP streaming for the new client, etc. Another important part in this initialization is a peer-to-peer (P2P) check which checks if the meeting can be streamed P2P rather than proxied through Zoom servers. If so, then the Zoom server can lay low, and leave the Audio/Video to be streamed directly from client to client. The TCP channel is then used throughout the meeting for updates on attendee status and meeting state.

Press enter or click to view image in full size
Networking of Zoom Clients

Summary: The TCP channel is used to communicate with the trusted Zoom server to receive status updates throughout the meeting, while the UDP channel is used for streaming Audio/Video (whether this is P2P or proxied through the Zoom server). Let’s dig deeper.

Networking Messages

One of the message pumps listed earlier was the “ssb::select_t::loop”. This will loop and call into “util.dll!process_io_event” which is responsible for calling a virtual function that generically handles “receiving network traffic” from a “socket_io_t” based class in tp.dll.

process_io_event calling into “recv_network_data” to generate a network message

Whether this traffic is UDP or TCP (socket_io_udp_t or socket_io_tcp_t), the abstraction takes care of it, and all that’s really expected from the process_io_event function is that incoming network data is read and wrapped in a message object (msg_db_t).

The message object is eventually “posted” to the “events” message queue, where the next message pump gets involved: “ssb::events_t::loop”.

The events message pump pops the message off the queue and dispatches it to the appropriate “event message handler” so that the Zoom program state can be properly updated according to the new network data received. This particular message handler (seen below) is a 35 block switch case located in ssb_sdk.dll.

Press enter or click to view image in full size
Message Handler for Event Messages

The network message is sent to this handler, where an identifier from the message tells it which case to invoke (for this scenario I call them function IDs). Some examples of switch case functionalities that can be triggered by these function IDs are:

Qos_receive
Pdu_keep_alive
Sdk_td_msg

So, there must be one that says “hijack screen controls” or “spoof chat messages,” right? Unfortunately, it’s not that simple, as things get incredibly more complex beyond these 35 cases that are invoked. Most of the cases will craft yet-another-message which will be posted to another messaging queue, get processed by different handlers that branch into a dll I won’t even talk about and invoke more and more switch cases that may craft more messages. So I will spare going into that part as it’s not vital to explaining this specific vulnerability.

The Logic Flaw

One thing you may have realized about this design, is that UDP and TCP data are both read by “process_io_event” and eventually posted to the same handler. Since TCP is considered the “Trusted channel” used by Zoom servers, it seems that one may be able to hit various function IDs in this message handler with “untrusted” UDP packets sent by the client, since at this point, Zoom is not checking where the crafted message came from. All it knows is it has an event message it needs to process, and process_io_event is just handing these out with whatever packets come its way, TCP or not. This means we can spoof the “trusted” TCP channel with our “untrusted” UDP channel.

Get David Wells’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

While that’s cool, the question now is: what special functionality can a Zoom server invoke in a client that’s unsolicited? It turns out…more than you may expect. Let’s look at Zooms screen sharing.

Desktop Control Hijacking

In a Zoom meeting, an attendee has the option to share their screen. They also have the option to hand over controls to another attendee. This means full control, as in remote desktop abilities for the other attendee to whom you wish to hand over control. Because of this, there is security built in so that control can’t easily be hijacked. One screen control option uses a request/granting method, where an attendee can request control, but a prompt is popped up for the presenter, and they have to click “allow” which then sends the proper “support_response_type” value to Zoom servers.

Press enter or click to view image in full size
Zoom’s Solicited Granting of Desktop Control

This is a dead end for us, since this is backwards to our ability. We can’t make the client say things to Zoom server, we can only impersonate a Zoom server and tell it things. So I looked into the second way of authenticating screen controls in Zoom, manually from the presenter’s side:

Press enter or click to view image in full size
Zoom’s Unsolicited Granting of Desktop Control

This second screen control option is the unsolicited approach, where presenters can decide to whom they want to give access. When the presenter hands over controls to a user in this manner, it may sound like the thick client requires a local change of state before reaching out to Zoom servers, meaning we shouldn’t be able to impersonate the Zoom server alone and trigger this functionality remotely…however that’s not the case. When the client reaches out to the Zoom server after clicking “give mouse/keyboard control”, it’s really just waiting for its local SDK to be invoked back by the Zoom servers so it can tell the presenter “who to give access to.” In short, this means Zoom server packets ultimately trigger who’s sharing what with whom, and anything else is just a request for Zoom servers to execute it for them.

After investigating this functionality, it turns out all we need to do is send the magical “give desktop control” packet to the target attendee. With the UDP channel however, the messages are parsed differently, so this means it’s not as simple as a “replay attack” from the TCP packets, as we need to arrange the function ID in a different offset as well as some other touch ups (such as changing the header altogether if we plan to exploit this over P2P vs Zoom Server or setting attendee ID field to apply proper desktop control context). Some of these variations can be seen in my POC’s message templates (https://github.com/tenable/poc/blob/master/Zoom/msg_templates.py), where these offsets are taken care of and various message fields are replaced with context relevant data from the attacker using the tool.

Press enter or click to view image in full size
TCP packet for invoking screen control
Press enter or click to view image in full size
Our Hacked UDP packet for invoking screen control

After reversing Zoom’s TCP desktop control instruction, I found the function ID we will need to hit is the sdk_msg_t (0x0e). We will also need to include additional data for specifically triggering the “desktop control” part. Once sent, this will tap into the Zoom client and hand over desktop control to a remote attendee of your choice (the remote attendee that an attacker chooses doesn’t matter, as the attacker’s follow up keystrokes will just spoof as the new authenticated attendee). Researching the general protocol for this to work, we will need to send 3 separate requests:

Tell attendee Y to give attendee X desktop control
Notify attendee Y that control is in effect from attendee X
Send keystrokes/mouse data from attendee X to attendee Y

Once this is done, we can successfully hijack desktop controls of a screen sharing user over UDP and send keystrokes.

Press enter or click to view image in full size
Popping Calculator in Remote Zoom Client.
Other Cool Functionality

Now that we can take advantage of this message handler and basically impersonate a Zoom server, we can do other things too. I found you can “raise” other people’s hands during a meeting, kick out meeting attendees (and locking them out), invoke the Zoom trial version timeout (which kills the meeting for everyone), and even spoof chat messages to come from other meeting attendees:

Press enter or click to view image in full size
Awkward…
Attack Vectors

This, in my opinion, is where it gets really interesting. Not only can you invoke all this as an attendee in the Zoom meeting, but because these attacks are over UDP and no response is needed for the attack, it also means this exploit can be carried out by non-attendees. If a Zoom meeting attendee is on your local network for example (and perhaps meeting with others over WAN), you can slip these UDP packets into their local stream (via spoofing, which then get sent to the Zoom server session and echoed back out to all other meeting members) and trigger this bug for any of the meeting attendees, even the ones over WAN.

It gets better though. Because no response is needed, theoretically (not yet tested), this can be exploited as a fully remote non-attendee over WAN, given that they know the public IP of the business/user that is part of the meeting and have the ability to spoof that public IP address. In this scenario, the attacker could send a UDP packet to the Zoom server (with spoofed source IP/port combo being used by the victim) and also slip into the conferencing UDP stream. The attacker would have to know the public IP part, while they could simply brute force the source port until they hijack controls. The destination UDP port for Zoom servers is always 8801, so this takes care of some of the unknowns and provides a feasible scenario where an attacker may be able to accomplish this. The desktop control will be blind for the attacker, however a WIN_KEY+R followed by a command might be all an attacker needs.

Here is a sketchup I made that demonstrates what’s going on in this vulnerability.

Press enter or click to view image in full size
Zoom Exploit Diagram

You may wonder, what about encrypted Zoom meetings? That must protect against this, since the attacker could not craft a properly encrypted UDP packet to exploit this. I can verify after testing, that encrypted meetings do not protect against this vulnerability, since the UDP channel uses unencrypted UDP packets for these function IDs we want to invoke.

Recent Patch

Investigating the patch that Zoom released for this, we see how this exploit is mitigated. Below is a function called before entering the message handler switch case. It checks if the message origin came from the TCP channel or not, by querying a member in the tp_adapter object. If it’s determined the message was not from the TCP channel, then an additional check is done to see if the packet contains sensitive function IDs. If found, then execution flow is diverted to the “red zone”.

Press enter or click to view image in full size
New Patch Checking if Message Came from TCP

The red zone will actually notify Zoom servers that this type of attack was attempted, which is quite interesting and great to see Zoom keeping an eye out for potential attack telemetry. A new tag is sent to Zoom servers called “EVT_CMD_ILLEGAL_SRC” which also reports the offending attack message.

It is also worth mentioning that Zoom servers appeared to patched against this attack and now filters out harmful UDP packets, so testing with the POC (https://github.com/tenable/poc/tree/master/Zoom) would require P2P meeting with an unpatched Zoom client.

Disclosure

This vulnerability has gone through Tenable’s coordinated disclosure process. You can find Tenable’s research advisory here along with a disclosure timeline and a link to Zoom’s Release Notes. Finally, you can find a more customer-oriented write up on Tenable’s blog.

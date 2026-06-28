---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2022-11-29_voip-spoofing-intigriti-1250.md
original_filename: 2022-11-29_voip-spoofing-intigriti-1250.md
title: VoIP Spoofing (Intigriti) 1,250€
category: documents
detected_topics:
- idor
- ssrf
- command-injection
- rate-limit
- api-security
tags:
- imported
- documents
- idor
- ssrf
- command-injection
- rate-limit
- api-security
language: en
raw_sha256: 34ec00ce796a96ab6322d908c58bbbda856dbb27764f92f1ff5bb755794ed536
text_sha256: d643a71208c1c08ccfc5551356fcbc97fca2a7a42be40aa15a24b9e42f1a8abf
ingested_at: '2026-06-28T07:32:16Z'
sensitivity: unknown
redactions_applied: false
---

# VoIP Spoofing (Intigriti) 1,250€

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2022-11-29_voip-spoofing-intigriti-1250.md
- Source Type: markdown
- Detected Topics: idor, ssrf, command-injection, rate-limit, api-security
- Ingested At: 2026-06-28T07:32:16Z
- Redactions Applied: False
- Raw SHA256: `34ec00ce796a96ab6322d908c58bbbda856dbb27764f92f1ff5bb755794ed536`
- Text SHA256: `d643a71208c1c08ccfc5551356fcbc97fca2a7a42be40aa15a24b9e42f1a8abf`


## Content

---
title: "VoIP Spoofing (Intigriti) 1,250€"
url: "https://0xjin.medium.com/voip-spoofing-intigriti-1-250-57b99bf8bd2b"
authors: ["0xJin (@0xJin)"]
bugs: ["VoIP", "Spoofing"]
bounty: "1,296"
publication_date: "2022-11-29"
added_date: "2022-11-30"
source: "pentester.land/writeups.json"
original_index: 1842
scraped_via: "browseros"
---

# VoIP Spoofing (Intigriti) 1,250€

VoIP Spoofing (Intigriti) 1,250€
N0t0d4y
Follow
4 min read
·
Nov 29, 2022

158

2

1

Hello Folks, i just want to explain a misconfiguration that affect an asset on Intigriti. So, let’s start!!

What is VoIP?

VoIP implementation allows audio calls to be made using an Internet connection instead of a conventional phone. Some VoIP gateway partners may allow you to call others who have a phone number, including local, long distance, mobile, and international numbers.

VoIP uses 5060 as a SIP signaling port by default. Used to register the phone (for example, Cisco, Polycom, etc.)

Among the most important features of VoIP are:

- Use of multiple lines

- Voicemail service

- Voice recording

- Call log

- Modular configurations

Press enter or click to view image in full size
What is SIP?

Session Initiation Protocol (SIP) allows users to establish communications, terminate, or modify voice or video calls. According to pentesting experts, voice or video traffic is transmitted via Real-Time Protocol (RTP). SIP is an application layer protocol that uses UDP or TCP for traffic. By default, SIP uses UDP/TCP port 5060.

Proof of Concept:

Realize that your target is 182.x.x.x/27, so i started using nmap and i started to scan the subnet, i just found an interesting IP that have the port 5060 open:

Get N0t0d4y’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

nmap -sC -sV -A -p- -T4 182.x.x.x
Starting Nmap 7.92 ( https://nmap.org ) at 2022-11-05 06:18 CDT
Nmap scan report for 182.x.x.x (194.x.x.x)
Host is up (0.038s latency).
Not shown: 65531 filtered tcp ports (no-response)
PORT  STATE  SERVICE  VERSION
443/tcp  closed https
5060/tcp open  sip?

first at all i used wireshark for take listen of this port and i found some username like:

Press enter or click to view image in full size
Username Enumeration

Actually, i got so many usernames, and i can actually listen,register, delete, or spoof their call but how?

Let’s try to send an HIT request with a “Test” Username using inviteflood

Spoofing

As you can see i already sent call to the user “102” with a Test as username, let’s open wireshark and filter for SIP and see what happen:

Press enter or click to view image in full size
Invite Call

As we can see i can invite to call any of their agents, using a VoIP spoofing, Currently, someone’s cell phone is ringing, and as you can see i Invite someone in their internal network IP start with 10.x.x.x . Now Let’s analyze that invite call.

Session Initiation Protocol (INVITE)
  Request-Line: INVITE sip:102@194.x.x.x SIP/2.0
  Method: INVITE
  Request-URI: sip:102@194.x.x.x
  Request-URI User Part: 102
  Request-URI Host Part: 194.x.x.x
  [Resent Packet: False]
  Message Header
  Via: SIP/2.0/UDP 192.168.1.6:9;branch=28a8d461-64d5-4636-9b0b-090000000001
  Transport: UDP
  Sent-by Address: 192.168.1.6
  Sent-by port: 9
  Branch: 28a8d461-64d5-4636-9b0b-090000000001
  Max-Forwards: 70
  Content-Length: 460
  To: 102 <sip:102@194.x.x.x:5060>
  SIP to display info: 102 
  SIP to address: sip:102@194.x.x.x:5060
  From: Test <sip:Test@192.168.1.6:9>;tag=28a8da38-64d5-4636-b984-2a0000000001
  SIP from display info: Test 
  SIP from address: sip:Test@192.168.1.6:9
  SIP from address User Part: Test
  SIP from address Host Part: 192.168.1.6
  SIP from tag: 28a8da38-64d5-4636-b984-2a0000000001
  Call-ID: 28a8df56-64d5-4636-b92f-5d0000000001
  [Generated Call-ID: 28a8df56-64d5-4636-b92f-5d0000000001]
  CSeq: 0000000001 INVITE
  Sequence Number: 1
  Method: INVITE
  Supported: timer
  Allow: NOTIFY
  Allow: REFER
  Allow: OPTIONS
  Allow: INVITE
  Allow: ACK
  Allow: CANCEL
  Allow: BYE
  Content-Type: application/sdp
  Contact: <sip:Test@192.168.1.6:9>
  Contact URI: sip:Test@192.168.1.6:9
  Supported: replaces
  User-Agent: Elite 1.0 Brcm Callctrl/1.5.1.0 MxSF/v.3.2.6.26
  Message Body

Ok as you can see i can NOTIFY, REFER, INVITE,ACK, CANCEL, BYE option. So i can CANCEL some outgoing call, i can LISTEN or Register inside call or spoof it.

This misconfiguration is marked as HIGH from the company and they rewarded me 1,250 EUR.

Press enter or click to view image in full size
Rewarded

Marked High:

Press enter or click to view image in full size
Resolved

Thank guys for reading, and Happy bug hunting!

0xJin

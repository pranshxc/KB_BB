---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2020-04-06_how-we-abused-slacks-turn-servers-to-gain-access-to-internal-services.md
original_filename: 2020-04-06_how-we-abused-slacks-turn-servers-to-gain-access-to-internal-services.md
title: How we abused Slack's TURN servers to gain access to internal services
category: documents
detected_topics:
- ssrf
- access-control
- cloud-security
- command-injection
- automation-abuse
- api-security
tags:
- imported
- documents
- ssrf
- access-control
- cloud-security
- command-injection
- automation-abuse
- api-security
language: en
raw_sha256: 8b2864a3143d6e0a2e9ad9f92c20d5aa802e9a745717ca1cf54ec3f911299e38
text_sha256: 49ec353c543684d66a8b077b9ee6733a4f7d2effa9b722df96df1e12722e79bf
ingested_at: '2026-06-28T07:32:01Z'
sensitivity: unknown
redactions_applied: false
---

# How we abused Slack's TURN servers to gain access to internal services

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2020-04-06_how-we-abused-slacks-turn-servers-to-gain-access-to-internal-services.md
- Source Type: markdown
- Detected Topics: ssrf, access-control, cloud-security, command-injection, automation-abuse, api-security
- Ingested At: 2026-06-28T07:32:01Z
- Redactions Applied: False
- Raw SHA256: `8b2864a3143d6e0a2e9ad9f92c20d5aa802e9a745717ca1cf54ec3f911299e38`
- Text SHA256: `49ec353c543684d66a8b077b9ee6733a4f7d2effa9b722df96df1e12722e79bf`


## Content

---
title: "How we abused Slack's TURN servers to gain access to internal services"
page_title: "How we abused Slack's TURN servers to gain access to internal services – Enable Security"
url: "https://www.rtcsec.com/article/slack-webrtc-turn-compromise-and-bug-bounty/"
final_url: "https://www.enablesecurity.com/blog/slack-webrtc-turn-compromise-and-bug-bounty/"
authors: ["Sandro Gauci (@sandrogauci)"]
programs: ["Slack"]
bugs: ["SSRF", "TURN", "WebRTC"]
bounty: "3,500"
publication_date: "2020-04-06"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 4664
---

![Sandro Gauci](https://www.enablesecurity.com/assets/img/sandro-thumb_hu_f1b0822e4d5c5b22.jpg)

**Sandro Gauci**, Enable Security

# How we abused Slack’s TURN servers to gain access to internal services

Published on Apr 6, 2020 in _[webrtc security](/tags/webrtc-security/)_ , _[bug bounty](/tags/bug-bounty/)_ , _[research](/tags/research/)_ , _[TURN security](/tags/turn-security/)_

## Executive summary (TL;DR)

Slack’s TURN server allowed relaying of TCP connections and UDP packets to internal Slack network and meta-data services on AWS. And we were awarded $3,500 for [our bug-bounty report on HackerOne](https://hackerone.com/reports/333419).

## A very brief introduction to the TURN protocol

The [Wikipedia page](https://en.wikipedia.org/wiki/Traversal_Using_Relays_around_NAT) for this protocol is somewhat handy because it explains that:

> Traversal Using Relays around NAT (TURN) is a protocol that assists in traversal of network address translators (NAT) or firewalls for multimedia applications. It may be used with the Transmission Control Protocol (TCP) and User Datagram Protocol (UDP). It is most useful for clients on networks masqueraded by symmetric NAT devices. TURN does not aid in running servers on well known ports in the private network through a NAT; it supports the connection of a user behind a NAT to only a single peer, as in telephony, for example.

> TURN is specified by [RFC 5766](https://tools.ietf.org/html/rfc5766). An update to TURN for IPv6 is specified in [RFC 6156](https://tools.ietf.org/html/rfc6156). The TURN URI scheme is documented in [RFC 7065](https://tools.ietf.org/html/rfc7065).

It might be also useful to note that TURN is actually an extension to the STUN (Session Traversal Utilities for NAT) protocol rather than a network protocol that stands on its own.

TURN servers can get peers behind NAT connected by acting as a relay, as it is called in the RFCs, or a proxy from the perspective of a pentester. In the case of TCP relaying, TURN servers make use of a connect message [method 0x000A in RFC 6062](https://tools.ietf.org/html/rfc6062#section-4.3) while with UDP, a send indication message [method 0x006 in RFC 5766](https://tools.ietf.org/html/rfc5766#section-10) is used. For UDP, [the channel method](https://tools.ietf.org/html/rfc5766#section-11) can also be used and has a similar function.

With that out of the way, one might ask, how is this related to WebRTC?

## Introduction to TURN in the WebRTC infrastructure context

With WebRTC, as well as VoIP in general, one of the more painful complications has been getting the media stream (i.e. RTP packets carrying audio and video) of two or more parties to reach each other. This tends to be a problem because of NAT, which is widely known to have inflicted a great deal of pain on human nature (at least that subculture which develops real-time communications software). The problem has to do with finding the IP and port tuple of each media stream which, when either or both hosts are behind NAT, tends to be less obvious. In many cases, this has been solved with STUN and when that fails, the TURN extension which tends to be the last resort before failing to get the media stream working. Here we should mention that the [ICE](https://en.wikipedia.org/wiki/Interactive_Connectivity_Establishment) protocol (Interactive Connectivity Establishment) is what ties in STUN and TURN. In fact, TURN has been designed to work with ICE.

Therefore, for many WebRTC systems, one key element is to have a TURN server to relay messages between peers when direct media traffic between peers is not allowed by a firewall or NAT device.

## How Slack uses TURN

When we tested Slack, we noticed that TURN was always used for establishing the media which is passed over SRTP. This has been described extensively by the webrtcHacks blog in an article called [Is Slack’s WebRTC Really Slacking? (Yoshimasa Iwase)](https://webrtchacks.com/slack-webrtc-slacking/) way back in 2016, and so we will not repeat the same explanation over here. But one thing that we should highlight is that the way that Slack uses its TURN server puts it in a critical position within its infrastructure, rather than it being a measure of last resort.

## What we found when testing Slack’s TURN servers

Our tests showed that Slack’s TURN servers can be abused to relay TCP and UDP traffic to the TURN server itself and also internal addresses on Slack’s AWS infrastructure. For the webapp-sort of penetration testers out there, this sounds familiar because that is how SSRF (server-side request forgery) vulnerabilities are usually abused. However, there is an important difference in that abuse of this vulnerability is not limited to just HTTP-based protocols (or targets that somehow respond to HTTP requests). Instead, we see it as closer to abusing an open proxy (e.g. a socks proxy or a web proxy with the `CONNECT` method).

What could one do by abusing Slack’s TURN servers?

  * Connect to the AWS meta-data services at `http://169.254.169.254` and obtain IAM temporary credentials
  * Connect to open ports on _localhost_ that are usually not exposed to the Internet (e.g. node exporter): 22, 25, 53, 443, 515, 5666, 8500, 8888, 9090 and 9100
  * Port-scan the Slack AWS infrastructure on `10.41.0.0/16` and find server management applications; possibly abuse such “trusted” services

![Obtaining IAM temporary credentials from AWS meta-data service](01-slack-meta-data-credentials.png)

## Our methodology for testing for open TURN relay abuse

At this point, one might get the wrong impression that TURN servers do not have any authentication or authorization but the truth is that they do make use of authentication. In fact, each time there is a WebRTC session, new temporary TURN credentials are generated and returned by the system. An attacker must therefore retrieve these credentials. We used the following steps to do so:

  * configure our web browser to use Burp proxy
  * in the _Proxy > HTTP history_ tab, filter for the keyword _screenhero_
  * start a call by pressing the call button
  * observe the TURN details returned in the call to `/api/screenhero.rooms.create` which include the temporary username and password, TURN hostname and ports
  * these details are then passed to our tool stunner that was written to abuse this vulnerability

![How we generated TURN credentials](01-slack-turn-credentials.png)

Stunner is an internal tool that we developed to test STUN, and by extension, TURN for various protocol vulnerabilities. The first subcommand of interest here is `turn peer scanner`, which runs a port scan through a TURN relay targeting a particular peer address. In the video demonstration we show the `turn peer httpproxy` subcommand that implemented an HTTP proxy so that web browsers could be configured to pass through stunner, which then proxies HTTP requests and responses to the TURN server speaking its protocol. Finally, the TURN server relays this HTTP traffic back and forth to stunner.

And the rest, as they say, is a historic video:

The video shows:

  1. How to obtain the TURN credentials
  2. Testing relaying to the Internet through the TURN server by checking our IP address
  3. Connecting to internal network and meta-data services on Slacks AWS infrastructure

## How to fix an open TURN relay to address this vulnerability

To address this issue, we recommend placing access control rules on the TURN server itself to block non-public addresses from being specified as the `XOR-PEER-ADDRESS` in the TURN messages. In practical terms, most systems, including Slack’s, make use of [Coturn](https://github.com/coturn/coturn). Our recommendation is to make use of the following options:
  
  
  no-multicast-peers
  denied-peer-ip=0.0.0.0-0.255.255.255
  denied-peer-ip=10.0.0.0-10.255.255.255
  denied-peer-ip=100.64.0.0-100.127.255.255
  denied-peer-ip=127.0.0.0-127.255.255.255
  denied-peer-ip=169.254.0.0-169.254.255.255
  denied-peer-ip=172.16.0.0-172.31.255.255
  denied-peer-ip=192.0.0.0-192.0.0.255
  denied-peer-ip=192.0.2.0-192.0.2.255
  denied-peer-ip=192.88.99.0-192.88.99.255
  denied-peer-ip=192.168.0.0-192.168.255.255
  denied-peer-ip=198.18.0.0-198.19.255.255
  denied-peer-ip=198.51.100.0-198.51.100.255
  denied-peer-ip=203.0.113.0-203.0.113.255
  denied-peer-ip=240.0.0.0-255.255.255.255
  

Our recommendation here is to make use of the latest coturn which by default, no longer allows peering with `127.0.0.1` or `::1`. In some older versions, you might also want to use the `no-loopback-peers`.

**Heads up**

Check out [our post about CVE-2020-26262](https://www.enablesecurity.com/blog/cve-2020-26262-bypass-of-coturns-access-control-protection/) which includes an updated configuration and further details about this.

**Warning**

Even when attackers can no longer abuse TURN servers to relay to internal addresses, in some cases, one might be concerned about TURN servers being used for anything other than their intended use. We can imagine attacks abusing TURN servers in the same way that they abuse open socks and HTTP proxies. But of course, this is a feature and not a bug.

## Our timeline

  * November 2017: added TURN abuse to our stunner toolset
  * December 2017: discovered and reported TURN vulnerability in private customer of Enable Security
  * February 2018: briefly tested Slack and discovered the vulnerability
  * April 2018: submitted our report to Slack, helped them reproduce and address the issue through various rounds of testing
  * May 2018: Slack pushed patch to live servers which was retested by Enable Security
  * January 2020: asked to publish report
  * February 2020: disclosure delayed by HackerOne/Slack
  * March 2020: [report published](https://hackerone.com/reports/333419)

## Thanks

We would like to extend our gratitude to the Slack security team who handled our report and provided us with test systems to check their security fixes. And many thanks to Alfred Farrugia for his work on stunner and reproducing this vulnerability reliably.

## FAQ

### Who first discovered the TURN open relay abuse vulnerability?

From public records, it looks like that would be Cisco, who released an [advisory](https://www.cisco.com/c/en/us/support/docs/csa/cisco-sa-20170913-cmsturn.html) for Cisco Meeting Server back in 2017 September 13.

We properly identified this issue separately, apparently in late 2016, by reading the TURN RFC and eventually proving the actual vulnerability by adding features within our internal toolset, stunner, to abuse this vulnerability. Since then, we have discovered various instances of the same vulnerability during our [WebRTC Penetration Test](https://www.enablesecurity.com/penetration-testing/) engagements.

### Is stunner available?

We use this during [our penetration test services](https://www.enablesecurity.com/#penetration-testing) but unfortunately at this stage we cannot make it available outside of Enable Security.

#### Subscribe to Updates

Stay updated with our latest security insights and updates.

Monthly RTCSec Newsletter

Blog Notifications

We hate spam and are committed to protecting and respecting your privacy. You can unsubscribe from our communications at any time. By subscribing, you are agreeing to the [Privacy Policy](/privacy/).

* * *

![Sandro Gauci](https://www.enablesecurity.com/assets/img/sandro-thumb_hu_d4528d812320cb98.jpg)

Sandro Gauci

[ __](https://www.linkedin.com/in/sandrogauci)[__](https://twitter.com/sandrogauci)[__](https://savvycal.com/sandrogauci/pub)CEO, Chief Mischief Officer at Enable Security

Sandro Gauci leads the operations and research at [Enable Security](https://www.enablesecurity.com). He is the original developer of [SIPVicious OSS](https://www.enablesecurity.com/sipvicious/), the SIP security testing toolset. His role is to focus on the vision of the company, design offensive security tools and engage in security research and testing. Therefore, he is the proud owner of the title of _Chief Mischief Officer_ at Enable Security.

He offers public office hours and is reachable [here](https://savvycal.com/sandrogauci/pub).

###### Contents

  * Executive summary (TL;DR)
  * A very brief introduction to the TURN protocol
  * Introduction to TURN in the WebRTC infrastructure context
  * How Slack uses TURN
  * What we found when testing Slack’s TURN servers
  * Our methodology for testing for open TURN relay abuse
  * How to fix an open TURN relay to address this vulnerability
  * Our timeline
  * Thanks
  * FAQ
  * Who first discovered the TURN open relay abuse vulnerability?
  * Is stunner available?

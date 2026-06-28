---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2022-06-26_bug-cisco-ios-snmpv3-acl-issues.md
original_filename: 2022-06-26_bug-cisco-ios-snmpv3-acl-issues.md
title: 'Bug: Cisco IOS SNMPv3 ACL Issues'
category: documents
detected_topics:
- command-injection
- information-disclosure
- api-security
- mobile-security
tags:
- imported
- documents
- command-injection
- information-disclosure
- api-security
- mobile-security
language: en
raw_sha256: 5b07d5de8382a2fb5792798c98353d8763c3b631dfc4b5db3c4c275c6bb29f71
text_sha256: f42546317c162e47e93f38c83e3498b3d072e4bf0e4cf30f6f0e83c45a190214
ingested_at: '2026-06-28T07:32:12Z'
sensitivity: unknown
redactions_applied: false
---

# Bug: Cisco IOS SNMPv3 ACL Issues

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2022-06-26_bug-cisco-ios-snmpv3-acl-issues.md
- Source Type: markdown
- Detected Topics: command-injection, information-disclosure, api-security, mobile-security
- Ingested At: 2026-06-28T07:32:12Z
- Redactions Applied: False
- Raw SHA256: `5b07d5de8382a2fb5792798c98353d8763c3b631dfc4b5db3c4c275c6bb29f71`
- Text SHA256: `f42546317c162e47e93f38c83e3498b3d072e4bf0e4cf30f6f0e83c45a190214`


## Content

---
title: "Bug: Cisco IOS SNMPv3 ACL Issues"
url: "https://medium.com/@gerrygosselin/cisco-ios-snmpv3-acl-issues-66dbab0bd138"
authors: ["Gerry Gosselin (@ggPixelHealth)"]
programs: ["Cisco"]
bugs: ["Information disclosure"]
publication_date: "2022-06-26"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 2517
scraped_via: "browseros"
---

# Bug: Cisco IOS SNMPv3 ACL Issues

Bug: Cisco IOS SNMPv3 ACL Issues
Gerry Gosselin @snafui@infosec.exchange
Follow
4 min read
·
Jun 26, 2022

1

Synopsis

Due to an acknowledged bug, a small sampling of Cisco IOS and IOS XE routers are exposing SNMPv3 despite configured ACL rules.

Introduction

Back in late 2019 to early 2020, my colleague and I discovered some bizarre behavior with SNMPv3. On Cisco IOS routers, SNMPv3 was listening even when only SNMPv2c was configured. This was only evident to us thanks to the network discovery tool, Rumble. I opened up a support case with Rumble to investigate why we were getting these odd results. A bit of back and forth with Rumble’s co-founder HD Moore and Rumble featured an article about SNMPv3 listening when not explicitly configured, but that was only part of the story. We discovered on our Cisco IOS router, SNMPv3 was listening on an interface’s network and broadcast addresses. We also discovered evidence that SNMPv3 may be exposed to the public Internet despite typical ACL configurations.

Cisco PSIRT

We disclosed the issue to Cisco Product Security Incident Response Team and they confirmed in their lab. In September 2020 it was approved as bug ID CSCvo49242 (login is required for details about the bug; no login for a summary). The bug affects Cisco IOS and IOS XE devices. Dishearteningly, Cisco deemed it not to be a security bug and chalked it up as a configuration issue.

The Issue

Imagine you’re a network engineer. You have a net block of 192.0.2.0/24. Your Cisco IOS router has an interface with an IP address assigned by your ISP and a LAN-side interface with the IP address of 192.0.2.1. You have SNMPv3 enabled but you only want your network management systems behind your corporate firewall to access it. Say your corporate firewall is NATing everything behind 192.0.2.5. You develop an ACL on the IOS router that says only allow SNMP (udp/161) to the router (192.0.2.1) from the firewall’s NAT IP (192.0.2.5). Scan 192.0.2.1 from the public Internet and you’re safe, udp/161 doesn’t show up. Scan the whole 192.0.2.0/24 from the public Internet and SNMPv3 shows up on your .0 and .255 addresses!

The Workaround

Cisco assessed that this is a configuration issue. The workaround, to ACL the interface in a way which prevents SNMPv3 from being accessible, is to include the interface’s network and broadcast address in the ACL (or simply the whole network, 192.0.2.0/24). We believe that without knowledge of this bug, one would not take this action because one would assume their router isn’t listening on IPs that they never configured.

Testing

HD and the Rumble team were very generous and offered me a Rumble sandbox account pre-loaded with scan data from over 917,000 IP addresses. I then went on to see how prevalent this was. What I set out to find were how many routers were exposing SNMP on their network and broadcast addresses and NOT exposing SNMP on their own IP address. To me, this would logically tell me the network operator is attempting to block SNMP via ACL but the bug is exposing it on the network and broadcast address.

I wrote a Python script that parsed the test data, pulling out unique SNMP engine IDs. There were 1,519 unique Cisco routers in the sample set, a mix of IOS and IOS XE. Next I removed all routers with only one IP listening for SNMPv3, followed by all networks with only one IP listening for SNMPv3. The remaining dataset contains routers that have multiple IPs within the same network exposing the same SNMP engine ID. The sample was now down to 566 Cisco routers of the original 1519. That’s 566 unique routers exhibiting the SNMP network/broadcast bug.

Get Gerry Gosselin @snafui@infosec.exchange’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

Finally, the set of 566 was filtered for routers that have exactly two IP addresses with the same SNMP engine ID and the two IP addresses land perfectly on a single subnet’s network and broadcast address. The distance between the first and last IP was used to gauge the network size and the first address and network size information was used to determine if the first IP was a valid network address. The final count of these routers was 21.

Conclusion

This bug is a security issue. Maybe not a terribly prevalent one but:

It exposes the size of networks
It exposes SNMPv3 when it might otherwise be protected by an ACL
The workaround is easy but not obvious unless you are specifically aware of and protecting against this bug

Although 21 of our 1,519 sample may be a small fraction, it was interesting to consider that the other 1,498 routers had SNMPv3 exposed to the public Internet and likely no attempt was being made to restrict it via ACL. SNMPv3 has pretty strong encryption but I still wouldn’t want the port, nor the info it can disclose, available to all.

Final Numbers
917,000 IP addresses scanned
1,519 routers exhibiting SNMPv3 EngineID info disclosure
566 routers exhibiting SNMPv3 network/broadcast bug
21 routers attempting to hide SNMPv3 via ACL and failing due to bug
Patching

It appears as of June 2022, two years since disclosure, only three versions of IOS XE include a fix for this behavior.

Amsterdam-17.3.1
17.3.1
17.3(0.59)

First published June 25, 2022
Copyright © 2022 Gerry Gosselin

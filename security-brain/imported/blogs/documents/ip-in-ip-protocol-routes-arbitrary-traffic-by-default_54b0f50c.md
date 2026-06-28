---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2020-06-02_ip-in-ip-protocol-routes-arbitrary-traffic-by-default.md
original_filename: 2020-06-02_ip-in-ip-protocol-routes-arbitrary-traffic-by-default.md
title: IP-in-IP protocol routes arbitrary traffic by default
category: documents
detected_topics:
- mobile-security
- access-control
- command-injection
- supply-chain
tags:
- imported
- documents
- mobile-security
- access-control
- command-injection
- supply-chain
language: en
raw_sha256: 54b0f50c6093873eba0311f9aaaf520d3ab54817f83642ad1c09550da503a4ec
text_sha256: 2337ba6dd75e145938946e8a36c7a9292165d75446f4f7ec0167d054cee72f6f
ingested_at: '2026-06-28T07:32:02Z'
sensitivity: unknown
redactions_applied: false
---

# IP-in-IP protocol routes arbitrary traffic by default

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2020-06-02_ip-in-ip-protocol-routes-arbitrary-traffic-by-default.md
- Source Type: markdown
- Detected Topics: mobile-security, access-control, command-injection, supply-chain
- Ingested At: 2026-06-28T07:32:02Z
- Redactions Applied: False
- Raw SHA256: `54b0f50c6093873eba0311f9aaaf520d3ab54817f83642ad1c09550da503a4ec`
- Text SHA256: `2337ba6dd75e145938946e8a36c7a9292165d75446f4f7ec0167d054cee72f6f`


## Content

---
title: "IP-in-IP protocol routes arbitrary traffic by default"
page_title: "VU#636397 - IP-in-IP protocol routes arbitrary traffic by default"
url: "https://kb.cert.org/vuls/id/636397"
final_url: "https://kb.cert.org/vuls/id/636397"
authors: ["yannayl (@Yannayli)"]
programs: ["Internet Bug Bounty"]
bugs: ["DoS", "Spoofing"]
bounty: "750"
publication_date: "2020-06-02"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 4533
---

* ×
  * [Home](/vuls/)
  * [Notes](/vuls/bypublished/desc/)
  * [Search](/vuls/search/)
  * [Report a Vulnerability](/vuls/report/)
  * [Disclosure Guidance](/vuls/guidance/)
  * [VINCE](/vince/)

[ [Carnegie Mellon University ](https://www.cmu.edu) ](https://www.cmu.edu/)

__

__

# [Software Engineering Institute](https://www.sei.cmu.edu/)

## CERT Coordination Center

  * [Home](/vuls/)
  * [Notes](/vuls/bypublished/desc/)
  * [Search](/vuls/search/)
  * [Report a Vulnerability](/vuls/report/)
  * [Disclosure Guidance](/vuls/guidance/)
  * [VINCE](/vince/)

  * [Home](/vuls/)
  * [Notes](/vuls/bypublished/desc/)
  * Current:  VU#636397

## IP-in-IP protocol routes arbitrary traffic by default 

#### Vulnerability Note VU#636397

Original Release Date: 2020-06-02 | Last Revised: 2020-09-30

__

[__](https://twitter.com/share?url=https%3A%2F%2Fwww.kb.cert.org%2Fvuls%2Fid%2F636397)

[__](https://www.facebook.com/sharer.php?u=https%3A%2F%2Fwww.kb.cert.org%2Fvuls%2Fid%2F636397)

[__](http://www.addthis.com/bookmark.php?url=https%3A%2F%2Fwww.kb.cert.org%2Fvuls%2Fid%2F636397)

* * *

### Overview

IP Encapsulation within IP (RFC2003 IP-in-IP) can be abused by an unauthenticated attacker to unexpectedly route arbitrary network traffic through a vulnerable device.

### Description

IP-in-IP encapsulation is a tunneling protocol specified in RFC 2003 that allows for IP packets to be encapsulated inside another IP packets. This is very similar to IPSEC VPNs in tunnel mode, except in the case of IP-in-IP, the traffic is unencrypted. As specified, the protocol unwraps the inner IP packet and forwards this packet through IP routing tables, potentially providing unexpected access to network paths available to the vulnerable device. An IP-in-IP device is considered to be vulnerable if it accepts IP-in-IP packets from any source to any destination without explicit configuration between the specified source and destination IP addresses. This unexpected Data Processing Error (CWE-19) by a vulnerable device can be abused to perform reflective DDoS and in certain scenarios used to bypass network access control lists. Because the forwarded network packet may not be inspected or verified by vulnerable devices, there are possibly other unexpected behaviors that can be abused by an attacker on the target device or the target device's network environment.

### Impact

An unauthenticated attacker can route network traffic through a vulnerable device, which may lead to reflective DDoS, information leak and bypass of network access controls.

### Solution

#### Apply updates

The CERT/CC recommends that you apply the latest patch provided by the affected vendor that addresses this issue. Review the vendor information below or contact your vendor or supplier for specific mitigation advice. If a device has the ability to disable IP-in-IP in its configuration, it is recommended that you disable IP-in-IP in all interfaces that do not require this feature. Device manufacturers are urged to disable IP-in-IP in their default configuration and to require their customers to explicitly configure IP-in-IP as and when needed.

#### Disable IP-in-IP

Users can block IP-in-IP packets by filtering IP protocol number 4. Note this filtering is for the IPv4 Protocol (or IPv6 Next Header) field value of 4 and _not_ IP protocol version 4 (IPv4).

#### Proof of Concept (PoC)

A proof-of-concept originally written by Yannay Livneh is [available](https://github.com/CERTCC/PoC-Exploits/tree/master/cve-2020-10136) in the CERT/CC PoC respository.

#### Detection Signature (IDS)

This Snort IDS rule looks for any IP-in-IP traffic, whether intentional or not seen at upstream network path of a vulnerable device. This Snort or Suricata rule can be modified to apply filters that ignore sources and destinations that are allowed by policy to route IP-in-IP traffic.

`alert ip any any -> any any (msg: "IP-in-IP Tunneling VU#636397 https://kb.cert.org"; ip_proto:4; sid: 1367636397; rev:1;)`

### Acknowledgements

Thanks to Yannay Livneh for reporting this issue to us.

This document was written by Vijay Sarvepalli.

### Vendor Information

636397

Filter by status: All Affected Not Affected Unknown

Filter by content: __Additional information available

__Sort by: Status Alphabetical

Expand all

###  Cisco __ Affected

Notified: 2020-03-26  Updated: 2020-06-24 **CVE-2020-10136**|  Affected  
---|---  
  
#### Vendor Statement

Please visit Cisco public advisory https://tools.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-nxos-ipip-dos-kCT9X4

#### References

  * <https://tools.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-nxos-ipip-dos-kCT9X4>

###  Digi International __ Affected

Updated: 2020-06-24 **CVE-2020-10136**|  Affected  
---|---  
  
#### Vendor Statement

SAROS VERSION 8.1.0.1 (Bootloader 7.67) released on 23 April 2020 fixes this issue.

#### References

  * <https://www.digi.com/resources/security>

###  HP Inc. __ Affected

Updated: 2020-06-24 **CVE-2020-10136**|  Affected  
---|---  
  
#### Vendor Statement

We have not received a statement from the vendor.

#### References

  * <https://support.hp.com/us-en/document/c06640149>

#### CERT Addendum

HP Security Bulletin c06640149 addresses this vulnerability along with others impacting HP Samsung branded printers. https://support.hp.com/us-en/document/c06640149

###  Samsung __ Affected

Updated: 2020-06-24 **CVE-2020-10136**|  Affected  
---|---  
  
#### Vendor Statement

We have not received a statement from the vendor.

#### CERT Addendum

As of September 12, 2016, HP has acquired and presently owns Samsung printer’s division. Please see HP vendor section for further information. https://investor.hp.com/news/press-release-details/2016/HP-Acquires-Samsung-Printer-Business/default.aspx

###  Treck __ Affected

Updated: 2020-06-24 **CVE-2020-10136**|  Affected  
---|---  
  
#### Vendor Statement

Starting with Treck release 6.0.1.67, configuring a 6over4 tunnel no longer automatically enables IP encapsulation within IP

#### CERT Addendum

Please update your Treck embedded TCP/IP software to the version 6.0.1.67 or later to prevent unexpected tunneling behavior in your TCP/IP stack.

###  Allegro Software Development Corporation __ Not Affected

Notified: 2020-04-09  Updated: 2020-06-24 **CVE-2020-10136**|  Not Affected  
---|---  
  
#### Vendor Statement

Allegro Software does not provide operating systems or network TCP/IP stack. Only webserver software is OEM sold to device manufacturers

###  Aruba Networks __ Not Affected

Notified: 2020-04-29  Updated: 2020-06-24 **CVE-2020-10136**|  Not Affected  
---|---  
  
#### Vendor Statement

Aruba Networks has tested products across our range and has not found the vulnerable behavior to be allowed anywhere. To the best of our knowledge no Aruba Network products are affected by this vulnerability.

###  Joyent __ Not Affected

Notified: 2020-04-29  Updated: 2020-06-24 **CVE-2020-10136**|  Not Affected  
---|---  
  
#### Vendor Statement

Default configurations of illumos, even where packet-forwarding is enabled (see the routeadm(1M) man page), should not be vulnerable to this attack.

###  LANCOM Systems GmbH __ Not Affected

Notified: 2020-04-29  Updated: 2020-06-24 **CVE-2020-10136**|  Not Affected  
---|---  
  
#### Vendor Statement

LANCOM Systems products are not vulnerable to these vulnerabilities.

###  Sierra Wireless __ Not Affected

Updated: 2020-06-24 **CVE-2020-10136**|  Not Affected  
---|---  
  
#### Vendor Statement

We have surveyed our products and determined we are unaffected by this issue.

#### References

  * <https://www.sierrawireless.com/company/security/>

###  TP-LINK Not Affected

Notified: 2020-04-29  Updated: 2020-06-24 **CVE-2020-10136**|  Not Affected  
---|---  
  
#### Vendor Statement

We have not received a statement from the vendor.

###  Technicolor Not Affected

Notified: 2020-06-15  Updated: 2020-06-24

**Statement Date: June 23, 2020**

**CVE-2020-10136**|  Not Affected  
---|---  
  
#### Vendor Statement

We have not received a statement from the vendor.

###  A10 Networks Unknown

Notified: 2020-04-29  Updated: 2020-06-24 **CVE-2020-10136**|  Unknown  
---|---  
  
#### Vendor Statement

We have not received a statement from the vendor.

###  ADTRAN Unknown

Notified: 2020-04-29  Updated: 2020-06-24 **CVE-2020-10136**|  Unknown  
---|---  
  
#### Vendor Statement

We have not received a statement from the vendor.

###  ANTlabs Unknown

Notified: 2020-04-29  Updated: 2020-06-24 **CVE-2020-10136**|  Unknown  
---|---  
  
#### Vendor Statement

We have not received a statement from the vendor.

###  ARRIS Unknown

Notified: 2020-04-29  Updated: 2020-06-24 **CVE-2020-10136**|  Unknown  
---|---  
  
#### Vendor Statement

We have not received a statement from the vendor.

###  ASUSTeK Computer Inc. Unknown

Notified: 2020-04-29  Updated: 2020-06-24 **CVE-2020-10136**|  Unknown  
---|---  
  
#### Vendor Statement

We have not received a statement from the vendor.

###  AVM GmbH Unknown

Notified: 2020-04-29  Updated: 2020-06-24 **CVE-2020-10136**|  Unknown  
---|---  
  
#### Vendor Statement

We have not received a statement from the vendor.

###  Actelis Networks Unknown

Notified: 2020-04-29  Updated: 2020-06-24 **CVE-2020-10136**|  Unknown  
---|---  
  
#### Vendor Statement

We have not received a statement from the vendor.

###  Actiontec Unknown

Notified: 2020-04-29  Updated: 2020-06-24 **CVE-2020-10136**|  Unknown  
---|---  
  
#### Vendor Statement

We have not received a statement from the vendor.

###  Advantech B-B Technology Unknown

Notified: 2020-04-08  Updated: 2020-06-24 **CVE-2020-10136**|  Unknown  
---|---  
  
#### Vendor Statement

We have not received a statement from the vendor.

###  AhnLab Inc Unknown

Notified: 2020-04-29  Updated: 2020-06-24 **CVE-2020-10136**|  Unknown  
---|---  
  
#### Vendor Statement

We have not received a statement from the vendor.

###  AirWatch Unknown

Notified: 2020-04-29  Updated: 2020-06-24 **CVE-2020-10136**|  Unknown  
---|---  
  
#### Vendor Statement

We have not received a statement from the vendor.

###  Akamai Technologies Inc. Unknown

Notified: 2020-04-29  Updated: 2020-06-24 **CVE-2020-10136**|  Unknown  
---|---  
  
#### Vendor Statement

We have not received a statement from the vendor.

###  Alcatel-Lucent Enterprise Unknown

Notified: 2020-04-29  Updated: 2020-06-24 **CVE-2020-10136**|  Unknown  
---|---  
  
#### Vendor Statement

We have not received a statement from the vendor.

###  Alpine Linux Unknown

Notified: 2020-04-29  Updated: 2020-06-24 **CVE-2020-10136**|  Unknown  
---|---  
  
#### Vendor Statement

We have not received a statement from the vendor.

###  Amazon Unknown

Notified: 2020-04-29  Updated: 2020-06-24 **CVE-2020-10136**|  Unknown  
---|---  
  
#### Vendor Statement

We have not received a statement from the vendor.

###  Android Open Source Project Unknown

Notified: 2020-04-29  Updated: 2020-06-24 **CVE-2020-10136**|  Unknown  
---|---  
  
#### Vendor Statement

We have not received a statement from the vendor.

###  Arch Linux Unknown

Notified: 2020-04-29  Updated: 2020-06-24 **CVE-2020-10136**|  Unknown  
---|---  
  
#### Vendor Statement

We have not received a statement from the vendor.

###  Aspera Inc. Unknown

Notified: 2020-04-29  Updated: 2020-06-24 **CVE-2020-10136**|  Unknown  
---|---  
  
#### Vendor Statement

We have not received a statement from the vendor.

###  Barracuda Networks Unknown

Notified: 2020-04-29  Updated: 2020-06-24 **CVE-2020-10136**|  Unknown  
---|---  
  
#### Vendor Statement

We have not received a statement from the vendor.

###  Bell Canada Enterprises Unknown

Notified: 2020-04-29  Updated: 2020-06-24 **CVE-2020-10136**|  Unknown  
---|---  
  
#### Vendor Statement

We have not received a statement from the vendor.

###  BlackBerry Unknown

Notified: 2020-04-29  Updated: 2020-06-24 **CVE-2020-10136**|  Unknown  
---|---  
  
#### Vendor Statement

We have not received a statement from the vendor.

###  BlueCat Networks Inc. Unknown

Notified: 2020-04-29  Updated: 2020-06-24 **CVE-2020-10136**|  Unknown  
---|---  
  
#### Vendor Statement

We have not received a statement from the vendor.

###  Blunk Microsystems Unknown

Notified: 2020-04-29  Updated: 2020-06-24 **CVE-2020-10136**|  Unknown  
---|---  
  
#### Vendor Statement

We have not received a statement from the vendor.

###  Brocade Communication Systems Unknown

Notified: 2020-04-29  Updated: 2020-06-24 **CVE-2020-10136**|  Unknown  
---|---  
  
#### Vendor Statement

We have not received a statement from the vendor.

###  Buffalo Technology Unknown

Notified: 2020-04-29  Updated: 2020-06-24 **CVE-2020-10136**|  Unknown  
---|---  
  
#### Vendor Statement

We have not received a statement from the vendor.

###  CA Technologies Unknown

Notified: 2020-04-29  Updated: 2020-06-24 **CVE-2020-10136**|  Unknown  
---|---  
  
#### Vendor Statement

We have not received a statement from the vendor.

###  CZ.NIC Unknown

Notified: 2020-04-29  Updated: 2020-06-24 **CVE-2020-10136**|  Unknown  
---|---  
  
#### Vendor Statement

We have not received a statement from the vendor.

###  Cambium Networks Unknown

Notified: 2020-04-29  Updated: 2020-06-24 **CVE-2020-10136**|  Unknown  
---|---  
  
#### Vendor Statement

We have not received a statement from the vendor.

###  Cirpack Unknown

Notified: 2020-04-29  Updated: 2020-06-24 **CVE-2020-10136**|  Unknown  
---|---  
  
#### Vendor Statement

We have not received a statement from the vendor.

###  Contiki OS Unknown

Notified: 2020-04-29  Updated: 2020-06-24 **CVE-2020-10136**|  Unknown  
---|---  
  
#### Vendor Statement

We have not received a statement from the vendor.

###  CoreOS Unknown

Notified: 2020-04-29  Updated: 2020-06-24 **CVE-2020-10136**|  Unknown  
---|---  
  
#### Vendor Statement

We have not received a statement from the vendor.

###  Cypress Semiconductor Unknown

Notified: 2020-04-29  Updated: 2020-06-24 **CVE-2020-10136**|  Unknown  
---|---  
  
#### Vendor Statement

We have not received a statement from the vendor.

###  D-Link Systems Inc. Unknown

Notified: 2020-04-29  Updated: 2020-06-24 **CVE-2020-10136**|  Unknown  
---|---  
  
#### Vendor Statement

We have not received a statement from the vendor.

###  Dell Unknown

Notified: 2020-04-29  Updated: 2020-06-24 **CVE-2020-10136**|  Unknown  
---|---  
  
#### Vendor Statement

We have not received a statement from the vendor.

###  Dell SecureWorks Unknown

Notified: 2020-04-29  Updated: 2020-06-24 **CVE-2020-10136**|  Unknown  
---|---  
  
#### Vendor Statement

We have not received a statement from the vendor.

###  DesktopBSD Unknown

Notified: 2020-04-29  Updated: 2020-06-24 **CVE-2020-10136**|  Unknown  
---|---  
  
#### Vendor Statement

We have not received a statement from the vendor.

###  Deutsche Telekom Unknown

Notified: 2020-04-29  Updated: 2020-06-24 **CVE-2020-10136**|  Unknown  
---|---  
  
#### Vendor Statement

We have not received a statement from the vendor.

###  DragonFly BSD Project Unknown

Notified: 2020-04-29  Updated: 2020-06-24 **CVE-2020-10136**|  Unknown  
---|---  
  
#### Vendor Statement

We have not received a statement from the vendor.

###  ENEA Unknown

Notified: 2020-04-29  Updated: 2020-06-24 **CVE-2020-10136**|  Unknown  
---|---  
  
#### Vendor Statement

We have not received a statement from the vendor.

###  EfficientIP Unknown

Notified: 2020-04-29  Updated: 2020-06-24 **CVE-2020-10136**|  Unknown  
---|---  
  
#### Vendor Statement

We have not received a statement from the vendor.

###  European Registry for Internet Domains Unknown

Notified: 2020-04-29  Updated: 2020-06-24 **CVE-2020-10136**|  Unknown  
---|---  
  
#### Vendor Statement

We have not received a statement from the vendor.

###  F-Secure Corporation Unknown

Notified: 2020-04-29  Updated: 2020-06-24 **CVE-2020-10136**|  Unknown  
---|---  
  
#### Vendor Statement

We have not received a statement from the vendor.

###  F5 Networks Inc. Unknown

Notified: 2020-04-29  Updated: 2020-06-24 **CVE-2020-10136**|  Unknown  
---|---  
  
#### Vendor Statement

We have not received a statement from the vendor.

###  Fedora Project Unknown

Notified: 2020-04-29  Updated: 2020-06-24 **CVE-2020-10136**|  Unknown  
---|---  
  
#### Vendor Statement

We have not received a statement from the vendor.

###  Foundry Brocade Unknown

Notified: 2020-04-29  Updated: 2020-06-24 **CVE-2020-10136**|  Unknown  
---|---  
  
#### Vendor Statement

We have not received a statement from the vendor.

###  GNU adns Unknown

Notified: 2020-04-29  Updated: 2020-06-24 **CVE-2020-10136**|  Unknown  
---|---  
  
#### Vendor Statement

We have not received a statement from the vendor.

###  Geexbox Unknown

Notified: 2020-04-29  Updated: 2020-06-24 **CVE-2020-10136**|  Unknown  
---|---  
  
#### Vendor Statement

We have not received a statement from the vendor.

###  Gentoo Linux Unknown

Notified: 2020-04-29  Updated: 2020-06-24 **CVE-2020-10136**|  Unknown  
---|---  
  
#### Vendor Statement

We have not received a statement from the vendor.

###  Google Unknown

Notified: 2020-04-29  Updated: 2020-06-24 **CVE-2020-10136**|  Unknown  
---|---  
  
#### Vendor Statement

We have not received a statement from the vendor.

###  Green Hills Software Unknown

Notified: 2020-04-29  Updated: 2020-06-24 **CVE-2020-10136**|  Unknown  
---|---  
  
#### Vendor Statement

We have not received a statement from the vendor.

###  HCC Unknown

Notified: 2020-04-29  Updated: 2020-06-24 **CVE-2020-10136**|  Unknown  
---|---  
  
#### Vendor Statement

We have not received a statement from the vendor.

###  HardenedBSD Unknown

Notified: 2020-04-29  Updated: 2020-06-24 **CVE-2020-10136**|  Unknown  
---|---  
  
#### Vendor Statement

We have not received a statement from the vendor.

###  Huawei Unknown

Notified: 2020-04-29  Updated: 2020-06-24 **CVE-2020-10136**|  Unknown  
---|---  
  
#### Vendor Statement

We have not received a statement from the vendor.

###  IBM Corporation (zseries) Unknown

Notified: 2020-04-29  Updated: 2020-06-24 **CVE-2020-10136**|  Unknown  
---|---  
  
#### Vendor Statement

We have not received a statement from the vendor.

###  Intel Unknown

Notified: 2020-04-29  Updated: 2020-06-24 **CVE-2020-10136**|  Unknown  
---|---  
  
#### Vendor Statement

We have not received a statement from the vendor.

###  Juniper Networks Unknown

Notified: 2020-04-28  Updated: 2020-06-24 **CVE-2020-10136**|  Unknown  
---|---  
  
#### Vendor Statement

We have not received a statement from the vendor.

###  LG Electronics Unknown

Notified: 2020-04-29  Updated: 2020-06-24 **CVE-2020-10136**|  Unknown  
---|---  
  
#### Vendor Statement

We have not received a statement from the vendor.

###  LITE-ON Technology Corporation Unknown

Notified: 2020-04-29  Updated: 2020-06-24 **CVE-2020-10136**|  Unknown  
---|---  
  
#### Vendor Statement

We have not received a statement from the vendor.

###  Lancope Unknown

Notified: 2020-04-29  Updated: 2020-06-24 **CVE-2020-10136**|  Unknown  
---|---  
  
#### Vendor Statement

We have not received a statement from the vendor.

###  Lantronix Unknown

Notified: 2020-04-29  Updated: 2020-06-24 **CVE-2020-10136**|  Unknown  
---|---  
  
#### Vendor Statement

We have not received a statement from the vendor.

###  LibreSSL Unknown

Notified: 2020-04-29  Updated: 2020-06-24 **CVE-2020-10136**|  Unknown  
---|---  
  
#### Vendor Statement

We have not received a statement from the vendor.

###  Linksys Unknown

Notified: 2020-04-29  Updated: 2020-06-24 **CVE-2020-10136**|  Unknown  
---|---  
  
#### Vendor Statement

We have not received a statement from the vendor.

###  LiteSpeed Technologies Unknown

Notified: 2020-04-29  Updated: 2020-06-24 **CVE-2020-10136**|  Unknown  
---|---  
  
#### Vendor Statement

We have not received a statement from the vendor.

###  Lynx Software Technologies Unknown

Notified: 2020-04-29  Updated: 2020-06-24 **CVE-2020-10136**|  Unknown  
---|---  
  
#### Vendor Statement

We have not received a statement from the vendor.

###  Maipu Communication Technology Unknown

Updated: 2020-06-24 **CVE-2020-10136**|  Unknown  
---|---  
  
#### Vendor Statement

We have not received a statement from the vendor.

###  Marvell Semiconductor Unknown

Notified: 2020-04-29  Updated: 2020-06-24 **CVE-2020-10136**|  Unknown  
---|---  
  
#### Vendor Statement

We have not received a statement from the vendor.

###  McAfee Unknown

Notified: 2020-04-29  Updated: 2020-06-24 **CVE-2020-10136**|  Unknown  
---|---  
  
#### Vendor Statement

We have not received a statement from the vendor.

###  McCain Inc Unknown

Updated: 2020-09-30 **CVE-2020-10136**|  Unknown  
---|---  
  
#### Vendor Statement

We have not received a statement from the vendor.

###  Men & Mice Unknown

Notified: 2020-04-29  Updated: 2020-06-24 **CVE-2020-10136**|  Unknown  
---|---  
  
#### Vendor Statement

We have not received a statement from the vendor.

###  Microchip Technology Unknown

Notified: 2020-04-29  Updated: 2020-06-24 **CVE-2020-10136**|  Unknown  
---|---  
  
#### Vendor Statement

We have not received a statement from the vendor.

###  Microsoft Unknown

Notified: 2020-04-29  Updated: 2020-06-24 **CVE-2020-10136**|  Unknown  
---|---  
  
#### Vendor Statement

We have not received a statement from the vendor.

###  Miredo Unknown

Notified: 2020-04-29  Updated: 2020-06-24 **CVE-2020-10136**|  Unknown  
---|---  
  
#### Vendor Statement

We have not received a statement from the vendor.

###  Mitel Networks Inc. Unknown

Notified: 2020-04-29  Updated: 2020-06-24 **CVE-2020-10136**|  Unknown  
---|---  
  
#### Vendor Statement

We have not received a statement from the vendor.

###  Muonics Inc. Unknown

Notified: 2020-04-29  Updated: 2020-06-24 **CVE-2020-10136**|  Unknown  
---|---  
  
#### Vendor Statement

We have not received a statement from the vendor.

###  NEC Corporation Unknown

Notified: 2020-04-29  Updated: 2020-06-24 **CVE-2020-10136**|  Unknown  
---|---  
  
#### Vendor Statement

We have not received a statement from the vendor.

###  NIKSUN Unknown

Notified: 2020-04-29  Updated: 2020-06-24 **CVE-2020-10136**|  Unknown  
---|---  
  
#### Vendor Statement

We have not received a statement from the vendor.

###  NLnet Labs Unknown

Notified: 2020-04-29  Updated: 2020-06-24 **CVE-2020-10136**|  Unknown  
---|---  
  
#### Vendor Statement

We have not received a statement from the vendor.

###  NetBSD Unknown

Notified: 2020-04-29  Updated: 2020-06-24 **CVE-2020-10136**|  Unknown  
---|---  
  
#### Vendor Statement

We have not received a statement from the vendor.

###  NetBurner Unknown

Notified: 2020-04-29  Updated: 2020-06-24 **CVE-2020-10136**|  Unknown  
---|---  
  
#### Vendor Statement

We have not received a statement from the vendor.

###  Nexenta Unknown

Notified: 2020-04-29  Updated: 2020-06-24 **CVE-2020-10136**|  Unknown  
---|---  
  
#### Vendor Statement

We have not received a statement from the vendor.

###  Nixu Unknown

Notified: 2020-04-29  Updated: 2020-06-24 **CVE-2020-10136**|  Unknown  
---|---  
  
#### Vendor Statement

We have not received a statement from the vendor.

###  Nokia Unknown

Notified: 2020-04-29  Updated: 2020-06-24 **CVE-2020-10136**|  Unknown  
---|---  
  
#### Vendor Statement

We have not received a statement from the vendor.

###  Nominum Unknown

Notified: 2020-04-29  Updated: 2020-06-24 **CVE-2020-10136**|  Unknown  
---|---  
  
#### Vendor Statement

We have not received a statement from the vendor.

###  OpenConnect Ltd Unknown

Notified: 2020-04-29  Updated: 2020-06-24 **CVE-2020-10136**|  Unknown  
---|---  
  
#### Vendor Statement

We have not received a statement from the vendor.

###  Openwall GNU/*/Linux Unknown

Notified: 2020-04-29  Updated: 2020-06-24 **CVE-2020-10136**|  Unknown  
---|---  
  
#### Vendor Statement

We have not received a statement from the vendor.

###  Oracle Corporation Unknown

Notified: 2020-04-29  Updated: 2020-06-24 **CVE-2020-10136**|  Unknown  
---|---  
  
#### Vendor Statement

We have not received a statement from the vendor.

###  Paessler Unknown

Notified: 2020-04-29  Updated: 2020-06-24 **CVE-2020-10136**|  Unknown  
---|---  
  
#### Vendor Statement

We have not received a statement from the vendor.

###  Palo Alto Networks Unknown

Notified: 2020-04-29  Updated: 2020-06-24 **CVE-2020-10136**|  Unknown  
---|---  
  
#### Vendor Statement

We have not received a statement from the vendor.

###  Philips Electronics Unknown

Notified: 2020-04-29  Updated: 2020-06-24 **CVE-2020-10136**|  Unknown  
---|---  
  
#### Vendor Statement

We have not received a statement from the vendor.

###  Proxim Inc. Unknown

Notified: 2020-04-29  Updated: 2020-06-24 **CVE-2020-10136**|  Unknown  
---|---  
  
#### Vendor Statement

We have not received a statement from the vendor.

###  QLogic Unknown

Notified: 2020-04-29  Updated: 2020-06-24 **CVE-2020-10136**|  Unknown  
---|---  
  
#### Vendor Statement

We have not received a statement from the vendor.

###  Qualcomm Unknown

Notified: 2020-04-29  Updated: 2020-06-24 **CVE-2020-10136**|  Unknown  
---|---  
  
#### Vendor Statement

We have not received a statement from the vendor.

###  Red Hat Unknown

Notified: 2020-04-29  Updated: 2020-06-24 **CVE-2020-10136**|  Unknown  
---|---  
  
#### Vendor Statement

We have not received a statement from the vendor.

###  Riverbed Technologies Unknown

Notified: 2020-04-29  Updated: 2020-06-24 **CVE-2020-10136**|  Unknown  
---|---  
  
#### Vendor Statement

We have not received a statement from the vendor.

###  Rocket RTOS (Inactive) Unknown

Notified: 2020-04-29  Updated: 2020-06-24 **CVE-2020-10136**|  Unknown  
---|---  
  
#### Vendor Statement

We have not received a statement from the vendor.

###  Ruckus Wireless Unknown

Notified: 2020-04-29  Updated: 2020-06-24 **CVE-2020-10136**|  Unknown  
---|---  
  
#### Vendor Statement

We have not received a statement from the vendor.

###  SMC Networks Inc. Unknown

Notified: 2020-04-29  Updated: 2020-06-24 **CVE-2020-10136**|  Unknown  
---|---  
  
#### Vendor Statement

We have not received a statement from the vendor.

###  SUSE Linux Unknown

Notified: 2020-04-29  Updated: 2020-06-24 **CVE-2020-10136**|  Unknown  
---|---  
  
#### Vendor Statement

We have not received a statement from the vendor.

###  Secure64 Software Corporation Unknown

Notified: 2020-04-29  Updated: 2020-06-24 **CVE-2020-10136**|  Unknown  
---|---  
  
#### Vendor Statement

We have not received a statement from the vendor.

###  SmoothWall Unknown

Notified: 2020-04-29  Updated: 2020-06-24 **CVE-2020-10136**|  Unknown  
---|---  
  
#### Vendor Statement

We have not received a statement from the vendor.

###  Snort Unknown

Notified: 2020-04-29  Updated: 2020-06-24 **CVE-2020-10136**|  Unknown  
---|---  
  
#### Vendor Statement

We have not received a statement from the vendor.

###  Sonos Unknown

Notified: 2020-04-29  Updated: 2020-06-24 **CVE-2020-10136**|  Unknown  
---|---  
  
#### Vendor Statement

We have not received a statement from the vendor.

###  Sony Unknown

Notified: 2020-04-29  Updated: 2020-06-24 **CVE-2020-10136**|  Unknown  
---|---  
  
#### Vendor Statement

We have not received a statement from the vendor.

###  Sophos Unknown

Notified: 2020-04-29  Updated: 2020-06-24 **CVE-2020-10136**|  Unknown  
---|---  
  
#### Vendor Statement

We have not received a statement from the vendor.

###  Symantec Unknown

Notified: 2020-04-29  Updated: 2020-06-24 **CVE-2020-10136**|  Unknown  
---|---  
  
#### Vendor Statement

We have not received a statement from the vendor.

###  TCPWave Unknown

Notified: 2020-04-29  Updated: 2020-06-24 **CVE-2020-10136**|  Unknown  
---|---  
  
#### Vendor Statement

We have not received a statement from the vendor.

###  Tenable Network Security Unknown

Notified: 2020-04-29  Updated: 2020-06-24 **CVE-2020-10136**|  Unknown  
---|---  
  
#### Vendor Statement

We have not received a statement from the vendor.

###  TippingPoint Technologies Inc. Unknown

Notified: 2020-04-29  Updated: 2020-06-24 **CVE-2020-10136**|  Unknown  
---|---  
  
#### Vendor Statement

We have not received a statement from the vendor.

###  Tizen Unknown

Notified: 2020-04-29  Updated: 2020-06-24 **CVE-2020-10136**|  Unknown  
---|---  
  
#### Vendor Statement

We have not received a statement from the vendor.

###  Turbolinux Unknown

Notified: 2020-04-29  Updated: 2020-06-24 **CVE-2020-10136**|  Unknown  
---|---  
  
#### Vendor Statement

We have not received a statement from the vendor.

###  Ubiquiti Networks Unknown

Notified: 2020-04-29  Updated: 2020-06-24 **CVE-2020-10136**|  Unknown  
---|---  
  
#### Vendor Statement

We have not received a statement from the vendor.

###  VMware Unknown

Notified: 2020-04-29  Updated: 2020-06-24 **CVE-2020-10136**|  Unknown  
---|---  
  
#### Vendor Statement

We have not received a statement from the vendor.

###  WizNET Technology Unknown

Notified: 2020-04-29  Updated: 2020-06-24 **CVE-2020-10136**|  Unknown  
---|---  
  
#### Vendor Statement

We have not received a statement from the vendor.

###  Xiaomi Unknown

Notified: 2020-04-29  Updated: 2020-06-24 **CVE-2020-10136**|  Unknown  
---|---  
  
#### Vendor Statement

We have not received a statement from the vendor.

###  Zebra Technologies Unknown

Notified: 2020-04-29  Updated: 2020-06-24 **CVE-2020-10136**|  Unknown  
---|---  
  
#### Vendor Statement

We have not received a statement from the vendor.

###  Zephyr Project Unknown

Notified: 2020-04-29  Updated: 2020-06-24 **CVE-2020-10136**|  Unknown  
---|---  
  
#### Vendor Statement

We have not received a statement from the vendor.

###  eero Unknown

Notified: 2020-04-29  Updated: 2020-06-24 **CVE-2020-10136**|  Unknown  
---|---  
  
#### Vendor Statement

We have not received a statement from the vendor.

###  lwIP Unknown

Notified: 2020-04-29  Updated: 2020-06-24 **CVE-2020-10136**|  Unknown  
---|---  
  
#### Vendor Statement

We have not received a statement from the vendor.

###  netsnmpj Unknown

Notified: 2020-04-29  Updated: 2020-06-24 **CVE-2020-10136**|  Unknown  
---|---  
  
#### Vendor Statement

We have not received a statement from the vendor.

###  wolfSSL Unknown

Notified: 2020-04-29  Updated: 2020-06-24 **CVE-2020-10136**|  Unknown  
---|---  
  
#### Vendor Statement

We have not received a statement from the vendor.

View all 132 vendors __View less vendors __

  

### References

  * <https://tools.ietf.org/html/rfc2003>
  * <https://tools.ietf.org/html/rfc6169>
  * <https://github.com/CERTCC/PoC-Exploits/tree/master/cve-2020-10136>

### Other Information

**CVE IDs:** |  [CVE-2020-10136 ](http://web.nvd.nist.gov/vuln/detail/CVE-2020-10136)  
---|---  
**Date Public:** | 2020-06-01  
**Date First Published:** | 2020-06-02  
**Date Last Updated:** | 2020-09-30 18:58 UTC  
**Document Revision:** | 14  
  
  * [About vulnerability notes](https://vuls.cert.org/confluence/display/VIN/Vulnerability+Note+Help)
  * [Contact us about this vulnerability](mailto:cert@cert.org?Subject=VU%23636397 Feedback)
  * [Provide a vendor statement](https://vuls.cert.org/confluence/display/VIN/Case+Handling#CaseHandling-Givingavendorstatusandstatement)

Sponsored by [CISA.](https://www.cisa.gov/cybersecurity)

[__Download PGP Key](https://vuls.cert.org/confluence/pages/viewpage.action?pageId=25985026)

[Read CERT/CC Blog](https://insights.sei.cmu.edu/cert/)

[Learn about Vulnerability Analysis](https://www.sei.cmu.edu/research-capabilities/all-work/display.cfm?customel_datapageid_4050=21304)

Carnegie Mellon University  
Software Engineering Institute  
4500 Fifth Avenue  
Pittsburgh, PA 15213-2612  
[412-268-5800](tel:+14122685800)  

  * [](https://www.facebook.com/SEICMU/)
  * [](https://twitter.com/sei_cmu)
  * [](https://www.linkedin.com/company/software-engineering-institute)
  * [](https://www.youtube.com/user/TheSEICMU)
  * [](https://itunes.apple.com/us/podcast/software-engineering-institute-sei-podcast-series/id566573552?mt=2)

[Office Locations](http://www.sei.cmu.edu/locations/index.cfm) | [Additional Sites Directory](http://www.sei.cmu.edu/additional-sites-directory/index.cfm) | [Legal](https://vuls.cert.org/confluence/display/VIN/VINCE+Code+of+Conduct#VINCECodeofConduct-TermsofUse) | [Privacy Notice ](https://www.sei.cmu.edu/legal/privacy-notice/index.cfm) | [CMU Ethics Hotline](https://www.cmu.edu/hr/ethics-hotline/) | [www.sei.cmu.edu](http://www.sei.cmu.edu)

©2022 Carnegie Mellon University

[Contact SEI](https://www.sei.cmu.edu/contact-us/)

#### Contact CERT/CC

__[412-268-5800](tel:+14122685800)  
__[ cert@cert.org](mailto:cert@cert.org)

---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2022-04-14_blinding-snort-breaking-the-modbus-ot-preprocessor.md
original_filename: 2022-04-14_blinding-snort-breaking-the-modbus-ot-preprocessor.md
title: 'Blinding Snort: Breaking The Modbus OT Preprocessor'
category: documents
detected_topics:
- sso
- access-control
- command-injection
- supply-chain
tags:
- imported
- documents
- sso
- access-control
- command-injection
- supply-chain
language: en
raw_sha256: 7962b9c8b94f0bd1ab0dd12503bb9d9fd5d773868dd20d74af2878555ff8da0e
text_sha256: cec69be635a7367bc4053aca5e8040594358f621772be39b5c853f6a5bd3226b
ingested_at: '2026-06-28T07:32:11Z'
sensitivity: unknown
redactions_applied: false
---

# Blinding Snort: Breaking The Modbus OT Preprocessor

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2022-04-14_blinding-snort-breaking-the-modbus-ot-preprocessor.md
- Source Type: markdown
- Detected Topics: sso, access-control, command-injection, supply-chain
- Ingested At: 2026-06-28T07:32:11Z
- Redactions Applied: False
- Raw SHA256: `7962b9c8b94f0bd1ab0dd12503bb9d9fd5d773868dd20d74af2878555ff8da0e`
- Text SHA256: `cec69be635a7367bc4053aca5e8040594358f621772be39b5c853f6a5bd3226b`


## Content

---
title: "Blinding Snort: Breaking The Modbus OT Preprocessor"
page_title: "Blinding Snort IDS/IPS: Breaking the Modbus OT Preprocessor | Claroty"
url: "https://claroty.com/2022/04/14/blog-research-blinding-snort-breaking-the-modbus-ot-preprocessor/"
final_url: "https://claroty.com/team82/research/blinding-snort-breaking-the-modbus-ot-preprocessor"
authors: ["Claroty's Team82 (@Claroty)"]
programs: ["Cisco"]
bugs: ["Memory corruption"]
publication_date: "2022-04-14"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 2713
---

[ ![Team82 Logo](https://claroty.com/build/assets/team82-logo-white-BGiCQ9zb.svg) ](/team82)

  * [Research](/team82/research)
  * [Vulnerability Dashboard](/team82/disclosure-dashboard)
  * [Talks](/team82/talks)
  * [Tools](/team82/#tools)
  * [About](/team82/#about)

[ ![Claroty](https://claroty.com/build/assets/logo-solid-white-DcRiqKcD.svg) ](/)

[ Return to Team82 Research ](/team82/research)

# Blinding Snort IDS/IPS: Breaking the Modbus OT Preprocessor

Uri Katz 

/ April 14th, 2022

![Simple Snort Network Topology](/img/asset/YXNzZXRzL2ltcG9ydGVkLWltYWdlcy9lZTEyM2IxYTVmODNmNmU4YzAyMTlhYmE1ZjhiZjE2Ny1DbGFyb3R5LVNub3J0LUJsb2ctRGlhZ3JhbS0xLnBuZw/ee123b1a5f83f6e8c0219aba5f8bf167-Claroty-Snort-Blog-Diagram-1.png?fm=webp&fit=crop&w=800&h=450&s=cc6103a356e6f988fe76211ac70822f4)

## Executive Summary

  * Team82 discovered a means by which it could blind the popular Snort intrusion detection and prevention system to malicious packets.

  * The vulnerability, [CVE-2022-20685](https://claroty.com/team82/disclosure-dashboard/cve-2022-20685), is an integer-overflow issue that can cause the Snort Modbus OT preprocessor to enter an infinite while-loop.

  * A successful exploit keeps Snort IDS/IPS from processing new packets and generating alerts.

  * The vulnerability, which can be attacked remotely, has been patched by Cisco and the Snort team.

  * All open source Snort project releases earlier than 2.9.19 and release 3.1.11.0 are vulnerable.

  * Read [Cisco's advisory here](https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-snort-dos-9D3hJLuj) for commercial product patching and mitigation information.

### Table of Contents

  * Snort Rules and Alerts

  * Modbus

  * CVE-2022-20685: Technical Details

  * Vulnerability and Exploitability

  * Conclusion

  * 

## What is the Snort Network Intrusion Detection System?

Network analysis tools are integral to keeping networks secure by providing real-time logging and analysis of events and traffic. Snort is atop this list of analysis tools as the most popular network intrusion detection and prevention system. The open-source version of the Snort IDS/IPS still has an active community of contributors and developers, while Cisco has developed commercial versions of Snort since acquiring parent company Sourcefire in 2013.

Snort is largely used passively on the network, but it can also take action on malicious packets, making it a powerful detection tool for defenders. An attacker who could blind this tool to malicious traffic, however, could gain an important advantage over network defenders.

![Simple Snort Network Topology](/img/asset/YXNzZXRzL2ltcG9ydGVkLWltYWdlcy9lZTEyM2IxYTVmODNmNmU4YzAyMTlhYmE1ZjhiZjE2Ny1DbGFyb3R5LVNub3J0LUJsb2ctRGlhZ3JhbS0xLnBuZw/ee123b1a5f83f6e8c0219aba5f8bf167-Claroty-Snort-Blog-Diagram-1.png?fm=webp&fit=crop&s=f0c9593fa19af2eca05f5379d24b16d6)

In this report, Team82 will demonstrate how it was able to do just that through a vulnerability, ([CVE-2022-20685](https://claroty.com/team82/disclosure-dashboard/cve-2022-20685)) we uncovered in Snort's Modbus OT preprocessor. Exploiting this vulnerability allowed us to blind Snort's ability to detect further attacks and run malicious packets on the network.

![Simple Snort Network](/img/asset/YXNzZXRzL2ltcG9ydGVkLWltYWdlcy82YzFkNTQxOGVjMGI2ZmMyOGNhOWYzZjZhNjBkNGU5ZS1DbGFyb3R5LVNub3J0LUJsb2ctRGlhZ3JhbS0yLnBuZw/6c1d5418ec0b6fc28ca9f3f6a60d4e9e-Claroty-Snort-Blog-Diagram-2.png?fm=webp&fit=crop&s=b7194dd81ca9bf86df908ea3407dfcbd)

## Snort Rules and Alerts

Snort's open-source network-based intrusion detection/prevention system (IDS/IPS) has the ability to perform real-time traffic analysis and packet logging on internet protocol (IP) networks. Snort IDS/IPS performs protocol analysis, content searching, and matching based on a predefined rule set. Snort rules can be based on raw data or on Snort's built-in protocol parsers.

Rules may trigger one of three actions:

  * Alert rules: Generate an alert

  * Log rules: Alert and log the alert

  * Pass rules: Ignore the packet

To make the rule-writing process simpler and improve the detection capabilities, Snort comes with a set of preprocessors that are on by default and analyze and structure network traffic into objects that can be referenced later in Snort rules. Some of the preprocessors included in Snort are: ARP, DNS, SSH and some OT (operational technology) protocols, such as [MODBUS](https://www.snort.org/faq/readme-modbus) / [DNP3](https://www.snort.org/faq/readme-dnp3).

![Modbus Preprocessor configuration](/img/asset/YXNzZXRzL2ltcG9ydGVkLWltYWdlcy84Y2E5NWZkZGE2ZTg2ZDhmNGFjNjI4YTMyYzAwNTQ1My1TY3JlZW4tU2hvdC0yMDIyLTA0LTEzLWF0LTUuMzkuMDEtUE0ucG5n/8ca95fdda6e86d8f4ac628a32c005453-Screen-Shot-2022-04-13-at-5.39.01-PM.png?fm=webp&fit=crop&s=c1949f965dff3830cf805423f6909403) Snort's default configuration (snort.conf).

When writing Snort rules, one can easily use these objects—for example to check the Modbus function ID the modbus.func_id attribute can be used, instead of checking offset of the sixth byte in the packet. Here is an example for a snort rule that use modbus preprocessor attributes:

![Protocol Scada Mobus](/img/asset/YXNzZXRzL2ltcG9ydGVkLWltYWdlcy85NzViYWNkZTQ5MWJlNGRlY2VhOTI5YWNlZWM2YjQxMS1TY3JlZW4tU2hvdC0yMDIyLTA0LTEzLWF0LTUuMzkuMTQtUE0ucG5n/975bacde491be4decea929aceec6b411-Screen-Shot-2022-04-13-at-5.39.14-PM.png?fm=webp&fit=crop&s=80e8e8f8e3e8fd7420de79f016062045)

## Snort Modbus OT Preprocessor

Modbus is an industrial protocol developed in 1979, first intended to transfer data over a serial line. Later it was expanded to include TCP/UDP support. The main Modbus function codes are:

![Mobus Function Codes](/img/asset/YXNzZXRzL2ltcG9ydGVkLWltYWdlcy8yNDdiNDUzZGY2YTk5NzBlZjE5NjMxZDNhYTE5YjMxNi1TY3JlZW4tU2hvdC0yMDIyLTA0LTEzLWF0LTUuMzkuMjQtUE0ucG5n/247b453df6a9970ef19631d3aa19b316-Screen-Shot-2022-04-13-at-5.39.24-PM.png?fm=webp&fit=crop&s=4311b2e84377f0aec5cf65f171e2638b)

## CVE-2022-20685: Technical Details

While researching Snort OT preprocessors, we decided to focus on Modbus because it was one of the more complex OT preprocessors Snort supports. To understand what we found, we first need to examine the structure of the Modbus Write File Record function code.

### Write File Record (command 0x15)

The Write File Record Modbus command writes multiple groups of file registers to the Modbus server. A file is an organization of records. Each file may contain up to 10,000 records, addressed 0000 to 9999 decimal or 0x0000 to 0x270F.

The Write File Record Modbus command allows writing multiple groups of references. Each group is defined in a separate sub-request field that contains 7 bytes plus the data:

  * **Reference type** : 1 byte (must be specified as 6)

  * **File number** : 2 bytes

  * **Starting record number within file** : 2 bytes

  * **Length of record to be written** : 2 bytes

  * **Data to be written** : 2 bytes of data per register

The number of registers to be written, combined with all other fields in the request, must not exceed the allowable length of the Modbus protocol data unit (PDU), which is 253 bytes.

Here is a summary of the Write File Record Modbus command request:

![Snort Blog Table](/img/asset/YXNzZXRzL2ltcG9ydGVkLWltYWdlcy9lMmMxOGU0YmM4YTA0MmVkZmI4OWUxNzcwNGY0ZTY5MS1DbGFyb3R5LVNub3J0LUJsb2ctVGFibGUucG5n/e2c18e4bc8a042edfb89e17704f4e691-Claroty-Snort-Blog-Table.png?fm=webp&fit=crop&s=2123d3ce5b6354d0d4c71617f89a9c6a)

## Vulnerability and Exploitability

The Modbus preprocessor handles multiple Modbus function codes. Snort IDS/IPS uses the ModbusCheckRequestLengths function to calculate the expected size for each packet.

If we look at the function ModbusCheckRequestLengths in the file modbus_decode.c, we see a while-loop that goes over all of the groups in the packet, in order to calculate the total record lengths.

![Function Modbus Check Request Lengths](/img/asset/YXNzZXRzL2ltcG9ydGVkLWltYWdlcy82YTdkMWNmZjk1ZTA4Mjg4ZDYzZWMwNDlkZDEwMGE4OC1TY3JlZW4tU2hvdC0yMDIyLTA0LTEzLWF0LTUuMzkuMzUtUE0ucG5n/6a7d1cff95e08288d63ec049dd100a88-Screen-Shot-2022-04-13-at-5.39.35-PM.png?fm=webp&fit=crop&s=c8bb2d55db2238241c3df364a72d2df0) Function ModbusCheckRequestLengths in file modbus_decode.c

## 3 Steps to Exploiting Modbus

### Step 1

The tmp_count parameter is initialized using a value from the packet->payload and represents the number of bytes remaining in the payload, according to the payload_length parameter. After tmp_count is set, we enter a while-loop with the exit condition of bytes_processed < tmp_count. Therefore, so far tmp_count = 10, which is constant and won't change during the loop. As long as bytes_processed remains less than 10, the while-loop will continue looping.

To do so, let's look at the content of the while-loop. We see that bytes_processed is affected by the record_length parameter, which consists of two bytes from the Modbus payload (Group → Record Length).

![Function Modbus Check Request Lengths](/img/asset/YXNzZXRzL2ltcG9ydGVkLWltYWdlcy8xMzllYzJiYTYyZjY5YWUzMjE5OTM5ZTJlYmVmMjBlOC1TY3JlZW4tU2hvdC0yMDIyLTA0LTEzLWF0LTUuMzkuNDktUE0ucG5n/139ec2ba62f69ae3219939e2ebef20e8-Screen-Shot-2022-04-13-at-5.39.49-PM.png?fm=webp&fit=crop&s=5584bc1dc30ce4c1525163f0ad72d486) Function ModbusCheckRequestLengths in file modbus_decode.c

### Step 2

The record_length parameter is of type uint16_t, with a value from the user-controlled Modbus payload. bytes_processed is also uint16_t, and is calculated by multiplying record_length by 2 + the sub-request header size, which is 7.

However, the result of the multiplication can be more than the maximum uint16_t size, thus overflowing the value.

For example:

  * **record_length** = 0xfffe

  * **MODBUS_FILE_RECORD_SUB_REQUEST_SIZE** = 7

  * **bytes_processed** = 7 + (2 * 0xfffe)

In this example, the bytes_processed will be 0x20003, which is:

0000000000000010|0000000000000011

**High Low**

In binary, when the result is cast to uint_16t, the lower 16 bits are kept, meaning the bytes_processed will be 0000000000000011, which equals 3. If the bytes_processed is 3, we do not exit the while-loop, because 3 (bytes_processed) < 10 (tmp_count), and we enter another iteration.

### Step 3

Now, the new record_length will be taken from the user-controlled payload, from a specific offset that is partially affected by the bytes_processed value. Since we fully control the value of the bytes_processed using the integer-overflow bug, we can craft the payload in such a way that the newly calculated record_length will be any number we choose.

Therefore, if the next value that is read into the record_length (allegedly the next group's record length) is 0xfffb, then the bytes_processed will be calculated as follows:

bytes_processed = bytes_processed + MODBUS_FILE_RECORD_SUB_REQUEST_SIZE + 2*record_length

bytes_processed = 3 + 7 + 2*(0xfffb) = 0

So, the bytes_processed is now 0.The next time we enter the while-loop, the bytes_processed is 0 again, so we will go through steps 2 and 3 over and over, until the process is terminated by the user. This essentially keeps the process stuck in the while-loop (steps 2 & 3) "blinding" it forever. In this state, Snort will not process new packets and will not alert.

![Modbus File Record](https://web-assets.claroty.com/imported-images/d386f1c2065071f1f4e7d90e637d50c5-Claroty-Snort-Blog.gif)

## Conclusion

Successful exploits of vulnerabilities in network analysis tools such as Snort IDS/IPS can have devastating impacts on enterprise and OT networks.

[CVE-2022-20685](https://claroty.com/team82/disclosure-dashboard/cve-2022-20685), uncovered by Team82, targeted just one facet of this popular network intrusion detection and prevention system. It can be exploited remotely to create a denial-of-service condition in Snort, keeping it from processing new packets, and generating alerts.

Team82 believes network analysis tools are an under-researched area that deserves more analysis and attention, especially as OT networks are increasingly being centrally managed by IT network analysis familiar with Snort and other similar tools.

[CVE-2022-20685](https://claroty.com/team82/disclosure-dashboard/cve-2022-20685)

**CWE-190** : Integer Overflow or Wraparound

**CVSSv3 score:** 7.5

**Description:** An integer overflow vulnerability in the Snort Modbus OT preprocessor enables an attacker to remotely send a crafted packet to a vulnerable system, triggering an infinite while-loop and creating a denial-of-service condition.

Share

[ __ LinkedIn ](https://www.linkedin.com/shareArticle/?url=https://claroty.com/team82/research/blinding-snort-breaking-the-modbus-ot-preprocessor) [ __ Twitter ](https://twitter.com/intent/post?text=Blinding Snort IDS/IPS: Breaking the Modbus OT Preprocessor&url=https://claroty.com/team82/research/blinding-snort-breaking-the-modbus-ot-preprocessor) [ __ Facebook ](https://www.facebook.com/sharer/sharer.php?u=https://claroty.com/team82/research/blinding-snort-breaking-the-modbus-ot-preprocessor) [ __ ](mailto:?subject=Blinding Snort IDS/IPS: Breaking the Modbus OT Preprocessor&body=https://claroty.com/team82/research/blinding-snort-breaking-the-modbus-ot-preprocessor)

![](https://claroty.com/build/assets/team82-newsletter-bg-BlXIsUMi.jpg)

Stay in the know Get the Team82 Newsletter

Share

[ __ LinkedIn ](https://www.linkedin.com/shareArticle/?url=https://claroty.com/team82/research/blinding-snort-breaking-the-modbus-ot-preprocessor) [ __ Twitter ](https://twitter.com/intent/post?text=Blinding Snort IDS/IPS: Breaking the Modbus OT Preprocessor&url=https://claroty.com/team82/research/blinding-snort-breaking-the-modbus-ot-preprocessor) [ __ Facebook ](https://www.facebook.com/sharer/sharer.php?u=https://claroty.com/team82/research/blinding-snort-breaking-the-modbus-ot-preprocessor) [ __ ](mailto:?subject=Blinding Snort IDS/IPS: Breaking the Modbus OT Preprocessor&body=https://claroty.com/team82/research/blinding-snort-breaking-the-modbus-ot-preprocessor)

Recent Vulnerability Disclosures

  * ##### [CVE-2026-28256 A Use of Hard-coded, Security-relevant Constants vulnerability in Trane Tracer SC, Tracer SC+, and Tracer Concierge could allow an attacker to disclose sensitive information and take over accounts. Successful exploitation of these vulnerabilities could allow an attacker to disclose sensitive information, execute arbitrary commands, or perform a denial-of-service on the product. The following versions of Trane Tracer SC, Tracer SC+, and Tracer Concierge are affected:
  * Tracer SC
  * Tracer SC+
  * Tracer Concierge
Trane asks Tracer SC+ users to upgrade to version v6.30.2313 CVSS v3: 5.8 ](/team82/disclosure-dashboard/cve-2026-28256)
  * ##### [CVE-2026-28255 A Use of Hard-coded Credentials vulnerability in Trane Tracer SC, Tracer SC+, and Tracer Concierge could allow an attacker to disclose sensitive information and take over accounts. Successful exploitation of these vulnerabilities could allow an attacker to disclose sensitive information, execute arbitrary commands, or perform a denial-of-service on the product. The following versions of Trane Tracer SC, Tracer SC+, and Tracer Concierge are affected:
  * Tracer SC
  * Tracer SC+
  * Tracer Concierge
Trane asks Tracer SC+ users to upgrade to version v6.30.2313 CVSS v3: 6.8 ](/team82/disclosure-dashboard/cve-2026-28255)
  * ##### [CVE-2026-28254 A Missing Authorization vulnerability in Trane Tracer SC, Tracer SC+, and Tracer Concierge could allow an unauthenticated attacker to access sensitive information through unprotected APIs. Successful exploitation of these vulnerabilities could allow an attacker to disclose sensitive information, execute arbitrary commands, or perform a denial-of-service on the product. The following versions of Trane Tracer SC, Tracer SC+, and Tracer Concierge are affected:
  * Tracer SC
  * Tracer SC+
  * Tracer Concierge
Trane asks Tracer SC+ users to upgrade to version v6.30.2313 CVSS v3: 5.8 ](/team82/disclosure-dashboard/cve-2026-28254)
  * ##### [CVE-2026-28253 A Memory Allocation with Excessive Size Value vulnerability in Trane Tracer SC, Tracer SC+, and Tracer Concierge could allow an unauthenticated attacker to cause a denial-of-service condition. Successful exploitation of these vulnerabilities could allow an attacker to disclose sensitive information, execute arbitrary commands, or perform a denial-of-service on the product. The following versions of Trane Tracer SC, Tracer SC+, and Tracer Concierge are affected:
  * Tracer SC
  * Tracer SC+
  * Tracer Concierge
Trane asks Tracer SC+ users to upgrade to version v6.30.2313 CVSS v3: 7.5 ](/team82/disclosure-dashboard/cve-2026-28253)
  * ##### [CVE-2026-28252 A Use of a Broken or Risky Cryptographic Algorithm vulnerability in Trane Tracer SC, Tracer SC+, and Tracer Concierge could allow an attacker to bypass authentication and gain root-level access to the device. Successful exploitation of these vulnerabilities could allow an attacker to disclose sensitive information, execute arbitrary commands, or perform a denial-of-service on the product. The following versions of Trane Tracer SC, Tracer SC+, and Tracer Concierge are affected:
  * Tracer SC
  * Tracer SC+
  * Tracer Concierge
Trane asks Tracer SC+ users to upgrade to version v6.30.2313 CVSS v3: 8.1 ](/team82/disclosure-dashboard/cve-2026-28252)

Solutions

  * [Claroty xDome Platform](/platform)
  * [Industrial Cybersecurity](/industrial-cybersecurity)
  * [Healthcare Cybersecurity](/healthcare-cybersecurity)
  * [Commercial Cybersecurity](/commercial-cybersecurity)
  * [Public Sector Cybersecurity](/public-sector-cybersecurity)

Threat Research

  * [Team82 Home](/team82)
  * [Vulnerability Disclosure Dashboard](/team82/disclosure-dashboard)
  * [Research](/team82/research)
  * [PGP Key](/team82/pgp-key)

Partners

  * [Partners](/partners)
  * [Technology Alliance Partners](/partners/technology-alliances)
  * [Channel Partners](/partners/channel-partners)
  * [Become a Partner](https://portal.claroty.com/#/page/partner-reg)
  * [Partner Login](https://portal.claroty.com/#/page/login)

Resources

  * [Resource Library](/resources)
  * [Blog](/blog)
  * [White Papers](/resources/white-papers)
  * [Reports](/resources/reports)
  * [Case Studies](/resources/case-studies)
  * [Datasheets](/resources/datasheets)
  * [Integration Briefs](/resources/integration-briefs)
  * [Videos](https://www.youtube.com/@claroty20)
  * [Claroty Nexus](https://nexusconnect.io)

Company

  * [About Us](/company)
  * [Careers](/careers)
  * [Leadership](/leadership)
  * [Newsroom](/newsroom)
  * [xCel Enablement & Training](/xcel-enablement-and-training)
  * [Trust Center](/trust)
  * [Customer Experience](/customer-experience)
  * [Events](/event-listing)
  * [Environmental, Social, and Governance Policies](/environmental-social-and-governance-policies)
  * [Contact Us](/contact-us)

[ ![Claroty](https://claroty.com/build/assets/logo-white-VeF9EwMy.svg) ](/)

© 2026 Claroty. All rights reserved.

[ __ LinkedIn ](https://www.linkedin.com/company/claroty/) [ __ Twitter ](https://twitter.com/claroty) [ __ YouTube ](https://www.youtube.com/@claroty20) [ __ Facebook ](https://www.facebook.com/ClarotyOT/)

[Terms & Conditions](/terms-conditions) / [Privacy Policy](/privacy-policy)

![Claroty](https://claroty.com/build/assets/logo-white-VeF9EwMy.svg) __ Close Menu

  * [Platform](/platform) __

[The Claroty Platform](/platform) [Claroty CPS Protection Program](/cps-protection-program) [Claire, the AI Security Agent](/claire) [Asset Inventory](/platform/asset-inventory) [Exposure Management](/platform/exposure-management) [Network Protection](/platform/network-protection) [Secure Access](/platform/secure-access) [Threat Detection](/platform/threat-detection) [Operational Efficiency](/platform/operational-efficiency) [Integrations](/platform/integrations)

  * [Industries]() __

[Industrial Home](/industrial-cybersecurity) [Industrial Verticals](/industrial-cybersecurity/verticals) [Healthcare Home](/healthcare-cybersecurity) [Commercial Home](/commercial-cybersecurity) [Commercial Verticals](/commercial-cybersecurity/verticals)

  * [Public Sector](/public-sector-cybersecurity) __

[Public Sector Home](/public-sector-cybersecurity) [Federal Government Home](/public-sector-cybersecurity/us-government-cybersecurity) [SLED Home](/public-sector-cybersecurity/sled-government-cybersecurity)

  * [Customers](/customer-experience) __

[Customer Experience](/customer-experience) [Case Studies](/resources/case-studies) [xCel Enablement & Training for Customers](/xcel-enablement-and-training-for-customers)

  * [Partners](/partners) __

[Partners](/partners) [Technology Alliance Partners](/partners/technology-alliances) [Channel Partners](/partners/channel-partners) [Partner Login](https://portal.claroty.com/#/page/login)

  * [Threat Research](/team82) __

[Team82 Home](/team82) [Threat Intelligence](/threat-intelligence) [Vulnerability Disclosure Dashboard](/team82/disclosure-dashboard) [Research](/team82/research) [Talks](/team82/talks) [PGP Key](/team82/pgp-key)

  * [Resources](/resources) __

[Blog](/blog) [Reports](/resources/reports) [White Papers](/resources/white-papers) [Datasheets & Solution Overviews](/resources/datasheets) [Integration Briefs](/resources/integration-briefs) [Case Studies](/resources/case-studies) [On-Demand Webinars](/resources/webinars) [Visit our Nexus Website](https://nexusconnect.io)

  * [Company](/company) __

[About Us](/company) [Careers](/careers) [Leadership](/leadership) [Newsroom](/newsroom) [xCel Enablement & Training](/xcel-enablement-and-training) [Trust Center](/trust) [Events](/event-listing) [Environmental, Social, and Governance Policies](/environmental-social-and-governance-policies) [Contact Us](/contact-us)

  * [__Search](/search)

[ __ LinkedIn ](https://www.linkedin.com/company/claroty/) [ __ Twitter ](https://twitter.com/claroty) [ __ YouTube ](https://www.youtube.com/@claroty20) [ __ Facebook ](https://www.facebook.com/ClarotyOT/)

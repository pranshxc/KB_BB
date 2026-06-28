---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2020-06-16_bug-bounty-bout-report-0x01-webrtc-edition.md
original_filename: 2020-06-16_bug-bounty-bout-report-0x01-webrtc-edition.md
title: Bug bounty bout report 0x01 - WebRTC edition
category: documents
detected_topics:
- access-control
- ssrf
- command-injection
tags:
- imported
- documents
- access-control
- ssrf
- command-injection
language: en
raw_sha256: 42638e5de7c5b0ebb1e9a8098d3a769520053ad5e17b3bbb7b59a3fbd05dba61
text_sha256: 637bf56af2c072b24ef2d36f8d6f697c9da4c62b19e98d33a6bdf65ba275fcb9
ingested_at: '2026-06-28T07:32:02Z'
sensitivity: unknown
redactions_applied: false
---

# Bug bounty bout report 0x01 - WebRTC edition

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2020-06-16_bug-bounty-bout-report-0x01-webrtc-edition.md
- Source Type: markdown
- Detected Topics: access-control, ssrf, command-injection
- Ingested At: 2026-06-28T07:32:02Z
- Redactions Applied: False
- Raw SHA256: `42638e5de7c5b0ebb1e9a8098d3a769520053ad5e17b3bbb7b59a3fbd05dba61`
- Text SHA256: `637bf56af2c072b24ef2d36f8d6f697c9da4c62b19e98d33a6bdf65ba275fcb9`


## Content

---
title: "Bug bounty bout report 0x01 - WebRTC edition"
page_title: "Bug bounty bout report 0x01 - WebRTC edition – Enable Security"
url: "https://www.rtcsec.com/post/2020/06/03-bug-bounty-bout-0x01-webrtc-edition/"
final_url: "https://www.enablesecurity.com/blog/bug-bounty-bout-0x01-webrtc-edition/"
authors: ["Enable Security (@enablesecurity)"]
bugs: ["WebRTC", "TURN", "Outdated component with a known vulnerability", "DoS", "RCE", "Default credentials", "SSRF"]
publication_date: "2020-06-16"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 4489
---

# Bug bounty bout report 0x01 - WebRTC edition

Published on Jun 16, 2020 in _[webrtc security](/tags/webrtc-security/)_ , _[bug bounty](/tags/bug-bounty/)_ , _[TURN security](/tags/turn-security/)_

Read the [full report here](https://github.com/EnableSecurity/reports/blob/master/bug-bounty-bout-0x01/technicalreport.pdf).

In April 2020, in between [SIPVicious PRO development](https://sipvicious.pro) and [VoIP Pentesting](https://www.enablesecurity.com/voip-penetration-testing/) and [WebRTC](https://www.enablesecurity.com/penetration-testing/), we dedicated some days to bug bounties and vulnerability disclosure programs to see what comes out of it. Our focus was on those that have WebRTC infrastructure in scope. In the end, we reported 3 vulnerabilities to 4 different vendors, for 6 different products. So finally, after making sure that the affected vendors have addressed these security issues and have agreed with publication, we are putting out a [compiled report](https://github.com/EnableSecurity/reports/blob/master/bug-bounty-bout-0x01/technicalreport.pdf)!

[![Bug bounty bout 0x01 report](enablesecurity-report.png#center)](https://github.com/EnableSecurity/reports/blob/master/bug-bounty-bout-0x01/technicalreport.pdf)

Each finding gives background information about the actual vulnerability, assessing its impact and instructions on how to reproduce the vulnerability. Additionally, we included our recommendations on how the vulnerability could be addressed and a timeline showing our bug reporting and re-testing process. The report structure is based on our normal pentest reports and so it includes additional sections found in our template.

The vulnerabilities that we reported were the following:

  * Open TURN relay abuse affects multiple vendors and products due to lack of peer access control
  * Outdated Coturn is vulnerable to known security issues
  * Default XMPP administrative accounts leading to DoS and potentially, spying on video calls, RCE

Some of the individual reports have been made public or mentioned at the following locations:

  * [Hackerone: 8x8 Open TURN relay abuse](https://hackerone.com/reports/843256)
  * [Hackerone: 8x8 Outdated Coturn known vulnerabilities](https://hackerone.com/reports/843263)
  * [Simwood blog: Jitsi Meet on Docker](https://blog.simwood.com/2020/04/jitsi-meet-on-docker/)

The conclusion from the compiled report sums it up:

> A number of tests were done on the target WebRTC infrastructures that were in our scope. Almost each vendor in scope had their own custom infrastructure and applications, therefore requiring dedicated research while taking a targeted approach. During the time allocated for this bounty bout, we realized that such effort was better spent focusing on known vulnerabilities. The TURN open relay vulnerability was, in fact, found to be wide spread enough to affect 3 of the vendors in our scope. This is possibly due the common requirement of having a TURN server for various types of WebRTC deployments. In the case of the Jitsi Meet for Docker default password, only one vendor was found to be vulnerable but we suspect that outside the scope of bug bounties and vulnerability disclosure programs, various other vendors may be affected.

> Enable Security would like to thank all the bug bounty programs and vendors involved for their positive reception and for handling our reports in a professional and timely manner. In this report, the open TURN relay finding is stated as one generic finding since two of the affected vendors asked us to redact or anonymize the information. The outdated coTURN finding was also redacted as requested by the affected vendor.

> We would like to especially thank Simwood for their open approach, allowing us to fully disclose the report that we provided to them, while quickly addressing the security issues and keeping us updated all throughout.

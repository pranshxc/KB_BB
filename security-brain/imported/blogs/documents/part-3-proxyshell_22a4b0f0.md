---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2021-08-18_part-3-proxyshell.md
original_filename: 2021-08-18_part-3-proxyshell.md
title: Part 3 - ProxyShell!
category: documents
detected_topics:
- access-control
- command-injection
- api-security
tags:
- imported
- documents
- access-control
- command-injection
- api-security
language: en
raw_sha256: 22a4b0f0e6a22f382494deda562f5ec1783e3f46912e0ca6b21082764de0e912
text_sha256: 1486edbf55d4af81d6f6e60602ab04592bcaa0b2a4c173c6a48033af208b0b6c
ingested_at: '2026-06-28T07:32:07Z'
sensitivity: unknown
redactions_applied: false
---

# Part 3 - ProxyShell!

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2021-08-18_part-3-proxyshell.md
- Source Type: markdown
- Detected Topics: access-control, command-injection, api-security
- Ingested At: 2026-06-28T07:32:07Z
- Redactions Applied: False
- Raw SHA256: `22a4b0f0e6a22f382494deda562f5ec1783e3f46912e0ca6b21082764de0e912`
- Text SHA256: `1486edbf55d4af81d6f6e60602ab04592bcaa0b2a4c173c6a48033af208b0b6c`


## Content

---
title: "Part 3 - ProxyShell!"
page_title: "A New Attack Surface on MS Exchange Part 3 - ProxyShell! | DEVCORE"
url: "https://devco.re/blog/2021/08/22/a-new-attack-surface-on-MS-exchange-part-3-ProxyShell/"
final_url: "https://devco.re/blog/2021/08/22/a-new-attack-surface-on-MS-exchange-part-3-ProxyShell/"
authors: ["Orange Tsai (@orange_8361)"]
programs: ["Microsoft"]
bugs: ["RCE", "Privilege escalation"]
bounty: "200,000"
publication_date: "2021-08-18"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 3409
---

[Tech Editorials](/en/blog/category/Tech Editorials) [#Advisory](/en/blog/tag/Advisory/) [#CVE](/en/blog/tag/CVE/) [#RCE](/en/blog/tag/RCE/) [#Exchange](/en/blog/tag/Exchange/) [#Pwn2Own](/en/blog/tag/Pwn2Own/)

#  A New Attack Surface on MS Exchange Part 3 - ProxyShell! 

[ __ ](/en/blog/author/orange) [Orange Tsai](/en/blog/author/orange) 2021-08-22

![](https://devco.re/assets/img/blog/20210822/cover.png)

* * *

This is a guest post DEVCORE collaborated with Zero Day Initiative (ZDI) and published at their blog, which describes the exploit chain we demonstrated at Pwn2Own 2021! Please visit the following link to read that :)

  * [FROM PWN2OWN 2021: A NEW ATTACK SURFACE ON MICROSOFT EXCHANGE - PROXYSHELL!](https://www.zerodayinitiative.com/blog/2021/8/17/from-pwn2own-2021-a-new-attack-surface-on-microsoft-exchange-proxyshell)

If you are interesting in more Exchange Server attacks, you can also check our series of articles:

  * [A New Attack Surface on MS Exchange Part 1 - ProxyLogon!](/blog/2021/08/06/a-new-attack-surface-on-MS-exchange-part-1-ProxyLogon/)
  * [A New Attack Surface on MS Exchange Part 2 - ProxyOracle!](/blog/2021/08/06/a-new-attack-surface-on-MS-exchange-part-2-ProxyOracle/)
  * [A New Attack Surface on MS Exchange Part 3 - ProxyShell!](/blog/2021/08/22/a-new-attack-surface-on-MS-exchange-part-3-ProxyShell/)
  * [A New Attack Surface on MS Exchange Part 4 - ProxyRelay!](/blog/2022/10/19/a-new-attack-surface-on-MS-exchange-part-4-ProxyRelay/)

With ProxyShell, an unauthenticated attacker can execute arbitrary commands on Microsoft Exchange Server through an exposed 443 port! Here is the [demonstration video](https://youtu.be/FC6iHw258RI):

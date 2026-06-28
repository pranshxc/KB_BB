---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2024-02-03_how-i-secured-the-united-nations-hall-of-fame.md
original_filename: 2024-02-03_how-i-secured-the-united-nations-hall-of-fame.md
title: How I secured the United Nations Hall of Fame
category: documents
detected_topics:
- xss
- command-injection
- api-security
- supply-chain
tags:
- imported
- documents
- xss
- command-injection
- api-security
- supply-chain
language: en
raw_sha256: 9308a2b7b8233d9c3b0af3e5745e8f73b4323c895c08bde606a3e2b90f025b79
text_sha256: 95ef654b11d03224b6caee852f2f9203b006f7bb97ae6dff0ce365bb6b7af872
ingested_at: '2026-06-28T07:32:31Z'
sensitivity: unknown
redactions_applied: false
---

# How I secured the United Nations Hall of Fame

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2024-02-03_how-i-secured-the-united-nations-hall-of-fame.md
- Source Type: markdown
- Detected Topics: xss, command-injection, api-security, supply-chain
- Ingested At: 2026-06-28T07:32:31Z
- Redactions Applied: False
- Raw SHA256: `9308a2b7b8233d9c3b0af3e5745e8f73b4323c895c08bde606a3e2b90f025b79`
- Text SHA256: `95ef654b11d03224b6caee852f2f9203b006f7bb97ae6dff0ce365bb6b7af872`


## Content

---
title: "How I secured the United Nations Hall of Fame"
url: "https://medium.com/@kamilrahman32/how-i-secured-the-united-nations-hall-of-fame-67b036ff2620"
authors: ["Kamil Rahuman"]
programs: ["United Nations"]
bugs: ["Components with known vulnerabilities"]
publication_date: "2024-02-03"
added_date: "2024-02-27"
source: "pentester.land/writeups.json"
original_index: 455
scraped_via: "browseros"
---

# How I secured the United Nations Hall of Fame

How I secured the United Nations Hall of Fame
Kamil Rahuman
Follow
3 min read
·
Feb 3, 2024

167

1

Press enter or click to view image in full size
UNITED NATIONS

Greetings, fellow cybersecurity enthusiasts! My name is Kamil Rahuman, Today, I’m thrilled to share my exhilarating journey of securing the United Nations Hall of Fame by uncovering a critical XSS vulnerability.

My journey began with a mission to contribute positively to the cybersecurity community. Little did I know that my efforts would lead me to the heart of one of the most prestigious organizations globally, the United Nations.

Getting Started : Recon

Let's get started…

Began with the routine by listing the Subdomains using Subfinder tool

Target domain: unep.org

subfinder -d unep.org > unep.txt

which was listed around 92 subdomains….

Now, let’s check out one of the domain by exploring its subdomains.

Randomly, I found a domain apps.unep.org which shows the endpoint as /test/server.php

Press enter or click to view image in full size
apps.unep.org listed in subdomains

At the time I didn’t have much idea about this endpoint. At last I came up with a tool called Nuclei

Nuclei-Vulnerability analysis tool

The Nuclei Advantage

Nuclei, an open-source tool, played a pivotal role in streamlining my vulnerability discovery process. Its extensible nature and comprehensive template library allowed me to perform detailed scans, helping uncover hidden vulnerabilities that might have eluded other tools. In this case, it proved invaluable in pinpointing the XSS vulnerability within the UN’s web infrastructure.

Get Kamil Rahuman’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

Discovery of XSS Vulnerability (CVE-2020–14413)

During the scanning with the tool Nuclei, Nuclei flagged a potential vulnerability — an XSS flaw in the UN’s web application, identified as CVE-2020–14413. XSS, or Cross-Site Scripting, is a critical security issue that allows attackers to inject malicious scripts into web pages viewed by other users.

URL: https://apps.unep.org/unepmediacentre/vendor/kriswallsmith/buzz/test/server.php

With XSS-URL: https://apps.unep.org/unepmediacentre/vendor/kriswallsmith/buzz/test/server.php/card_scan.php?No=0000&ReaderNo=0000&CardFormatNo=%3Cimg%20src%3Dx%20onerror%3Dalert%28document.domain%29%3E

Press enter or click to view image in full size
XSS Reflected !
Yes XSS Found!!

Responsible Disclosure

With the vulnerability identified, my next step was clear — responsible disclosure. Understanding the sensitivity and global impact of the United Nations, I ensured that my findings were communicated to their security team promptly and securely. This involved providing a detailed report outlining the nature of the XSS vulnerability, its potential impact and suggested mitigation strategies.

Recognition in the Hall of Fame

After the vulnerability was successfully patched, the United Nations acknowledged my contribution by including me in their Hall of Fame. It was a moment of immense pride and satisfaction to see my name alongside other cybersecurity enthusiasts who had made significant contributions to securing the organization.

Reported: 25th December 2023

Fixed: 1st January 2024

Acknowledged: 23th January 2024

Press enter or click to view image in full size
https://unite.un.org/content/un-information-security-hall-fame

Hall Of Fame: Hall of Fame | Office of Information and Communications Technology

Let’s meet again in other article

Bye !

Bye !

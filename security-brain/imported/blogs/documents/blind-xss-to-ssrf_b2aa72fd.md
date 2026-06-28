---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2023-01-29_blind-xss-to-ssrf.md
original_filename: 2023-01-29_blind-xss-to-ssrf.md
title: Blind XSS To SSRF
category: documents
detected_topics:
- ssrf
- xss
- command-injection
tags:
- imported
- documents
- ssrf
- xss
- command-injection
language: en
raw_sha256: b2aa72fd685267a88f40da04adacea575886733614ffea72ee55480566b0d58e
text_sha256: d15a541e9e57d8202a3f436d0010f2e4c552a73b0ee3d70db9ea415663732535
ingested_at: '2026-06-28T07:32:17Z'
sensitivity: unknown
redactions_applied: false
---

# Blind XSS To SSRF

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2023-01-29_blind-xss-to-ssrf.md
- Source Type: markdown
- Detected Topics: ssrf, xss, command-injection
- Ingested At: 2026-06-28T07:32:17Z
- Redactions Applied: False
- Raw SHA256: `b2aa72fd685267a88f40da04adacea575886733614ffea72ee55480566b0d58e`
- Text SHA256: `d15a541e9e57d8202a3f436d0010f2e4c552a73b0ee3d70db9ea415663732535`


## Content

---
title: "Blind XSS To SSRF"
url: "https://akashc99.medium.com/blind-xss-to-ssrf-e2bc579976d"
authors: ["Akash c"]
bugs: ["Blind XSS", "SSRF"]
bounty: "500"
publication_date: "2023-01-29"
added_date: "2023-02-03"
source: "pentester.land/writeups.json"
original_index: 1610
scraped_via: "browseros"
---

# Blind XSS To SSRF

Blind XSS To SSRF
Akash c
Follow
2 min read
·
Jan 30, 2023

91

1

During bug hunting in a private bug bounty program, I came across a feature within the application that allowed for the generation of PDF documents. Since the user input was reflected in the generated PDF documents, I decided to try injecting HTML and XSS payloads.

I used a well-known tool called XSSHunter, which allows us to find blind cross-site scripting vulnerabilities. To my surprise, my payload was immediately executed and I was able to retrieve the screenshot and the following details on XSSHunter.

Press enter or click to view image in full size

Further investigation revealed that the payload had been executed on the file path

“file:///gotenberg/e86fbc55ef893d878821c1bc76c3b1e3/index.html”.

Gotenberg is an open-source API for converting HTML, Markdown, and Office documents to PDF. It uses a set of configurable rendering engines to convert the input document to a PDF file. The Gotenberg parser is the component of Gotenberg that takes the input document and converts it into a format that can be rendered by the engines.

Get Akash c’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

Upon further testing, I discovered that the Gotenberg parser was vulnerable to server-side request forgery attacks. I was able to successfully execute a payload that included an iframe with the src set to “file:///etc/passwd”. This allowed me to view the contents of the “/etc/passwd” file.

Press enter or click to view image in full size

This type of vulnerability allows an attacker to access sensitive files on a server by manipulating the file path in a way that allows them to traverse the file system. This can potentially lead to the exposure of sensitive information and even complete system compromise.

I immediately reported my findings to the security team, who classified the vulnerability as high. However, another security researcher had also reported the vulnerability at the same time. As a result, the team decided to split the bounty and I received $500.

Press enter or click to view image in full size

The XSS Hunter has been deprecated and is no longer in use. A new version has been launched by Truffle Security, available at https://xsshunter.trufflesecurity.com.

Resources

https://media.defcon.org/DEF%20CON%2027/DEF%20CON%2027%20presentations/DEFCON-27-Ben-Sadeghipour-Owning-the-clout-through-SSRF-and-PDF-generators.pdf

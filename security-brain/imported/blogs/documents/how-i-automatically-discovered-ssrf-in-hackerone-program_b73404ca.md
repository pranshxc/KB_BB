---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2023-12-15_how-i-automatically-discovered-ssrf-in-hackerone-program.md
original_filename: 2023-12-15_how-i-automatically-discovered-ssrf-in-hackerone-program.md
title: How I Automatically Discovered SSRF in Hackerone Program
category: documents
detected_topics:
- ssrf
- command-injection
tags:
- imported
- documents
- ssrf
- command-injection
language: en
raw_sha256: b73404cad8cfc4669c2f0ce8f1a510768fdeab135fafc20a974faed85cda3c87
text_sha256: 65df4e0da61a73ead4f90ee4dd81e27c6d40410d054ce95e25975c830b96258a
ingested_at: '2026-06-28T07:32:28Z'
sensitivity: unknown
redactions_applied: false
---

# How I Automatically Discovered SSRF in Hackerone Program

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2023-12-15_how-i-automatically-discovered-ssrf-in-hackerone-program.md
- Source Type: markdown
- Detected Topics: ssrf, command-injection
- Ingested At: 2026-06-28T07:32:28Z
- Redactions Applied: False
- Raw SHA256: `b73404cad8cfc4669c2f0ce8f1a510768fdeab135fafc20a974faed85cda3c87`
- Text SHA256: `65df4e0da61a73ead4f90ee4dd81e27c6d40410d054ce95e25975c830b96258a`


## Content

---
title: "How I Automatically Discovered SSRF in Hackerone Program"
page_title: "How I Auto-Discovering SSRF on Hackerone Program | Medium"
url: "https://medium.com/@kerstan/how-i-automatically-discovered-ssrf-in-hackerone-program-2ae0b7a6ef1b"
authors: ["kerstan"]
bugs: ["SSRF"]
publication_date: "2023-12-15"
added_date: "2023-12-27"
source: "pentester.land/writeups.json"
original_index: 623
scraped_via: "browseros"
---

# How I Automatically Discovered SSRF in Hackerone Program

Member-only story

How I Auto-Discovering SSRF on Hackerone Program
kerstan
Follow
4 min read
·
Dec 15, 2023

201

1

Get an email whenever kerstan publishes.
Get an email whenever kerstan publishes. By signing up, you will create a Medium account if you don't already have one…

medium.com

Hi guys, I am Kerstan. Today, I will share you how I automatically discoverd SSRF on hackerone Program.

F
inding a blind SSRF is relatively easy, but to earn more bounty, you need to exploit it and gain more access. It requires relentless effort. Try harder, bro!

If this writing has been helpful to you, please consider giving it a clap and following. Thanks bro.

So, let’s get started.

Press enter or click to view image in full size
1. Download & Install

First, you need to download AutoRepeater from the following address. Once downloaded, go to the Extender interface of Burp and import AutoRepeater.jar.

Press enter or click to view image in full size
https://github.com/nccgroup/AutoRepeater
2. Automatically Discovered SSRF

You need to do two preparatory steps:

You need a dnslog platform where you can view the logs, such as Burp’s Collaborator or ceye.io. You…

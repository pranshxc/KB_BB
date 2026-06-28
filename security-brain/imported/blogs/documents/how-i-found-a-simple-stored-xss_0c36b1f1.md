---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2022-10-24_how-i-found-a-simple-stored-xss.md
original_filename: 2022-10-24_how-i-found-a-simple-stored-xss.md
title: How I Found A Simple Stored XSS
category: documents
detected_topics:
- xss
- command-injection
tags:
- imported
- documents
- xss
- command-injection
language: en
raw_sha256: 0c36b1f16e98e57f9539f123f54b6363c0c24da0bc95f43dafff3fece4df1694
text_sha256: 841948b3e3c8cf43b071996cbd8618477d42839d1a28b97c0aa0d0a64783729a
ingested_at: '2026-06-28T07:32:15Z'
sensitivity: unknown
redactions_applied: false
---

# How I Found A Simple Stored XSS

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2022-10-24_how-i-found-a-simple-stored-xss.md
- Source Type: markdown
- Detected Topics: xss, command-injection
- Ingested At: 2026-06-28T07:32:15Z
- Redactions Applied: False
- Raw SHA256: `0c36b1f16e98e57f9539f123f54b6363c0c24da0bc95f43dafff3fece4df1694`
- Text SHA256: `841948b3e3c8cf43b071996cbd8618477d42839d1a28b97c0aa0d0a64783729a`


## Content

---
title: "How I Found A Simple Stored XSS"
url: "https://medium.com/@raymond-lind/how-i-found-a-simple-stored-xss-9a6b1c5e0afa"
authors: ["Raymond Lind"]
bugs: ["Stored XSS"]
publication_date: "2022-10-24"
added_date: "2022-10-25"
source: "pentester.land/writeups.json"
original_index: 2001
scraped_via: "browseros"
---

# How I Found A Simple Stored XSS

Member-only story

How I Found A Simple Stored XSS
Raymond Lind
4 min read
·
Oct 24, 2022

--

3

--

This is the story of how I found my first Stored XSS (“Cross Site Scripting”) vulnerability in a bug bounty program and a walk through on the details regarding how I came to find this bug.

Press enter or click to view image in full size
Introduction

This is the story about the time I found a Stored XSS in a eCommerce bug bounty website. For those of you who are unaware of bug bounty programs, they are when companies allow ethical hackers to break apart their application and attempt to find vulnerabilities for an award or recognition. These can either be publicly known BBP’s (“Bug Bounty Programs”), VDP’s (“Vulnerability Disclosure Programs”), or Private Invite Only Programs. Now we will jump into the details about how the XSS was found.

What is XSS?

XSS or Cross Site Scripting is a vulnerability in which a user is able to use a provided input field to insert an XSS payload to break out of the context of the code. This causes the user to be able to execute javascript on the vulnerable webpage which can turn out to be very dangerous.

An example of an XSS payload can be seen below:

"><img src=x onload=alert(document.cookie)>

In the example above, we break out of the context of the code with the quote and greater-than sign at the beginning. We then have full capabilities…

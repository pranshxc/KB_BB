---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2023-03-29_a-short-tell-of-lfi-from-pdf-link-professor-the-hunter.md
original_filename: 2023-03-29_a-short-tell-of-lfi-from-pdf-link-professor-the-hunter.md
title: A short tell of LFI from PDF link → Professor the Hunter
category: documents
detected_topics:
- path-traversal
- sso
- command-injection
- information-disclosure
tags:
- imported
- documents
- path-traversal
- sso
- command-injection
- information-disclosure
language: en
raw_sha256: 5d07234030f9b7c4f06a8553ba87d212c4c9cf0cd0cd777722b542d1401dd6ff
text_sha256: c6d0a99260764479118587cb979a4c9c2249aae077024a43e78224d64ac330d6
ingested_at: '2026-06-28T07:32:19Z'
sensitivity: unknown
redactions_applied: false
---

# A short tell of LFI from PDF link → Professor the Hunter

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2023-03-29_a-short-tell-of-lfi-from-pdf-link-professor-the-hunter.md
- Source Type: markdown
- Detected Topics: path-traversal, sso, command-injection, information-disclosure
- Ingested At: 2026-06-28T07:32:19Z
- Redactions Applied: False
- Raw SHA256: `5d07234030f9b7c4f06a8553ba87d212c4c9cf0cd0cd777722b542d1401dd6ff`
- Text SHA256: `c6d0a99260764479118587cb979a4c9c2249aae077024a43e78224d64ac330d6`


## Content

---
title: "A short tell of LFI from PDF link → Professor the Hunter"
page_title: "LFI Vulnerability Exploited in Edge Network — A Quick Discovery | by Professor Software Solutions | Medium"
url: "https://medium.com/@bughuntar/a-short-tell-of-lfi-from-pdf-link-professor-the-hunter-43a8be853e"
authors: ["Professor the Hunter (@bughuntar)"]
bugs: ["LFI"]
publication_date: "2023-03-29"
added_date: "2023-03-31"
source: "pentester.land/writeups.json"
original_index: 1330
scraped_via: "browseros"
---

# A short tell of LFI from PDF link → Professor the Hunter

LFI Vulnerability Exploited in Edge Network — A Quick Discovery
Professor Software Solutions
Follow
2 min read
·
Mar 29, 2023

138

1

By Professor the Hunter

Press enter or click to view image in full size
Who Am I?

I’m a Security Researcher and active participant in bug bounty programs on platforms like HackerOne Inc. For more bug bounty tips and updates, feel free to follow me on Twitter: @bughuntar.

Summary:

Today, I came across a Local File Inclusion (LFI) vulnerability in Redacted’s Edge Network. As many of you know, the consequences of an LFI vulnerability can range from information disclosure to a complete system compromise. Even if the file inclusion doesn’t immediately execute malicious code, attackers can still extract valuable information, potentially giving them the means to escalate their attack.

In this case, the LFI vulnerability provided critical information that could lead to full system compromise if exploited further.

How I Discovered the LFI Vulnerability:

While performing a routine security test on https://erecruitment.redacted.com, I stumbled upon a PDF link that looked like a potential candidate for further exploration. The URL was:

https://erecruitment.redacted.com/onlineapp/rocketpreepay.pdf

At first, I tried injecting different paths into the URL to test for an LFI vulnerability, but I kept getting redirected. After several attempts, I assumed there was no LFI issue with the link. However, after carefully testing a specific payload, I was surprised to find that it worked and allowed me to access sensitive files on the server.

LFI Exploit:

Here’s the proof of concept (PoC) demonstrating the LFI vulnerability:

Get Professor Software Solutions’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

Exploit URL:

https://erecruitment.redacted.com/onlineapp/rocketpreepay.pdf../../../../../../../etc/passwd

When I appended the path traversal sequence (../../../../../../../etc/passwd), I was able to access the passwd file located on the server, which is a crucial system file containing user account information. This is a clear indication of an LFI vulnerability that could lead to further exploitation.

Conclusion:

While I’m unsure of the exact bounty I’ll receive if this vulnerability is accepted, I’m grateful to have discovered it. It’s always exciting when you find an issue that has the potential to affect the security of a system. Alhamdulillah — I’m thankful for the opportunity to contribute to the security community.

Follow Me

You can stay connected with me across the following platforms:

Website: https://bughuntar.com
Facebook: https://facebook.com/bughuntar
Twitter: https://twitter.com/bughuntar
Telegram: https://t.me/bughuntar
YouTube: https://youtube.com/bughuntar
Medium: https://bughuntar.medium.com
LinkedIn: https://www.linkedin.com/in/SoftwareDeveloperSagor

Feel free to reach out for tips, discussions, or collaborations. I’m always open to connecting with fellow security enthusiasts and bug hunters!

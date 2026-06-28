---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2022-03-14_how-i-access-other-domains-in-infinityfreenet-using-directory-traversal.md
original_filename: 2022-03-14_how-i-access-other-domains-in-infinityfreenet-using-directory-traversal.md
title: How I access other domains in infinityfree.net using Directory Traversal
category: documents
detected_topics:
- path-traversal
- command-injection
- cloud-security
- supply-chain
tags:
- imported
- documents
- path-traversal
- command-injection
- cloud-security
- supply-chain
language: en
raw_sha256: 0f58341400f667ae4197c23d36bf6cd16c40ce9bbbb9c2ead61f0f7ec601e900
text_sha256: fbf3d7fb683dcf1ee4de830034a634158888707f5d455be557ea902a4fa8afef
ingested_at: '2026-06-28T07:32:10Z'
sensitivity: unknown
redactions_applied: false
---

# How I access other domains in infinityfree.net using Directory Traversal

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2022-03-14_how-i-access-other-domains-in-infinityfreenet-using-directory-traversal.md
- Source Type: markdown
- Detected Topics: path-traversal, command-injection, cloud-security, supply-chain
- Ingested At: 2026-06-28T07:32:10Z
- Redactions Applied: False
- Raw SHA256: `0f58341400f667ae4197c23d36bf6cd16c40ce9bbbb9c2ead61f0f7ec601e900`
- Text SHA256: `fbf3d7fb683dcf1ee4de830034a634158888707f5d455be557ea902a4fa8afef`


## Content

---
title: "How I access other domains in infinityfree.net using Directory Traversal"
url: "https://xkurtph.medium.com/how-i-access-other-domains-in-infinityfree-net-using-directory-traversal-4625692d6a2d"
authors: ["Kurt Russelle Marmol"]
programs: ["InfinityFree"]
bugs: ["Directory traversal"]
publication_date: "2022-03-14"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 2824
scraped_via: "browseros"
---

# How I access other domains in infinityfree.net using Directory Traversal

How I access other domains in infinityfree.net using Directory Traversal
Kurt Russelle Marmol
Follow
2 min read
·
Mar 14, 2022

8

Hi, it’s me again haha Kurt Russelle Marmol aka xkurtph, Web Developer (noobie) and Security Researcher.

Vulnerability Method:
Directory / Path Traversal
What is infinityfree.net?

Infinity Free is a US-based web hosting provider launched in 2016, and, as its name suggests, it offers free hosting services for an indeterminate period of time.

Story:

This bug was I accidentally found haha when my friend want to access my files on the web hosting, so I gave them a PHP shell instead of the FTP account. I gave PHP shell because it is easy to use rather than FTP bcz u needed it to log in and access files (time-consuming).

Let’s say I have a domain name iamxkurtph.com I gave my friend a shell path which is iamxkurtph.ml/shell.php

When you try to open a folder or files, your URL path would become like this https://iamxkurtph.ml/shell.php?path=/home/vol11_6/epizy.com/epiz_30774583/htdocs/images

Press enter or click to view image in full size

can you see the clue? how I access other domains hahaha

Get Kurt Russelle Marmol’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

here it is

as you can see the epiz_30774583, it is my username in the domain therefore I change it incrementally like this epiz_30774584, epiz_30774585, or epiz_30774586 the whole URL will be like this https://iamxkurtph.ml/shell.php?path=/home/vol11_6/epizy.com/epiz_30774584

and gotcha! you already access other domain files by this method, but it will only work if the other domain has the same host/server as what you use.

The bug is originated from a third-party website but it is also used by infinityfree.net to serve, I already reported the bug from infinityfree.net but they told me to report to iFastNet because iFastNet was the main provider to host domain.

A bug was already reported and fixed, iFastNet is not offering a bug bounty program but they give me free .com domain as a reward :>

You can watch my full demonstration below.

20220310_142443.mp4
Directory Traversal using PHP Shells

drive.google.com

Impact:

Using the bug as a method could be lead to breaching other domains and leaking files and sensitive information they have.

Timeline:

March 10, 2022 — Bug submitted and review

March 13, 2022 — Bug fixed and rewarded

Shawarawt sa PlagueSec at KumaTechDevs

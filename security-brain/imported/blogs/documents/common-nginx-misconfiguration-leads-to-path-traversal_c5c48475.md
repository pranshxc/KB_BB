---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2021-12-28_common-nginx-misconfiguration-leads-to-path-traversal.md
original_filename: 2021-12-28_common-nginx-misconfiguration-leads-to-path-traversal.md
title: Common Nginx Misconfiguration leads to Path Traversal
category: documents
detected_topics:
- command-injection
- path-traversal
tags:
- imported
- documents
- command-injection
- path-traversal
language: en
raw_sha256: c5c484755cac96b3f6f733558a52f20e1db71c72335191a3268c17285a6d18dd
text_sha256: 073c6507f3822edc80d173bcaf24c0c09833b36ea94bc85cc78354c7dbcb02c3
ingested_at: '2026-06-28T07:32:09Z'
sensitivity: unknown
redactions_applied: false
---

# Common Nginx Misconfiguration leads to Path Traversal

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2021-12-28_common-nginx-misconfiguration-leads-to-path-traversal.md
- Source Type: markdown
- Detected Topics: command-injection, path-traversal
- Ingested At: 2026-06-28T07:32:09Z
- Redactions Applied: False
- Raw SHA256: `c5c484755cac96b3f6f733558a52f20e1db71c72335191a3268c17285a6d18dd`
- Text SHA256: `073c6507f3822edc80d173bcaf24c0c09833b36ea94bc85cc78354c7dbcb02c3`


## Content

---
title: "Common Nginx Misconfiguration leads to Path Traversal"
url: "https://systemweakness.com/common-nginx-misconfiguration-leads-to-path-traversal-d58701e997bc"
authors: ["MikeChan"]
bugs: ["Path traversal"]
publication_date: "2021-12-28"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 3056
scraped_via: "browseros"
---

# Common Nginx Misconfiguration leads to Path Traversal

Member-only story

Common Nginx Misconfiguration leads to Path Traversal
MikeChan
Follow
3 min read
·
Dec 27, 2021

61

Press enter or click to view image in full size
Photo by Ferenc Almasi on Unsplash

Recently, I have been invited by my friend to participate into a private pentest project. The target has been using Nginx as its Reverse Proxy and I found a common Nginx misconfiguration that leads to a path traversal bug. In order to help the owner of the target to have a better understanding the root cause, I have made a demonstration of how the misconfiguration was setup. So, this passage mainly record of what the bug is, how the misconfiguration is done and how to prevent it.

So, let’s begin!

Install Nginx

In order to have a solid understanding of what the bug is, you may setup a Nginx on your own. In here, I will go through how you can setup yours on an Ubuntu box. If you are using window, you may download virtualbox to setup one on your virtual machine. Otherwise, you may setup a VPS in Digital ocean by this referral link. You can get USD100 credit to be spent in 60 days. That should be more than enough for your testing

So, suppose you have your ubuntu box setup. Now, let’s update your ubuntu and download Nginx:

sudo apt-get update -y && sudo apt-get upgrade -y && sudo apt install nginx -y

After successful install, type following commands:

sudo systemctl start nginx
sudo systemctl enable…

---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2022-02-14_hacking-aws-cognito-misconfiguration-to-zero-click-account-takeover.md
original_filename: 2022-02-14_hacking-aws-cognito-misconfiguration-to-zero-click-account-takeover.md
title: Hacking AWS Cognito Misconfiguration to Zero Click Account Takeover
category: documents
detected_topics:
- command-injection
- cloud-security
tags:
- imported
- documents
- command-injection
- cloud-security
language: en
raw_sha256: b0471d5ce52ff07903474f8979df62b3a252e1abbe6dce9ec5845efaa7941dc1
text_sha256: 079825aa24bb74acb186fbfae1824e6e706bef7caa1f52c4c17b2e4e65a48571
ingested_at: '2026-06-28T07:32:10Z'
sensitivity: unknown
redactions_applied: false
---

# Hacking AWS Cognito Misconfiguration to Zero Click Account Takeover

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2022-02-14_hacking-aws-cognito-misconfiguration-to-zero-click-account-takeover.md
- Source Type: markdown
- Detected Topics: command-injection, cloud-security
- Ingested At: 2026-06-28T07:32:10Z
- Redactions Applied: False
- Raw SHA256: `b0471d5ce52ff07903474f8979df62b3a252e1abbe6dce9ec5845efaa7941dc1`
- Text SHA256: `079825aa24bb74acb186fbfae1824e6e706bef7caa1f52c4c17b2e4e65a48571`


## Content

---
title: "Hacking AWS Cognito Misconfiguration to Zero Click Account Takeover"
url: "https://infosecwriteups.com/hacking-aws-cognito-misconfiguration-to-zero-click-account-takeover-36a209a0bd8a"
authors: ["Preetham Bomma (@cyber01_)"]
bugs: ["AWS misconfiguration", "Account takeover"]
publication_date: "2022-02-14"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 2909
scraped_via: "browseros"
---

# Hacking AWS Cognito Misconfiguration to Zero Click Account Takeover

Member-only story

Hacking AWS Cognito Misconfiguration to Zero Click Account Takeover
Hi all, hope you are keeping well and staying safe. This blog is about my recent Account Takeover finding.
Preetham Bomma
Follow
4 min read
·
Feb 14, 2022

104

1

Inspiration

I was going through Hackivity from Hackerone and read about the amazing Flickr Account Takeover. Thanks to Lauritz for the find and an excellent blog post. If you haven’t read it, it is here. I’ll also provide some references at the end of this post.

Introduction

I was testing a web application related to health care. Some of the functionalities were to schedule appointments with doctors, order medicines, interact with doctors within the website via messaging, etc. It was an authenticated test, credentials were provided.

It is important to note that the email address and other details cannot be changed from the application, we had to send a request to support for any changes.

Upon logging in to the app, I have noticed the login request is sent to Amazon Cognito URL. If you need a thorough understanding of the login, pl go through Laurtiz blog or this blog by Appseco.

Press enter or click to view image in full size
The image is taken from the Appseco blog.

So, the login flow in the app I was testing was as follows.

Login to the App, a POST…

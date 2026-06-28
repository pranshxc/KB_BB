---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2023-02-10_disabling-js-for-the-win.md
original_filename: 2023-02-10_disabling-js-for-the-win.md
title: Disabling js for the win
category: documents
detected_topics:
- command-injection
- file-upload
- api-security
tags:
- imported
- documents
- command-injection
- file-upload
- api-security
language: en
raw_sha256: e928bf7de35f3035d726e2daa91c745fab03a3c38b3473cb447030d82cadfa51
text_sha256: d0d6a399d98c0387257e72fcabf2ecb9aa65b9991f00303a348b997ff1fb7cd4
ingested_at: '2026-06-28T07:32:18Z'
sensitivity: unknown
redactions_applied: false
---

# Disabling js for the win

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2023-02-10_disabling-js-for-the-win.md
- Source Type: markdown
- Detected Topics: command-injection, file-upload, api-security
- Ingested At: 2026-06-28T07:32:18Z
- Redactions Applied: False
- Raw SHA256: `e928bf7de35f3035d726e2daa91c745fab03a3c38b3473cb447030d82cadfa51`
- Text SHA256: `d0d6a399d98c0387257e72fcabf2ecb9aa65b9991f00303a348b997ff1fb7cd4`


## Content

---
title: "Disabling js for the win"
url: "https://infosecwriteups.com/disabling-js-for-the-win-9d13c606f910"
authors: ["Vuk Ivanovic"]
bugs: ["Unrestricted file upload", "RCE"]
publication_date: "2023-02-10"
added_date: "2023-03-02"
source: "pentester.land/writeups.json"
original_index: 1548
scraped_via: "browseros"
---

# Disabling js for the win

Member-only story

Disabling js for the win
,or how reading the html code w/ care lead to rce through file upload
Vuk Ivanovic
Follow
3 min read
·
Feb 10, 2023

44

Javascript. Used practically everywhere, even in your washing machine (this is a joke, I think (: ) And if you really want to know how unavoidable it is just turn off js globally using either extension or manually, and try using any of the popular websites — good luck with that :) I mean, I had js disabled globally some time ago, and I have obvious websites whitelisted for js, which means that every now and again I find myself visiting some website that heavily relies on js, to the point where it’s impossible to read its content without enabling js. But, it has lead me to accessing various admin panels without logging in, if the website relied on js to determine if you should be redirected to the login screen or admin panel (which in most cases is just access to the design/layout of the admin panel without any functionality that relies on authenticated access), but this article is about the recent bug hunt session where I found a functional file upload area that was hidden by the devs instead of being fully removed or better protected. It does require authenticated access though, but even as an authenticated user, the js code verifies if you’re on that page and if so for some reason dev(s) decided to hide the file upload form. Why? Perhaps they knew that a bug was present? Or it was meant to be under construction/patching process?

Step 1 — Disable js

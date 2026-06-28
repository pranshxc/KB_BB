---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2013-10-21_content-types-and-xss-facebook-studio.md
original_filename: 2013-10-21_content-types-and-xss-facebook-studio.md
title: 'Content Types and XSS: Facebook Studio'
category: documents
detected_topics:
- xss
- command-injection
- otp
- csrf
- api-security
- cloud-security
tags:
- imported
- documents
- xss
- command-injection
- otp
- csrf
- api-security
- cloud-security
language: en
raw_sha256: 06f32661e49c3377345f228141c1a7ae17135a5ab14dfa4ce07396762c7d2e6f
text_sha256: 126d1ca4dba9b2c343fbef2024d444df32fcfca9d316cae3b31e965d4d71ae02
ingested_at: '2026-06-28T07:31:55Z'
sensitivity: unknown
redactions_applied: false
---

# Content Types and XSS: Facebook Studio

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2013-10-21_content-types-and-xss-facebook-studio.md
- Source Type: markdown
- Detected Topics: xss, command-injection, otp, csrf, api-security, cloud-security
- Ingested At: 2026-06-28T07:31:55Z
- Redactions Applied: False
- Raw SHA256: `06f32661e49c3377345f228141c1a7ae17135a5ab14dfa4ce07396762c7d2e6f`
- Text SHA256: `126d1ca4dba9b2c343fbef2024d444df32fcfca9d316cae3b31e965d4d71ae02`


## Content

---
title: "Content Types and XSS: Facebook Studio"
page_title: "Content Types and XSS: Facebook Studio – Jack"
url: "https://whitton.io/articles/content-types-and-xss-facebook-studio/"
final_url: "https://whitton.io/articles/content-types-and-xss-facebook-studio/"
authors: ["Jack Whitton (@fin1te)"]
programs: ["Meta / Facebook"]
bugs: ["XSS"]
publication_date: "2013-10-21"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 6394
---

# [Content Types and XSS: Facebook Studio](https://whitton.io/articles/content-types-and-xss-facebook-studio/ "Content Types and XSS: Facebook Studio")

## October 21, 2013

__Reading time ~1 minute

I’ve found a few bugs on various Facebook satellite/marketing domains (ones which are part of the Facebook brand, but not necessarily hosted/developed by them, and not under the *.facebook.com domain). Most of them aren’t that serious.

This one isn’t an exception, and I wouldn’t normally blog about it, but it’s an interesting use case as to why content types are important.

The bug is an XSS discovered on [Facebook Studio](http://www.facebook-studio.com). This is linked to by some Facebook marketing pages, and is used to showcase advertising campaigns on Facebook.

[ ![](/images/fbstudio/fb-studio-1.png) ](/images/fbstudio/fb-studio-1.png)

There is an area which allows you to submit work to the [Gallery](https://www.facebook-studio.com/gallery). This form conveniently has an option to scrape details from your Facebook page and fill in boxes for you (such as Company Name, Description).

This calls an AJAX end-point with your pages URL as a parameter.

[ ![](/images/fbstudio/fb-studio-2-1.png) ](/images/fbstudio/fb-studio-2-1.png)

If we set our pages description to something containing HTML/Javascript, it’s properly escaped. However, it’s escaped client-side. The end-point incorrectly sends a content-type header of `text/html`, when the response is actually JSON.

When browsed to directly (it doesn’t need any CSRF tokens to be viewed, despite the `hash` param), we see our script executed.

[ ![](/images/fbstudio/fb-studio-3-1.png) ](/images/fbstudio/fb-studio-3-1.png)

The cool thing about this bug is that whilst it’s not persistent (the payload is fetched when the page is visited), the code is not present in the request body, therefore avoiding Chrome’s XSS Auditor and IE’s XSS Filter.

Had the content type been set to `application/json`, the code would have not run (until you start to consider content sniffing…).

### Fix

The content type is now set correctly.

### Timeline

  * 15th August 2013 - Issue Reported
  * 21st August 2013 - Acknowledgment of Report
  * 21st August 2013 - Issue Fixed

[facebook](https://whitton.io/tags/#facebook "Pages tagged facebook")[bugbounty](https://whitton.io/tags/#bugbounty "Pages tagged bugbounty")[websec](https://whitton.io/tags/#websec "Pages tagged websec")[xss](https://whitton.io/tags/#xss "Pages tagged xss") Updated on October 21, 2013 Jack

  * [__Like](https://www.facebook.com/sharer/sharer.php?u=https://whitton.io/articles/content-types-and-xss-facebook-studio/ "Share on Facebook")
  * [__Tweet](https://twitter.com/intent/tweet?text=https://whitton.io/articles/content-types-and-xss-facebook-studio/ "Share on Twitter")
  * [__+1](https://plus.google.com/share?url=https://whitton.io/articles/content-types-and-xss-facebook-studio/ "Share on Google Plus")

[Read More](https://whitton.io/articles/removing-covers-images-on-friendship-pages-on-facebook/)

### [From Bug Bounty Hunter, to Engineer, and Beyond](https://whitton.io/articles/from-researcher-to-engineer-and-beyond/ "From Bug Bounty Hunter, to Engineer, and Beyond")

A couple weeks ago I had my last day on Facebook's Product Security team. Abittersweet moment, but one which marks a "new chapter" in my ...… [Continue reading](https://whitton.io/articles/from-researcher-to-engineer-and-beyond/)

#### [Obtaining Login Tokens for an Outlook, Office or Azure Account](https://whitton.io/articles/obtaining-tokens-outlook-office-azure-account/ "Obtaining Login Tokens for an Outlook, Office or Azure Account")

Published on April 03, 2016

#### [Uber Bug Bounty: Turning Self-XSS into Good-XSS](https://whitton.io/articles/uber-turning-self-xss-into-good-xss/ "Uber Bug Bounty: Turning Self-XSS into Good-XSS")

Published on March 22, 2016
